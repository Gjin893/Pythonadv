class MyClass():
    def __init__(self):
        self.public_variable = "this is public"
        self.__private_variable ="this is private"
        self._protected_variable ="this is protected variable"


my_class = MyClass()
print(my_class.public_variable)
#print(my_class.__private_variable)
print(my_class._protected_variable)