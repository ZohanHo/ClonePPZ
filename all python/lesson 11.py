"""Функции в качестве аргументов"""

def add1(x, y):
    return x + y

def do_twice(func_add, x, y): # принимает на вход функцию и два параметра
    return func_add(x, y)   # Функция которая вызывает add1

a = 5
b = 10

print("результат первой", do_twice(add1, a, b)) # Прументинимает как аргумент функцию и 2 числа a, b



def add2(x, y):
    return x + y

def do_twice(func_add, x, y): # принимает на вход функцию и два параметра
    return func_add(func_add(x, y), func_add(x, y)) # В скобках выполняется 2 раза, а результаты берутся как аргументы

a = 5
b = 10

print("результат второй", do_twice(add2, 5, 10))