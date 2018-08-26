"""Функции isinstance() и type()"""

"""isinstance()  проверят является ли обьект экземпляром какогото класса"""

"""type() Хотя функция type() возвращает тип переданного аргумента,
 с ее помощью можно проверить, принадлежит ли аргумент тому или иному типу:"""


a = 10
b = [1,2,3]
print(type(a) == int) # True
print(type(b) == list) #True
print(type(a) == float) #False

"""В отличие от type(), функция isinstance() специально создана для проверки
 принадлежности данных определенному классу (типу данных):"""

isinstance(a,int) #True
isinstance(b,list) #True
isinstance(b,tuple) #False

c = (4,5,6)
isinstance(c,tuple) #True
"""Кроме того isinstance() по сравнению с type() позволяет проверить данное на принадлежность
 хотя бы одному типу из кортежа, переданного в качестве второго аргумента:"""

isinstance(a,(float, int, str)) #True
isinstance(a,(list, tuple, dict)) #False

"""Другое отличие isinstance(). Эта функция поддерживает наследование. 
Для isinstance() экземпляр производного класса также является экземпляром базового класса. 
Для type() это не так:"""

class A (list):
    pass

a = A()
type(a) == list #False
type(a) == A #True
isinstance(a,A) #True
isinstance(a,list) #True


