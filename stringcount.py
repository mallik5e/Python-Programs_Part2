def count_ch(str,ch):
    count=0
    for i in str:
         if str==ch:
            count+=1
    return count



str=input("\nEnter the value: ")
ch=input("\nEnter the value: ")
print("no. of counts",count_ch(str,ch))
