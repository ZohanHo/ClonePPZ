""""""
"""Вызов исключений - raise"""


num = input("введите число: ")
if int(num) < 0: # Проверка введенного числа на целое, положительное
    raise ValueError ("Ошибка - меньше нуля") # если не указать аргументц, будет и скать все ошибки

