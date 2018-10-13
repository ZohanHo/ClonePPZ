""""""
"""Словари или ассоциативные масивы, dict

В языке Питон ключом может быть произвольный неизменяемый тип данных:
целые и действительные числа, строки, кортежи. Ключом в словаре не может быть множество,
но может быть элемент типа frozenset: специальный тип данных, являющийся аналогом типа set,
который нельзя изменять после создания.
Значением элемента словаря может быть любой тип данных, в том числе и изменяемый.
"""


dictionary = {"name":4, 4:"name", 5:6, 7:[1, 2, 3], 10:{"key":10, "man":20}}

dictionary["rus"] = "Moskow" # Добавляем в словарь новые данные
dictionary["ukr"] = "kiev"

# Как можно создавать словари, для небольших словарей
Capitals = {'Russia': 'Moscow', 'Ukraine': 'Kiev', 'USA': 'Washington'} # стандартный метод
Capitals1 = dict(Russia = 'Moscow', Ukraine = 'Kiev', USA = 'Washington') # чеоез dict, ключь равно значение

# Для создания необходимо передать список, каждый элемент которого является кортежем из двух элементов: ключа и значения
Capitals2 = dict([("Russia", "Moscow"), ("Ukraine", "Kiev"), ("USA", "Washington")])

# Для создания из двух одинаковых по длине списков - словаря
Capitals3 = dict(zip(["Russia", "Ukraine", "USA"], ["Moscow", "Kiev", "Washington"]))

# С помощью данной конструкции можно сделать номерацию для списка, сделав словарь, можно указать с какой по какую, и шаг
Capitals4 = dict(zip(range(2,7),["Russia", "Ukraine", "USA", "Pl", "Bg"]))
print(Capitals4)



print(Capitals)
print(Capitals1)
print(Capitals2)
print(Capitals3)

for i, j in dictionary.items(): # С помощью функции items, можно реребрать все ключи или значения, или то и то
    print(i, j)

key = 'name'
key2 = 4

"""Удаление обьектов"""
if key in dictionary:  # Проверка
    del dictionary[key]

try:
    del dictionary[key2]
except KeyError:
        print('There is no element with key "' + key2 + '" in dict')
print(dictionary)

# Удаление через функцию pop
"""использование метода pop: A.pop(key). 
Этот метод возвращает значение удаляемого элемента, если элемент с данным ключом отсутствует в словаре, 
то возбуждается исключение. Если методу pop передать второй параметр, то если элемент в словаре отсутствует, 
то метод pop возвратит значение этого параметра. 
Это позволяет проще всего организовать безопасное удаление элемента из словаря: A.pop(key, None)"""
dictionary.pop(10)
print("Удалил через pop", dictionary)


"""Работа с елементами словаря"""
print(dictionary[7]) # Получить обьект по ключу

""" способ определения значения по ключу — метод get: dictionary.get(key). 
Если элемента с ключом get нет в словаре, то возвращается значение None. 
В форме записи с двумя аргументами A.get(key, val) метод возвращает значение val, 
если элемент с ключом key отсутствует в словаре"""
print(dictionary.get(7))
print(dictionary.get(15)) # Возвращает None если ключ не найден

# Запись с двумя аргументами, второй в строке позвращается, если ключ не найден
print(dictionary.get(11, "does not exist"))


ab = {
        'Swaroop' : 'swaroop@swaroopch.com',
        'Larry' : 'larry@wall.org',
        'Matsumoto' : 'matz@ruby-lang.org',
        'Spammer' : 'spammer@hotmail.com'
}
print("Адрес Swaroop'а:", ab['Swaroop'])

# Удаление пары ключ-значение
del ab['Spammer'] # Удаляется по ключу
print('\nВ адресной книге {0} контактов\n'.format(len(ab)))

for name, address in ab.items(): #можно перебрать в цыкле как ключи так и значения, items - содержит пару (ключ и значение)
    print('Контакт {0} с адресом {1}'.format(name, address))

# Добавление пары ключ-значение
ab['Guido'] = 'guido@python.org'
if 'Guido' in ab: # проверка на наличие
    print("\nАдрес Guido:", ab['Guido'])

