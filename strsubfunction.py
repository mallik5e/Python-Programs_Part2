import re
string="she sells sea shells on the sea sores"
pattern1="sells"
repl="ocean"
new_string=re.sub(pattern1,repl,string,1)
print(new_string)