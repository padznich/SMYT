# test.py
import unittest

from regexp_method import cut
from string_method import cut_s


class RegexpTestCase(unittest.TestCase):
    """Tests for regexp.py."""

    def test_input_type(self):
        """Type error handler"""
        self.assertTrue(cut(1) == "It must be a string.")
        self.assertTrue(cut([]) == "It must be a string.")

    def test_output(self):
        """Check output"""
        self.assertTrue(cut('') == '')
        self.assertTrue(cut(')') == ')')
        self.assertTrue(cut('(') == '')
        self.assertTrue(cut(')d') == ')d')
        self.assertTrue(cut('(d') == '')
        self.assertTrue(cut('(d)') == '(d)')
        self.assertTrue(cut('(d)(') == '(d)')
        self.assertTrue(cut('(d)((((((') == '(d)')
        self.assertTrue(cut('(d)))((((((') == '(d)))')
        self.assertTrue(cut('esdfd((esdf)(es)dsa(df') == 'esdfd((esdf)(es)dsa')


class StringTestCase(unittest.TestCase):
    """Tests for regexp.py."""

    def test_input_type(self):
        """Type error handler"""
        self.assertTrue(cut_s(1) == "It must be a string.")
        self.assertTrue(cut_s([]) == "It must be a string.")

    def test_output(self):
        """Check output"""
        self.assertTrue(cut_s('') == '')
        self.assertTrue(cut_s(')') == ')')
        self.assertTrue(cut_s('(') == '')
        self.assertTrue(cut_s(')d') == ')d')
        self.assertTrue(cut_s('(d') == '')
        self.assertTrue(cut_s('(d)') == '(d)')
        self.assertTrue(cut_s('(d)(') == '(d)')
        self.assertTrue(cut_s('(d)((((((') == '(d)')
        self.assertTrue(cut_s('(d)))((((((') == '(d)))')
        self.assertTrue(cut_s('esdfd((esdf)(es)dsa(df') == 'esdfd((esdf)(es)dsa')


if __name__ == '__main__':
    unittest.main()
