import unittest
from city_functions import city_function

class NameTestCase(unittest.TestCase):
	"""Тесты для функции city_function"""
	
	def test_city_country(self):
		"""Ответ вида 'Беларусь Минск'"""
		format_city = city_function('Беларусь', 'Минск')
		self.assertEqual(format_city, 'Беларусь Минск') #сравнивает левую часть с правой

unittest.main()