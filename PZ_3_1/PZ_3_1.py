#1. Даны три целых числа: A, B, C. Проверить истинность высказывания: «Ровно одно из чисел A, B, C положительное».
a = input("Введите целое число A")
b = input("Введите целое число B")
c = input("Введите целое число C")
n = 0
while type(a) !=int:
    try:
        a = int(a)
    except ValueError:
        print("Неправильно ввели")
        a = input("ВВедите целое число")
while type(b) !=int:
    try:
        b = int(b)
    except ValueError:
        print("Неправильно ввели")
        b = input("ВВедите целое число")
while type(c) !=int:
    try:
        c = int(c)
    except ValueError:
        print("Неправильно ввели")
        c = input("ВВедите целое число")
if a > 0:
    n += 1
if b > 0:
    n += 1
if c > 0:
    n += 1
if n == 1:
    print("Одно из чисел A B C положительное")
else:
    print("Нет положительных или больше одного положительного")