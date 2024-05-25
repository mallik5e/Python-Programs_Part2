import re
pattern=r"[a-zA-Z]+ \d+" ##this finds all pattern that begins with character followed by space and digits
matches=re.findall(pattern,"LXT 2013, VXI 2015, VDI 20104, Maruti suzuki cars in india")
for match in matches:
    print(match,end=" ")