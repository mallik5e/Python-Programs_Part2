import re
string="she sells sea shells on the sea shore"
pattern1="sells"
if re.search(pattern1,string):
    print("match found")
else:
    print(pattern1,"is not present in string")