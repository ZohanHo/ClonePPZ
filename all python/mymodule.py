print("hello")

a = 10

def sayhi():
    print('Привет! Это говорит мой модуль.')
    __version__ = '0.1'


def saybb():
    print('Привет! Импортирована только функция.')
    a = 10



class School():
    '''Представляет любого человека в школе.'''

    def __init__(self, name, age = 25):
        self.name = name
        self.age = age

    def __str__(self):
        return "Сроковое имя в етом обьекте {}".format( self.name)

    def tell(self):
        '''Вывести информацию.'''
        print("hi")

    def sum(self, x, y):
        result = x + y
        print(result)

    def new(self):
        print("1 - {} 2 - {}".format(self.name, self.age))



class Sadic(School):

    def __init__(self, name, age):
        super(Sadic, self).__init__(name, age)  # вызываем конструктор у базового класса, и он не будет повторятся при множественном наследовании

    def tell(self):
        super(Sadic, self).tell()
        print("Занято") # добавил новый функционал в функцию

    # def suma(self, x, y):
    #     result = x + y
    #     print(result)
    #     super(Sadic, self).suma()

t = School("Zohan")
s = School("Grom")

z = Sadic("Grob", 24)

