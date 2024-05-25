import re
pattern=r"[aeiou]" ##matches single character in the given string
if re.search(pattern,"clue"):
    print("match clue")
if re.search(pattern,"bcdfg"):
    print("match bcdfg")