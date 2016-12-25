"""A class that stores admin privileges"""

class Privileges():
	"""A wrapper class that manages admin privileges"""
	
	def __init__(self, privileges = ['can delete post', 'can ban user']):
		self.privileges = privileges
	
	def describe_privileges(self):
		print("You can do the following tasks \n\t" + str(self.privileges))
	
