'''
Цикл for
Синтаксис:
for <переменная> in <последовательность>:
    <тело цикла>

<переменная> - любая переменная, в которую будут присвоены элементы последовательности

Функция range(start, stop, step=1)
Функция генерирует последовательность 
range(5) - 0, 1, 2, 3, 4
range(9) - 0, 1, 2, 3, 4, 5, 6, 7, 8
range(2, 6) - 2, 3, 4, 5
range(5, 6) - 5
range(5, 1) - 
range(2, 10, 3) - 2, 5, 8
range(2, 11, 3) - 2, 5, 8
range(2, 12, 3) - 2, 5, 8, 11

# s = 'cat'
# # for i in range(len(s)):
# for ch in s:
#     print(ch)


Задача 1:
Пользователь вводит строку
Вывести все символы, стоящие на нечетных индексах в столбик (используя цикл for)

# s = 'qwerty'
# for ch in s[1::2]: # wry
#     print(ch)

# s = 'qwerty'
# for i in range(1, len(s), 2): # 1, 3, 5
#     print(s[i])


Пример функции upper через for:

# def k_upper(s: str) -> str:
#     res_str = ''
#     for ch in s:
#         if ch >= 'a' or ch <= 'z':
#             res_str += chr(ord(ch) - 32)
#         else:
#             res_str += ch
#     return res_str

Переменные в python:
Изменяемые
Списки

Неизменяемые:
int
float
str
bool
None

== сравнивает по значениям
is сравнивает по адресу в памяти
a = 1
b = 1
print(a == b)
print(a is b)
print(id(a))
print(id(b))

Неизменяемые типы данных передаются в функцию "по значению" (копируются)
Изменяемые типы данных передаются в функцию "по ссылке"


Списки (создание и индексы):
# lst = [1, 2, 3, 2.2, 'qwerty', [88, 99], True]
# print(lst)
# print(lst[1])
# print(lst[4][2])
# print(lst[5])
# print(lst[5][0])

Двумерный список:
# a = [
#     [1, 2, 3], 
#     [4, 5, 6], 
#     [7, 8, 9]
# ]
# print(a[0][1])

Два одинаковых списка, но в разных областях памяти
# lst1 = [1, 2, 3, 2.2, 'qwerty', [88, 99], True]
# lst2 = [1, 2, 3, 2.2, 'qwerty', [88, 99], True]
# print(lst1 == lst2) # True
# print(lst1 is lst2) # False

Передаем аргумент по-значению:
# def foo(a):
#     a = 1

# a = 2
# foo(a)
# print(a) # 2

Передаем аргумент по-ссылке:
# def foo(a):
#     a[0] = 555

# a = [1, 2, 3]
# foo(a)
# print(a) # [555, 2, 3]


Создание копии списка:
# a = [1, 2, 3]
# b = a # скопировалась ссылка
# print(a == b, a is b) # True, True
# c = a[:]
# print(a == c, a is c) # True, False
# d = a.copy()
# print(a == d, a is d) # True, False

Глубокое копирование:
# a2 = [1, 2, 3, [66, 77, 88], 4, 5]
# b2 = a2[:]
# print(a2 == b2, a2 is b2)
# b2[3][0] = 'Bag is here!!'
# print(a2) # внутренний список скопировался по ссылке

# from copy import deepcopy
# c2 = deepcopy(a2)
# c2[3][0] = 'Bag is here!!'
# print(a2) # внутренний список не изменился

Поиск жлемента в последовательности:
# s = 'abcdefg'
# if 'c' in s:
#     print(True)
# else:
#     print(False)

Генерация списков:
<переменная> = [<формула> for i in range(...)]


Задача 1:
Задан массив A, содержащий 10 целых чисел. Найти сумму элементов этого массива. ​Элементы вводятся с клавиатуры.

import random
lst = [random.randint(1,100) for _ in range(10)]
summ = 0
for i in lst:
    summ += i
print(summ)

# 2 способ решения%
print(sum([int(input()) for _ in range(10)]))

Задача 2:
Задан рандомный массив из 10 элементов
Найти минимальное число

import random

lst = [random.randint(1,100) for _ in range(10)]
min_elem = lst[0]
for elem in lst:
    if elem < min_elem:
        min_elem = elem
print(min_elem)
'''
