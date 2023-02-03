# В последовательности на n целых чисел найти и вывести:
# 1. максимальный среди положительных
# 2. минимальный среди отрицательных
# 3. произведение элементов
import random
from functools import reduce
A = []
F = 5
while F > 0:
    F -= 1
    A.append(random.randint(-100, 100))
print(A)
prois = reduce(lambda x,y: x*y, A)
A.sort(key=None, reverse=True)
max = A[0]
print('Максимальный среди положительных', max)
A.sort(key=None, reverse=False)
min = A[0]
print('Минимальный среди отрицательных', min)
print('Произведение элементов:', prois)