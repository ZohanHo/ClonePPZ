""""""
"""Списковые включения или генераторы"""

cubes = [i*3 for i in range(5)]
print(cubes)

# Поддерживает if
evens=[i*2 for i in range(10) if i*2 % 2 == 0] # Остаток от деления равен нулю
print(evens)

