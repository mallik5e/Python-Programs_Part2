m=int(input("enter the value : "))
sum=0
while(m>0):
    r=m%10
    sum=sum+r
    m=m/10
print(int(sum))