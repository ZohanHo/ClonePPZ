"""Кортежи - tuple"""

s = ("one", "Two", "three", "four", "five")

d= ["one", "Two", "three", "four", "five"]


w = "one", "Two", "three", "four", "five"  # Можно без скобок

name = s[1]


d[1] = "bingo"
# s[1] = "bingo" С кортежем так сделать нельзя, их нельзя менять


print(w[0])
print(name)
print(d)



