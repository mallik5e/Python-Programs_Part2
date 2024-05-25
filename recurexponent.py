def expo(x,y):
    if(x==0 or y==0):
        return 1
    else:
        return (x*expo(x,(y-1)))



x=int(input("enter the value :"))
y=int(input("enter the value : "))
print("exponent= ",expo(x,y))