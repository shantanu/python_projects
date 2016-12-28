import unittest
from city_functions import city_country

class CitiesTestCase(unittest.TestCase):
	def test_city_country(self):
		formatted_name = city_country('santiago', 'chile')
		self.assertEqual(formatted_name, "Santiago, Chile")
	
	def test_city_country_population(self):
		formatted_name = city_country('santiago', 'chile', '5000000')
		self.assertEqual(formatted_name, "Santiago, Chile - population 5000000")
	
unittest.main()
