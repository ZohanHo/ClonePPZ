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
        #print("skip 5")
        continue # Останавливает текущую итерацию и переходит к следующей
    if b == 3:
        print("stop 4")
        break # Щстановка цыкла

