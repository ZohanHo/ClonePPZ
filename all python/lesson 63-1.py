""""""
"""Наследование"""

class SchoolMember:  # Родительский класс
    '''Представляет любого человека в школе.'''

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Создан SchoolMember: {0})'.format(self.name)) # принт сработает только если создать обьект класса, и передать аргументы

    def tell(self):
        print('Имя:"{0}" Возраст:"{1}"'.format(self.name, self.age), end=" ")

class Teacher(SchoolMember): # Подкласс
    '''Представляет преподавателя.'''

    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age) # такой конструкцием можно инициализировать поля родительского класса
        self.salary = salary # и добавляем нужное поле, которое требуется именно в етом класе
        print('(Создан Teacher: {0})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self) # такой конструкцией можем использовать метод родительского класса и добавить что то из подкласа
        print('Зарплата: "{0:d}"'.format(self.salary))

class Student(SchoolMember):
    '''Представляет студента.'''
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('(Создан Student: {0})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Оценки: "{0:d}"'.format(self.marks))

t = Teacher('Mrs. Shrividya', 40, 30000)
s = Student('Swaroop', 25, 75)

print() # печатает пустую строку

t.tell()
s.tell()

# можно цыклом
members = [t, s]
for member in members:
    member.tell() # работает как для преподавателя, так и для студента

