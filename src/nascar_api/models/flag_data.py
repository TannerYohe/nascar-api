"""Flag data models for NASCAR API race information.

This module contains models for flag-related data during races,
including flag states, timing information, and associated comments.
"""

from typing import Optional

from pydantic import BaseModel

from nascar_api.enums import Flag


class FlagData(BaseModel):
    """Represents flag data for a specific lap during a race.

    Contains information about flag states, timing, and any
    associated comments or beneficiaries.
    """

    lap_number: int
    flag_state: Flag
    elapsed_time: float
    comment: Optional[str]
    beneficiary: Optional[str]
    time_of_day: float
    time_of_day_os: str
