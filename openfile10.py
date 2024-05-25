file=input("enter the filename : ")
with open(file) as file:
    txt=file.readline()
    ltr=input("enter the letter to be count : ")
    count=0
    for i in txt:
        if i==ltr:
         count+=1
print(ltr,"appears",count,"times in file")