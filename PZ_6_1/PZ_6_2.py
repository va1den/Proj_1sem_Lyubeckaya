# 2. Дан целочисленный список размера N, все элементы которого упорядочены (по возрастанию или по убыванию).
# Найти количество различных элементов в данном списке.

import random

N = random.randrange(2, 21)
a = []
b = N
while b > 0:
    b -= 1
    a.append(random.randint(1, 20))
print("N:", N)
print("List not sorted \n", a)
List = []
for i in a:
    if i not in List:
        List.append(i)
List.sort()
print("List sorted \n", List)
print("amount of numbers", len(List))
