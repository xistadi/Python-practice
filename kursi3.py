#2.1
"""a = 5
while a <= 55:
	print(a)
	a += 2"""

"""a, b = int(input()), int(input())
s = 0
while a <= b:
	s += a
	a += 1
print(s)"""

"""value = 0
a = int(input())
while a != 0:
	value += a
	a = int(input())
print(value)"""

"""s, n =0, int(input())
while n:
    s, n = s + n, int(input())
print(s)"""

"""a, b = int(input()), int(input())
h = 2
tempa = a
tempb = b
if a == b:
	print(a)
elif a > b:
	while a % b:
		a = tempa
		a *= h 
		h += 1
	else:
		print(a)			
elif b > a:
	while b % a:
		b = tempb
		b *= h 
		h += 1	
	else:
		print(b)"""

"""a = int(input())
b = int(input())
d = a
while d%b:
    d += a
print(d)"""

"""a=int(input())
b=int(input())
m=a
if a==b:
	print(m)
while m%a!=0 or m%b!=0: #or - это суммирование(0+0=0, 0+1=1, 1+1=1), and - это умножение (0*0=0, 0*1=0, 1*1=1)
	m += a
print(m)"""

#2.2
"""i = 0
while i < 5:
	a, b = input(), input()
	a = int(a)
	b = int(b)
	if (a == 0) and (b == 0):
		break # досрочно завершаем цикл
	if (a == 0) or (b == 0): # если хоть один из введенных равен нулю идем к принт
		continue
	print(a * b)
	i += 1"""

"""while True:
	a = int(input())
	if a < 10:
		continue
	elif a > 100:
		break
	print(a)"""

"""st = ""
while True:
    i = int(input())
    if i < 10:
        continue
    elif i > 100:
        break
    else:
        st += str(i) + "\n"
print (st)"""

#2.3
"""n = int(input())
for i in range(n):
	for j in range(n):
		print("*", end = "")
	print()"""

"""n = int(input())
for i in range(n):
	print("*" * n)"""

"""a, b, c, d = int(input()), int(input()), int(input()), int(input())
for i in range(c, d + 1):
	print("\t", i, end = "")
print()
for i in range(a, b + 1):
	print(i, end = "\t")
	for j in range(c, d + 1):
		print(i * j, end = "\t")
	print()"""

"""a, b = int(input()), int(input())
s = 0
value = 0
for i in range(a, b + 1):
	if i % 3 == 0:
		value += i
		s += 1
print(value / s)"""

#2.4
"""a = input()
temp = 0
for i in a:
	if "c" in i.lower():
		temp += 1
	elif "g" in i.lower():
		temp += 1
print((temp / len(a)) * 100)"""

"""s = input().upper()
print((s.count('G') + s.count('C'))/len(s) * 100)"""

"""message = str(input())
cnt = 1
x = 1
j = message[x:x+1]
for i in message:
    if i in j:
        cnt += 1
    else:
        print(i, end='')
        print(cnt, end='')
        cnt = 1
    x += 1
    j = message[x:x+1]"""



#2.5
""" Напишите программу, на вход которой подается одна строка с целыми числами. Программа должна вывести сумму этих чисел.

Используйте метод split строки. """
"""a = [int(i) for i in input().split()]
value = 0
for i in a:
	value += i
print(value)

s = 0
for i in input().split():
    s += int(i)
print(s)"""

#print(sum(int(i) for i in input().split())) #sum = плюсует все что внутри sum([1, 2])

"""Программа должна для каждого элемента этого списка вывести сумму двух его соседей. Для элементов списка, являющихся крайними, одним из соседей считается элемент, находящий на противоположном конце этого списка. Например, если на вход подаётся список "1 3 5 6 10", то на выход ожидается список "13 6 9 15 7" (без кавычек).

Если на вход пришло только одно число, надо вывести его же.

Вывод должен содержать одну строку с числами нового списка, разделёнными пробелом."""


"""a=[int(i) for i in input().split()]
if len(a)>1:
    for i in range(len(a)):
        print(a[i-1]+a[i+1-len(a)], end = " ")
else:
    print(a[0])"""

"""Напишите программу, которая принимает на вход список чисел в одной строке и выводит на экран в одну строку значения, которые повторяются в нём более одного раза.

Для решения задачи может пригодиться метод sort списка.

Выводимые числа не должны повторяться, порядок их вывода может быть произвольным."""
"""a=[int(i) for i in input().split()]
for x in set(a): #проход по всем без дублей 
	if a.count(x) > 1: # если в изначальном списке "а" есть элементы к колличестве >1 делаем принт
		print(x, end = " ")"""

#2.6
# Поиск минимума в списке
"""a = [int(i) for i in input().split()]
m = a[0]
for x in a:
	if m > x:
		m = x
print(m)"""

"""Сапер
Даны размеры поля для игры в сапер и координаты мин,
стоящих на этом поле. Вывести полу игры на экран.
Ввод
5 4 4 - 5строк 4 столбцов 4 мины 
"""
"""n, m, k = (int(i) for i in input().split())  # чтение размеров поля и числа мин
a = [[0 for j in range(m)] for i in range(n)]  # заполнение поля нулями
for i in range(k):
    row, col = (int(i) - 1 for i in input().split())
    a[row][col] = -1  # расставляем мины
for i in range(n):
    for j in range(m):
        if a[i][j] == 0:  # в этой клетке мины нет, поэтому считаем число мин вокруг
            for di in range(-1, 2):
                for dj in range(-1, 2):
                    ai = i + di
                    aj = j + dj
                    # (ai, aj)
                    if 0 <= ai < n and 0 <= aj < m and a[ai][aj] == -1:
                        a[i][j] += 1
# вывод результата
for i in range(n):
    for j in range(m):
        if a[i][j] == -1:
            print('*', end='')
        elif a[i][j] == 0:
            print('.', end='')
        else:
            print(a[i][j], end='')
    print()"""

"""Напишите программу, которая считывает с 
консоли числа (по одному в строке) до тех пор, 
пока сумма введённых чисел не будет равна 0 и 
сразу после этого выводит сумму квадратов всех 
считанных чисел.

Гарантируется, что в какой-то момент сумма введённых 
чисел окажется равной 0, после этого считывание 
продолжать не нужно."""

"""a = 0
value = 0
value1 = 0
while True:
	a = int(input())
	value += a
	value1 += a**2
	if value == 0:
		break
print(value1)"""

