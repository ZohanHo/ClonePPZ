"""Цыкл while"""
i = 5
while i > 0:
    print(i)
    i -= 1
    if i == 2:
        break

print("Finish")

"""Почемуто не работает, хотя все верно"""

b = 10
while b > 0:
    print(b)
    b -= 1
    if b == 5:
        print("gg")
            #print("skip 5")
        continue # Останавливает текущую итерацию и переходит к следующей



for i in 'hello world':
    if i == 'o':
        continue
    print(i * 2, end='')