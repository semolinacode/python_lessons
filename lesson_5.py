# s = 'hello'
# # print(s[start:stop:step])
# print(s[1:4]) # ell
# print(s[:4]) # ell
# print(s[:]) # hello
# print(s[::2]) # hlo

# # Задача 4:
# s = 'abcdifghijk'
# s[3:6] # dif
# s[:6] # abcdif
# s[3:] # difghijk
# s[::-1] # cba
# s[-3:] # ijk
# s[:-6] # abcdi
# s[-1:-10:-2] # kigic

# s = 'qwerty'
# for ch in s:
#     print(ch)

# Задача 6:
# Напишите программу, которая сможет посчитать как часто встречается в введенной строке, 
# введенный символ. Ответ в процентах.
# def foo(text, ch):
#     count = 0
#     for i in text:
#         if i == ch:
#             count += 1
#     return count / len(text) * 100


# text = '''мороз и солнце; день чудесный!\nеще ты дремлешь, друг прелестный —\nпора, красавица, проснись:\nоткрой сомкнуты негой взоры\nнавстречу северной авроры,\nзвездою севера явись!\nвечор, ты помнишь, вьюга злилась,\nна мутном небе мгла носилась;\nлуна, как бледное пятно,\nсквозь тучи мрачные желтела,\nи ты печальная сидела —\nа нынче... погляди в окно:'''
# ch = input('Введите символ, который хотите найти: ') # о
# res = foo(text, ch)
# print(res)


# s = 'Hello  worl d!!'
# # new_str = s.replace('l', '@')
# # print(new_str)
# lst = s.split(' ')
# print(lst)


email = 'qwert@gmail.ru'
lst = email.split('@')
print(lst)
domen = lst[0]
lst2 = lst[1].split('.')
print(lst2)




'''
Задача 1:
Значения каких выражений будет True?
print("239" < "30" and 239 < 30)
print("239" < "30" and 239 > 30)
print("239" > "30" and 239 < 30)
print("239" > "30" and 239 > 30)

Задача 2:
есть 2 строки:
a = 'Hello'
b = 'World'
вывести:
1) HelloWorld
2) Hello World
3)  Hello
    World


Задача 3: 
Паша очень любит кататься на общественном транспорте, 
а получая билет, сразу проверяет, счастливый ли ему попался. 
Билет считается счастливым, если сумма первых трех цифр совпадает с 
суммой последних трех цифр номера билета. 
Программа должна выводить “Счастливый” или “Обычный”. 

Задача 4:
s = 'abcdifghijk'
s[3:6]?
s[:6]?
s[3:]? 
s[::-1]? 
s[-3:]? 
s[:-6]? 
s[-1:-10:-2]

Задача 5:
Дана последовательность символов. Проверить, является ли она палиндромом

Задача 6:
Напишите программу, которая сможет посчитать как часто встречается в введенной строке, 
введенный символ. Ответ в процентах. 
Программа не должна зависеть от регистра вводимых символов.

Задача 7:
Написать функцию проверки email

Задача 8:
Необходимо написать программу, которая сможет посчитать повторяющиеся символы и вывести сокращенную строку, пример:
Вход: s = 'aaaabbcaa'
Выход: 'a4b2c1a2'

Задача 9:
Определить количество слов в строке.
Вводится строка, состоящая из слов, разделенных пробелами. 
Требуется посчитать количество слов в ней.

Задача 10:
определить сложность пароля

Задача 11:
На основании предоставленного отрывка текста определить 3 наиболее часто встречаемых символа в нем. 
Пробелы нужно игнорировать (не учитывать при подсчете). 
Для выведения результатов вычислений требуется написать функцию top3(st). 
Итог работы функции представить в виде строки: «символ – количество раз, символ – количество раз…».

Задача 12:
Дмитрий считает, что когда текст пишут в скобках (как вот тут, например), его читать не нужно. 
Вот и надумал он существенно укоротить время чтения, написав функцию, которая будет удалять все, что расположено внутри скобок. 

Задача 13:
Спарсить с помощью методов строки инструменты с coingecko

'''
