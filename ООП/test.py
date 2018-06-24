class Bdo:
    def __init__(self, name):
        self.name = name
    jump = "up"

    def run(self):
        self.run = "Беги"  #Можно не передавать переменные, а указать их сразу
        print(self.run, self.name)

zohan = Bdo("Зохан")
zohan.run()

nitrich = Bdo("Нитрыч")
nitrich.run()

#Bdo().run() #Можно вызвать метод  не через обьект класса, а непосредственно через класс, но пока не указан конструктор, потом не раб.
#print(Bdo().jump)
