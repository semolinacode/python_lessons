'''
# Файл log_100.json:
# 1) чему равен общий вклад топ-3 всех IP по количеству посещений? Указать процентом
# 2) сколько в файле уникальных IP, с которых на сайт заходили только 1 раз

# Файл log_full.csv:
# 5) найти максимально часто встречающийся IP
# 6) посчитать в процентах вклад этого IP адреса в общее кол-во запросов 
# 7) найти последнюю запись в логах с этим IP и выяснить какой user-agent был у этой записи
# получить словарь:

# suspicious_agent = {
#     "ip": '...',            # самый частовстречаемый ip в логах
#     'fraction': 70.205,     # процент запросов с таким ip от общего кол-ва запросов
#     'count': 29427,         # число запросов с таким IP
#     'last': {               # вложенный словарь с 2-мя полями
#         'agent': '...',     # последний user-agent для этого ip
#         'timestamp': '...', # последний timestap для этого ip
#     }
# }

import json

path_json = 'log_100.json'
path_csv = 'log_full.csv'

ip_amount_dict = {}

with open(path_json) as f:
    res = json.load(f)
total_request = len(res)

for row in res:
    ip = row['ip']
    if ip in ip_amount_dict:
        ip_amount_dict[ip] += 1
    else:
        ip_amount_dict[ip] = 1
sorted_ip_amount_dict = dict(sorted(ip_amount_dict.items(), key=lambda item: item[1], reverse=True))
# print(sum(list(sorted_ip_amount_dict.values())[:3]) / total_request)

# amount_uniq = 0
# for row in sorted_ip_amount_dict.items():
#     if row[1] == 1:
#         amount_uniq += 1
# print(amount_uniq)


# O(...)
# O - "О большое" показывает зависимость времени от количества элементов
# O(N) - для списка из N элементов, придется сделать N операция (обратиться к каждому элемну 1 раз)
# O(1) - время поиска элемента в словаре
# O(N) - время поиска элемента в списке

# O(2N) 
# O(N^2)
# O(log(N))
# O(fact(N))



# Файл log_full.csv:
# 5) найти максимально часто встречающийся IP
# 6) посчитать в процентах вклад этого IP адреса в общее кол-во запросов 
# 7) найти последнюю запись в логах с этим IP и выяснить какой user-agent был у этой записи
# получить словарь:

# suspicious_agent = {
#     "ip": '...',            # самый частовстречаемый ip в логах
#     'fraction': 70.205,     # процент запросов с таким ip от общего кол-ва запросов
#     'count': 29427,         # число запросов с таким IP
#     'last': {               # вложенный словарь с 2-мя полями
#         'agent': '...',     # последний user-agent для этого ip
#         'timestamp': '...', # последний timestap для этого ip
#     }
# }

# import csv

# ip_amount_dict = {}
# total_request = 0
# ip_info_dict = {}

# with open(path_csv) as f:
#     reader = csv.reader(f)
#     for row in reader:
#         if row[1] == 'ip':
#             continue
#         timestamp = row[0]
#         ip = row[1]
#         user_agent = row[2]
#         if ip not in ip_amount_dict:
#             ip_amount_dict[ip] = 1
#         else:
#             ip_amount_dict[ip] += 1
#         ip_info_dict[ip] = {
#             'agent': user_agent,
#             'timestamp': timestamp
#         }
#         total_request += 1
# sorted_ip_amount_dict = dict(sorted(ip_amount_dict.items(), key=lambda item: item[1], reverse=True))
# res_ip, res_amount = list(sorted_ip_amount_dict.items())[0]
# # total_request = sum(list(sorted_ip_amount_dict.values()))
# # print(total_request)
# fraction = res_amount / total_request * 100
# # ip_info_dict[res_ip]

# suspicious_agent = {
#     "ip": res_ip,            # самый частовстречаемый ip в логах
#     'fraction': fraction,     # процент запросов с таким ip от общего кол-ва запросов
#     'count': res_amount,         # число запросов с таким IP
#     # 'last': {               # вложенный словарь с 2-мя полями
#     #     'agent': '...',     # последний user-agent для этого ip
#     #     'timestamp': '...', # последний timestap для этого ip
#     # }
#     'last': ip_info_dict[res_ip]
# }
# # 4.128943104927094
# # 4.128844733519167
# print(suspicious_agent)
'''

# import os
# from os import path
# import sys


# print(path.abspath('.'))
# a = path.join('lululu/lalala', 'lololo')
# print(a)
# print(sys.argv)
# print(sys.int_info)

'''
minishell

Написать программу, которая будет постоянно считывать ввод пользователя и 
обрабатывать его команды как это делает терминал 
Команды, которые нужно обработать:
1) ls - вывести все папки и файлы текущей директории
2) ls path - вывести все папки и файлы директории path
3) cd path - переместиться в директорию path
4) pwd - вывести путь до текущей директории
5) mkdir name - создать директорию
6) touch name - создать файл
7) rm name - удалить файл
8) rm -rf - удалить директорию и всё, что внутри нее

!!!!!!!!!!! ИСПОЛЬЗОВАТЬ os.system() НЕЛЬЗЯ !!!!!!!!!!!!!!!
'''

import os


def error(command):
    print(f'zsh: command not found: {command}')


def ls_handler(args):
    if args is None:
        for file in os.listdir('.'):
            print(file)
    elif os.path.isdir(args):
        for file in os.listdir(args):
            print(file)
    else:
        error(command)


commands = {'ls': ['', 'path'], 
            'cd': ['path'],
            'pwd': [''],
            'mkdir': ['path'],
            'touch': ['path'],
            'rm': ['path', '-rf']
}

while True:
    command = input()
    # "ls"

    command_lst = command.split()
    if len(command_lst) == 1:
        command, args = command_lst[0], None
    elif len(command_lst) == 2:
        command, args = command_lst[0], command_lst[1]
    else:
        error(command)
        continue

    if command not in commands:
        error(command)
        continue

    if command == 'ls':
        ls_handler(args)
        continue
