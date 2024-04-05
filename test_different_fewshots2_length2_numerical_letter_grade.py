def test_numerical_letter_grade(numerical_letter_grade):
    assert numerical_letter_grade([4.0, 3, 1.7, 2, 3.5]) == ['A+', 'B', 'C-', 'C', 'A-']
    assert numerical_letter_grade([4.0, 3.8, 3.5, 3.1, 3, 2.7, 2.3, 2, 1.7,1.3,1.0,0.7,0]) == ['A+', 'A','A-','B+', 'B', 'B-','C+','C','C-','D+','D','D-','E']
    assert numerical_letter_grade([1.2]) == ['D+']
    assert numerical_letter_grade([4.0, 3.8, 3.5, 3.1, 3, 2.7, 2.3, 2, 1.7,1.3,1.0,0.7,0]) == ['A+', 'A','A-','B+', 'B', 'B-','C+','C','C-','D+','D','D-','E']
