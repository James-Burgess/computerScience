from random import randint

number = randint(5,20)

print ("Your number is:" +str(number))

for i in range (number,0,-1):
    for j in range(i,0,-1):
        print(j, end="")
    print()

print("Jared is pretty cool")
