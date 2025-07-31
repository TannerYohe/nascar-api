"""Live repository module for NASCAR API operations.

This module provides the live repository class that handles requests
for real-time race data from the NASCAR API.
"""

from typing import List

from nascar_api.enums import Series
from nascar_api.models import (
    FlagData,
    LiveInfo,
    PointsData,
)

from .base import NascarRepo


class LiveNascarFeedRepo(NascarRepo):
    """Repository for accessing live NASCAR race data.

    Provides methods to retrieve real-time race information including
    live flags, race feed data, and live points standings.
    """

    DOMAIN = f"{NascarRepo.DOMAIN}/live/feeds"

    def get_live_flags(self) -> List[FlagData]:
        """Retrieve current flag data from the live race.

        Returns:
            List of FlagData objects containing current flag states and timing.

        Raises:
            ValidationError: If the API response contains invalid flag data.

        """
        url = f"{self.DOMAIN}/live-flag-data.json"
        response_json = self.safe_get(url)
        flags = []
        for data in response_json:
            flags.append(FlagData.model_validate(data))
        return flags

    def get_live_feed(self) -> LiveInfo:
        """Retrieve comprehensive live race feed information.

        Returns:
            LiveInfo object containing current race status, vehicle information,
            and other live race data.

        Raises:
            ValidationError: If the API response contains invalid live feed data.

        """
        url = f"{self.DOMAIN}/live-feed.json"
        response_json = self.safe_get(url)
        return LiveInfo.model_validate(response_json)

    def get_live_points(self, series: Series, race_id: int) -> List[PointsData]:
        """Retrieve live points standings for a specific race.

        Args:
            series: The series the race belongs to.
            race_id: The unique identifier for the race.

        Returns:
            List of PointsData objects containing current points standings.

        Raises:
            ValidationError: If the API response contains invalid points data.

        """
        url = f"{self.DOMAIN}/series_{series.value}/{race_id}/live_points.json"
        response_json = self.safe_get(url)
        points = []
        for data in response_json:
            points.append(PointsData.model_validate(data))
        return points
