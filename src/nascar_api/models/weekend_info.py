"""Weekend information models for NASCAR API data structures.

This module contains models for weekend event information,
including race and run data for multi-day racing events.
"""

from typing import List

from pydantic import BaseModel

from .weekend_race_info import WeekendRaceInfo
from .weekend_run_info import WeekendRunInfo


class WeekendInfo(BaseModel):
    """Represents comprehensive weekend event information.

    Contains race and run data for an entire racing weekend,
    including multiple races and practice/qualifying sessions.
    """

    race_id: int
    weekend_race: List[WeekendRaceInfo]
    weekend_runs: List[WeekendRunInfo]
