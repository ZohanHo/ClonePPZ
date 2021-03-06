""""""
"""Функции"""

"""Переменное число параметров

Иногда бывает нужно определить функцию, способную принимать любое число параметров.
Этого можно достичь при помощи звёздочек
"""
def total(initial, *numbers, **keywords): # 
    count = initial
    for number in numbers:
        count += number  # Так как ето кортеж, то при помощи цыкла добавляем 10, 1, 2, 3
    for key in keywords:
        count += keywords[key] #Так как ето словарь, по ключу получаем значение, при помощи цыкла добавляем  50, 100
    return count # возвращаем полученую сумму
print(total(10, 1, 2, 3, vegetables=50, fruits=100))

"""Когда мы объявляем параметр со звёздочкой (например, *param), все позиционные
аргументы начиная с этой позиции и до конца будут собраны в кортеж
под именем param.
Аналогично, когда мы объявляем параметры с двумя звёздочками (**param),
все ключевые аргументы начиная с этой позиции и до конца будут собраны
в словарь под именем param """



def total(initial, *numbers, extra_number):
    count = initial
    for number in numbers: # добавит все значения с полученого кортежа
        count += number
    count += extra_number # просто добавит переменную
    print(count)

total(10, 1, 2, 3, extra_number=50)