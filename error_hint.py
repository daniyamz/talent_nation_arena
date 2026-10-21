"""
Implement error_hint(error_type). Return a helpful debugging hint for common Python errors.
For NameError return Check variable names and spelling. For TypeError return Check the types before using an operator.
For ValueError return Check whether the value can be converted. For ZeroDivisionError return Check that the denominator is not zero. 
For IndexError return Check the index is inside the valid range. For anything else return Read the traceback carefully.
"""
def error_hint(error_type):
   match error_type:
      case "NameError":
         return "Check variable names and spelling."
      case "TypeError":
         return "Check the type before using an operator."
      case "ValueError":
         return "Check whether the value can be canverted."
      case "ZeroDivisionError":
         return "Check that the denominator is not zero."
      case "IndexError":
         return "Check the index is inside the valid range"
      case _:
         return "Read the trackback carefully."
print(error_hint("IndexError"))