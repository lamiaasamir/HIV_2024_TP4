def test_numerical_letter_grade(numerical_letter_grade):
    assert numerical_letter_grade([1.2]) == ['D+']
    assert numerical_letter_grade([1.2, 1.2]) == ['D+', 'D+']
    assert numerical_letter_grade([1.2, 1.2, 1.2]) == ['D+', 'D+', 'D+']
    
