class Car:
    def __init__(self, date):
        self.date = date

bmw = Car(5).date #При создании передаю значение и обращаюсь к нему через точку
print(bmw)
