import pytest
from numerical_letter_grade import numerical_letter_grade
# Assuming your code is in module named "mycode"
# Replace "<module>" with the actual name of your module

@pytest.mark.parametrize('gpas,expected', [
    ([4.0, 3, 1.7, 2, 3.5], ['A+', 'B', 'C-', 'C', 'A-'])
])
def test_numerical_letter_grade(gpas, expected):
    assert numerical_letter_grade(gpas) == expected