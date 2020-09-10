#3.1
""" Нахождение мин символа """
"""def min2(a, b): #объявление функции
	if a <= b:
		return a
	else:
		return b
print(min2(2,3)) #выводит минимальное тоесть 2"""

"""def min(*a): #произвольное число параметров min(5, 3, 4, 5)
	m = a[0]
	for x in a:
		if m > x:
			m = x
	return m			"""

""" Функция range """
"""def my_range(start, stop, step=1):
    res = []
    if step > 0:
        x = start
        while x < stop:
            res += [x]
            x += step
    elif step < 0:
        x = start
        while x > stop:
            res += [x]
            x += step
    return res"""

"""def append_zero(xs):
    xs.append(0)
    xs = [100]
    
a = []
append_zero(a)
print(a)  # [0]"""

"""def f(x):
    result = 0

    if x <= -2:
        result = 1 - (x + 2)**2
    elif -2 < x <= 2:
        result = -(x / 2)
    elif 2 < x:
        result = (x - 2)**2 + 1

    return result"""

""" Напишите функцию modify_list(l), которая принимает на вход список
целых чисел, удаляет из него все нечётные значения, а чётные нацело 
делит на два. Функция не должна ничего возвращать,требуется только
изменение переданного списка """
"""def modify_list(l):
    for x in l[:]:
        if x % 2 == 0:
            l.append(x//2)
        l.remove(x)"""

#3.2
"""Напишите функцию update_dictionary(d, key, value), которая принимает на вход словарь dd и два числа: keykey и valuevalue.

Если ключ key есть в словаре d, то добавьте значение value 
в список, который хранится по этому ключу.
Если ключа key нет в словаре, то нужно добавить значение в 
список по ключу 2 * key. Если и ключа 2 * key нет, 
то нужно добавить ключ 2 * key в словарь и сопоставить ему 
список из переданного элемента [value]."""

"""def update_dictionary(d, key, value):
    if key in d:
        d[key].append(value)
    elif 2*key in d:
        d[2*key].append(value)
    else:
        d[2*key] = []
        d[2*key].append(value)"""


"""Когда Антон прочитал «Войну и мир», ему стало интересно, 
сколько слов и в каком количестве используется в этой книге.

Помогите Антону написать упрощённую версию такой программы,
которая сможет подсчитать слова, разделённые пробелом и 
вывести получившуюся статистику.

Программа должна считывать одну строку со стандартного ввода и 
водить для каждого уникального слова в этой строке число его 
повторений (без учёта регистра) в формате "слово количество" 
Порядок вывода слов может быть произвольным, каждое уникальное 
слово﻿ должно выводиться только один раз."""

"""text = input().lower().split()
dictionary = dict()
for word in text:
    if(word not in dictionary):
        dictionary[word] = 1
    else:
        dictionary[word]+=1
for word, count in dictionary.items():
    print(word, count)"""


"""http://joxi.ru/brR5xo0U7GNbVA"""
"""n=int(input())
d={}
for i in range(n):
    x=int(input())
    if x not in d:
        d[x]=f(x)   
    print(d[x])"""