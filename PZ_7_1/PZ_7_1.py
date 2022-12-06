# 1. Дана строка. Подсчитать общее количество содержащихся в ней строчных
# латинских и русских букв.

string_ru = "абвгдеёжзийклмнопрстуфхцчшщъьыэюя"
string_en = "abcdefghijklmnopqrstuvwxyz"

n = 0
c = 0

a = input("Введите буквы")

for i in a:
  if i in string_ru:
    n += 1
print("Русских строчных", n)

for i in a:
  if i in string_en:
    c += 1
print("Английских строчных", c)

