#Дано вещественное число A и целое число N (>0). Используя один цикл, найти сумму 1 + A + A2 + A3 + ... + A^N
A = input("Введите первое число")
while type(A) != float:
    try:
        A = float(A)
    except ValueError:
        print("Неправильно написали")
        A = input("Введите первое число")

N = input("Введите второе число")
while type(N) != int:
    try:
        N = int(N)
    except ValueError:
        print("Неправильно написали")
        N = input("Введите второе число")

a = 0
b = 0
while a<=N:
    b = b + (A ** a)
    a += 1
print(b)