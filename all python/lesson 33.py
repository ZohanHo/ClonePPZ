"""Итераторы и генераторы"""

# Когда вы создаёте список, вы можете считывать его элементы один за другим — это называется итерацией:
mylist = [1, 2, 3]
for i in mylist :
    print(i)

print("--------------------------")

# Mylist является итерируемым объектом. Когда вы создаёте список, используя генераторное выражение,
# вы создаёте также итератор:
mylist = [x*x for x in range(3)]
for i in mylist :
    print(i)

print("--------------------------")

"""Генераторы"""

# Генераторы это тоже итерируемые объекты, но прочитать их можно лишь один раз.
# Это связано с тем, что они не хранят значения в памяти, а генерируют их на лету:

mygenerator = (x*x for x in range(3))
for i in mygenerator:
    print(i)


# Всё то же самое, разве что используются круглые скобки вместо квадратных.
# НО: нельзя применить конструкцию for i in mygenerator второй раз, так как генератор может быть
# использован только единожды: он вычисляет 0, потом забывает про него и вычисляет 1,
# завершаяя вычислением 4 — одно за другим.