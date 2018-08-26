"""Полиморфизм, когда обьект в разеых ситуациях ведет себя по разному"""

class VectorClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    #def multiplay(self, v2): # В Функцию прийдет обьект класса как аргумент, но мы бужем использовать магичесуий метод
    def __mul__(self, other): # Принимаем какойто озер и используем инициализированые переменныее
        return VectorClass(self.x * other.x, self.y * other.y) # Возвращаем...

v1 = VectorClass(2, 3)
v2 = VectorClass(6 ,7)
# v3 = v1.multiplay(v2)  можно использовать так, но оптимальней использовать магические методы
v3 = v1 * v2

print(v3.x)
print(v3.y)

