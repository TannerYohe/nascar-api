from pydantic import ValidationError
from ..models import (
    LapData,
    RaceLaps,
    PitData,
    RaceLoopStat,
    RaceInfo,
    WeekendInfo,
)
from base import NascarRepo
from typing import List
from .. import Series
import logging

log = logging.getLogger(__name__)


class HistoricNascarRepo(NascarRepo):
    DOMAIN = f"{super().DOMAIN}/cacher"

    def get_races(self, year: int, series: Series = None) -> List[RaceInfo]:
        url = f"{self.DOMAIN}/{year}/race_list_basic.json"
        response_json = self.safe_get(url)
        races = []
        if series:
            for race in response_json[f"series_{series.value}"]:
                try:
                    races.append(RaceInfo.model_validate(race))
                except ValidationError:
                    print(race)
                    raise
        if not series:
            for series in response_json:
                for race in response_json[series]:
                    races.append(RaceInfo.model_validate(race))
        return races

    def get_lap_notes(self, year: int, series: Series, race_id: int) -> List[LapData]:
        url = f"{self.DOMAIN}/{year}/{series.value}/{race_id}/lap-notes.json"
        response_json = self.safe_get(url)
        laps = []
        for lap_number, flag_datas in response_json["laps"].items():
            for flag_data in flag_datas:
                laps.append(
                    LapData(
                        race_id=race_id,
                        lap_number=lap_number,
                        flag_state=flag_data.get("FlagState"),
                        note=flag_data.get("Note"),
                        note_id=flag_data.get("NoteID"),
                        driver_ids=filter(None, flag_data.get("DriverIDs")),
                    )
                )
        return laps

    def get_lap_times(self, year: int, series: Series, race_id: int) -> List[RaceLaps]:
        url = f"{self.DOMAIN}/{year}/{series.value}/{race_id}/lap-times.json"
        response_json = self.safe_get(url)
        output = []
        for data in response_json["laps"]:
            data.update({"race_id": race_id})
            output.append(RaceLaps.model_validate(data))
        return output

    def get_pit_data(self, series: Series, race_id: int) -> List[PitData]:
        url = f"{self.DOMAIN}/live/series_{series.value}/{race_id}/live-pit-data.json"
        response_json = self.safe_get(url)
        pits = []
        for data in response_json:
            data.update({"race_id": race_id})
            pits.append(PitData.model_validate(data))
        return pits

    def get_weekend_data(self, year: int, series: Series, race_id: int) -> WeekendInfo:
        url = f"{self.DOMAIN}/{year}/{series.value}/{race_id}/weekend-feed.json"
        response_json = self.safe_get(url)
        response_json.update({"race_id": race_id})
        return WeekendInfo.model_validate(response_json)

    def get_loopstats(self, year: int, series: Series, race_id: int) -> RaceLoopStat:
        url = f"{super().DOMAIN}/loopstats/prod/{year}/{series.value}/{race_id}.json"
        response_json = self.safe_get(url)
        return RaceLoopStat.model_validate(response_json[0])
