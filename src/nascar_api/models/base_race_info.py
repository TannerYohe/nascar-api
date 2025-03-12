from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
from enums import Series


class Event(BaseModel):
    event_name: str
    notes: str
    start_time_utc: datetime
    run_type: int


class BaseRaceInfo(BaseModel):
    class Infraction(BaseModel):
        car_number: int
        driver_fullname: Optional[str] = Field(default=None)
        driver_id: Optional[int] = Field(default=None)
        infraction: str
        lap: int
        lap_assessed: int
        notes: str
        penalty: str

    race_id: int
    series_id: Series
    race_season: int
    race_name: str
    race_type_id: int
    restrictor_plate: bool
    track_id: int
    track_name: str
    date_scheduled: datetime
    race_date: datetime
    qualifying_date: datetime
    tunein_date: Optional[datetime] = Field(default=None)
    scheduled_distance: float
    actual_distance: float
    scheduled_laps: int
    actual_laps: int
    stage_1_laps: Optional[int] = Field(default=None)
    stage_2_laps: Optional[int] = Field(default=None)
    stage_3_laps: Optional[int] = Field(default=None)
    number_of_cars_in_field: int
    pole_winner_driver_id: int
    pole_winner_speed: float
    number_of_lead_changes: int
    number_of_leaders: int
    number_of_cautions: int
    number_of_caution_laps: int
    average_speed: float
    total_race_time: Optional[str] = Field(default=None)
    margin_of_victory: Optional[str] = Field(default=None)
    race_purse: float
    race_comments: Optional[str] = Field(default=None)
    attendance: int
    infractions: Optional[List[Infraction]] = Field(default=[])
    schedule: List[Event] = Field(default=[])
    radio_broadcaster: Optional[str] = Field(default=None)
    television_broadcaster: str
    satellite_radio_broadcaster: Optional[str] = Field(default=None)
    master_race_id: int
    inspection_complete: Optional[bool] = Field(default=None)
    playoff_round: Optional[int] = Field(default=None)
