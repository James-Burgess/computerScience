#!/lib/bin/python3
#any number >9 if you subtract the digits will reduce to 9
import _thread

startNumber = 55580944
endNumber = 999999999999


def numberCheck(startNumber, endNumber):
	for count in range (endNumber):
		number = startNumber + count
		print(number)
		
		digits = (list(str(number)))
		for digit in digits:
			number -= int(digit)

		if number % 9 == 0:
			print("passed")
		else:
			print("fail")
			break

diff = (endNumber - startNumber)//2
print(diff)
# Create two threads as follows
try:
   _thread.start_new_thread( numberCheck, (startNumber, (endNumber-diff), ) )
   _thread.start_new_thread( numberCheck, ((startNumber+diff), endNumber, ) )
except:
   print ("Error: unable to start thread")

while 1:
	pass