# Средствами языка Python сформировать текстовый файл (.txt), содержащий
# последовательность из целых положительных и отрицательных чисел. Сформировать
# новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
# обработку элементов:
# Исходные данные:
# Количество элементов:
# Индекс последнего минимального элемента:
# Умножаем все элементы на первый элемент:
A = ['-33 36 -18 22 -81 89']
f = open('data.txt', 'w')
f.writelines(A)
f.close()
f1 = open('data_1.txt', 'w')
f1.write('Исходные данные: ')
f1.write('\n')
f1.writelines(A)
f1.close()
f = open('data.txt')
k = f.read()
k = k.split()
for i in range(len(k)):
    k[i] = int(k[i])
f.close()
f = open('data.txt')
min, t = 0, 0
for i in range(len(k)):
    min = min if min < k[i] else k[i]
    t = i
f1 = open('data_1.txt', 'a')
f1.write('\n')
print('Количество элементов: ', len(k), 'Индекс минимального элемента: ', i-1, file=f1)
f1.close()
B = []
c = 0
f = open('data.txt')
for i in range(len(k)):
    c = k[i]*k[0]
    B.append(c)
f1 = open('data_1.txt', 'a')
print('Умножаем все элементы на первый элемент:', B, file=f1)
