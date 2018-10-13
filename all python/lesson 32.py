""""""
"""Функция filter, фидьтрует по условию"""

z = [1, 2, 3, 4, 5, 10]

result = list(filter(lambda x: x % 5 == 0, z)) # Получает так как и map 2 аргумента, фильтрует по условию
print(result)



# проверили ключь делится ли на 2
result2 = {4 : 6, 2 : 3}

def func(x):
    if x != str:
        return x % 2 == 0

print(tuple(filter(func, result2)))
