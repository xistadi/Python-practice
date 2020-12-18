class Restaurant():
	"""docstring for Restaurant"""
	def __init__(self, restaurant_name, cuisine_type):
		self.name = restaurant_name
		self.cuisine_type = cuisine_type

	def describe(self):
		print("Название ресторана: " + self.name + ", тип кухни: " + self.cuisine_type)

	def greet_users(self):
		print("Hello dolbaebi")


class User():
	"""docstring for User"""
	def __init__(self, first_name, last_name):
		self.first = first_name
		self.last = last_name

	def describe(self):
		print("Имя долбаеба: " + self.first + ", фамилия: " + self.last)

	def greet_users(self):
		print("Hello dolbaeb " + self.first + " " + self.last)
russian = Restaurant("Русские долбаебы", "кухня хуйня")
blr = Restaurant("Белорусские долбаебы", "кухня хуйня")
russian.greet_users()
russian.describe()
blr.describe()

print("============================")

oleg = User("Oleg", "Ivanov")
oleg.describe()
oleg.greet_users()

