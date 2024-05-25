def fab(n):
    if(n<2):
        return 1
    else:
        return (fab(n-1)+fab(n-2))

n=int(input("enter the value :"))
for i in range(n):
    print("fabinocci(",i,")=",fab(i))