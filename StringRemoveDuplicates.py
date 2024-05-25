str=input()
str1=""
str2=""
for i in str:
    if i not in str1:
        str1+=i 
    else:
        str2+=i
print(str1)