"""Pit data models for NASCAR API race information.

This module contains models for pit stop data including
timing information, tire changes, and pit stop performance metrics.
"""

from typing import Optional

from pydantic import BaseModel, Field

from nascar_api.enums import Flag


class BasePitData(BaseModel):
    """Base model for pit stop data containing comprehensive pit information.

    Contains detailed timing data, tire change information,
    and pit stop performance metrics.
    """

    vehicle_number: int
    driver_name: str
    vehicle_manufacturer: str
    leader_lap: int
    lap_count: int
    pit_in_flag_status: Flag
    pit_out_flag_status: Flag
    pit_in_race_time: float
    pit_out_race_time: float
    total_duration: float
    box_stop_race_time: float
    box_leave_race_time: float
    pit_stop_duration: float
    in_travel_duration: float
    out_travel_duration: float
    pit_stop_type: str
    left_front_tire_changed: bool
    right_front_tire_changed: bool
    left_rear_tire_changed: bool
    right_rear_tire_changed: bool
    previous_lap_time: float
    next_lap_time: float
    pit_in_rank: Optional[int] = Field(default=None)
    pit_out_rank: Optional[int] = Field(default=None)
    positions_gained_lost: Optional[int] = Field(default=None)


class PitData(BasePitData):
    """Extended pit data model with race identification.

    Extends BasePitData to include race-specific information.
    """

    race_id: int
