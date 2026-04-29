class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,name):
        self.__name= name

    @property
    def age(self):
       return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

student1 = Student("Alice", 21)

print(student1.name)
student1.name= "Andi"
print(student1.name)

print(student1.age)