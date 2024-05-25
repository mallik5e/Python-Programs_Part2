import re 
match=re.search("([0-9]+).*: (.*)", "phone number: 12345678, dob: october 17, 2000")
print(match.group())
print(match.group(1))
print(match.group(2))
print(match.group(1,2))