from fuel import gauge, convert
import pytest

def test_c_right():
    assert convert("50/100") == 50 and gauge(50) == "50%"
    assert convert("99/100") == 99 and gauge(99) == "F"
    assert convert("1/100") == 1 and gauge(1) == "E"


def test_zero_division_err():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_val_err():
    with pytest.raises(ValueError):
        convert("cat/dog")