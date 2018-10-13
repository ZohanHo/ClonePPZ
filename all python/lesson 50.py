class Person:
    def __init__(self, name = "Зоро"):
        self.ima = name   # Имя переменный self.ima значение name, куда передали Зохан при инициализации

    def sayHi(self):
        print('Привет! Меня зовут', self.ima)
p = Person('Зохан')

p.sayHi()
