# 1. Сгенерировать словарь вида {0: 0, 1: 1, 2: 8, 3: 27, 4: 64, 5: 125, 6: 216},
# удалить из него первый и последний элементы. Отобразить исходный и
# получившийся словарь. Использовать for, range.(Преподаватель разрешил
# сделать без for, range)

slovar = {0: 0, 1: 1, 2: 8, 3: 27, 4: 64, 5: 125, 6: 216}
slovar_2 = slovar.copy()
print("Исходный словарь: ", slovar)
slovar_2.pop(0)
slovar_2.pop(6)
print('Получившийся словарь: ', slovar_2)