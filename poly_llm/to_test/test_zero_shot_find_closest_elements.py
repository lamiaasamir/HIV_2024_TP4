import pytest
from find_closest_elements import find_closest_elements
# Assuming your code is in module named "mycode"
# Replace "<module>" with the actual name of your module

@pytest.mark.parametrize('numbers,expected', [
    ([1.0, 2.0, 3.0], (1.0, 2.0)),
    ([1.0, 2.0, 3.0, 4.0, 5.0, 2.2], (2.0, 2.2)),
    ([1.0, 2.0, 3.0, 4.0, 5.0, 2.0], (2.0, 2.0)),
    ([-1.0, 2.0, 3.0, 10.0], (2.0, 3.0)),
    ([1.0, 2.0, 3.0, 4.0, 5.0], (1.0, 2.0)),
])
def test_find_closest_elements(numbers, expected):
    assert find_closest_elements(numbers) == expected