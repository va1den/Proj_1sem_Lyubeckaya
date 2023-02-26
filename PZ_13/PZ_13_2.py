# В матрице найти минимальный элемент в предпоследней строке.
import random
from functools import reduce
count = 0
mat = []
while count < 3:
    strk = [random.randint(-10,10) for n in range(0,3)]
    count += 1
    mat.append(strk)
print('Матрица: ', mat)
for i in mat:
    if i == mat[-2]:
        print('Минимальный элемент в предпоследней строке.',
              reduce(lambda x, y: y if y<x else x, i ))