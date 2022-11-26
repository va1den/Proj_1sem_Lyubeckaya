# 1. Дан список A размера N. Вывести его элементы в следующем порядке: A1, AN, A2,AN-1, A3, AN-2, ….

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
index = 1
count = 0
K = N-1

while (index+count) < N :
  A1.append(A[index])
  index += 1
  if index+count >= N: break
  A1.append(A[K-count])
  count += 1
print(A)
print(A1)