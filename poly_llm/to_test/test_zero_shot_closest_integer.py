import pytest
from closest_integer import closest_integer
# Assuming your code is in module named "mycode"
# Replace "<module>" with the actual name of your module

@pytest.mark.parametrize('input_val, expected', [
    ("10", 10),
    ("15.3", 15),
])
def test_closest_integer(input_val, expected):
    assert closest_integer(input_val) == expected

@pytest.mark.parametrize('input_val, expected', [
    ('14.5', 15),
    ('-14.5', -15),
])
def test_rounded_away_zero(input_val, expected):
    assert closest_integer(input_val) == expected

def test_empty():
    assert closest_integer('0') == 0