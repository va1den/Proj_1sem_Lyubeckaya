# Вариант 15.
# Туристические агентства предлагают следующие туры. Вояж – Мексика,Канада,Израиль,
# Италия,США. РейнаТур – Англия,Япония,Канада,ЮАР. Радуга – США,Испания,Швеция,
# Австралия, Италия, Канада. .Определить:
# 1. в каких турагенствах можно одновременно приобрести туры в Италию и Канаду.
# 2. в турагенство РейнаТур добавить тур в Индию.
# 3. полный список всех туров
voyash = {"Мексика", "Канада", "Израиль", "Италия", "США"}
reina_tour = {"Англия", "Япония", "Канада", "ЮАР"}
rainbow = {"США", "Испания", "Швеция", "Австралия", "Канада"}
print("Одновременно приобрести туры в Италию и Канаду можно в:")
if "Италия" in voyash:
  i = 0
  i += 1
if "Канада" in voyash:
  i += 1
if i == 2:
  print('Вояже')
if "Италия"  in reina_tour:
  i = 0
  i += 1
if "Канада"  in reina_tour:
  i += 1
if i == 2:
  print("РейнаТуре")
if "Италия"  in rainbow:
  i = 0
  i += 1
if "Канада"  in rainbow:
  i += 1
if i == 2:
  print("Радуге")
reina_tour.add("Индия")
print("Полный список всех туров: ",  voyash | reina_tour | rainbow)
