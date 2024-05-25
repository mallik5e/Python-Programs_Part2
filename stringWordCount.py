string=input()
count=1
for i in string:
    if i in ' ':
        count+=1
print(count)