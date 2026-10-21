import unittest
from initials_badge import initials_badge

class TestInitialBadge(unittest.TestCase):
    def test_initials(self):
        expected = "P.E."
        got = initials_badge("pete emma")
        self.assertEqual(expected, got)
if __name__ =="__main__":
    unittest.main