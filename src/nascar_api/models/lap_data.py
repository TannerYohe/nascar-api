from typing import List

from pydantic import BaseModel

from nascar_api.enums import Flag


class LapData(BaseModel):
    race_id: int
    lap_number: int
    flag_state: Flag
    note: str
    note_id: int
    driver_ids: List[int]
