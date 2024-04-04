def test_numerical_letter_grade(numerical_letter_grade):
    assert numerical_letter_grade([4.0, 3.9, 3.0, 2.7, 0.8, 3.8]) == ['A+', 'A', 'B', 'B-', 'D', 'A']