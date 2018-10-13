""""""
"""Запись в файл"""

myfile = open("file.txt", "w") # Открыли фаил в режиме чтения
myfile.write("This text invite to file") # Записуем текст в фвил
myfile.close()

myfile = open("file.txt", "r")
cont = myfile.read()  # Читаем фаил построчно
myfile.close()
print(cont) # Печатаем переменную



try:   # В конструкции try мы уверены что фаил всегда закроется
    f = open("file.txt")
    print(f.read())
finally:
    f.close()