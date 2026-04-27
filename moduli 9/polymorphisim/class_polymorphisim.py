from moduli1.main import name_of_the_list


class Dog:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print(f"{self.name} makes the sound: Woof!")


class Cat:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print(f"{self.name} makes the sound: Meow!")

class Bird:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print(f"{self.name}makes the sound: Chirp")



dog = Dog("Buddy")
cat = Cat("Whiskers")
bird= Bird("tweetie")

for animal in (dog, cat, bird):
    animal.sound()





