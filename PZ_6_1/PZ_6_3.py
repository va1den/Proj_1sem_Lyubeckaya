# 3. Дан список размера N. Осуществить циклический сдвиг элементов списка влево на одну позицию
# (при этом AN перейдет в AN-1, AN-1 — в AN-2, . . ., A1 — в AN).

import random

A = []
A1 = []
N = input("Введите размер списка: ")

while type(N) != int:
    try:
        N = int(N)
    except ValueError:
        print('Введите целое число!')
        N = input("Введите размер списка: ")
F = N

while F > 0:
    F -= 1
    A.append(random.randint(-100, 100))
N = N - 1
count = 1

while count <= N:
  A1.append(A[count])
  count += 1
A1.append(A[0])
print(A)
print(A1)