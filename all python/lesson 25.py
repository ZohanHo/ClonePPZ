""""""
"""Функции обработки строк"""

print(", ".join(["spam", "eggs", "ham"])) # разбивает список на слова
#spam, eggs, ham

print("Hello ME".replace("ME", "world")) # Замещает одну строку на другую
#prints Hello world

print("This is a sentence.".startswith("This"))  # Определят есть ли строка в начале
# prints "True"

print("This is a sentence.".endswith("sentence.")) # Определят есть ли строка в конце
# prints "True"

print("This is a sentence.".upper()) # Вся строка большими буквами
# prints "THIS IS A SENTENCE."

print("AN ALL CAPS SENTENCE".lower())  # Вся строка маленькими буквами
#prints "an all caps sentence"

print("spam, eggs, ham".split(", ")) # Каждое слово становится строкой в списке
#prints "['spam', 'eggs', 'ham']"