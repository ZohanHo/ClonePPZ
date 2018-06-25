class Fructs:

    #def __init__(self, weight):  #Cоздать через конструктор
    #self.w = weight

    def set(self, weight):  # Метод не вызван, его переменные не доступны классу
        self.w = weight

    def test(self, g):
        self.g = g
        print(self.g, self.w )

aplle = Fructs()
aplle.test(10)  #



