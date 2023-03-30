from Animal import Animal


class Duck(Animal):
    def sound(self):
        self.quack()

    def __init__(self, name):
        self.name = name

    def quack(self):
        print(self.name + " says Quack")
