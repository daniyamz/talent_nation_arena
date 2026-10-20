import unittest

from exact_calculator import calculator

class TestCalculator(unittest.TestCase):
    #Test for invalide input
    

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
        left = 3
        right = 2
        operator = "+"

        self.assertEqual(calculator(left, operator, right), 5)

    # Test for subtraction 
    def test_subtraction(self):
        left = 3
        right = 2
        operator = "-"
        self.assertEqual(calculator(left,operator, right), 1)

    # Test for Multiplication
    def test_multiplication(self):
        left = 3
        right = 2
        operator = "*"
        self.assertEqual(calculator(left, operator, right), 6)
    
    # Test for exponent
    def test_exponent(self):
        operator = "**"
        self.assertEqual(calculator(2, operator, 3), 8)
if __name__ =="__main__":
    unittest.main
