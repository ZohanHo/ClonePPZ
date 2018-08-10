"""Лямбда функции"""

def mylambdaFunc(func, arg):
    return func(arg)
print(mylambdaFunc(lambda x: x + 2 * 3, 5))


x = lambda y, x ,z = 20: y + x + z
print(x(5, 6))  # Можно передавать аргументы как обычнвм функциям.