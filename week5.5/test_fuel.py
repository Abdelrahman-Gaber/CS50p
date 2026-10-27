from fuel import convert
from fuel import gauge
import pytest

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert('0/0')

def test_negative_number():
    with pytest.raises(ValueError):
        convert('-15/30')

    with pytest.raises(ValueError):
            convert('15/-30')

    with pytest.raises(ValueError):
            convert('-15/-30')

def test_E():
     assert gauge(convert('1/100')) == 'E'

def test_F():
     assert gauge(convert('99/100')) == 'F'


def test_values():
     assert gauge(convert('50/100')) == '50%'