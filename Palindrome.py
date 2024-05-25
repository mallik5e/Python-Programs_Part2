s = input() 
temp = s[::-1]

if(temp == s ):
    print('palindrome')
else:
    print('not palindrome')
    
##########################
number = int(input())
temp = number
reverse = 0

while(number>0):
    digit = number%10
    reverse = reverse * 10 + digit
    number = number//10

if(temp == reverse):
    print('palindrome')
else:
    print('not palindrome')