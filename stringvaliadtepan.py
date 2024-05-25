while(1):
    name=input("\nenter your name: ")
    if name.isalpha()==False:
        print("Invalid Name, sorry you cannot proceed")
        break
    else:
        pan_card = input("\nenter your pan number: ")
        if pan_card.isalnum() == False:
            print("Invalid pan,sorry can't proceed")
            break
    print("please check,"+name+", your pan number is: "+pan_card+"")
    break