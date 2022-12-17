'''
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
'''

'''
import os, shutil


def error(command):
    print(f'Command not found: {command}')


def ls(arg):
    if arg is None:
        print(os.listdir(path='.'))
    else:
        print(os.listdir(arg))


def cd(arg):
    if arg is None:
        error(command_list[0])
    else:
        os.chdir(arg)


def pwd(arg):
    if arg is None:
       print(os.getcwd())
    else:
        error(command_list[0])


def mkdir(arg):
    if arg is None:
       error(command_list[0])
    else:
        os.mkdir(arg)


def touch(arg):
    if arg is None:
       error(command_list[0])
    else:
        f = open(arg, 'w')
        f.close()

def rm(arg):
    if arg is None:
       error(command_list[0])
    elif arg == '-rf':
       shutil.rmtree('.', True)
    else:
        os.remove(arg)


commands = ['ls', 'cd', 'pwd', 'mkdir', 'touch', 'rm']
while True:
    command = input()
    command_list = command.split()
    if command_list[0] not in commands:
        error(command_list[0])
        continue

    if len(command_list) == 1:
        arg = None
    elif len(command_list) == 2:
        arg = command_list[1]
    else:
        error(command_list[0])
        continue

    if command_list[0] == 'ls':
        ls(arg)
        continue
    elif command_list[0] == 'cd':
        cd(arg)
        continue
    elif command_list[0] == 'pwd':
        pwd(arg)
        continue
    elif command_list[0] == 'mkdir':
        mkdir(arg)
        continue
    elif command_list[0] == 'touch':
        touch(arg)
        continue
    elif command_list[0] == 'rm':
        rm(arg)
        continue
'''

'''
player:
    имя
    сила
    ловкость
    расса
    -----------
    ударить
    сделать комбо
    подобрать предмет
    стрелять

enemy:
    имя: str
    уровень: int
    здоровье: int
    -----------
    искать противника
    стрелять
    умереть

boss(enemy):
    суперспособность
    -----------
    использовать суперспособность

'''

# s = 'hello'
# s.capitalize()


'''
класс - новый тип данных. Структура, которая хранит поля и методы какой-то сущности
объект (экземпляр) - определенный класс
поле (свойстро, атрибут) - переменная, которая характеризует класс
метод (функция) - то, что объект может делать
'''

'''
Human:
    def помолоть_кофе(кофе, кофемолка):
        ...

Player:
    имя
    ---------
    def стрелять(оружие):
        оружие.shoot()


Pistol:
    калибр
    размер обоймы
    ---------
    shoot():
        print('пиф-паф')

Bazuka:
    калибр
    размер обоймы
    ---------
    shoot():
        print('бабах')
'''

# class CryptoUser:
#     pass

class CryptoUser:
    # статическое поле
    bear_market = True

    # вызывается во время создания объекта
    def __init__(self, name, wallet, luck_chance=0.5) -> None:
        # self - текущий объект
        self.name = name
        self.wallet = wallet
        self.luck_chance = luck_chance
    
    def print_info(self):
        # self - объект перед точкой
        print(self.name, self.wallet, self.luck_chance)

    # статический метод:
    @staticmethod
    def swith_market():
        CryptoUser.bear_market = not CryptoUser.bear_market


a = CryptoUser('SBF', '0x8437yuy34ru34nj34')
# b = CryptoUser('CZ', '0xiubfub76rgf7rebufei', 0.8)
# a.print_info()
# b.print_info()

# print(a.bear_market)
# print(b.bear_market)

# print(CryptoUser.bear_market)
# CryptoUser.swith_market()
# print(CryptoUser.bear_market)

# print(a.bear_market)
# a.swith_market()
# print(a.bear_market)

'''
Задача 1:
Написать класс "Point"
У класса есть 2 поля: x, y
Реализовать методы:
1) вывод
2) рассчитать расстояние между 2-мя точками
3) если точки находятся на одной линии по-горизонтали или по-вертикали, то нарисовать их
1, 2
1, 5

 |
 |
 |

2, 3
8, 3
  ------
'''

from typing import Any

class Point:
    def __init__(self, x=0, y=0) -> None:
        self.x = x
        self.y = y
        # print(f'вывзвался конструктор {self}')
    
    def __del__(self):
        # print(f'вывзвался деструктор {self}')
        pass

    def __repr__(self) -> str:
        return f'Координата х: {self.x}, координата y {self.y}'
    
    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        print(args)
        print(kwargs)
        return 1
    
    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        elif isinstance(other, int):
            return Point(self.x + other, self.y + other)
        raise TypeError('unsupported operands')
    
    def __lt__(self, other) -> bool:
        start_point = Point(0, 0)
        dist1 = self.dist(start_point)
        dist2 = other.dist(start_point)
        if dist1 < dist2:
            return True
        return False
    
    def dist(self, other):
        if isinstance(other, Point):
            return ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5

    def draw(self, other):
        if self.x == other.x:
            for _ in range(abs(self.y - other.y)):
                print('|')
        if self.y == other.y:
            print('-' * (abs(self.x - other.x)))


p1 = Point(1, 2)
p2 = Point(1, 1)
print(p1)
print(p2)

# print(p1 + p2)
print(p1 + 3)
print(p1.__add__(3))

print(p1 < p2)
print(p1.__lt__(p2))
