class People:
    eyes = 2  #Переменная класа (Наз. ПОЛЕ КЛАССА) Статические переменные(Применяются как константы)

    def set(self, work_hors = 8):
        self.wh = work_hors

    def __init__(self, name = "noname"):
        self.nm = name


    def run(self):  #К переменным класа и методу класа, могу обращатся как через обьект так и через self !!!
        print("{} бежит, смотрит {} глазами, потом работает по {} часов".format(self.nm, People().eyes, self.wh))
        print("{} бежит, смотрит {} глазами".format(jenya.nm, self.eyes))
                    #Через self можно обращатся только врурти класса. кажись

jenya = People("Женя") #Указал в конструкторе что по умолчанию name = noname, тут же указую что name = Женя
jenya.set() #Необходимо вызать метод для того что-бы стали доступны его переменные

print("Меня зовут {}".format(People().nm)) #Обращаюсь к переменной конструктора через класс, получаю по умолчанию переменную
print("Меня зовут {}".format(jenya.nm))    #Oбращаюсь к переменной через обьект, получаю значение переданое при етого обьекта
jenya.run()
