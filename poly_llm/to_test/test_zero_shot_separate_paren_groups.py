import unittest
from separate_paren_groups import separate_paren_groups
class TestSeperateParenthesisGroups(unittest.TestCase):
    def test_separate_parenthesis_groups(self):
        self.assertEqual(separate_paren_groups(""), [])
        self.assertEqual(separate_paren_groups("((()))"), ["((()))"])
        self.assertEqual(separate_paren_groups("(a)(b)"), ["(a)", "(b)"])
        self.assertEqual(separate_paren_groups("(ab)(cd)"), ["(ab)", "(cd)"])
        self.assertEqual(separate_paren_groups("((a)(b))"), ["((a)(b))"])
        self.assertRaises(ValueError, separate_paren_groups, "(") # Unbalanced parenthesis
        self.assertRaises(ValueError, separate_paren_groups, ")") # Unbalanced parenthesis
        self.assertRaises(ValueError, separate_paren_groups, "abcde") # No parenthesis
        self.assertRaises(TypeError, separate_paren_groups, None) # Not a valid argument type