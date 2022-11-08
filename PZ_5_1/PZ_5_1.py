#1. Составить функцию, которая выведет на экран строку, содержащую задаваемое с клавиатуры число символов

def countFish(b):
    a = 0
    while b > 0:
        b //= 10
        a += 1
    return a

void = input("Введите число: ")

while type(void) != int:
    try:
        void = int(void)
    except ValueError:
            print("Неправильно ввели!")
            void = input("Введите целое число: ")

print('Число символов: ', countFish(void))