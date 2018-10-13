""""""
"""Исключения"""

try:
    print(1) # Выполняется пока не сработаеи ошибка
    print(10 / 0)
except ZeroDivisionError:
    print("unknown_var") # если в try ошибка
finally:
    print("This is executed last") # работает всегда