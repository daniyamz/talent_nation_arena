import unittest
from error_hint import error_hint

class TestErrorHint(unittest.TestCase):
    def test_NameError(self):
        expected = "Check variable names and spelling."
        got = error_hint("NameError")
        self.assertEqual(expected, got)
    def test_ValueError(self):
        expected = "Check whether the value can be canverted."
        got = error_hint("ValueError")
        self.assertEqual(expected, got)
    def test_TypeError(self):
        expected = "Check the type before using an operator."
        got = error_hint("TypeError")
        self.assertEqual(expected, got)
    def test_ZrrorDivisioError(self):
        expected = "Check that the denominator is not zero."
        got = error_hint("ZeroDivisionError")
        self.assertEqual(expected, got)
    def test_IndextError(self):
        expected = "Check the index is inside the valid range."
        got = error_hint("IndexError")
        self.assertEqual(expected, got)
    def test_invalid(self):
        expected = "Read the trackback carefully."
        got = error_hint("")
        self.assertEqual(expected, got)
if __name__ == "__main__":
    unittest.main