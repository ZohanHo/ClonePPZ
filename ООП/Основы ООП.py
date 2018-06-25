class Phone:

    def __init__(self, date = 97593):
        self.number = date

    def set(self): #Что бы использовать переменную через self в данной вункции, перед использование переменной функцию нужно вызвать
        self.samsung = "Вызов"

    def call(self):  #self говорит что при вызое метода от определенного обьекта, он будет работать от имени етого метода
        print("call", self.number, self.samsung)

    def __str__(self):
        return "Число {}".format(self.number)

    def __add__(self, other):  #Переопределяем метод сложения, после чего можем добалять к обьекту число, или другой обьект
        return Phone(nokia.number + lenovo.number) #Доступ через имя класа, вместо второго аргумента можно указать othet, и добавить число

nokia = Phone()
print(nokia.number)

nokia.set() #Вызываю функцию что бы стала доступна переменная

nokia.call() # При вызове функции неявным аргументом в питоне, а в некоторых языках явным, передается self,
             # что бы функция знала с каким обьектом ей работать

lenovo = Phone()
print(lenovo.number)

nokia.b43 = 15000 # Создали переменную внутри обьекта, но так не принято, принято создавать с помощью конструктора

# Как достучатся с функции к конструктору, достаточно использовать предложениый namespace(пространство имен),
# self в методе ссылается на обьект которым он вызван, и при создании обьекта был инициализирован конструктор соответственно
# его переменные автоматически доступны

print(nokia + lenovo)
