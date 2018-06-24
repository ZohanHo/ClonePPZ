class Phone:

    def __init__(self, date = 20): #Аргумент должен быть, или переопределение ариф. операцю. не сработает, можно сразу указать значение
        self.number = date

    def __str__(self):
        return "Число {}".format(self.number)

    def __add__(self, other):  #Переопределяем метод сложения, после чего можем добалять к обьекту число, или другой обьект
        return Phone(nokia.number + lenovo.number) #Доступ через имя класа

nokia = Phone()

lenovo = Phone()

print(nokia + lenovo)