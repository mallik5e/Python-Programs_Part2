p=0
n=0
z=0
while(1):
    num=int(input("enter the value : "))
    if(num==-1):
        break
    if(num>0):
        p=p+1
    elif(num==0):
        z=z+1
    else:
        n=n+1
print("p = ",(p))
print("n = ",(n))
print("z = ",(z))