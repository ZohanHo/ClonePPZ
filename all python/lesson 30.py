""""""

"""Лямбда функции"""

def mylambdaFunc(func, arg):
    return func(arg)
print(mylambdaFunc(lambda x: x + 2 * 3, 5))


func = lambda y, x ,z = 20: y + x + z
print(func(5, 6))  # Можно передавать аргументы как обычным функциям.