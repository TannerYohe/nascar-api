# nascar-api

A typed Python client for NASCAR's undocumented Content Feed (CF) API. Provides access to both historical and live race data across the Cup, Xfinity, and Truck series.

Built with [Pydantic](https://docs.pydantic.dev/) for data validation and [tenacity](https://tenacity.readthedocs.io/) for automatic retry logic.

## Installation

```bash
pip install nascar-api
```

Or with Poetry:

```bash
poetry add nascar-api
```

## Quick Start

```python
from nascar_api.repos import HistoricNascarRepo
from nascar_api.enums import Series

repo = HistoricNascarRepo()

# Get all Cup Series races from 2024
races = repo.get_races(2024, Series.CUP)

for race in races:
    print(f"{race.race_name} at {race.track_name} — Winner ID: {race.winner_driver_id}")
```

## Features

### Historical Data

```python
from nascar_api.repos import HistoricNascarRepo
from nascar_api.enums import Series

repo = HistoricNascarRepo()

# Race schedules and results for any year/series
races = repo.get_races(2024, Series.CUP)

# Lap-by-lap timing data
lap_times = repo.get_lap_times(2024, Series.CUP, race_id=5161)

# Lap notes (cautions, incidents, flags)
lap_notes = repo.get_lap_notes(2024, Series.CUP, race_id=5161)

# Pit stop data with detailed timing and tire info
pit_stops = repo.get_pit_data(Series.CUP, race_id=5161)

# Full weekend feed (results, cautions, leaders, stages, pit reports)
weekend = repo.get_weekend_data(2024, Series.CUP, race_id=5161)

# Loop statistics (driver performance metrics)
loop_stats = repo.get_loopstats(2024, Series.CUP, race_id=5161)
```

### Live Race Data

```python
from nascar_api.repos import LiveNascarFeedRepo
from nascar_api.enums import Series

repo = LiveNascarFeedRepo()

# Current flag state across all active races
flags = repo.get_live_flags()

# Full live race feed (positions, speeds, pit stops, vehicle data)
feed = repo.get_live_feed()
for vehicle in feed.vehicles:
    print(f"#{vehicle.vehicle_number} — P{vehicle.running_position}, "
          f"Last Lap: {vehicle.last_lap_speed:.1f} mph")

# Live points standings
points = repo.get_live_points(Series.CUP, race_id=5161)
```

## API Reference

### Repositories

| Class | Description |
|---|---|
| `HistoricNascarRepo` | Historical race data (schedules, results, lap times, pit stops, weekend feeds, loop stats) |
| `LiveNascarFeedRepo` | Real-time race data (live flags, race feed, points standings) |

### Models

| Model | Description |
|---|---|
| `RaceInfo` | Race metadata — schedule, track, distance, laps, cautions, speed, purse, broadcast info |
| `RaceLaps` | Per-driver lap-by-lap timing (lap times, speeds, running position) |
| `LapData` | Lap notes with flag states, incident notes, and involved drivers |
| `PitData` | Pit stop details — timing, tire changes, positions gained/lost |
| `WeekendInfo` | Full weekend container with race results and practice/qualifying runs |
| `WeekendRaceInfo` | Detailed race results, caution segments, race leaders, stage results, pit reports |
| `WeekendRunInfo` | Practice/qualifying session results |
| `LiveInfo` | Live race state — flag, lap, timing, and all vehicle telemetry |
| `FlagData` | Live flag state with timing and beneficiary info |
| `PointsData` | Championship points standings with stage breakdowns |
| `RaceLoopStat` | Race-level loop statistics with per-driver performance metrics |

### Enums

| Enum | Values |
|---|---|
| `Series` | `CUP` (1), `XFINITY` (2), `TRUCK` (3) |
| `Flag` | `GREEN` (1), `YELLOW` (2), `RED` (3), `WHITE` (4), `CHECKERED` (5), `HOT_TRACK` (8), `COLD_TRACK` (9) |

## Retry Behavior

All API requests automatically retry up to 3 times with a 2-second delay on transient failures (5xx errors, JSON decode errors). Requests that receive a 403 (data not available for that endpoint/year) do not retry.

## Requirements

- Python 3.11+
- No API key required — NASCAR's CF API is publicly accessible

## License

[MIT](LICENSE)
