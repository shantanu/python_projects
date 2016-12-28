class Employee():
	def __init__(self, first, last, money):
		self.first_name = first
		self.last_name = last
		self.salary = money
		
	def give_raise(self, amount=''):
		if amount:
			self.salary += amount
		else:
			self.salary += 5000
			
