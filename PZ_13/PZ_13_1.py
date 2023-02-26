# В матрице найти суммы элементов каждого столбца и поместить их в новый массив.
# Выполнить замену элементов второй строки исходной матрицы на полученные
# суммы.
import random
from functools import reduce
count = 0
mat = []
while count < 3:
    strk = [random.randint(-10,10) for n in range(0,3)]
    count += 1
    mat.append(strk)
print('Матрица: ', mat)
spisok = []
for i in range(0,3):
    stol = [f[i] for f in mat]
    suma = reduce(lambda x,y: x+y, stol)
    spisok.append(suma)
mat[1]=spisok
print('Сумма элементов каждого столбца', spisok)
print('Матрица после замены: ', mat)