from Dog import Dog
from Cat import Cat
from Duck import Duck

if __name__ == '__main__':
    animals = []
    animals.append(Dog("Pluto"))
    animals.append(Cat("Sylvester"))
    animals.append(Duck("Donald"))

    for animal in animals:
        animal.sound()
