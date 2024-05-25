def remove_str(s):
    new_str=""
    for i in s:
       if i in "aeiouAEIOU":
        pass
       else:
          new_str+=i
    print(new_str)



str=input("\nenter the vowels: ")
remove_str(str)