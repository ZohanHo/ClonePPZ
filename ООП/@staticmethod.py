#Статический метод можно вызвать не создавая обьект класса. доступен как функция класса


class Money:

    @staticmethod
    def static():
        print("Статический метод")


Money.static()

