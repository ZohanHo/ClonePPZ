class Car:
    def __init__(self, date):
        self.date = date

bmw = Car(5).date #Создаю обьект, сразу передаю значение для инициализации, и обращаюсь к нему

print(bmw)

print(bmw.date)  # Тоже самое, только обращаюсь через класс
