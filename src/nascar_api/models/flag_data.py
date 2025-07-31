from typing import Optional

from pydantic import BaseModel

from nascar_api.enums import Flag


class FlagData(BaseModel):
    lap_number: int
    flag_state: Flag
    elapsed_time: float
    comment: Optional[str]
    beneficiary: Optional[str]
    time_of_day: float
    time_of_day_os: str
