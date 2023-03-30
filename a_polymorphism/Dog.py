from Animal import Animal


class Dog(Animal):
    def __init__(self, name):
        self.name = name

    def sound(self):
        print(self.name + " says Woof")
