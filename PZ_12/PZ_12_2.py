# Составить генератор (yield), который выводит из строки только буквы.
from string import ascii_letters
cyrillic_lower_letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя' \
                         'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
def bukvi(a):
    for i in a:
        if i in ascii_letters or i in cyrillic_lower_letters:
         yield i
a = input('Введите строку:')
otvet = bukvi(a)
for i in otvet:
    print(i)