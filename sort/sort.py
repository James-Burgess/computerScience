from random import randint

n = [randint(0,250) for x in range (100)]
print("Un-ordered List:\n" + str(n))

def sorter(l):
	i = c = 0
	while (i != (len(l)-1)):
		c += 1
		if l[i] > l[i+1]:
			l[i], l[i+1] = l[i+1], l[i]
			i=0			
		else: i += 1
	return(str(l),str(c))

print("Ordered List:\n%s\nIteration count: %s" %sorter(n))

