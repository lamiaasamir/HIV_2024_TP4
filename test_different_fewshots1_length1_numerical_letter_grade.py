def test_numerical_letter_grade(numerical_letter_grade):
    assert numerical_letter_grade([4.0, 3.8, 3.5, 3.1, 3, 2.7]) == ['A+', 'A','A-','B+', 'B', 'B-']
