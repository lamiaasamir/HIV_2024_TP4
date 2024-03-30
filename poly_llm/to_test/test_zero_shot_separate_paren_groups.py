import unittest
from separate_paren_groups import separate_paren_groups
class TestSeperateParenthesisGroups(unittest.TestCase):
    def test_separate_parenthesis_groups(self):
        self.assertEqual(separate_paren_groups(""), [])
        self.assertEqual(separate_paren_groups("((()))"), ["((()))"])
        self.assertEqual(separate_paren_groups("(a)(b)"), ["()", "()"])
        self.assertEqual(separate_paren_groups("(ab)(cd)"), ["()", "()"])
        self.assertEqual(separate_paren_groups("((a)(b))"), ["(()())"])