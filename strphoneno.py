import re 
list=['7883456789','1234567890','9876543210','8901234567','4576890123']
for i in list:
    result=re.findall(r'[7-9]{1}[0-9]{9}',i)
    if result:
        print(result,end=" ")