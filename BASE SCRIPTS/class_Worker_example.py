# A first Python script class

class Worker:
	def __init__(self, name, pay):  # Initialize when created
		self.name = name  # self is the new object

		self.pay = pay

	def lastName(self):
		return self.name.split()[-1]  # Split string on blanks
	def giveRaise(self, percent):
		self.pay *= (1.0 + percent)  # Update pay in-place

bob = Worker('Bob Smith', 50000)  # Make two instances
sue = Worker('Sue Jones', 60000)  # Each has name and pay attrs


print(sue, sue.name, sue.pay)


print(bob, bob.name, bob.pay)
bob.giveRaise(0.1)
print(bob.lastName(), bob.pay)
