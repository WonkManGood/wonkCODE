from fuel import convert, gauge
import pytest

def test_fraction_to_int():
    assert convert("1/4") == 25
    assert convert("1/2") == 50
    assert convert("1/3") == 33

def test_zero_div():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_value():
    with pytest.raises(ValueError):
        convert("2/1")

def test_int_to_fraction():
    assert gauge(25) == "25%"
    assert gauge(99) == "F"
    assert gauge(1) == "E"
