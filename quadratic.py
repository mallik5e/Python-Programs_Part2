a=int(input("enter the value : "))
b=int(input("enter the value : "))
c=int(input("enter the value : "))
d = (b*b)-(4*a*c)
print("D = ",d)
deno=2*a
if(d>0):
    print("real roots")
    root1=(-b + d**0.05)/deno
    root2=(-b + d**0.05)/deno
    print("root1 = ",root1, "\t root2 = ",root2)
elif(d==0):
    print("equal root")
    root1=-b/deno 
    print("root1 and root2 = ",root1)
else:
    print("imaginary root")