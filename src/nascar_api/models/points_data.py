from pydantic import BaseModel, BeforeValidator
from typing import Optional
from nascar_api.enums import Series
from typing_extensions import Annotated
from .util import optional_str_to_int, bad_int_to_series


class PointsData(BaseModel):
    bonus_points: int
    car_number: Annotated[Optional[int], BeforeValidator(optional_str_to_int)]
    delta_leader: int
    delta_next: int
    first_name: str
    driver_id: int
    is_in_chase: bool
    is_points_eligible: bool
    is_rookie: bool
    last_name: str
    membership_id: int
    points: int
    points_position: int
    points_earned_this_race: int
    stage_1_points: int
    stage_1_winner: bool
    stage_2_points: int
    stage_2_winner: bool
    stage_3_points: int
    stage_3_winner: bool
    wins: int
    top_5: int
    top_10: int
    poles: int
    series_id: Annotated[Optional[Series], BeforeValidator(bad_int_to_series)]
    race_id: int
    run_id: int
