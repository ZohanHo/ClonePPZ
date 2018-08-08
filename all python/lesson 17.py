"""Запись в файл"""

myfile = open("file.txt", "w") # Открыли фаил в режиме чтения
myfile.write("This text invite to file") # Записуем текст в фвил
myfile.close()

myfile = open("file.txt", "r")
cont = myfile.read()  # Читаем фаил построчн
myfile.close()
print(cont) # Печатаем переменную
