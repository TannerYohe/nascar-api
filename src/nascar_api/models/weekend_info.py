from pydantic import BaseModel
from typing import List
from .weekend_race_info import WeekendRaceInfo
from .weekend_run_info import WeekendRunInfo


class WeekendInfo(BaseModel):
    race_id: int
    weekend_race: List[WeekendRaceInfo]
    weekend_runs: List[WeekendRunInfo]
