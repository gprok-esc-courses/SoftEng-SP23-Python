from Animal import Animal


class Cat(Animal):
    def __init__(self, name):
        self.name = name

    def sound(self):
        print(self.name + " says Mieow")


