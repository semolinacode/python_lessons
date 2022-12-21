"""
class Car:
    def __init__(self, name, weight, power, passwd) -> None:
        # private, public
        self.name = name
        self.weight = weight
        self.__power = power
        self.__passwd = passwd
    
    def get_passwd(self):
        return '*' * len(self.__passwd)

    def get_power(self):
        return self.__power
    
    def set_power(self, value):
        if value < 0:
            return
        self.__power = value

    def __repr__(self) -> str:
        return f'Car: {self.name}; {self.weight}; {self.__power}'


a = Car('BMW', 1000, 189, 'qwerty')
print(a)
'''
доступ к полю, которое начинается с 2-х нижних подчеркиваний (private поле) осуществляется с помощью:
_ClassName__AttributeName
'''
# print(dir(a))
# print(a._Car__power)
# a._Car__power = 12

print(a.get_power())
a.set_power(11)
print(a.get_power())
print(a.get_passwd())
"""

"""
class A:
    def __init__(self) -> None:
        self.first = 1
        self._second = 2
        self.__third = 3
    
    def __repr__(self) -> str:
        return f'{self.first}; {self._second}; {self.__third}'


class B(A):
    def __init__(self) -> None:
        super().__init__()
        self.fourth = 4
    
    def __repr__(self) -> str:
        # res = super().__repr__()
        # res = res + f'; {self.fourth}'
        # return res
        return super().__repr__() + f'; {self.fourth}'
        

obj1 = B()
# print(B.mro())
print(obj1)
print(obj1.first)
print(obj1._second)
print(obj1._A__third)
print(dir(obj1))
"""

"""
class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

# MRO - method resolution order
# MRO2 - поиск в глубину
# MRO3 - поиск в ширину

print(D.mro())
"""
from abc import ABC, abstractmethod

class Weapon(ABC):
    def __init__(self, name, caliber, magazine) -> None:
        self.name = name
        self.caliber = caliber
        self.magazine = magazine

    @abstractmethod
    def shoot(self):
        return


class Pistol(Weapon):
    def shoot(self):
        print('Пиф-Паф')


class Bazuka(Weapon):
    def shoot(self):
        print('БАБАХ')


class Player:
    def __init__(self, name: str, speed: int) -> None:
        self.name = name
        self.speed = speed

    def shoot(self, weapon: Weapon):
        print(f'{self.name} стреляет из {weapon.name}!!')
        weapon.shoot()


# player = Player('Duke', 20)

# pistol = Pistol('ПМ', 9, 12)
# bazuka = Bazuka('Базука', 50, 2)

# # player.shoot(pistol)
# player.shoot(bazuka)

o = Weapon('lalala', 10, 8)
print(o.name)

