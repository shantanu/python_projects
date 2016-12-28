import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
	def setUp(self):
		self.my_employee = Employee("Shantanu", "Laghate", 50000)
		
	def test_give_default_raise(self):
		self.my_employee.give_raise()
		self.assertEqual(self.my_employee.salary, 55000)
	
	def test_give_custom_raise(self):
		self.my_employee.give_raise(10000)
		self.assertEqual(self.my_employee.salary, 60000)
		
unittest.main()
