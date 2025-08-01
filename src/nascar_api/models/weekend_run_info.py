"""Weekend run information models for NASCAR API data structures.

This module contains models for weekend run data including
practice sessions, qualifying runs, and other timed events.
"""

from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, BeforeValidator, Field
from typing_extensions import Annotated

from .util import optional_str_to_int


class WeekendRunInfo(BaseModel):
    """Represents weekend run information for timed events.

    Contains data about practice sessions, qualifying runs,
    and other timed events during a race weekend.
    """

    class Result(BaseModel):
        """Represents a driver's result in a specific run.

        Contains driver performance data including lap times,
        speeds, and finishing position for timed events.
        """

        run_id: int
        car_number: Annotated[int, BeforeValidator(optional_str_to_int)]
        vehicle_number: Annotated[
            Optional[int], BeforeValidator(optional_str_to_int)
        ] = Field(default=None)
        manufacturer: Optional[str] = Field(default=None)
        driver_id: int
        driver_name: Optional[str] = Field(default=None)
        finishing_position: int
        best_lap_time: float
        best_lap_speed: float
        best_lap_number: int
        laps_completed: int
        comment: Optional[str] = Field(default=None)
        delta_leader: float
        disqualified: Optional[bool] = Field(default=None)

    weekend_run_id: int
    race_id: int
    timing_run_id: int
    run_type: int
    run_name: str
    run_date: datetime
    run_date_utc: Optional[datetime] = Field(default=None)
    results: List[Result]
