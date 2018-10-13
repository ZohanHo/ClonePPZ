 #Есть два обьекта, апельсины и яблоки, необходимо сложить апельсины и яблоки по их весу

class Fructs:

    def __init__(self, weight):
        self.w = weight

    def __str__(self):
        return "Вес яблок {} кг.".format(self.w)  #Вернуть нужно обязательно str (строку), поесле чего доступен принт обьекта

    def __add__(self, other):
        return Fructs(aplle.w + orange.w) #К яблокам можно обратится через self.apple, other нужно указыать

    def __mul__(self, other):   #Умножение аналогично сложению
        return Fructs(aplle.w * orange.w)

    def __mod__(self, other):
        return Fructs(aplle.w % orange.w)

    def __len__(self):
        return self.w

aplle = Fructs(5)
orange = Fructs(3)

print(aplle)  #Даю на печать обьект класса в строковом представлении
print(orange)  #Даю на печать обьект класса в строковом представлении

add = aplle + orange
print("Общий результат сложения {}".format(add))

mul = aplle * orange
print("Общий результат умноженый {}".format(mul))

mod = aplle % orange
print("Остаток от деления {}".format(mod))

print(len(aplle))