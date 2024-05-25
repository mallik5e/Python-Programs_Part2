with open("file2.txt","r") as file:
    line=file.readline()
    word=line.split()
    print(word)
    file.close()

