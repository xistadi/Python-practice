# Дебильный калькулятор 
from colorama import init
from colorama import Fore, Back, Style

# use Colorama to make Termcolor work on Windows too
init()

print(Fore.BLACK)
print(Back.GREEN)

what = input("Che(+ или -) : ")

print(Back.CYAN)

a=float(input("vvedi 1 chislo: "))
b=float(input("vvedi 2 chislo: "))

if what =="+":
	c=a+b
	print("Result: " + str(c))	
elif what =="-":
	c=a-b
	print("Result: " + str(c))	
else:
	print ("Ты че написал дурень?")			