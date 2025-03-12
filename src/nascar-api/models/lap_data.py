from pydantic import BaseModel
from enums import Flag
from typing import List


class LapData(BaseModel):
    race_id: int
    lap_number: int
    flag_state: Flag
    note: str
    note_id: int
    driver_ids: List[int]
