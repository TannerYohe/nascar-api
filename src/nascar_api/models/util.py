import locale
import re
from typing import Optional

from nascar_api.enums import Flag, Series


def get_series_str(series: Series) -> str:
    """Convert a Series enum to its human-readable string representation.
    
    Args:
        series: The Series enum value to convert.
    
    Returns:
        Human-readable string representation of the series.
        
    Raises:
        ValueError: If the series enum value is not recognized.
    """
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
    """Convert a Flag enum to its human-readable string representation.
    
    Args:
        flag: The Flag enum value to convert.
    
    Returns:
        Human-readable string representation of the flag.
        
    Raises:
        ValueError: If the flag enum value is not recognized.
    """
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
    """Convert an optional string to an integer, handling various formats.
    
    This function attempts to extract integer values from strings that may contain
    commas, decimal points, or other non-numeric characters. It will extract the
    first sequence of digits found in the string.
    
    Args:
        input_value: The string to convert, or None.
    
    Returns:
        The extracted integer value, or None if no valid integer could be found.
        
    Examples:
        >>> optional_str_to_int("123")
        123
        >>> optional_str_to_int("1,234")
        1234
        >>> optional_str_to_int("abc123xyz")
        123
        >>> optional_str_to_int(None)
        None
    """
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
    """Convert an optional string to a float, handling comma-separated numbers.
    
    This function handles strings that may contain comma-separated numbers
    (e.g., "1,234.56") and converts them to float values.
    
    Args:
        input_value: The string to convert, or None.
    
    Returns:
        The converted float value, or None if the input is empty or invalid.
        
    Examples:
        >>> optional_str_to_float("123.45")
        123.45
        >>> optional_str_to_float("1,234.56")
        1234.56
        >>> optional_str_to_float(None)
        None
    """
    if input_value:
        if isinstance(input_value, float):
            return input_value
        if "," in input_value:
            return comma_str_to_float(input_value)
        else:
            return float(input_value)
    return None

def bad_int_to_series(int_value: Optional[int]) -> Optional[int]:
    """Convert an integer to a series ID if it's within the valid range.
    
    This function validates that an integer represents a valid series ID.
    Valid series IDs are 1, 2, and 3 (corresponding to Cup, Xfinity, and Truck series).
    
    Args:
        int_value: The integer to validate, or None.
    
    Returns:
        The validated series ID if valid, or None if invalid or None.
        
    Examples:
        >>> bad_int_to_series(1)
        1
        >>> bad_int_to_series(4)
        None
        >>> bad_int_to_series(None)
        None
    """
    if int_value is None:
        return None
    if 0 < int_value < 4:
        return int_value
    return None


def comma_str_to_float(input_value: Optional[str]) -> Optional[float]:
    """Convert a comma-separated string to a float using locale-aware parsing.
    
    This function uses the locale module to properly parse numbers that contain
    commas as thousand separators (e.g., "1,234.56").
    
    Args:
        input_value: The comma-separated string to convert, or None.
    
    Returns:
        The parsed float value, or None if the input is empty or invalid.
        
    Examples:
        >>> comma_str_to_float("1,234.56")
        1234.56
        >>> comma_str_to_float("1,000")
        1000.0
        >>> comma_str_to_float(None)
        None
    """
    if not input_value:
        return None
    locale.setlocale(locale.LC_ALL, "en_US.UTF-8")
    return locale.atof(input_value)
