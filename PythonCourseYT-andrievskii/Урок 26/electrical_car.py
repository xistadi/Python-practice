from car import Car

class Battery():
	"""Аккумулятор для электроавто"""
	def __init__(self, battery = 100):
		self.battery = battery

	def description_battery(self):
		print("Батарея мощностью: " + str(self.battery) + " киловат")

class ElectricCar(Car):
	def __init__(self, make, model, year):
		"""Инициализация атрибутов родителя"""
		super().__init__(make, model, year)
		self.battery = Battery()

	def description_name(self):
		"""Переопределение"""
		desc = self.model + " " + str(self.year) 
		return desc.title()

