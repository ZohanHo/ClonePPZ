from mymodule import *

#from mymodule import School   # можно отдельно вызвать не через *,
#from mymodule import t
#from mymodule.School import tell_me


sayhi() # вызвал обычную функцию
saybb()
print(a) # распечатал обычную переменную


School("Zro").tell()  # обратился через класс, один аргумент конструктора необходимо указать при обращении
t.tell() # обратился через обьект к методу
School("Zro").sum(13, 114) # Функция которая считает суму аргументов
s.sum(12, 45)
t.sum(132, 435)


print(s.name, s.age) # обратился к переменной конструктора через обьект
print(t.name, t.age) # обратился к переменной конструктора через обьект

t.new()  # через обьект вывожу поля (переменные конструктора)

print(t) # __str__ - могу прочитать имя обьекта в строковом представлении
print(s)

Sadic("ff", 23).tell()

