num1 = 100
num2 = 100
answer = 0
palindrome = 0

for i in range (899 * 899):
    answer = str(n1 * n2)

    reverse = ''.join(reversed(list(answer))) #reverses answer for check

    if answer == reverse:                     #check if palindrome
        if palindrome < int(answer):          #check if bigger
            palindrome = int(answer)
     
    num1 += 1                                 #change nubers from 100 - 999
    if num1 == 999:
        num2 += 1
        num1 = 100
    
print(palindrome)                             #prints highest Palindrome
