from random import randint

number = randint(5,20)

print("The random number is: %s" %number)

for i in range (number,0,-1): 
    for j in range (i,0,-1):
        print(j, end=" ")
    print()