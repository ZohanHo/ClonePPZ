""""""
"""функции епрст"""

def fun(x, y, z): # x И y - Параметры функции, у - указали по умолчанию, но он заменится если мы передадим его в аргументе
    return x + y + z
    #print(x) После return ничего не выполняется
a = 10
b = 20

print(fun(a, b, z = 3)) # x И y - Аргументы, которые передаем как переменные + ключевой аргумент
print(fun(7, 3, z = 3)) # x И y - Прямая передача аргументов + ключевой аргумент


"""Локальные переменные"""

x = 50
def func(x):
    print('x равен', x)
    x = 2 # переопределили переменную внутри функции, но за функцией она осталась прежней
    print('Замена локального x на', x)
func(x)
print('x по прежнему', x)

"""Зарезервированное слово «global»"""

x = 50
def func():
    global x
    """
    Зарезервированное слово global используется для того, чтобы объявить, что x
    – это глобальная переменная, а значит, когда мы присваиваем значение имени
    x внутри функции, это изменение отразится на значении переменной x в
    основном блоке программы
    """
    print('x равно', x)
    x = 2
    print('Заменяем глобальное значение x на', x)
func()
print('Значение x составляет', x)


"""
Зарезервированное слово «nonlocal»

Когда мы находимся внутри func_inner, переменная x, определённая в первой
строке func_outer находится ни в локальной области видимости (определение
переменной не входит в блок func_inner), ни в глобальной области видимости
(она также и не в основном блоке программы). Мы объявляем, что хотим
использовать именно эту переменную x, следующим образом: nonlocal
x.
Попробуйте заменить «nonlocal x» на «global x», а затем удалить это зарезервированное
слово, и пронаблюдайте за разницей между этими двумя
случаями.

"""

def func_outer():
    x = 2
    print('x равно', x)
    def func_inner():
        nonlocal x
        x = 5
    func_inner()
    print('Локальное x сменилось на', x)
func_outer()
