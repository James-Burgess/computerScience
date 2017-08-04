from random import randint
n = [randint(0,250) for x in range (100)]
print("Un-ordered List:\n" + str(n))
def sorter(myList):
	i = c = 0
	while (i != (len(myList)-1)):
		c += 1
		if myList[i] > myList[i+1]:
			myList[i], myList[i+1] = myList[i+1], myList[i]; i=0			
		elif: i += 1
	return(str(myList),str(c))
print("Ordered List:\n%s\nIteration count: %s" %sorter(n))