import unittest

from exact_calculator import calculator

class TestCalculator(unittest.TestCase):

    #Test for invalide input
    def test_convert(self):
        expected = "Invalid Number"
        got = calculator("ten", "+", "5")
        self.assertEqual(expected, got)
    # Test for ZerodivisionError
    def test_zerodivision_error(self):
        p= ""
        try:
            if p =="/":
                self.assertEqual(calculator(4, p, 2), 2)
            elif p=="%":
                self.assertEqual((4, p, 2), 0)
        except ZeroDivisionError:
            self.assertEqual((2, p, 0), "Cannot divide by zero")
    # Test for addition
    def test_addition(self):
        expected = 5
        got = calculator("2", "+", "3")
        self.assertEqual(expected, got)
    # Test for subtraction
    def test_subtraction(self):
        expected = 1
        got = calculator("3", "-", "2")
        self.assertEqual(expected, got)

    # Test for Multiplication
    def test_multiplication(self):
        expected = 1
        got = calculator("3", "-", "2")
        self.assertEqual(expected, got)
    
    # Test for exponent
    def test_exponent(self):
        operator = "**"
        self.assertEqual(calculator(2, operator, 3), 8)
if __name__ =="__main__":
    unittest.main
