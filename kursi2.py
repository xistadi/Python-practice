#1.7
#print(9**19-int(float(9**19)))
#print(type(7))
#1.8
#name = input("Vvedi ima epta: ")
#print("Hello yeba ", name," vo eblan")

#a=int(input("vvedi a: "))
#b=int(input("vvedi b: "))
#print(a*b)

#X = int(input())
#Y = int(input())
#print(X*60 + Y)

#x = int(input())
#value = x // 60
#print(value)
#print(x-(value * 60))

#x = int(input())
#h = int(input())
#m = int(input())
#value = x + (h * 60) + m
#print(value // 60)
#print(value % 60)

#x=int(input()) + int(input()) * 60 + int (input())
#print(x // 60, "\n", x % 60)

#1.9
#a = int(input())
#print(10 <= a < 100)

#x1, x2, x3 = True, False, True
#print(not x1 or x2 and x3)#сначала нот потом энд потом ор (приоритет)

#((a and b) or ((not a) and (not b)))

#x = 5
#y = 10
#print(y > x * x or y >= 2 * x and x < y)

"""a = True
b = False
print(a and b or not a and not b)"""

#1.10
"""if x % 2 ==0:
	print("Chet")
   else:
   	print("nechet")"""

"""a = int(input())
b = int(input())
remaining = True
while remaining:
	if b == 0:
		print("Are you dolbaeb na 0 nel'za delit")
		b = int(input("Vvedi b eshe raz eblo: "))
	else: 
		remaining = False	
print("Otvet", a / b)"""

"""a = int(input())
b = int(input())
h = int(input())

if h < a:
	print("Недосып")
elif h > b:
	print ("Пересып")
else: 
	print("Это нормально")"""

""" Альтернативное решение 
a = int(input())
b = int(input())
x = int(input())
print(("Недосып", "Это нормально", "Пересып")[(x > b) - (x < a) + 1])"""

"""a = int(input())
if a % 4 == 0 and a % 100 != 0 and a % 400 != 0:
	print("Високосный")
elif a % 4 == 0 and a % 100 == 0 and a % 400 == 0:
	print("Високосный")
else:
	print("Обычный")"""
""" Попроще
a = int(input())
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print("Високосный")
else:
    print("Обычный")"""

"""import calendar
year = int(input())
if calendar.isleap(year):
    print ("Високосный")
else:
    print ("Обычный")"""

#1.11
#print("sa" * 2)
#print(len("dasdas")) выводит количество символов
#print("asd", "\n\n", "kek") 

"""a = "string"
b = "another string"
print(a, b)
print(a, "\n", b)#print in two different lines"""

#формула Герона
"""a = int(input())
b = int(input())
c = int(input())
p = (a + b + c) / 2
print((p * (p - a) * (p - b) * (p - c)) ** 0.5)"""

"""a, b, c = int(input()), int(input()), int(input()) # a,b,c=int(input()),int(input()),int(input())
p = (a + b + c) / 2
print((p * (p - a) * (p - b) * (p - c)) ** 0.5)"""

"""a = int(input())
if -15 < a <= 12 or 14 < a < 17 or a >= 19:
	print(True)
else:
	print(False)"""

"""n = int(input())
print(-15 < n <= 12 or 14 < n < 17 or 19 <= n)"""

"""a = float(input())
b = float(input())
mod = str(input())
if mod == "+":
	print(a + b)
elif mod == "-":
	print(a - b)
elif mod == "/" and b != 0:
	print(a / b)
elif mod == "*":
	print(a * b)
elif mod == "mod" and b != 0:
	print(a % b)
elif mod == "pow":
	print(a ** b)
elif mod == "div" and b != 0:
	print(a // b)
else:
	print("Деление на 0!")"""

""" лучше ебануть проверку в самом начале 
if(b == 0 and (op == "mod" or op == "/" or op == "div")):
    print("Деление на 0!")"""

"""form = str(input())
if form == "треугольник":
	a = int(input())
	b = int(input())
	c = int(input())
	p = (a + b + c) / 2
	print((p * (p - a) * (p - b) * (p - c)) ** 0.5)
elif form == "прямоугольник":
	a = int(input())
	b = int(input())
	print(a * b)
elif form == "круг":
	a = int(input())
	print(3.14 * (a ** 2))"""
#покатит но можно a, b, c = int(input()), int(input()), int(input())

"""a, b, c = int(input()), int(input()), int(input())
s = a + b + c;
print(max(a,b,c))
print(min(a,b,c))
print(s - max(a,b,c) - min(a,b,c))"""

"""number = str(input())
if (int(number[0]) + int(number[1]) + int(number[2])) == (int(number[3]) + int(number[4]) + int(number[5])):
	print("Счастливый")
else:
	print("Обычный")"""

"""a, b, c, d, e, f = input()
n= int(a)+int (b)+int(c)
m= int(d)+int (e)+int(f)
if n==m:
    print ('Счастливый')
else:
    print ('Обычный')"""

"""number = int(input())
a = number % 10
b = number % 100
if b == 11 or b == 12 or b == 13 or b == 14:
	print(number, "программистов")
elif a == 0 or a == 5 or a == 6 or a == 7 or a == 8 or a == 9:
	print(number, "программистов")
elif a == 1 and b != 11:
	print(number, "программист")
elif a == 2 or a == 3 or a == 4 and b != 12 and b != 13 and b != 14:
	print(number, "программиста")"""

