""""""

"""Чистые функции возвращают значение которое зависит только от их aргументов"""

def clear(x, y):
    return x * 2 + y

print(clear(3, 4))



# Не чистые функции, потому что изменилв состояни Mylist

Mylist = []
def app(arg):
    return Mylist.append(arg)

app("1")

print(Mylist)