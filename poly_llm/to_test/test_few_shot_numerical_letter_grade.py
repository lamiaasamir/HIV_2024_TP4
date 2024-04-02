import unittest
from numerical_letter_grade import numerical_letter_grade
class NumericalLetterGradeConverterTest(unittest.TestCase):
    """Tests for the `numerical_letter_grade` function."""
    def test_all_cases(self):
        """Test all defined cases."""
        tests = {
            'A+': [4.0],
            'A': [3.8, 3.9],
            'B+': [3.1, 3.2],
            'B': [2.8, 2.9],
            'B-': [2.4, 2.5, 2.6, 2.7],
            'C+': [2.1, 2.2],
            'C': [1.8, 1.9],
            'C-': [1.4, 1.5, 1.6, 1.7],
            'D+': [1.1, 1.2],
            'D': [0.8, 0.9],
            'D-': [0.1]
            }
        for letter_grade, gpas in tests.items():
            for gpa in gpas:
                result = numerical_letter_grade([gpa])
                self.assertListEqual(result, [letter_grade])