class Car():
	"""docstring for Car"""
	def __init__(self, make, model, year):
		"""Инициализация атрибутов"""
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def description_name(self):
		desc = str(self.year) + " " + self.make + " " + self.model
		return desc.title()

	def read_odometer(self):
		"""Вывод пробега авто"""
		print("Пробег авто: " + str(self.odometer_reading) + " км")

	def update_odometer(self, km):
		"""Устанавливаем значение на одометре"""
		if km >= self.odometer_reading:
			self.odometer_reading = km
		else:
			print("Скручивать нельзя!")

	def increment_odometer(self, km):
		"""Увеличиваем одометра щначение"""
		if km < 0:
			print("Скручивание не пройдет!")
		else:
			self.odometer_reading += km


my_car = Car("audi", "a4", 2017)
print(my_car.description_name())
my_car.update_odometer(50)
my_car.increment_odometer(100)
my_car.read_odometer()