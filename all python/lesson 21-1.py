""""""
"""Словари"""

ab = {
        'Swaroop' : 'swaroop@swaroopch.com',
        'Larry' : 'larry@wall.org',
        'Matsumoto' : 'matz@ruby-lang.org',
        'Spammer' : 'spammer@hotmail.com'
}
print("Адрес Swaroop':", ab['Swaroop'])


# Удаление пары ключ-значение
del ab['Spammer'] # Удаляется по ключу
print('\nВ адресной книге {0} контактов\n'.format(len(ab)))

for name, address in ab.items(): #можно перебрать в цыкле как ключи так и значения, items - содержит пару (ключ и значение)
    print('Контакт {0} с адресом {1}'.format(name, address))

# Добавление пары ключ-значение
ab['Guido'] = 'guido@python.org'
if 'Guido' in ab: # проверка на наличие
    print("\nАдрес Guido:", ab['Guido'])