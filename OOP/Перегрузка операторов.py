class Money:

    def __init__(self, money):
        self.money = money  #Говорим что обьект.мани = мани которые передаем при создании обьекта

    def __add__(self, other):  #Переопределяем метод сложения, после чего можем добалять к обьекту число
        return Money(self.money + other) #Доступ через имя класа

    def push(self):
        print(self.money)

    def __str__(self):  #Превращает обьект в строку
        return "Количество {} $".format(self.money)

zohan = Money(100)

zohan += 200
print(zohan)
zohan.push()