def find_ch(str,ch):
    index=len(str)-1
    while index>=0:
       if str[index]==ch:
        print(index)
        return index
       index-=1
    return -1  



str=input("\nEnter the value: ")
ch=input("\nEnter the value: ")
find_ch(str,ch)