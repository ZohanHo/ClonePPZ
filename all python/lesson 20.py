""""""
"""Когда мы присваиваем функцию переменной var то на экран выводиться Hi,
а в переменную заносится значение от возврата функции. так как return отсутствует
то возвращается еще и значение по умолчанию, то есть None"""

def func():
    print("hi")

var = func()
print(var)

