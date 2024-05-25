def max(numbers):#global namespace
    print("USER DEFINDED MAX FUNCTION =")
    large = -1 #local namespace
    for i in numbers:
        if i>large:
            large=i 
    return large
no=[9,-1,7,4,2]
print(max(no))
print("sum of max numbers =",sum(no))#builtin function namespace 