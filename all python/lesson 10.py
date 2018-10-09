""""""
"""Функции как обьекты"""

def myfunc(x, y):
    return x * y

a = 10
b = 5
myNewFunc = myfunc # Можем переназначить имя функции как и переменной
print(myNewFunc(a, b))

