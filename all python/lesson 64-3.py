""""""
"""Наследование"""

class Phone(object):

    def __init__(self):
        self.model = ""
        self.color = "red"

    def call(self):
        print("Звонить")


class Phone2(Phone):
    def __init__(self):
        super(Phone2, self).__init__()  # вызываем конструктор у базового класса, и он не будет повторятся при множественном наследовании

    def call(self):
        if False:  # если функция не срабатывает (False) вызывается ета фунция у базового класса
            pass
        else:
            super(Phone2, self).call()
            print("Занято") # добавил новый функционал в функцию

a = Phone()
b = Phone2()
print(a.color)
print(b.color)

b.call()