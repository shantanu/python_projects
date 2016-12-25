from user import User
from privileges import Privileges

class Admin(User):
	"""Create an administrator"""
	
	def __init__(self, first_name, last_name, age):
		super().__init__(first_name, last_name, age)
		self.privileges = Privileges()
		
	

