"""Булева Логика - оператор and, True - когда оба истина"""
print("Две истины - равно : ", 1 == 1 and 2 == 2) # True
print("Одна истина, одна ложь - равно : ", 1 == 1 and 2 == 3) # False
print("Две лжи : ", 1 == 2 and 2 == 3) # False

"""Булева Логика - оператор or, True - когда хоть один истина"""
print("Две истины - равно : ", 1 == 1 or 2 == 2) # True
print("Одна истина, одна ложь - равно : ", 1 == 1 or 2 == 3) # True
print("Две лжи : ", 1 == 2 or 2 == 3) # False

"""Логический оператор not"""
print("not - ",not 1 == 1) # False - Инвертирует верное значение


"""Приоритер операторв"""
"""" 
** - степень
* / % // - умножение, деление, модуль, целочисленое
+ - сложение ыфчитание
"""