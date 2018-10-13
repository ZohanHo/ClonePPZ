""""""
"""Полиморфизм, когда обьект в разных ситуациях ведет себя по разному"""


# Данный пример отличается от преведущего тем что мы хотим чтобы вектор можно было умножить не только на вектор,
# но и на число, получили полиморфизм нашему вектору, в разной ситуации он будет работать по разному
class VectorClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    #def multiplay(self, v2): # В Функцию прийдет обьект класса как аргумент, но мы бужем использовать магичесуий метод
    def __mul__(self, other): # Принимаем какойто озер и используем инициализированые переменныее
        if isinstance(other, int): # Проверяем является ли other обьектом класа int
            return VectorClass(self.x * other, self.y * other)
        else:
            return VectorClass(self.x * other.x, self.y * other.y) # Возвращаем...

    def __call__(self, *args, **kwargs): # для того что бы вызвать как функцию
        return (self.x, self.y)

    def __repr__(self): # representation - Показует как будет выглядеть обьект на печати, но не печатает, а возвращает значение
        return (self.x, self.y)

    def __str__(self):
        return "Моя строка с векторами {}".format( self.__repr__()) #Строковое представление обьекта, возвращает только строку!

    def __getitem__(self, item):  # Возможность доступа по индексу
        if isinstance(item, (int, float)):
            if 0 <= item <= 1:  # Проверка диапазона индекса
                if item == 0:  # при индексе 0 выдаст self.x
                    return self.x
                if item == 1:   # аналогично
                    return self.y
            else:
                raise("Не в диапазоне от 0 до 2")
        else:
            raise("не int, float")

    def __len__(self):
        return self.x

v1 = VectorClass(2, 3)
v2 = VectorClass(6 ,7)
# v3 = v1.multiplay(v2)  можно использовать так, но оптимальней использовать магические методы
v3 = v1 * v2
v4 = v1 * 10

print(v3.x)
print(v3.y)

print(v4.x)
print(v4.y)

print(v4())  # После того как мы прописал мультиметод __call__ мы можем вызывать его как функцию

print(v4) # После етого обращения получим строковое представление

print("Обьект по заданному индеку равен", v2[1])

print(len(v2)) # Можем найти длину после умножения что описано в магическом методе len