file=open("file2.txt","r")
print("position of the file pointer before readline is : ",file.tell())
print(file.read(10))
print("position of the file pointer after readline is : ",file.tell())
print("setting 3 bytes from the position of file pointer")
file.seek(3,1)
print(file.read())
file.close()