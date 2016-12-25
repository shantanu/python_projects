"""A class to model a user"""

class User():
	"""Making a simple user"""
	def __init__(self, first_name, last_name, age):
		"""Initialize a user with a first and last name, and age"""
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.login_attempts = 0
	
	def describe_user(self):
		"""Prints a description of the user"""
		print(self.first_name.title() + " " + self.last_name.title() + " - " + str(self.age))
		
	def greet_user(self):
		print("Welcome, " + self.first_name.title())
		
	def get_login_attempts(self):
		print(self.login_attempts)
	
	def increment_login_attempts(self):
		self.login_attempts += 1
	
	def reset_login_attempts(self):
		self.login_attempts = 0
	
