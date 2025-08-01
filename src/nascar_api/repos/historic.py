"""Historic repository module for NASCAR API operations.

This module provides the historic repository class that handles requests
for historical race data from the NASCAR API.
"""

import logging
from typing import Any, Dict, List, Optional

from pydantic import ValidationError

from nascar_api.enums import Series
from nascar_api.models import (
    LapData,
    PitData,
    RaceInfo,
    RaceLaps,
    RaceLoopStat,
    WeekendInfo,
)

from .base import NascarRepo

log = logging.getLogger(__name__)

class HistoricNascarRepo(NascarRepo):
    """Repository for accessing historical NASCAR race data.

    Provides methods to retrieve historical race information, lap times,
    pit data, and other race-related data from the NASCAR API.
    """

    DOMAIN = f"{NascarRepo.DOMAIN}/cacher"

    def get_races(
        self, year: int, series: Optional[Series] = None
    ) -> List[RaceInfo]:
        """Retrieve race data for a specific year and optionally a specific series.

        Args:
            year: The year to retrieve races for.
            series: Optional series filter. If None, returns races for all series.

        Returns:
            List of RaceInfo objects containing race details.

        Raises:
            ValidationError: If the API response contains invalid race data.

        """

        def validate_race(json_data: Dict[Any, Any]) -> RaceInfo:
            try:
                return RaceInfo.model_validate(json_data)
            except ValidationError:
                log.error(f"Invalid race object: {json_data}")
                raise

        url = f"{self.DOMAIN}/{year}/race_list_basic.json"
        response_json = self.safe_get(url)
        races = []
        if series:
            for race in response_json[f"series_{series.value}"]:
                races.append(validate_race(race))
        if not series:
            for series in response_json:
                for race in response_json[series]:
                    races.append(validate_race(race))
        return races

    def get_lap_notes(self, year: int, series: Series, race_id: int) -> List[LapData]:
        """Retrieve lap notes and flag data for a specific race.

        Args:
            year: The year of the race.
            series: The series the race belongs to.
            race_id: The unique identifier for the race.

        Returns:
            List of LapData objects containing lap notes and flag information.

        """
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
                        driver_ids=list(filter(None, flag_data.get("DriverIDs"))),
                    )
                )
        return laps

    def get_lap_times(self, year: int, series: Series, race_id: int) -> List[RaceLaps]:
        """Retrieve lap times for a specific race.

        Args:
            year: The year of the race.
            series: The series the race belongs to.
            race_id: The unique identifier for the race.

        Returns:
            List of RaceLaps objects containing lap time data.

        Raises:
            ValidationError: If the API response contains invalid lap time data.

        """
        url = f"{self.DOMAIN}/{year}/{series.value}/{race_id}/lap-times.json"
        response_json = self.safe_get(url)
        output = []
        for data in response_json["laps"]:
            data.update({"race_id": race_id})
            output.append(RaceLaps.model_validate(data))
        return output

    def get_pit_data(self, series: Series, race_id: int) -> List[PitData]:
        """Retrieve pit stop data for a specific race.

        Args:
            series: The series the race belongs to.
            race_id: The unique identifier for the race.

        Returns:
            List of PitData objects containing pit stop information.

        Raises:
            ValidationError: If the API response contains invalid pit data.

        """
        url = f"{self.DOMAIN}/live/series_{series.value}/{race_id}/live-pit-data.json"
        response_json = self.safe_get(url)
        pits = []
        for data in response_json:
            data.update({"race_id": race_id})
            pits.append(PitData.model_validate(data))
        return pits

    def get_weekend_data(
        self, year: int, series: Series, race_id: int
    ) -> WeekendInfo:
        """Retrieve comprehensive weekend information for a specific race.

        Args:
            year: The year of the race.
            series: The series the race belongs to.
            race_id: The unique identifier for the race.

        Returns:
            WeekendInfo object containing comprehensive weekend data.

        Raises:
            ValidationError: If the API response contains invalid weekend data.

        """
        url = f"{self.DOMAIN}/{year}/{series.value}/{race_id}/weekend-feed.json"
        response_json = self.safe_get(url)
        response_json.update({"race_id": race_id})
        return WeekendInfo.model_validate(response_json)

    def get_loopstats(
        self, year: int, series: Series, race_id: int
    ) -> RaceLoopStat:
        """Retrieve loop statistics for a specific race.

        Loop statistics include driver performance metrics such as average speed,
        fastest lap, and other race analytics.

        Args:
            year: The year of the race.
            series: The series the race belongs to.
            race_id: The unique identifier for the race.

        Returns:
            RaceLoopStat object containing loop statistics.

        Raises:
            ValidationError: If the API response contains invalid loop statistics data.

        """
        url = f"{super().DOMAIN}/loopstats/prod/{year}/{series.value}/{race_id}.json"
        response_json = self.safe_get(url)
        return RaceLoopStat.model_validate(response_json[0])
