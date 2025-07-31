
from nascar_api.enums import Series
from nascar_api.models import FlagData, LiveInfo, PointsData
from nascar_api.repos import LiveNascarFeedRepo
from tests.data_factories.flag_data import FlagDataFactory
from tests.data_factories.live_info import LiveInfoFactory
from tests.data_factories.points_data import PointsDataFactory


def test_get_live_flags(requests_mock):
    repo = LiveNascarFeedRepo()
    mock_flags = [FlagDataFactory.build().model_dump() for _ in range(5)]
    mock_url = f"{repo.DOMAIN}/live-flag-data.json"
    requests_mock.get(mock_url, json=mock_flags)

    flags = repo.get_live_flags()
    assert len(flags) == 5
    assert all([isinstance(flag, FlagData) for flag in flags])


def test_get_live_feed(requests_mock):
    repo = LiveNascarFeedRepo()
    mock_live_info = LiveInfoFactory.build().model_dump(mode="json")
    mock_url = f"{repo.DOMAIN}/live-feed.json"
    requests_mock.get(mock_url, json=mock_live_info)

    live_info = repo.get_live_feed()
    assert isinstance(live_info, LiveInfo)


def test_get_live_points(requests_mock):
    repo = LiveNascarFeedRepo()
    mock_series = Series.CUP
    mock_race_id = 123
    mock_points = [PointsDataFactory.build().model_dump() for _ in range(10)]
    mock_url = f"{repo.DOMAIN}/series_{mock_series.value}/{mock_race_id}/live_points.json"
    requests_mock.get(mock_url, json=mock_points)

    points = repo.get_live_points(mock_series, mock_race_id)
    assert len(points) == 10
    assert all([isinstance(point, PointsData) for point in points])


def test_get_live_points_different_series(requests_mock):
    repo = LiveNascarFeedRepo()
    mock_series = Series.XFINITY
    mock_race_id = 456
    mock_points = [PointsDataFactory.build().model_dump() for _ in range(8)]
    mock_url = f"{repo.DOMAIN}/series_{mock_series.value}/{mock_race_id}/live_points.json"
    requests_mock.get(mock_url, json=mock_points)

    points = repo.get_live_points(mock_series, mock_race_id)
    assert len(points) == 8
    assert all([isinstance(point, PointsData) for point in points])


def test_get_live_flags_empty_response(requests_mock):
    repo = LiveNascarFeedRepo()
    mock_url = f"{repo.DOMAIN}/live-flag-data.json"
    requests_mock.get(mock_url, json=[])

    flags = repo.get_live_flags()
    assert len(flags) == 0


def test_get_live_points_empty_response(requests_mock):
    repo = LiveNascarFeedRepo()
    mock_series = Series.TRUCK
    mock_race_id = 789
    mock_url = f"{repo.DOMAIN}/series_{mock_series.value}/{mock_race_id}/live_points.json"
    requests_mock.get(mock_url, json=[])

    points = repo.get_live_points(mock_series, mock_race_id)
    assert len(points) == 0
