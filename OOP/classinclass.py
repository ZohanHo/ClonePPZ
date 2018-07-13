class One:

    s = 30

    def __init__(self, name = 40, root = 10):
        self.n = name
        self.r = root

    def yo(self):
        self.nova = "Нова"
        print(self.nova)

    class Two:

        a = 1000
        def set(self, date = 104):
            self.date = date
            print(self.date)

one = One()
#print(One("FF").__class__)
One().Two().set(105)  # Достучатся до метода класса который нвходится в теле другого класса, можно так:
one.yo()


print(One().s)
#print(One().yo())




# #print(one.Two.a)
# print(one.__class__) # Можем узнать какой у екзкмпляра класс
# print(one.__dict__) # В словаре хранятся все атрибуты екземпляра
# print(One.__dict__) # В словаре хранятся все атрибуты класса


