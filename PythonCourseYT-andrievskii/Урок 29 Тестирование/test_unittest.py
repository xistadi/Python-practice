import unittest
from work import full_name

class NameTestCase(unittest.TestCase):
	"""Тесты для функции full_name"""
	
	def test_first_last_name(self):
		"""Имена вида 'Олег Иванов' работают нормально"""
		format_name = full_name('Олег', 'Иванов')
		self.assertEqual(format_name, 'Олег Иванов') #сравнивает левую часть с правой

	def test_first_last_middle_name(self):
		"""Имена вида 'Олег Иванов Иванович' работают нормально"""
		format_name = full_name('Олег', 'Иванов', 'Иванович')
		self.assertEqual(format_name, 'Олег Иванов Иванович')


unittest.main()