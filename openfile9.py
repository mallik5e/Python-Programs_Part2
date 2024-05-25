with open("file1.txt","rb") as file1:
    with open("file2.txt","wb") as file2:
        while True:
         buf=file1.readline()
         if len(buf)!=0:
            if buf[0]=='#':
                continue
            else:
                file2.write(buf)
         else:
            break
print("file copied") 