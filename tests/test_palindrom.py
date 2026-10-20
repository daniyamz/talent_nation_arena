import unittest

from manual_palindrome import manual_palindrome

class TestPalindrome(unittest.TestCase):
    def test_radar(self):
        text = "radar"
        expected = True

        got = manual_palindrome(text)

        self.assertEqual(got, expected)
    def test_python(self):
        word = "python"
        expected = False

        got = manual_palindrome(word)

        self.assertEqual(got, expected)
if __name__ == "__main__":
    unittest.main()