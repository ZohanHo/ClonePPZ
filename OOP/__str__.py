class Fructs:

    #def __init__(self, weight):  #Cоздать через конструктор
        #self.w = weight

    def set(self, weight):  #Создать через обычый метод, который нужно вызввать
        self.w = weight

    def __str__(self):
        return "Вес яблок {} кг.".format(self.w)  #Вернуть нужно обязательно str (строку)

aplle = Fructs()
aplle.set(5) #Вызыаю метод


print(aplle)  #Даю на печать обьект класса в строковом представлении