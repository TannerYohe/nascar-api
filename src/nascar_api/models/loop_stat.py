"""Loop statistics models for NASCAR API race data.

This module contains models for loop statistics which provide
detailed performance metrics for drivers during races.
"""

from typing import List

from pydantic import BaseModel

from nascar_api.enums import Series


class DriverLoopStat(BaseModel):
    """Represents loop statistics for a specific driver.

    Contains comprehensive performance metrics including
    position changes, passing statistics, and race ratings.
    """

    driver_id: int
    start_ps: int
    mid_ps: int
    ps: int
    closing_ps: int
    closing_laps_diff: int
    best_ps: int
    avg_ps: float
    worst_ps: int
    passes_gf: int
    passing_diff: int
    passed_gf: int
    quality_passes: int
    fast_laps: int
    top15_laps: int
    lead_laps: int
    laps: int
    rating: float


class RaceLoopStat(BaseModel):
    """Represents loop statistics for an entire race.

    Contains race-level statistics and driver performance
    data for all participants.
    """

    race_id: int
    race_name: str
    series_id: Series
    sch_laps: int
    act_laps: int
    drivers: List[DriverLoopStat]
