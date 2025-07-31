import locale
import re
from typing import Optional

from nascar_api.enums import Flag, Series


def get_series_str(series: Series) -> str:
    match series:
        case Series.CUP:
            return "Cup Series"
        case Series.XFINITY:
            return "Xfinity"
        case Series.TRUCK:
            return "Truck Series"
        case _:
            raise ValueError("Unknown series code")


def get_flag_str(flag: Flag) -> str:
    match flag:
        case Flag.GREEN:
            return "Green"
        case Flag.YELLOW:
            return "Yellow"
        case Flag.RED:
            return "Red"
        case Flag.WHITE:
            return "White"
        case Flag.CHECKERED:
            return "Checkered"
        case Flag.HOT_TRACK:
            return "Hot Track"
        case Flag.COLD_TRACK:
            return "Cold Track"
        case _:
            raise ValueError("Unknown flag code")


def optional_str_to_int(input_value: Optional[str]) -> Optional[int]:
    if input_value:
        if isinstance(input_value, int):
            return input_value
        if input_value.isdigit():
            return int(input_value)
        elif "," in input_value:
            flt = comma_str_to_float(input_value)
            if flt is not None:
                return int(flt)
        else:
            match = re.findall(r"\d+", input_value)
            if match:
                return int(match[0])
    return None

def optional_str_to_float(input_value: Optional[str]) -> Optional[float]:
    if input_value:
        if isinstance(input_value, float):
            return input_value
        if "," in input_value:
            return comma_str_to_float(input_value)
        else:
            return float(input_value)
    return None

def bad_int_to_series(int_value: Optional[int]) -> Optional[int]:
    if int_value is None:
        return None
    if 0 < int_value < 4:
        return int_value
    return None


def comma_str_to_float(input_value: Optional[str]) -> Optional[float]:
    if not input_value:
        return None
    locale.setlocale(locale.LC_ALL, "en_US.UTF-8")
    return locale.atof(input_value)
