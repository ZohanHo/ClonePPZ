class Bdo:

    jump = "up"

    def run(self):
        self.run = "Беги"  #Можно не передавать переменные, а указать их сразу
        print(self.run)

zohan = Bdo()
zohan.run()


nitrich = Bdo()
nitrich.run()

Bdo().run() #Можно вызвать метод  не через обьект класса, а непосредственно через класс

print(Bdo().jump)
