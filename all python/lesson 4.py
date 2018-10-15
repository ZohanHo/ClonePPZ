""""""
"""Булева Логика - оператор and, True - когда оба истина"""
print("Две истины - равно : ", 1 == 1 and 2 == 2) # True
print("Одна истина, одна ложь - равно : ", 1 == 1 and 2 == 3) # False
print("Две лжи : ", 1 == 2 and 2 == 3) # False

"""Булева Логика - оператор or, True - когда хоть один истина"""
print("Две истины - равно : ", 1 == 1 or 2 == 2) # True
print("Одна истина, одна ложь - равно : ", 1 == 1 or 2 == 3) # True
print("Две лжи : ", 1 == 2 or 2 == 3) # False

"""Логический оператор not"""
print("not - ",not 1 == 1) # False - проверяе что значения не равны

x = True
print(not x) # Если x равно True, оператор вернёт False. Если же x равно False, получим True.



"""
Краткая запись мат. операций и присваивания
"""
a = 2; a = a * 3
print(a)

b = 2; b *= 3
print(b)

print ("умножение первое", 2 + 3 * 4) # 14  умножение всегда первое

"""Приоритер операторв

lambda       лямбда-выражение
or           Логическое “ИЛИ”
and          Логическое “И”
not x        Логическое “НЕ”
in, not in   Проверка принадлежности
is, is not   Проверка тождественности
<, <=, >, >=, !=, ==    Сравнения
|            Побитовое “ИЛИ”
^            Побитовое “ИСКЛЮЧИТЕЛЬНО ИЛИ”
&            Побитовое “И”
<<, >>       Сдвиги
+, -         Сложение и вычитание
*, /, //, %  Умножение, деление, целочисленное деление и остаток от деления
+x, -x       Положительное, отрицательное
~x           Побитовое НЕ
**           Возведение в степень
x.attribute  Ссылка на атрибут
x[индекс]    Обращение по индексу
x[индекс1:индекс2]     Вырезка
f(аргументы ...)       Вызов функции
(выражения, ...)       Связка или кортеж 2
[выражения, ...]       Список
{ключ:данные, ...}     Словарь
 
"""

"""Ассоциативность

Операторы обычно обрабатываются слева направо. Это означает, что операторы с равным
приоритетом будут обработаны по порядку от левого до правого. Например, 2 + 3 + 4
обрабатывается как (2 + 3) + 4. Некоторые операторы, как, например, оператор присваивания,
имеют ассоциативность справа налево, т.е. a = b = c рассматривается как a = (b
= c).
"""

