# Пилим счетчик для подсчета количества созданых обьектов

class Counter:

    count = 0

    def __init__(self):
        self.__class__.count +=1 # Обращаюсь непосредственно к Классу и его стат. переменной
                                 # при создании обьекта count увеличивается на 1

a = Counter()

b = Counter()

c = Counter()

print(a.count)  # Равно 3

print(Counter.count)  # Доступна через имя класа