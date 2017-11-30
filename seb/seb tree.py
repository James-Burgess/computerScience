from random import randint

n = randint(5,20)

for i in range(n,0,-1):
	for j in range(i,0,-1):
		print(j, end= "")
	print()


