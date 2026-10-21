"""
Implement exact_calculator(left, operator, right). 
Convert left and right to numbers. Support addition, subtraction, 
multiplication, division, remainder, and exponent.
If either number cannot be converted, return Invalid number. 
If the operator is not supported, return Invalid operator. 
If division or remainder uses zero on the right side, 
return Cannot divide by zero. Round numeric results to 2 decimal places.
"""

def calculator(left, operator, right):
    try:
        left = int(left)
        right = int(right)
    except ValueError:
        return "Invalid Number"
    try:
        if operator == "/":
            return round((left/right), 2)
        elif operator == "%":
            return round((left%right), 2)
    except ZeroDivisionError:
        return "Cannot divide by zero"
    if operator == "+":
        return left + right
    elif operator == "-":
        return left - right
    elif operator == "*":
        return left*right
    elif operator == "**":
        return left ** right
    else:
        return "Invalid operator"
calculator("t", "%", "0")