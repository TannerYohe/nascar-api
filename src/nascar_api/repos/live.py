from typing import List
from nascar_api.models import (
    FlagData,
    PointsData,
    LiveInfo,
)
from nascar_api.enums import Series
from .base import NascarRepo


class LiveNascarFeedRepo(NascarRepo):
    DOMAIN = f"{NascarRepo.DOMAIN}/live/feeds"

    def get_live_flags(self) -> List[FlagData]:
        url = f"{self.DOMAIN}/live-flag-data.json"
        response_json = self.safe_get(url)
        flags = []
        for data in response_json:
            flags.append(FlagData.model_validate(data))
        return flags

    def get_live_feed(self) -> LiveInfo:
        url = f"{self.DOMAIN}/live-feed.json"
        response_json = self.safe_get(url)
        return LiveInfo.model_validate(response_json)

    def get_live_points(self, series: Series, race_id: int) -> List[PointsData]:
        url = f"{self.DOMAIN}/series_{series.value}/{race_id}/live_points.json"
        response_json = self.safe_get(url)
        points = []
        for data in response_json:
            points.append(PointsData.model_validate(data))
        return points
