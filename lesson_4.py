import random


# lst = []
# for _ in range(10):
#     lst.append(random.randint(1, 100))

# print(lst)

'''
Генерация списков
синтаксис:
название_переменной = [формула for переменная in range(количество_элементов)]
'''

# lst = [random.randint(1, 10) for _ in range(5)]
# print(lst)

# for i in lst:
#     i = -1
# print(lst)

# i = 0
# while i < len(lst):
#     lst[i] = -1
#     i += 1
# print(lst)

# for i in range(len(lst)):
#     lst[i] = -1
# print(lst)

# lst = [random.randint(0, 20) for i in range(7)]
# print(lst)
# # print(min(lst), max(lst))
# min_elem = lst[0]
# min_elem_index = 0
# max_elem = lst[0]
# max_elem_index = 0
# for i in range(len(lst)):
#     if lst[i] < min_elem:
#         min_elem = lst[i]
#         min_elem_index = i
#     if lst[i] > max_elem:
#         max_elem = lst[i]
#         max_elem_index = i
# print(max_elem, max_elem_index)
# print(min_elem, min_elem_index)

'''
DRY - don't repeat youself
'''


'''
1) Написать функцию, которая выводит на экран hello world 5 раз
2) Написать функцию, которая будет выводить на экран прямоугольник из символов *, 
размером MxN.
3) Известны оценки 25 учеников. Есть ли среди них двойки?
4) Удалить из списка все отрицательные элементы.
'''

def print_hello_world(a, n=5):
    print(a)
    for _ in range(n):
        print('hello world!!')


def print_rectangle(m, n):
    for _ in range(m):
        print('* ' * n)


def find_mark_in_lst(marks, mark):
    if mark in marks:
        print('есть')
    else:
        print('нет')


def remove_negative(lst):
    i = 0
    while i < len(lst):
        if lst[i] < 0:
            lst.remove(lst[i])
            i -= 1
        i += 1
    print(lst)


# print_hello_world(2)
# print_hello_world()
# m = int(input())
# n = int(input())
print_rectangle(int(input()), int(input()))

# def print_triangle():
#     print('  *')
#     print(' ***')
#     print('*****')

a = [random.randint(2, 5) for _ in range(5)]
find_mark_in_lst(a, 3)

# lst2 = [1, 3, 5, -9, 3]
# remove_negative(lst2)
# print(min(lst2))

# print_triangle()
# print_triangle()
# print_triangle()
# print_triangle()



def foo():
    global JUST_NUMBER
    JUST_NUMBER = 42

JUST_NUMBER = 1
print(a) # 1
foo()
print(a) # 42




















'''
) Написать функцию, которая выводит на экран hello world 5 раз
) Написать функцию, которая будет выводить на экран прямоугольник из символов *, размером MxN.
) Известны оценки 25 учеников. Есть ли среди них двойки?
) Удалить из списка все отрицательные элементы.

1) Написать функцию, которая будет искать и выводить на экран минимальное число, большее 300 и кратное 19.
2) Написать функцию, которая будет обменивать местами первую и последнюю цифру числа N (1234 → 4231).
3) Написать функцию, которая будет определять, делится ли число N на: 2, 3, 4, 5, ... (без использования %)
4) Написать функцию, которая будет вычислять и выводить на экран значение выражения
N^M без использования оператора возведения в степень (**).
5) С клавиатуры вводится пять чисел. Для каждого из них вывести, 
является ли оно степенью числа 3. Вынести определение степени в функцию.
6) Реализовать набор функций для работы со списком:
• Ввод с клавиатуры/инициализация случайными числами (с параметрами).
• Вывод списка на экран (в одну строчку).
• Подсчет максимума и минимума (с индексами).
• Подсчет количества элементов, равных (больших/меньших) N.
• Добавление элемента К [в конец массива/на N-ю позицию].
• Удаление из списка [последнего/Nго элемента].
• Сортировка списка по (возрастанию/убыванию). Повторяющиеся — убирать.
7) Найти третий максимум в списке.
8) Сдвинуть все элементы массива на два вправо. Оставшиеся элементы — поставить слева в том же порядке.
9) Вставить K после максимального элемента.

x) Написать функцию, которая будет выводить на экран треугольник Паскаля до N-й строчки.
• Если N <= 0, то сообщать об ошибке.
• Если N <= 8, то выводить на экран треугольник.
• В остальных случаях сообщать, что треугольник слишком велик.
x) Даны стороны треугольников. Проверить, что треугольник с указанными сторонами существует. 
Вывести на экран его периметр и площадь.
'''