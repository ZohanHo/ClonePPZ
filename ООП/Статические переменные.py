class Car:

#print(Car.__bases__)  #Класс наследован от object

    def __init__(self): #Обьяляю переменные сразу, их не нужно передавать при создании класа
        self.x = 10
        self.y = 20
        self.z = 30

bmv = Car()
print(bmv.x)




