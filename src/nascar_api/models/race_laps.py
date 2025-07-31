from typing import List, Optional

from pydantic import BaseModel, BeforeValidator, Field
from typing_extensions import Annotated

from .util import optional_str_to_float


class LapInfo(BaseModel):
    lap: int = Field(alias="Lap")
    lap_time: Optional[float] = Field(alias="LapTime")
    lap_speed: Annotated[Optional[float], BeforeValidator(optional_str_to_float)] = Field(
        alias="LapSpeed"
    )
    running_pos: int = Field(alias="RunningPos")


class RaceLaps(BaseModel):
    race_id: int
    number: int = Field(alias="Number")
    full_name: str = Field(alias="FullName")
    manufacturer: str = Field(alias="Manufacturer")
    position: int = Field(alias="RunningPos")
    driver_id: int = Field(alias="NASCARDriverID")
    laps: List[LapInfo] = Field(alias="Laps")
