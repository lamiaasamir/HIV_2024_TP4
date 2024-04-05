def test_numerical_letter_grade(numerical_letter_grade):
    assert numerical_letter_grade([4.0, 3.8, 3.5, 3.1, 3, 2.7, 2.3, 2, 1.7,1.3,1.0,0.7,0]) == ['A+', 'A','A-','B+', 'B', 'B-','C+','C','C-','D+','D','D-','E']
