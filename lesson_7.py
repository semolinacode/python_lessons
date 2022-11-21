'''
1) чему равен общий вклад топ-3 всех IP по количеству посещений? Указать процентом
2) сколько в файле уникальных IP, с которых на сайт заходили только 1 раз

3) наименьшая стоимость пачки манки
4) средняя цена на крупу за весь период наблюдений 

5) найти максимально часто встречающийся IP
6) посчитать в процентах вклад этого IP адреса в общее кол-во запросов 
7) найти последнюю запись в логах с этим IP и выяснить какой user-agent был у этой записи
получить словарь:

suspicious_agent = {
    "ip": '...',            # самый частовстречаемый ip в логах
    'fraction': 70.205,     # процент запросов с таким ip от общего кол-ва запросов
    'count': 29427,         # число запросов с таким IP
    'last': {               # вложенный словарь с 2-мя полями
        'agent': '...',     # последний записанный user-agent для этого ip
        'timestamp': '...', # последний записанный timestap для этого ip
    }
}

'''

# путь до файла может быть либо "абсолютным" либо "относительным"
# абсолютный путь - путь от корневой папки
# относительный путь - путь относительно файла, который запускают
# условные обозначения в пути:
# . - текущая директория
# .. - верхняя директория
# path = './test.txt'

# открытие файла:
# f = open(path)

# если файл читается в неправильной котировке, можно добавить параметр:
# f = open(path, encoding='utf-8')

'''
# 1 способ чтения файла "прочитать всё":
text = f.read() # читает всё содержимое файла в переменную text
'''

'''
# 2 способ чтения файла считывать по 1 строке:
line1 = f.readline() # hello\n
line2 = f.readline().strip() # world
print(line1)
print(line2)
'''

'''
# 2 способ можно использовать в цикле, чтобы прочитать файл по строкам:
line = f.readline()
# while len(line) > 0:
while line:
    print(line, end='')
    line = f.readline()
'''

'''
# 3 способ чтения файла - получить все строки файла в список
lines = f.readlines()
print(lines)
'''

'''
# для работы с json обязательно испортируем библиотеку json
import json

# json.dumps(obj) - превращает obj python в json
# json.loads(json) - превращает json в obj python

d = {
    'a': 1,
    'b': 2,
    'c': 3,
}

j = json.dumps(d)
print(j)            # {"a": 1, "b": 2, "c": 3}
print(type(j))      # <class 'str'>
d2 = json.loads(j)
print(d2)           # {'a': 1, 'b': 2, 'c': 3}
print(type(d2))     # <class 'dict'>

# json.dump(obj, fp) - превращает obj из python в json, который записывается в поток fp
# json.load(fp) - превращает json из файла в obj python

path = './test.txt'
with open(path, 'w') as fp:
    json.dump(d, fp)

with open(path) as fp:
    j = json.load(fp)
    print(j) # {'a': 1, 'b': 2, 'c': 3}
'''

# path = './test.txt'
# # режимы открытия файла (если не указать, то по-умолчанию будет использоваться r):
# # r - открывает файл только для чтения
# # w - открыт для записи (перед записью файл будет очищен)
# # a - открыт для добавления в конец файла
# # + (r+/w+) - символ обновления (чтение + запись).
# # b - символ двоичного режима
# # x - эксклюзивное создание, бросается исключение FileExistsError, если файл уже существует
# f = open(path, 'w')
# f.write('какой-то тексwwт\n')
# f.write('вторая строка')
# f.close()


# для работы с csv обязательно испортируем библиотеку csv
# import csv

# path = './test.csv'

# # чтение из csv файла:
# with open(path) as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row) # 

# запись в csv
# with open(path, 'w') as f:
#     writer = csv.writer(f)
#     # строчка в csv - список, где каждый элемент - колонка:
#     # 1 способ (записывать по отдельности)
#     row1 = ['name', 'age']
#     row2 = ['Bob', '17']
#     row3 = ['John', '22']
#     writer.writerow(row1)
#     writer.writerow(row2)
#     writer.writerow(row3)
#     # 2 способ (записать сразу все строчки):
#     # создаем двумерный список (список, элементами которого являются списки)
#     rows = [
#         ['name', 'age'],
#         ['Bob', '17'],
#         ['John', '22']
#     ]
#     writer.writerows(rows)

# # чтение csv файла
# with open(path) as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row) # будет выводить каждую строчку как список ['name', 'age']



# fp = open('./test.txt')
# 1 способов
# text = fp.read()

# 2 способ (чтение построчно)
# line1 = fp.readline()
# line2 = fp.readline()
# line3 = fp.readline()
# print(line1.strip())
# print(line2.replace('\n', ''))
# print(line3, end='')

# line = fp.readline()
# while line:
#     print(line, end='')
#     line = fp.readline()

# # 3 способ
# lines = fp.readlines()
# print(lines)

# for row in fp:
#     print(row, end='')

# fp.close()

# fp = open('./test.txt', 'w')
# fp.write('new text!!')
# fp.close()

# with open('./test.txt', 'w') as fp:
#     fp.write('new text!!')


import csv

semolina = []

with open('log_cereals.csv') as f:
    reader = csv.reader(f)
    i = 0
    for row in reader:
        if i == 0:
            i += 1
            continue
        semolina.append(float(row[1]))
print(min(semolina))
