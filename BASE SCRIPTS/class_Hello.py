# Create a class called MessageHolder
class MessageHolder:
# Constructor - called automatically
# when an object of this class is created 
	def __init__(self, msg):
		self.msg = msg

# Function to return the stored message string
	def getMsg(self):
		return self.msg

zxc = MessageHolder('Ce mai faci draga ?')
print(zxc)

print(zxc.msg)

