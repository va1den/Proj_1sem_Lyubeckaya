# Из предложенного текстового файла (text18-15.txt) вывести на экран его содержимое,
# количество букв в нижнем регистре. Сформировать новый файл, в который поместить текст
# в стихотворной форме предварительно заменив символы нижнего регистра на верхний.

f1 = open('18-15.txt', encoding='UTF-8')
print('Содержимое файла:')
print(f1.read())
f1.close()
count = 0
for i in open('18-15.txt', encoding='UTF-8'):
    for j in i:
        if j.islower()==True:
            count = count + 1
print('Количество букв в нижнем регистре:', count)
f1.close()
f2 = open('18-15-1.txt', 'w', encoding='UTF-8')
for i in open('18-15.txt', encoding='UTF-8'):
    f2.writelines(i.upper())
f2.close()