import unittest
from find_closest_elements import find_closest_elements
import unittest
class TestClosestElements(unittest.TestCase):
    def test_find_closest_elements(self):
        result = find_closest_elements([-6,-7,8,2])
        expectedResult = (-7,-6)
        self.assertEqual(result, expectedResult)