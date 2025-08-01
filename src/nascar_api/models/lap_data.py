"""Lap data models for NASCAR API race information.

This module contains models for lap-by-lap race data,
including flag states, notes, and driver information.
"""

from typing import List

from pydantic import BaseModel

from nascar_api.enums import Flag


class LapData(BaseModel):
    """Represents lap-specific data during a race.

    Contains information about flag states, notes, and
    driver IDs associated with each lap.
    """

    race_id: int
    lap_number: int
    flag_state: Flag
    note: str
    note_id: int
    driver_ids: List[int]
