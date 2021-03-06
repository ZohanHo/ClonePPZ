""""""
"""
Множества set - это неупорядоченные наборы простых объектов, они немогут быть проиндексированы, также они немогут иметь дубликаты
Множества восновном используют для проверки на вхождение и устранения дубликатов
Они необходимы тогда, когда присутствие объекта в наборе важнее порядка или того, сколько раз данный объект там встречается.
"""

# Создаются при помощи функции set или {} скобок, значения через запятую
s = set("one tr, er")
ss = {1, 3, 5, 6}

# Что бы добавить елемент используется метод add
ss.add(-7)

# что бы удалить елемент используетсся remove
ss.remove(5)

# что бы удалить произвольный елемент используется pop
ss.pop()

print(s, ss)


bri = {'Бразилия', 'Россия', 'Индия'}
print('Индия' in bri) # True
print('США' in bri) # False


"""модуль copy
copy.copy(x) - возвращает поверхностную копию x.
copy.deepcopy(x) - возвращает полную копию x.

Исключение copy.error - возникает, если объект невозможно скопировать.
Разница между поверхностным и глубоким копированием существенна только для составных объектов, содержащих изменяемые объекты 
(например, список списков, или словарь, в качестве значений которого - списки или словари):
Поверхностная копия создает новый составной объект, и затем (по мере возможности) вставляет в него ссылки на объекты, находящиеся в оригинале.
Глубокая копия создает новый составной объект, и затем рекурсивно вставляет в него копии объектов, находящихся в оригинале.
"""

bric = bri.copy() # Возвращает копию, а не делает ссылку как при ( с = "переменная"; d = c )
bric.add('Китай')
print("bri = {}".format(bri))
print("bric = {}".format(bric))

"""
Копирование при помощи полной вырезки - можно еще так:
mylist = shoplist[:] # создаём копию путём полной вырезки
del mylist[0] # удаляем первый элемент
В mylist он удалится, а в shoplist останется
"""

print(bric.issuperset(bri)) # Проверяет является ли данное множество - подмножеством другого множества ()
# можно сделать с помощью операций   < > =
print("bri является подмножеством bric - ", bric > bri)
print("bri является подмножеством bric - ", bric < bri)
print("bri является подмножеством bric - ", bric == bri)


bri.remove('Россия') # Удаляем

print(bri & bric) # OR bri.intersection(bric)  -   возвращает только множества содержащиеся в обоих множествах
