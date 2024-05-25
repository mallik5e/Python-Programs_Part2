str=input()
temp=str.lower().replace(' ','')
abc=26
count=0
temp1=""
for i in temp:
    if i not in temp1:
        temp+=i
        count+=1
print(str)
print(temp)    
print(temp1)
if(abc==count):
    print('panagram')
print(count)
