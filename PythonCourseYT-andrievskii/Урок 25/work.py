class Car(): # супер класс
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


class Battery():
	"""Аккумулятор для электроавто"""
	def __init__(self, battery = 100):
		self.battery = battery

	def description_battery(self):
		print("Батарея мощностью: " + str(self.battery) + " киловат")


class ElectricCar(Car): #создали экземпляр класса который строиться на родителе Car(дочерний класс)
	def __init__(self, make, model, year): #копируем с Car
		"""Инициализация атрибутов родителя"""
		super().__init__(make, model, year) #связываем c Car
		self.battery = Battery() #атрибут self.battery равняется классу Battery

	def description_name(self):
		"""Переопределение родительского метода"""
		desc = self.model + " " + str(self.year) + " " + str(self.battery) 
		return desc.title()
		
	
tesla = ElectricCar("tesla", "model s ", 2017)
print(tesla.description_name())
tesla.battery.description_battery() #мы используем только то что есть в классе Battery
