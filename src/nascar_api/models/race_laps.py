"""Race lap data models for NASCAR API race information.

This module contains models for lap-by-lap race data including
lap times, speeds, and position information for drivers.
"""

from typing import List, Optional

from pydantic import BaseModel, BeforeValidator, Field
from typing_extensions import Annotated

from .util import optional_str_to_float


class LapInfo(BaseModel):
    """Represents lap-specific information for a driver.

    Contains lap number, timing data, speed, and position
    information for a specific lap.
    """

    lap: int = Field(alias="Lap")
    lap_time: Optional[float] = Field(alias="LapTime")
    lap_speed: Annotated[
        Optional[float], BeforeValidator(optional_str_to_float)
    ] = Field(alias="LapSpeed")
    running_pos: int = Field(alias="RunningPos")


class RaceLaps(BaseModel):
    """Represents lap data for a specific driver in a race.

    Contains driver information and a list of lap-by-lap
    performance data for the entire race.
    """

    race_id: int
    number: int = Field(alias="Number")
    full_name: str = Field(alias="FullName")
    manufacturer: str = Field(alias="Manufacturer")
    position: int = Field(alias="RunningPos")
    driver_id: int = Field(alias="NASCARDriverID")
    laps: List[LapInfo] = Field(alias="Laps")
