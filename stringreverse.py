def reverse(str):
    new_str=''
    i=len(str)-1
    while i>=0:
        new_str+=str[i]
        i-=1
    return new_str

str=input("enter the value: ")
print(reverse(str))