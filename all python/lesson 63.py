""""""
"""Наследование"""

class Phone():
    def __init__(self, color, model):
        self.color = color
        self.model = model
        self.number = "0665502911"

    def call(self):
        print("Звонить {}".format(self.number))

class Phone2(Phone):
    def __init__(self, color, model):
        super(Phone2, self).__init__(color, model)

    # Виртуальные функции, ето те функции которые могут быть переопределены в дочерних классах
    def call(self): # Переопределение функции или виртуальные функции
        print("Написать маил") # Дописал новые условия
        super(Phone2, self).call() # Вызываю функцию предок, и она выполняется как должна


nokia = Phone("red", "3310")
samsung = Phone2("green", "v35")
samsung.call()
print(samsung.model)
print(nokia.number)
print(samsung.number)

