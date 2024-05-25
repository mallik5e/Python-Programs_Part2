def char_index(s,c):
    index=0
    while (index<len(s)):
     
     if  s[index]==c:
            print(index)
            return
     else:
        pass
     index+=1
    print("no such character")



str=input("\nEnter the value: ")
ch=input("\nEnter the value: ")
char_index(str,ch)