from unittest.mock import MagicMock

from nascar_api.enums import Flag, Series
from nascar_api.models import LapData, PitData, RaceInfo, RaceLaps, RaceLoopStat, WeekendInfo
from nascar_api.repos import HistoricNascarRepo
from nascar_api.repos.base import NascarRepo
from tests.data_factories.loop_stat import RaceLoopStatFactory
from tests.data_factories.pit_data import PitDataFactory
from tests.data_factories.race_info import RaceInfoFactory
from tests.data_factories.race_laps import RaceLapsFactory
from tests.data_factories.weekend_info import WeekendInfoFactory

MOCK_RESPONSE = {
    "series_1": [info.model_dump(mode="json") for info in RaceInfoFactory.batch(10)],
    "series_2": [info.model_dump(mode="json") for info in RaceInfoFactory.batch(10)],
}


def test_races_no_series(requests_mock):
    repo = HistoricNascarRepo()
    mock_year = 2000
    mock_url = f"{repo.DOMAIN}/{mock_year}/race_list_basic.json"
    requests_mock.get(mock_url, json=MOCK_RESPONSE)
    races = repo.get_races(mock_year)
    assert len(races) == 20
    assert all([isinstance(info, RaceInfo) for info in races])

def test_races_with_series(requests_mock):
    repo = HistoricNascarRepo()
    mock_year = 2000
    mock_series = MagicMock(spec=Series)
    mock_series.value = 1
    mock_url = f"{repo.DOMAIN}/{mock_year}/race_list_basic.json"
    requests_mock.get(mock_url, json=MOCK_RESPONSE)
    races = repo.get_races(mock_year, mock_series)
    assert len(races) == 10
    assert all([isinstance(info, RaceInfo) for info in races])

def test_lap_notes(requests_mock):
    repo = HistoricNascarRepo()
    mock_year = 2000
    mock_series = MagicMock(spec=Series)
    mock_series.value = 1
    mock_race_id = 123
    mock_url = f"{repo.DOMAIN}/{mock_year}/{mock_series.value}/{mock_race_id}/lap-notes.json"
    mock_response = {
        "laps": {
            "0": [{"FlagState": 1, "Note": "Green flag", "NoteID": 1, "DriverIDs": [None]}],
            "21": [
                {"FlagState": 2, "Note": "Caution", "NoteID": 2, "DriverIDs": [4, None, 7]},
            ],
        }
    }
    requests_mock.get(mock_url, json=mock_response)
    notes = repo.get_lap_notes(mock_year, mock_series, mock_race_id)
    assert all([isinstance(note, LapData) for note in notes])
    assert [(n.lap_number, n.flag_state) for n in notes] == [(0, Flag.GREEN), (21, Flag.YELLOW)]
    assert notes[0].driver_ids == []
    assert notes[1].driver_ids == [4, 7]
    assert all([note.race_id == mock_race_id for note in notes])

def test_lap_notes_skips_non_flag_states(requests_mock):
    """FlagState 1000 marks broadcast trivia, not a flag; one used to fail the whole race."""
    repo = HistoricNascarRepo()
    mock_year = 2000
    mock_series = MagicMock(spec=Series)
    mock_series.value = 1
    mock_race_id = 123
    mock_url = f"{repo.DOMAIN}/{mock_year}/{mock_series.value}/{mock_race_id}/lap-notes.json"
    mock_response = {
        "laps": {
            "21": [
                {"FlagState": 1000, "Note": "Trivia", "NoteID": 1, "DriverIDs": []},
                {"FlagState": 2, "Note": "Caution", "NoteID": 2, "DriverIDs": [4]},
            ],
        }
    }
    requests_mock.get(mock_url, json=mock_response)
    notes = repo.get_lap_notes(mock_year, mock_series, mock_race_id)
    assert [(n.note_id, n.flag_state) for n in notes] == [(2, Flag.YELLOW)]

def test_lap_times(requests_mock):
    repo = HistoricNascarRepo()
    mock_year = 2000
    mock_series = MagicMock(spec=Series)
    mock_series.value = 1
    mock_race_id = 123
    mock_url = f"{repo.DOMAIN}/{mock_year}/{mock_series.value}/{mock_race_id}/lap-times.json"
    mock_response = {"laps": [lap.model_dump(by_alias=True) for lap in RaceLapsFactory.batch(10)]}
    requests_mock.get(mock_url, json=mock_response)
    laps = repo.get_lap_times(mock_year, mock_series, mock_race_id)
    assert len(laps) == 10
    assert all([isinstance(info, RaceLaps) for info in laps])

def test_pit_data(requests_mock):
    repo = HistoricNascarRepo()
    mock_series = MagicMock(spec=Series)
    mock_series.value = 1
    mock_race_id = 123
    mock_url = f"{repo.DOMAIN}/live/series_{mock_series.value}/{mock_race_id}/live-pit-data.json"
    requests_mock.get(mock_url, json=[pit.model_dump() for pit in PitDataFactory.batch(10)])
    pit_data = repo.get_pit_data(mock_series, mock_race_id)
    assert len(pit_data) == 10
    assert all([isinstance(data, PitData) for data in pit_data])

def test_weekend_data(requests_mock):
    repo = HistoricNascarRepo()
    mock_year = 2000
    mock_series = MagicMock(spec=Series)
    mock_series.value = 1
    mock_race_id = 123
    mock_url = f"{repo.DOMAIN}/{mock_year}/{mock_series.value}/{mock_race_id}/weekend-feed.json"
    requests_mock.get(mock_url, json=WeekendInfoFactory.build().model_dump(mode="json"))
    weekend_info = repo.get_weekend_data(mock_year, mock_series, mock_race_id)
    assert isinstance(weekend_info, WeekendInfo)
    assert weekend_info.race_id == mock_race_id

def test_loopstats(requests_mock):
    repo = HistoricNascarRepo()
    mock_year = 2000
    mock_series = MagicMock(spec=Series)
    mock_series.value = 1
    mock_race_id = 123
    mock_url = f"{NascarRepo.DOMAIN}/loopstats/prod/{mock_year}/{mock_series.value}/{mock_race_id}.json"
    requests_mock.get(mock_url, json=[RaceLoopStatFactory.build().model_dump(mode="json")])
    loopstats = repo.get_loopstats(mock_year, mock_series, mock_race_id)
    assert isinstance(loopstats, RaceLoopStat)
