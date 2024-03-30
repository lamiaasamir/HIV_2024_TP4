import unittest
from closest_integer import closest_integer
class TestClosestIntegerFunction(unittest.TestCase):
    """Tests for the `closest_integer` function."""
    def test_positive_integers(self):
        """Test positive integers as input values."""
        self.assertEqual(closest_integer('9'), 9)
        self.assertEqual(closest_integer('786'), 786)
        self.assertEqual(closest_integer('12345'), 12345)
    def test_negative_integers(self):
        """Test negative integers as input values."""
        self.assertEqual(closest_integer('-9'), -9)
        self.assertEqual(closest_integer('-786'), -786)
        self.assertEqual(closest_integer('-12345'), -12345)
    def test_floating_point_numbers(self):
        """Test floating point numbers as input values."""
        self.assertEqual(closest_integer('9.1'), 9)
        self.assertEqual(closest_integer('9.5'), 10)
        self.assertEqual(closest_integer('9.9'), 10)
        self.assertEqual(closest_integer('-9.1'), -9)
        self.assertEqual(closest_integer('-9.5'), -10)
        self.assertEqual(closest_integer('-9.9'), -10)
