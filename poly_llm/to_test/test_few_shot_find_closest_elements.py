import unittest
import random
from find_closest_elements import find_closest_elements
class FindClosestElementsTest(unittest.TestCase):
    """Tests for the `find_closest_elements` function."""
    def test_basic_case(self):
        """Basic test case with distinct elements."""
        result = find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
        expected_output = (2.0, 2.2)
        self.assertTupleEqual(result, expected_output)
    def test_repeated_element(self):
        """Test case with repeated element."""
        result = find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
        expected_output = (2.0, 2.0)
        self.assertTupleEqual(result, expected_output)
    def test_large_input(self):
        """Large test case with several pairs having similar distances."""
        arr = [i * 1.2 + j / 10 for i in range(-100, 100) for j in range(-100, 100)]
        random.shuffle(arr)
        result = find_closest_elements(arr)
        expected_output = (-1.8, -1.7)
        self.assertTupleEqual(result, expected_output)
    def test_single_element_array(self):
        """Edge case with single element array."""
        with self.assertRaisesRegexp(ValueError, r".*at least two.*"):
            find_closest_elements([1.0])
    def test_two_element_array(self):
        """Special case with two element array."""
        result = find_closest_elements([1.0, 2.0])
        expected_output = (1.0, 2.0)
        self.assertTupleEqual(result, expected_output)
