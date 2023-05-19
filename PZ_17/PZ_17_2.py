# Создайте класс "Животное", который содержит информацию о виде и возрасте
# животного. Создайте классы "Собака" и "Кошка", которые наследуются от класса
# "Животное" и содержат информацию о породе.

class Animal:
    def __init__(self, vid, age):
        self.vid = vid
        self.age = age

    def get_animal(self):
        return self.vid, self.age


class Dog(Animal):
    def __init__(self, vid, age, poroda_dog):
        Animal.__init__(self, vid, age)
        self.poroda_dog = poroda_dog

    def get_dog(self):
        return self.vid, self.age, self.poroda_dog


class Cat(Animal):
    def __init__(self, vid, age, poroda_cat):
        Animal.__init__(self, vid, age)
        self.poroda_cat = poroda_cat

    def get_cat(self):
        return self.vid, self.age, self.poroda_cat

AnimalOne = Animal('Мышь', 1)
DogOne = Dog('Cобака', 3, "Бульдог Вик")
CatOne = Cat('Кошка', 2, "Вислоухая Гато")
print(AnimalOne.get_animal())
print(DogOne.get_dog())
print(CatOne.get_cat())