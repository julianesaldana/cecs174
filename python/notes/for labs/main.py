class Mammal:
    def __init__(self, species):
        self.species = species

    def show_species(self):
        print("I am a {}".format(self.species))


class Dog(Mammal):
    def makesounds(self):
        print("Woof! Woof!")


class Cat(Mammal):
    def makesounds(self):
        print("Meow")


animal1 = Dog("dog")
animal2 = Cat("cat")
animals = [animal1, animal2]

for obj in animals:
    obj.show_species()
    obj.makesounds()

