num=int(input("enter the value : "))
sum=0
for i in range(1,num+1):
    a=float(i**i)/i
    sum=sum+a
print(sum)