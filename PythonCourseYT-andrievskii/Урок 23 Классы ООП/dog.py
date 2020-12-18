class Dog():
	"""docstring for Dog"""
	def __init__(self, name, age):
		self.name = name
		self.age = age
		print("Dog is ready")

	def sit(self):
		print(self.name.title() + " dog is sitting")