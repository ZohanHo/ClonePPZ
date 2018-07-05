class Bdo:

    jump = "up"

    def __init__(self, name):
        self.name = name

    def run(self):
        self.run = "Беги"  #Можно не передавать переменные, а указать их сразу
        self.age = 10
        print(self.run, self.name)

    def noname(self):
        print(self.run)

zohan = Bdo("Зохан")
zohan.run()
print(zohan.age)

nitrich = Bdo("Нитрыч")
#nitrich.run()

Bdo("IOI").run() #Можно вызвать метод не через обьект класса, а непосредственно через класс, но необхoдимо указать аргументы для конструктора
print(Bdo("name1").jump)
