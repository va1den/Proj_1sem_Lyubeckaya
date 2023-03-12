from figures import triangle_area, square_area
a = int(input('Ввести первую сторону треугольника: '))
b = int(input('Ввести вторую сторону треугольника: '))
c = int(input('Ввести третью сторону треугольника: '))
print('Площадь треугольника',int(triangle_area(a, b, c)))

print('Площадь квадрата: ', square_area()) # взяты дефолтные значения

