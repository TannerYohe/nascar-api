from pydantic import BaseModel
from typing import List
from enums import Flag, Series
from datetime import datetime


class LiveVehicleInfo(BaseModel):
    class LapInterval(BaseModel):
        start_lap: int
        end_lap: int

    class Pitstop(BaseModel):
        positions_gained_lossed: int
        pit_in_elapsed_time: float
        pit_in_lap_count: int
        pit_in_leader_lap: int
        pit_out_elapsed_time: float
        pit_in_rank: int
        pit_out_rank: int

    average_restart_speed: float
    average_running_position: float
    average_speed: float
    best_lap: int
    best_lap_speed: float
    best_lap_time: float
    vehicle_manufacturer: str
    vehicle_number: int
    vehicle_elapsed_time: float
    fastest_laps_run: int
    laps_position_improved: int
    laps_completed: int
    laps_led: List[LapInterval]
    last_lap_speed: float
    last_lap_time: float
    passes_made: int
    passing_differential: int
    position_differential_last_10_percent: int
    qualifying_status: int
    running_position: int
    status: int
    delta: float
    sponsor_name: str
    starting_position: int
    times_passed: int
    quality_passes: int
    is_on_track: bool
    is_on_dvp: bool
    pit_stops: List[Pitstop]


class LiveInfo(BaseModel):
    class Stage(BaseModel):
        stage_num: int
        finish_at_lap: int
        laps_in_stage: int

    lap_number: int
    elapsed_time: int
    flag_state: Flag
    race_id: int
    laps_in_race: int
    laps_to_go: int
    run_id: int
    run_name: str
    series_id: Series
    time_of_day: int
    time_of_day_os: datetime
    track_id: int
    track_length: float
    track_name: str
    run_type: int
    number_of_caution_segments: int
    number_of_caution_laps: int
    number_of_lead_changes: int
    number_of_leaders: int
    avg_diff_1to3: int
    stage: Stage
    vehicles: List[LiveVehicleInfo]
