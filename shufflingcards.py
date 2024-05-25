import itertools,random #itertools module to create a deck of cards 
deck=list(itertools.product(range(1,14),['spade','heart','diamond','club']))
random.shuffle(deck)
print("your combination of cards is :")
for i in range(5):
    print(deck[i][0],"of",deck[i][1])