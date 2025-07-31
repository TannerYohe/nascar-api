from typing import List, Optional

from pydantic import BaseModel, BeforeValidator, Field
from typing_extensions import Annotated

from nascar_api.enums import Flag

from .base_race_info import BaseRaceInfo
from .pit_data import BasePitData
from .util import optional_str_to_int


class WeekendRaceInfo(BaseRaceInfo):
    class CautionSegment(BaseModel):
        race_id: int
        start_lap: int
        end_lap: int
        reason: str
        comment: str
        beneficiary_car_number: Annotated[
            Optional[int], BeforeValidator(optional_str_to_int)
        ] = Field(default=None)
        flag_state: Flag

    class RaceLeader(BaseModel):
        start_lap: int
        end_lap: int
        car_number: int
        race_id: int

    class StageResult(BaseModel):
        class Result(BaseModel):
            driver_fullname: str
            driver_id: int
            car_number: int
            finishing_position: int
            stage_points: int

        stage_number: int
        results: List[Result]

    class WeekendResult(BaseModel):
        car_make: str
        car_model: Optional[str] = Field(default=None)
        car_number: int
        crew_chief_fullname: Optional[str] = Field(default=None)
        crew_chief_id: Optional[int] = Field(default=None)
        diff_laps: Optional[int] = Field(default=None)
        diff_time: Optional[int] = Field(default=None)
        disqualified: Optional[bool] = Field(default=None)
        driver_fullname: str
        driver_hometown: Optional[str] = Field(default=None)
        driver_id: int
        finishing_position: int
        finishing_status: str
        hometown_city: str
        hometown_country: Optional[str] = Field(default=None)
        hometown_state: str
        laps_complete: Optional[int] = Field(default=None)
        laps_led: int
        official_car_number: int
        owner_fullname: str
        owner_id: int
        playoff_points_earned: Optional[int] = Field(default=None)
        points_delta: int
        points_earned: int
        points_position: int
        qualifying_order: int
        qualifying_position: int
        qualifying_speed: float
        race_id: int
        race_season: int
        result_id: int
        series_id: int
        sponsor: str
        starting_position: int
        team_id: int
        team_name: str
        times_led: int
        winnings: int

    class PitReport(BasePitData):
        infraction: Optional[str] = Field(default=None)

    stage_4_laps: Optional[int] = Field(default=None)
    results: List[WeekendResult]
    caution_segments: List[CautionSegment]
    race_leaders: List[RaceLeader]
    stage_results: List[StageResult] = Field(default=[])
    pit_reports: List[PitReport] = Field(default=[])
