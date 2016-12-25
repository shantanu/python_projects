from random import randint

class Die():
	"""A class that represents a dice"""
	
	def __init__(self, sides = 6):
		"""Initializes a dice with a number of sides"""
		self.sides = sides
		
	def roll_die(self):
		roll = randint(1, self.sides)
		print(roll)
		
six_sided = Die(6)

for i in range(10):
	six_sided.roll_die()
	
ten_sided = Die(10)

for i in range(10):
	ten_sided.roll_die()

twenty_sided = Die(20)

for i in range(10):
	twenty_sided.roll_die()
	
