# Дан прямоугольник, длины сторон которого равны натуральным числам А и В.
# Составить функцию, которая будет находить на сколько квадратов можно разрезать
# данный прямоугольник, если от него каждый раз отрезать квадрат наибольшей
# площади.
A = input("Введите целое число: ")
while type(A) != int:
    try:
        A = int(A)
    except ValueError:
        print("Введено неправильно ")
        A = input("Введите целое число: ")
B = input("Введите целое число: ")
while type(B) != int:
    try:
        B = int(B)
    except ValueError:
        print("Введено неправильно")
        B = input("Введите целое число: ")
def golden_ratio(A1, B1):
    h = 0
    while (A1 != 0) and (B1 != 0):
        if A1 > B1:
            A1 = A1 - B1
            h = h + 1
        elif A1 < B1:
            B1 = B1 - A1
            h = h + 1
        elif A1 == B1:
            A1 = A1 - B1
            B1 = A1
            h = h + 1
    return h
kvadrati = golden_ratio(A, B)
print('Количество квадратов:', kvadrati )




