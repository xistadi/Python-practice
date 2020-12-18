import unittest
from work import AnonymousSurvey

class TestAnonymousmySurvey(unittest.TestCase):
	"""Test for AnonymousSurvey"""

	def setUp(self):
		"""Создание опроса и набора ответов для всех методов"""
		question = "Какой язык программирования интересен?:"
		self.my_survey = AnonymousSurvey(question)
		self.responses = ["Java", "Python", "C++", "GO", "JS"]
		self.responses3 = ["Java", "Python", "C++"]

	def test_store_single_respose(self):
		"""Проверяем один элемент в списке"""
		self.my_survey.store_responce(self.responses[0])
		self.assertIn(self.responses[0], self.my_survey.responses)

	def test_five_responses(self):
		"""Проверяет 5 ответов"""
		for response in self.responses:
			self.my_survey.store_responce(response)
		for response in self.responses:
			self.assertIn(response, self.my_survey.responses)

	def test_three_responses(self):
		"""Проверяет 5 ответов"""
		for response in self.responses3:
			self.my_survey.store_responce(response)
		for response in self.responses3:
			self.assertIn(response, self.my_survey.responses)


unittest.main()