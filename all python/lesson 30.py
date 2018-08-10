"""Лямбда функции"""

def mylambdaFunc(func, arg):
    return func(arg)
print(mylambdaFunc(lambda x: x + 2 * 3, 5))


x = lambda y: y + y
print(x(5))  # Можно передавать аргументы как обычнвм функциям