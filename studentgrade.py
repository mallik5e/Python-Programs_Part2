m1=int(input("enter the marks : "))
m2=int(input("enter the marks : "))
m3=int(input("enter the marks : "))
m4=int(input("enter the marks : "))
total = m1+m2+m3+m4
print("Total = ",total)
avg = total/4
print("Average= ",avg)
if(avg>75):
    print("destination")
elif(avg>=60 and avg<75):
    print("first class")
elif(avg>=50 and avg<60):
    print("second class")
elif(avg>=40 and avg<50):
    print("third class")
else:
    print("fail")
