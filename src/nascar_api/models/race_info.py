from typing import Optional

from pydantic import Field

from .base_race_info import BaseRaceInfo


class RaceInfo(BaseRaceInfo):
    is_qualifying_race: Optional[bool] = Field(default=None)
    qualifying_race_no: Optional[int] = Field(default=None)
    qualifying_race_id: Optional[int] = Field(default=None)
    has_qualifying: Optional[bool] = Field(default=None)
    winner_driver_id: Optional[int] = Field(default=None)
    pole_winner_lap_time: Optional[str] = Field(default=None)
