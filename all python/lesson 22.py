""""""
"""Кортежи - tuple"""

c = ('питон', 'слон', 'пингвин')
s = ("one", "Two", "three", "four", "five", c) # кортеж в круглых скобках

d= ["one", "Two", "three", "four", "five"] # словарь


w = "one", "Two", "three", "four", "five"  # Можно без скобок. тоже кортеж

name = s[1]


d[1] = "bingo" # в списке поменял
# s[1] = "bingo" С кортежем так сделать нельзя, их нельзя менять

print(w[0])
print(s[5][1]) # Слон - со  вложеного кортежа - с
print(name)
print(d)

myempty = () # пустой кортеж
myempty1 = (1,) # кортеж с одного елемента
print(myempty)
print(myempty1)