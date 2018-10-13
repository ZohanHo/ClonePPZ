# пример с генератором и булевой логикой
a = 6
root = [x for x in range(1, a) if a % x == 0] # результатом будет список root, 6 делится без остатка на 1, 2, 3, в суме будет 6
print(sum(root) == a and a > 0) # 6 = 6 и 6 > 0, потому True



# пример 2
def decor(a, b):   # не разобрался
    def sq(func):
        return func(a, b) * func(a, b)
    return sq
def subs(a, b):
    return (a-b)
def add(a, b):
    return (a+b)
f = decor(2, 3)
print(f(add) + f(subs))

#пример 3
a = [1, 2]
b = {1, 2}
c = (2, 1)

print(a == list(b))   #True
print(tuple(b) == c)  #False
print(b == set(c))    #True
print(tuple(a) == c)  # False

