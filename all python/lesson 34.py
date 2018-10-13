""""""
"""
yield это ключевое слово, которое используется примерно как return —
отличие в том, что функция вернёт генератор.
"""

def createGenerator() : # Данная функция подобна итератору, т.е. может использоваться в цыкле
    for i in range(5):
        yield i*i

def createGenerator2():
    mylist2 = [i * i for i in range (10)]
    return mylist2

mygenerator = createGenerator() # создаём генератор, присваиваем переменной
print(mygenerator) # покажет что mygenerator является объектом!

for i in mygenerator: # Итерируем генератор
    print(i)

mygenerator2 = createGenerator2() # создаём генератор обычным способом, присваиваем переменной
print(mygenerator2) # покажет список mпygenerator2

for i in mygenerator2: # Итерируем генератор
    print(i)

print("------------------- пример не решил")

# пример - создать генератор простых чисел, который возвращает все простые числа цыкла.
# функцию is_prime неоюходимо написатьсли число можно разделить на какоето целое число, оно не простое
# Простые числа (натуральные) - Которые делятся только на самих себя и на 1 и все,
# ессли число можно разделить на какое-то целое число, оно не простое


# def get_primes():
#     num = 2
#     while True:
#         if is_prime(num):
#             yield num
#         num += 10