""""""
"""Открытие файлов"""

myfile = open("file.txt", "r") # Открыли фаил в режиме чтения с помощюц фунции open, указуем два параметра, имя файда и режим (чтение, запись)
cont = myfile.read((100)) # Читаем фаил, присваиваем переменной, аргументом передал сколько байт прочитать
cont1 = myfile.readlines()  # Читаем фаил построчно
print(cont) # Печатаем переменную
print(cont) # Печатаем переменную

for i in cont: # Можно цыклом
    print(i)


myfile.close() # Закрываем фаил



# w - режим записи
# r - режим чтения
# a - режим добавления
# a - режим открития в двоичном коде, используется для не текстовых файлов


