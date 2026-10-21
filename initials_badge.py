"""
Implement initials_badge(full_name). Remove leading and trailing spaces, split the name into words, 
take the first character of each word, convert each initial to uppercase, and return the initials joined with dots. 
The returned badge should end with a dot.
"""

def initials_badge(full_name):
    full_name = full_name.strip()
    new_full_name = full_name.split()
    words = []
    i=0
    while i < len(new_full_name):
        word = new_full_name[i][0].upper()
        words.append(word)
        i += 1
    return(".".join(words) + ".")
print(initials_badge("daniel terkimbi Terungwa"))