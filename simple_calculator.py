import math
print("\t___calculator______")

def sum(a,b):
    a+=b
    return a
def sub(a,b):
    if a>b:
     a-=b
     return a
    else:
        b-=a
        return b

def mul(a,b):
    a*=b
    return a
def div(a,b):
    q=a/b
    r=a%b 
    print("\n the quotient is : %s " %q)
    print("\n the remainder is : %s" %r)

def sqrt(a):
    x=math.sqrt(a)
    return x 

while(True):
    print("\n\nchoose the operation you want to perform: ")
    print("\n\t1.Addition")
    print("\n\t2.subtraction")
    print("\n\t3.multiplication")
    print("\n\t4.division")
    print("\n\t5.squareroot")
    print("\n\t6.exit")

    choice = int(input('>'))
    
    if choice==1:
        print("enter the values: ")
        n1=int(input('>'))
        n2=int(input('>'))
        s=sum(n1,n2)
        print("sum= ",s)
    elif choice==2:
        print("enter the values: ")
        n1=int(input('>'))
        n2=int(input('>'))
        sb=sub(n1,n2)
        print("sub= ",sb)
    elif choice==3:
        print("enter the values: ")
        n1=int(input('>'))
        n2=int(input('>'))
        m=mul(n1,n2)
        print("mul= ",m)
    elif choice==4:
        print("enter the values: ")
        n1=int(input('>'))
        n2=int(input('>'))
        d=div(n1,n2)
        print("div= ",d)
    elif choice==5:
        print("enter the values: ")
        n1=int(input('>'))
        sq=sqrt(n1)
        print("sqrt= ",sq)
    else:
        print("\nyou choose exit.bye....")
        break

