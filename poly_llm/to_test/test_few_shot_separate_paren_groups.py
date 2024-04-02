import unittest
from separate_paren_groups import separate_paren_groups
class TestSeperateParenthesisGroups(unittest.TestCase):
    """Tests for the `separate_parenthesis_group` function."""
    def test_simple_case(self):
        """Simple test case with four parenthetical groups."""
        input_string = "(()()) ((())) () ((())()())"
        expected_output = ["(()())", "((()))", "()", "((())()())"]
        actual_output = separate_paren_groups(input_string)
        self.assertCountEqual(expected_output, actual_output)
    def test_nested_and_overlapping_groups(self):
        """Input string with nested and overlapping groups."""
        input_string = "(()) ((())) (()()) (((())))"
        expected_output = ["(())", "((()))", "(()())", "(((())))"]
        actual_output = separate_paren_groups(input_string)
        self.assertCountEqual(expected_output, actual_output)
    