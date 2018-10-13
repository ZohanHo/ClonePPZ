""""""
"""Полиморфизм, когда обьект в разных ситуациях ведет себя по разному"""

class VectorClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    #def multiplay(self, v2): # В Функцию прийдет обьект класса как аргумент, но мы будем использовать магичесуий метод
    def __mul__(self, other): # Принимаем какойто озер и используем инициализированые переменныее
        return VectorClass(self.x * other.x, self.y * other.y) # Возвращаем...

v1 = VectorClass(2, 3)
v2 = VectorClass(6 ,7)
# v3 = v1.multiplay(v2)  можно использовать так, но оптимальней использовать магические методы
v3 = v1 * v2

print("v3.x = ", v3.x)
print("v3.y = ", v3.y)



print("---------")

class Multiplay():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __mul__(self, other):
        # print("self x {}".format(self.x))
        # print("self y {}".format(self.y))
        return Multiplay(self.x * other.x, self.y * other.y)

    def __add__(self, other):
        return Multiplay(self.x + other.x, self.y + other.y)

    def __repr__(self): # representation - Показует как будет выглядеть обьект на печати, но не печатает, а возвращает значение
        return "self.x = {} и self.y = {}".format(self.x, self.y) # без него выглядело бы так    <__main__.Multiplay object at 0x00A5DCB0>

apple = Multiplay(2, 4)
orange = Multiplay(3, 6)
banana = Multiplay (5, 10)


"""Захоит 2 аргумента, в зависимости над какими обьктами происходит операция, 
в етой операции равно self.x = 3, self.y = 6, orange, other.x = 2, other.y = 4, apple"""
fructs = orange * apple
print(fructs.x)
print(fructs.y)

# Тут banana будет и self и other
fructs2 = banana * banana # захоит 2 аргумента, в зависимости над какими обьктами происходит операция, в етой операции равно 5, 10
print(fructs2.x)
print(fructs2.y)

fructs3 = orange + apple
print(fructs3.x)
print(fructs3.y)

print(apple)