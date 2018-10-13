class Divider:

    def __init__(self):
        self.__div = 2

    def set_div(self, set_div):
        if self.__SetNum(set_div):
                self.__div = set_div
        else:
            print("Error")

    def __SetNum(self, set_div):   # Метод возвращает True, такие методы нужны для внутренего использоваия в программе
            return not set_div == 0


    def result (self, set_mun):
            c =  set_mun / self.__div
            print(c)


obj = Divider()

obj.set_div(2)

obj.set_div(10)
