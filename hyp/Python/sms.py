#An SMS Simulation
class SMSMessage(object):

    def __init__(self, hasBeenRead, messageText, fromNumber):
        self.hasBeenRead = False
        self.messageText = messageText
        self.fromNumber = fromNumber
 
    def MarkAsRead(self):
        if userChoice == read:
            self.hasBeenRead = True
             
    def add_sms():
    	pass
 
    def get_count():
    	pass
 
    def get_message():
    	pass
 
    def get_unread_messages():
    	pass
 
    def remove():
    	pass

no_1 = SMSMessage(False, "Hello", "0798653452")
no_2 = SMSMessage(False, "WYD", "0845673864")
no_3 = SMSMessage(False, "How are you?", "0631873298")
 
SMSStore = []
userChoice = ""

while userChoice != "quit":
    userChoice = input("What would you like to do - read/send/quit?\n>")
    if userChoice == "read":
    	#after a few if statements to find out which message
    	userChoice = int(input("which message?\n#"))
    	if len(SMSStore) > userChoice-1:#assuming the user indexs from 1
    		print (SMSStore[userChoice-1].messageText)

    elif userChoice == "send":
    	#you could add messages to an array like this
        msg = input("What would you like to send? \n>")
        nbr = input("to which number?\n#")
        SMSStore.append(SMSMessage(False, msg, nbr))

    elif userChoice == "quit":
        print ("Goodbye")

    else:
        print ("Oops - incorrect input")

