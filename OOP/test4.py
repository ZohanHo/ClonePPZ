class Phone:

    def __init__(self, date = None): # Аргумент должен быть указан, хоть даже None, или переопределение ариф. операции не сработает
        self.number = date

    def __str__(self):
        return "Число {}".format(self.number)

    def __add__(self, other):  #Переопределяем метод сложения, после чего можем добалять к обьекту число, или другой обьект
        return Phone(nokia.number + lenovo.number) #Доступ через имя класа

nokia = Phone(10)  # При необходимости могу указать нужное значение при определении класса

lenovo = Phone(10)

print(nokia + lenovo)