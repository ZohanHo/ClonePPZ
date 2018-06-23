class Money:

    def standart(self):
        print("Я обычный метод")

    @staticmethod
    def static():
        print("Я статический метод")


dollar = Money()

Money.static()  #Вызов статического метода через имякласса.метод
dollar.standart() #Вызов обычного метода класа через обьект
Money().standart()  #Вызов обычного метода класа через Класс
