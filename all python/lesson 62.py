"""Принцыпы ООП - Инкапсуляция, Наследование, Полиморфизм"""

"""Инкапсуляция - подобие создания капсулы, закрытого обьекта"""

class DividerClass():
    def __init__(self):
        self.__div = 5 # Делитель

    def __func_chek(self, val):
        return not val == 0 # Возвращаем если не равно 0, оч просто

    def setdivider(self, val):
        try:
            self.__func_chek(val)
            self.__div = val
        except:
            print("error")


    def divid(self, value):
        return value / self.__div



primer1 = DividerClass()
#primer1.div = 0 # проблема в том что пользователь имеет прямой доступ к класу, и при изменении дилителя на 0, будет ошика, инкапсуляция закрывает доступ
primer1.setdivider(29)

print(primer1.divid(100))


