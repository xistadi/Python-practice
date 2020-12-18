def multiply(a, b):
	print(a*b)

def add(a, b):
	print(a+b)

def divide(a, b):
	if b != 0:
		print(a/b)
	else: 
		print("Деление на 0!")


divide(int(input("Vvedite a: ")), int(input("Vvedite b: ")))