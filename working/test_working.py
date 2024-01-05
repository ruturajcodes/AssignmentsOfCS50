from working import convert

import pytest

def main():
    test_w_f()
    test_timing()
    test_w_hr()
    test_w_min()

def test_w_f():
    with pytest.raises(ValueError):
        convert('9 AM - 9 PM')



def test_timing():
    assert convert('9 AM to 5 PM') == "09:00 to 17:00"
    assert convert('11 PM to 8 AM') == "23:00 to 08:00"
    assert convert('11:30 PM to 8:30 AM') == "23:30 to 08:30"



def test_w_hr():
    with pytest.raises(ValueError):
        convert('13 AM to 17 PM')


def test_w_min():
    with pytest.raises(ValueError):
        convert('8:61 AM to 8:62 PM')

