import re
pattern = r"[\w.-]+@[\w.-]+"
string="please send your feedback at info@oxford.com"
match=re.search(pattern,string)
if match:
    print("email to: ",match.group())
else:
    print("no match")