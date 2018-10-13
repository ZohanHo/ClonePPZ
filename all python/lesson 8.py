""""""
"""Список"""

num = [1, 2, 3, 4]
num.append(5) # добавляет елемент в конец
print(num) # [1, 2, 3, 4, 5]

print(len(num)) # 5

#del num  - удалить список

num.insert(2, 6)  # На место 2 считая с нуля вставляем 6

print(num)

# range - возвращает последовательность чисел, list - преобразовывает в список

shoplist = ['яблоки', 'манго', 'морковь', 'бананы']
print('Я должен сделать ', len(shoplist), 'покупок.')
print('Покупки:', end=' ') # Говорим что хочем закончить строку  - пробелом

for item in shoplist:
    print(item, end=' ')
print('\nТакже нужно купить риса.')

shoplist.append('рис')
print('Теперь мой список покупок таков:', shoplist)
print('Отсортирую-ка я свой список')

shoplist.sort()
print('Отсортированный список покупок выглядит так:', shoplist)
print('Первое, что мне нужно купить, это', shoplist[0])

olditem = shoplist[0]
del shoplist[0]
print('Я купил', olditem)
print('Теперь мой список покупок:', shoplist)