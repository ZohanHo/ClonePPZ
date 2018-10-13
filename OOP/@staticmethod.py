""""""
"""Статический метод можно вызвать не создавая обьект класса. доступен как функция класса"""


class Money:

    @staticmethod
    def static():
        print("Статический метод")

Money.static()




class Grom:

    @classmethod
    def rain(self):
        print("Метод класа")

a = Grom()

a.rain()
Grom().rain()

