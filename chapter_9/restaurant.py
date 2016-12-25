"""A class to model a restaurant"""

class Restaurant():
	"""A simple class to model a restaurant"""
	def __init__(self, restaurant_name, cuisine_type):
		"""Define Name and Cuisine Type Attributes"""
		self.name = restaurant_name
		self.cuisine = cuisine_type
		self.number_served = 0
		
	def describe_restaurant(self):
		"""Prints out information about a restaurant"""
		print(self.name.title())
		print('-' + self.cuisine.title())
	
	def open_restaurant(self):
		"""Prints out a message declaring the restaurant open"""
		print("This restaurant is now open!")
	
	def get_number_served(self):
		print("We have served " + str(self.number_served) + " people")
		
	def set_number_served(self, people):
		self.number_served = people
		
	def increment_number_served(self, people):
		self.number_served += people

