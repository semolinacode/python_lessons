def prepare_string(s: str):
    return s.replace('"', '').replace('(', '').replace(')', '').replace('.', '').replace(',', '').lower()


s = '''которая сможет подсчитать слова, разделённые пробелом и вывести получившуюся статистику.
Программа должна считывать одну строку со стандартного ввода и 
выводить для каждого уникального слова в этой строке число его повторений (без учёта регистра) 
в формате "слово количество" (см. пример вывода).
Порядок вывода слов может быть произвольным, каждое уникальное слово​ должно выводиться только один раз'''

s = prepare_string(s)
d = {}
for word in s:
    if word in d:
        d[word] += 1
    else:
        d[word] = 1

# сортировка по ключам
d = dict(sorted(d.items()))
# print(d)

# сортировка по значениям
sorted_d = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
# print(sorted_d)

'''
lambda функция - анонимная функция
синтаксис
lambda список_паратров: возвращаемое_значение

def foo(x):
    return x**2

foo = lambda x: x**2


в python все сущности являются объектами 2-го типа
то есть все объекты можно передавать в функции, присваивать к переменным итд

# 1 пример (еще одна функция print)
print('hello')
print(print)
a = print
a('world')

# 2 пример (передаем функцию в функцию) (callback)
def foo(foo2, a, b):
    res = foo2(a, b)
    return res

# def some_foo(c, d):
#     return c + d

# print(foo(some_foo, 1, 2))
print(foo(lambda a, b: a + b, 1, 2))
'''

'''
Практика:

def foo(a, b, c):
    return a * b + c

def foo2(a):
    if a % 2 == 1:
        return True
    else:
        return False

def foo3(s):
    result = s.replace('a', '@')
    return result


f1 = lambda a, b, c: a * b + c
f2 = lambda a: bool(a % 2)
f3 = lambda s: s.replace('a', '@')
'''

'''
map(function, query)
функция map() применяем функцию function к каждому элементу query и формирует коллекцию из результатов

words_lst = ['hello', 'apple', 'cat']
new_words_lst = list(map(lambda word: word.replace('a', '@'), words_lst))
print(new_words_lst)

# аналог
# new_words_lst = []
# for word in words_lst:
#     new_words_lst.append(word.replace('a', '@'))
# print(new_words_lst)


filter(function, query)
функция filter применяем функцию function к каждому элементу query и если функция возвращает True, 
    элемент попадает в новую коллекцию (если False, то не попадает)
lst = [1, 2, 3, 
4, 5, 6, 7, 8, 9, 10]
new_lst = list(filter(lambda a: bool(a % 2), lst))
print(new_lst)
'''

'''
import json

school = {
    '1a': 20,
    '1b': 23,
    '2b': 10,
    '6a': 22,
    '7c': 26,
    '8': [
        ('a', 22),
        ('b', 23),
        ('c', 24),
    ],
    '9': {
        'a': 25,
        'b': 26,
        'c': 27,
    },
}

json_school = json.dumps(school)
print(json_school)
print(type(json_school))

res = json.loads(json_school)
print(res)
print(type(res))
'''

'''
import csv

rows = [
    ['some1', 1, 100],
    ['some2', 4, 50],
    ['some3', 100, 0],
    ['some4', 21, 2],
    ['some5', 3, 1000],
]

# запись
# with open('test.csv', 'a') as f:
#     writer = csv.writer(f)
#     writer.writerows(rows)

# чтение:
rows = []
with open('test.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        rows.append(row)
        print(row)
print(rows)
'''


'''
import pickle

school = {
    '1a': 20,
    '1b': 23,
    '2b': 10,
    '6a': 22,
    '7c': 26,
    '8': [
        ('a', 22),
        ('b', 23),
        ('c', 24),
    ],
    '9': {
        'a': 25,
        'b': 26,
        'c': 27,
    },
}

with open('test.dat', 'wb') as f:
    pickle.dump(school, f)

with open('test.dat', 'rb') as f:
    res = pickle.load(f)
print(res)
print(type(res))
'''


# import csv

# 1) найти наименьшую стоимость пачки манки
# 2) найти среднюю цену на крупу за весь период наблюдений

# 1 способ:
# semolina_min = None
# with open('./resources/log_cereals.csv') as f:
#     readed = csv.reader(f)
#     for row in readed:
#         if not row[0].isnumeric():
#             continue
#         semolina_price = float(row[1])
#         if semolina_min is None:
#             semolina_min = semolina_price
#             continue
#         if semolina_price < semolina_min:
#             semolina_min = semolina_price
# print(semolina_min)

# 2 способ:
# rows = []
# with open('./resources/log_cereals.csv') as f:
#     readed = csv.reader(f)
#     for row in readed:
#         rows.append(row)
# rows = rows[1:]
# print(min(list(map(lambda row: float(row[1]), rows))))

# 3 способ:
# rows = []
# with open('./resources/log_cereals.csv') as f:
#     readed = csv.reader(f)
#     for row in readed:
#         rows.append(row[1])
# rows = rows[1:]
# print(min(rows))


# 3) чему равен общий вклад топ 3 всех ip по количеству посещений
# 4) сколько в файле уникальных ip, с которых на сайт заходили только 1 раз

# import json

# json_school = json.dumps(school)
# print(json_school)
# print(type(json_school))

# res = json.loads(json_school)
# print(res)
# print(type(res))
