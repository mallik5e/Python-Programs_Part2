def swap(a,b):
    a,b=b,a
    print("after swap :")
    print("first number :",a)
    print("second numberc :",b)

a=int(input("enter the value : "))
b=int(input("enter the value : "))
print("before swap :")
print("first number : ",a)
print("second number : ",b)
swap(a,b)