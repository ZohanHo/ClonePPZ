class People:
    eyes = 2  #Переменная класа (Наз. ПОЛЕ КЛАССА) Статические переменные(Применяются как константы)

    def set(self, work_hors = 8):
        self.wh = work_hors

    def __init__(self, name = "noname"):
        self.nm = name

    def run(self):  #К переменным класа и методу класа, могу обращатся как через обьект так и через self !!!?
        print("{} бежит, смотриу {} глазами, потом работает по {} часов".format(self.nm, jenya.eyes, self.wh))
        print("{} бежит, смотриу {} глазами".format(jenya.nm, self.eyes))

    def __str__(self):  #Возвращает строковое представление метода
        return str(self.eyes)

jenya = People("Женя") #Указал в конструкторе что по умолчанию name = noname, тут же указую что name = Женя
jenya.set()

#jenya.name = "Женя Хо Хо" Могу переопредилить имя которое получил при инициализации, при необходимости

Zohan_name = jenya.nm #Присвоил переменной  имя обьекта jenya
Zohan_eyes = jenya.eyes #Присвоил переменной  количество глаз через обьект jenya


print("Меня зовут {}, глаз у меня {}".format(Zohan_name, Zohan_eyes))
jenya.run()
#jenya.set(10) #Устанавливает значение методу set в заданое число
jenya.set() #Нужно вызвать метод для того что бы можно было получить доступ к его полям через обьект, в отличии от __init__
print(jenya.wh) #Печатаю значение кторое передал методу
print(jenya) #Печатает обьект благодаря тетоду __str__