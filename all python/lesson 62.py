""""""
"""Принцыпы ООП - Инкапсуляция"""

"""Инкапсуляция - подобие создания капсулы, закрытого обьекта"""

class DividerClass():

    def __init__(self):
        self.__div = 2 # Делитель

    def __funcChek(self, val):
        return not val == 0 # функция проверят равно ли 0

    # def setdivider(self, val):
    #     try:
    #         self.__funcChek(val)
    #         self.__div = val
    #     except:
    #         print("error")

    def setdiv(self,val):
        if self.__funcChek(val): # если функция проверила что равно 0  - True
            self.__div = val    # то self.div = етому значению
        else:
            print("eroor")

    def divide(self, val):
            print(val / self.__div)


primer1 = DividerClass()
#primer1.div = 0 # проблема в том что пользователь имеет прямой доступ к класу, и при изменении дилителя на 0, будет ошибка, инкапсуляция закрывает доступ
primer1.setdiv(0)
primer1.divide(120)


