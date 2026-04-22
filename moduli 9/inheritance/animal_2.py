class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print("Some generic animal sound.")

    def description(self):
        print(f"This is an animal sound name{self.name}")


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.bredd = breed

    def sound(self):
        print("WOOF! WOOF!")

    def description(self):
        super().description()
        print(f"Breed: {self.breed}")

animal = Animal("Generic Animal")
animal.sound()
animal.description()

dog = Dog("Rex","Gold Retriver")
dog.sound()
dog.description()



