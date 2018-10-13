""""""
"""Цыкл for"""

# range – англ. «диапазон», «интервал»
for i in range(1, 5): # Начинается с 1 и заканчивается 4  - 1, 2, 3, 4, можем указать шаг
    print(i)
else:
    print('Цикл for закончен')



for i in 'hello world':
    if i == 'o':
        continue
    print(i * 2, end="")

