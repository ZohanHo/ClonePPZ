class Money:

    def stanart(self):
        print("Я обычный метод")

    def static():
        print("Я статический метод")
    static = staticmethod(static)      #Не обязательно указывать что ето статикметод

dollar = Money()

Money.static()  #Вызов статического метода через имякласса.метод
dollar.stanart() #Вызов обычного метода через обьект
