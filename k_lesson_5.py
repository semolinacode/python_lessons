'''
Задача 1:
Температура воды в кастрюле 7 градусов. Кастрюлю
поставили на огонь, температура увеличивается каждые
2с на 1 градус, нужно определить через сколько
секунд вода закипит т.е. будет равна 100 градусов.

Задача 2:
Задача 1 только сколько потребуется минут и секунд
для достижения температуры в 100 градусов.

start_t = 7
delta_t = 1
delta_time = 2
target_t = 100
result_seconds = 0

while start_t < target_t:
    start_t += delta_t
    result_seconds += delta_time
print(result_seconds)
print(f'minutes: {result_seconds // 60}; seconds: {result_seconds % 60}')

Задача 3:
Написать программу, которая выводит таблицу
умножения числа N в интервале от L до K. Ввод N, L,
K выполнять с клавиатуры.

Задача 4:
реализовать стандартную функцию isdigit()

s = '12j434376875785785757'
i = 0
result = True
while i < len(s):
    if not (s[i] >= '0' and s[i] <= '9'):
        result = False
        break
    i += 1
print(result)

Задача 5:
Магазин. Пользователю постоянно предлагается выбрать
товар из списка:
1- хлеб - 100р
2- молоко - 120р
3- огурцы - 60р
4- апельсины - 450р
Для выхода введите EXIT
За один подход пользователь может взять только один
товар и после продолжить выбирать еще товары. Если
пользователь ввел EXIT мы прекращаем выводить ему
список товаров и показываем сколько он должен
заплатить за товары.

a = input()
res_summ = 0
while a != 'EXIT':
    if a == '1':
        res_summ += 100
    elif a == '2':
        res_summ += 120
    else:
        print('нет такого номера')
    a = input()
print(res_summ)

Задача 6:
Клиент оформил вклад на m тысяч рублей в банке под
k% годовых. Через сколько лет сумма вклада превысит
s тысяч рублей, если за это время клиент не будет
брать деньги со счета.

Задача 7:
Необходимо написать программу, которая сможет посчитать повторяющиеся символы и вывести сокращенную строку, пример:
Вход: s = 'aaaabbcaa'
Выход: 'a4b2c1a2'

s = 'a'
res = ''
i = 0
while i < len(s):
    ch = s[i]
    num = 1
    while i < len(s) - 1 and ch == s[i+1]:
        num += 1
        i += 1
    res += f'{ch}{num}'
    i += 1
print(res)

Задача 8:
Дмитрий считает, что когда текст пишут в скобках (как вот тут, например), его читать не нужно. 
Вот и надумал он существенно укоротить время чтения, написав функцию, которая будет удалять все, что расположено внутри скобок.

Задача 9:
Определить сложность пароля (сделать функцию как на обычных сайтах. То есть проверять большие буквы, символы, цифры И так далее. Подсказка: ascii)

Задача 10:
Вывести равнобедренный треугольник из символа "*" (высота указывается с клавиатуры)
У треугольника равнобедренными должны быть левая и правая стороны. Например для высоты 3:
    *
  * * *
* * * * *
'''

# def count_time(start_t: int, delta_t: int, delta_time: int, target_t: int, result_seconds: int = 0) -> int:
#     '''get initial params and count result\n
#     start_t - start time\n
#     delta_time - delta time'''
#     while start_t < target_t:
#         start_t += delta_t
#         result_seconds += delta_time
#     return result_seconds


# !! То, что написано после return, будет подставлено на место вызова функции !!
# a = count_time(1, 2, 2, 100)
# print(a)

# a = count_time(1, 2, 2, 100)
# print(a)

'''
1 задача:
функция принимает 2 числа a и b
возвращает a, если a - наибольшее число
в ином случае возвращает b
'''

def my_max(a: int, b: int) ->int:
    if a < b:
        a = b
    return a


def bigger(a, b):
    if a > b:
        return a
    return b
    

def isdigit(s):
    i = 0
    result = True
    while i < len(s):
        if not (s[i] >= '0' and s[i] <= '9'):
            result = False
            break
        i += 1
    return result

def isdigit(s):
    i = 0
    while i < len(s):
        if not (s[i] >= '0' and s[i] <= '9'):
            return False
        i += 1
    return True


# Составьте программу, выводящую на экран квадраты
# чисел от 10 до 20 включительно.
def print_sq(a, b):
    while a <= b:
        print(a ** 2)
        a += 1


def check_password(passwd: str) -> int:
    big_letters = 0
    small_letters = 0
    digits_letters = 0
    symbols_letters = 0
    i = 0
    while i < len(passwd):
        if passwd[i] >= '0' and passwd[i] <= '9':
            digits_letters += 1
        elif ord(passwd[i]) >= 33 and ord(passwd[i]) <= 47 or \
                ord(passwd[i]) >= 58 and ord(passwd[i]) <= 64:
            symbols_letters += 1
        elif passwd[i] >= 'a' and passwd[i] <= 'z':
            small_letters += 1
        elif passwd[i] >= 'A' and passwd[i] <= 'Z':
            big_letters += 1
        else:
            return 0
        i += 1
    
    if len(passwd) < 8 or symbols_letters == 0 and digits_letters == 0:
        return 1
    elif len(passwd) <= 12:
        return 2
    return 3

# реализовать свою функцию find()

def my_find(string: str, ch: str):
    i = 0
    while i < len(string):
        if string[i] == ch:
            return i
        i += 1
    return -1


s = 'wqwerty'
ch = 'we'
print(my_find(s, ch) == s.find(ch))
