"""Функциональное програмирование"""

def apply(func, arg):
    return func(func(arg))
def add(x):
    return (x + 5)


print(apply(add, 10))

"""
Изначально вызывается функция apply, которая принимает на вход другую функцию и параметр
вернутся нам должен ответ от функции add, которая вызвана два раза(10+5)  + 5 , запутано в том что функция add берет отгумент
c функции apply
"""
