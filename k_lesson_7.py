'''
# def foo(lst: list = []):
#     lst.append(1)
#     print(lst)


# foo() # [1]
# foo() # [1, 1]
# foo() # [1, 1, 1]

Задача 1:
Пользователь вводит длину стороны квадрата N и символ CH. Программа должна вывести с помощью символа CH квадрат со стороной N

n = int(input()) # 5
ch = input()
# 1 сп
# for _ in range(n): # 0, 1, 2, 3, 4
#     print(f'{ch} ' * n)
# 2 сп
# print((((f'{ch} ' * n) + '\n') * n)[:-1])

Задача 2:
Сгенерировать рандомную последовательность из 5 чисел. Диапазон последовательности от 1 до 100. 
Если все числа в последовательности больше 50, вывести True, в ином случае False

# def foo(lst):
#     for i in lst:
#         if i < 50:
#             return False
#     return True


# lst = [random.randint(1, 100) for _ in range(5)]
# print(lst)
# print(foo(lst))

lst = [random.randint(1, 100) for _ in range(5)]
print(lst)
if min(lst) < 50:
    print(False)
else:
    print(True)  

Задача 3: 
Задачу начать решать с пустого списка:
lst = []
Папа написал Саше список продуктов (молоко, огурцы, пиво, рыбка) и бабушка тоже попросила купить 
некоторые продукты (чай, сахар, сухарики).
Мама увидела список и сказала вычеркнуть пиво и рыбку
Помоги Саше сформировать единый список покупок и посчитать сколько пунктов содержит общий список покупок

lst = []
# молоко, огурцы, пиво, рыбка
# lst.append('молоко')
# lst.append('огурцы')
# lst.append('пиво')
# lst.append('рыбка')
lst += ['молоко', 'огурцы', 'пиво', 'рыбка']

# чай, сахар, сухарики
# lst.append('чай')
# lst.append('сахар')
# lst.append('сухарики')
lst += ['чай', 'сахар', 'сухарики']
# lst.extend(['чай', 'сахар', 'сухарики'])

# -пиво, -рыбку
lst.remove('пиво')
lst.remove('рыбка')
print(lst)
print(len(lst))


Задача 4:
Есть список. пользователь вводит число. Нужно определить, есть ли это число в списке 

import random

lst = [random.randint(1, 100) for _ in range(5)]
n = int(input())
if n in lst:
    print(True)
else:
    print(False)


Задача 5:
Есть список и число, которое ввел пользователь
посчитать сколько раз это число встречается в списке

lst = [2, 2, 4, 5, 21]
n = int(input())
# print(lst)
# print(lst.count(n))
amount_n = 0
for i in lst:
    if i == n:
        amount_n += 1
print(amount_n)
'''

'''
Работа с файлами
f = open(path_to_file, mode)

функция open открывает файл, который лежит по пути path_to_file
функция возвращает объект для работы с файлом

path:
1) абсолютные - полный путь от начальной точки до самого файла/директории
2) относительные - путь относительно точки запуска программы
. - текущая директория
.. - предыдущая директория

mode:
r - read - открытие файла для чтения
w - write - открытие файла для записи (создает фаил, если его не было). 
    Если файл был, полностью перезаписывает его
a - append - открытие файла для записи (создает фаил, если его не было). 
    Если файл был, текст записывается в конец файла
b - binary - для работы с бинарными файлами
'''

# f = open('/Users/riocrash/python_lessons/lesson_today/text.txt')
# f = open('./text.txt', 'r')

# 1 способ: прочитать весь файл
# text = f.read()
# print(text)

# 2 способ:
# lines = f.readlines()
# print(lines)

# 3 способ:
# line = f.readline()
# while line != '':
#     print(line, end='')
#     line = f.readline()

# !! 4 способ !!
# for line in f:
#     print(line, end='')

# f.close()

# запись в файл
# f = open('./text3.txt', 'a')
# f.write('\nthe end')
# f.close()

# добавляем кодировку encoding
# f = open('./text.txt', encoding='utf-8')
# print(f.read())
# f.close()

# менеджер контекста
# f = open('./text.txt', encoding='utf-8')
# print(f.read())
# f.close()

# with open('./text.txt', 'r', encoding='utf-8') as f:
#     # print(f.read())
#     for line in f:
#         print(line)


'''
задача 1:
написать программу, которая создает файл python с кодом, который выводит 
hello world!!

# with open('first.py', 'w') as f:
#     f.write('print("Hello World!!")')

задача 2:
1) создайте папку test
пользователь вводит число N
создать N txt файлов

# n = int(input()) # 10
# for i in range(n):
#     with open(f'./test/file_' + str(i) +'.txt', 'w') as f:
#         pass

задача 3:
создать файл ex3.txt
в файл записать 123456 строк
в каждой строке написано qwerty столько раз, чему равна сумма цифр в 
номере строки
'''

# with open('text.txt', 'w') as f:
#     for i in range(1, 123456+1):
#         f.write(f'{i}: {)}\n')
#         f.writelines()

def add_numbers_digits(num: int) -> int:
    res = 0
    for i in str(num):
        res += int(i)
    return res
    # return sum([int(ch) for ch in str(num)])


n = int(input('введите кол-во строк: '))
with open('ex3.txt', 'w') as f:
    for i in range(1, n+1):
        f.write(('qwerty, ' * add_numbers_digits(i))[:-2] + '\n')
