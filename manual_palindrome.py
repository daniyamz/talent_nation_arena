"""
Implement manual_palindrome(text). Ignore spaces and letter case.
Return true if the cleaned text reads the same forward and backward,
otherwise return false. Do not use slicing shorthand or reversed.
Students may need to research manual string reversal.
"""

def manual_palindrome(text):
    text =  text.strip().lower()
    text = text.replace(" ", "")
    cleaned_text = ""
    i = len(text) -1
    while i >=0:
        cleaned_text += text[i]
        i -=1
    if cleaned_text == text:
        return True
    else:
        return False
print(manual_palindrome(" level radar level"))