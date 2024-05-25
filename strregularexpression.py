import re
string="she sells sea shells on the sea shore"
pattern1="sells"
if re.match(pattern1,string):
    print("match found")
else:
    print(pattern1,"is not present in string")
pattern2="she"
if re.match(pattern2,string):
    print("match found")
else:
    print(pattern2,"not found in the string")