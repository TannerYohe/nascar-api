from pytest import raises

from nascar_api.models.util import (
    get_series_str,
    get_flag_str,
    optional_str_to_int,
    optional_str_to_float,
    bad_int_to_series
)

from nascar_api.enums import Series, Flag


def test_series_str():
    for series in Series:
        series_str = get_series_str(series)
        assert isinstance(series_str, str)
        assert series_str != ""

def test_series_str_invalid():
    with raises(ValueError):
        get_series_str("InvalidSeries")

def test_flag_str():
    for flag in Flag:
        flag_str = get_flag_str(flag)
        assert isinstance(flag_str, str)
        assert flag_str != ""

def test_flag_str_invalid():
    with raises(ValueError):
        get_flag_str("InvalidFlag")

def test_optional_str_to_int():
    assert optional_str_to_int("123") == 123
    assert optional_str_to_int("1,234") == 1234
    assert optional_str_to_int("1,234.56") == 1234
    assert optional_str_to_int("abc123xyz") == 123
    assert optional_str_to_int(None) is None
    assert optional_str_to_int("") is None
    assert optional_str_to_int("abc") is None
    assert optional_str_to_int("abc123xyz456") == 123
    assert optional_str_to_int(123) == 123

def test_optional_str_to_float():
    assert optional_str_to_float("123") == 123.0
    assert optional_str_to_float("123.45") == 123.45
    assert optional_str_to_float("1,234.56") == 1234.56
    assert optional_str_to_float(None) is None
    assert optional_str_to_float("") is None
    assert optional_str_to_float(123.45) == 123.45

def test_optional_str_to_float_invalid():
    with raises(ValueError):
        optional_str_to_float("abc123.45xyz456")
    with raises(ValueError):
        optional_str_to_float("1,234,567.89.01")
    with raises(ValueError):
        optional_str_to_float("abc")

def test_bad_int_to_series():
    assert bad_int_to_series(1) == 1
    assert bad_int_to_series(2) == 2
    assert bad_int_to_series(3) == 3
    assert bad_int_to_series(4) is None
    assert bad_int_to_series(0) is None