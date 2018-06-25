class Money:

    def __init__(self):
        self.x = 10

    def standart(self):
        print("Я обычный метод")

    @staticmethod
    def static():  # Можно вызывать без создания класса
        print("Я статический метод")

# Статические методы нужны что бы возращать екземпляры класса уже в каком то состоянии
v = Money.static()


dollar = Money()

Money.static()  #Вызов статического метода через имя_класса.метод
dollar.standart() #Вызов обычного метода класа через обьект
Money().standart()  #Вызов обычного метода класа через Класс
