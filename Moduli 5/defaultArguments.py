def greet_person(name, greeting="Hello"):
    message = f"{greeting},{name}"
    return message

default_greeting = greet_person("Alice",)
print(default_greeting)

default_greeting = greet_person("Alice","Hi")
print(default_greeting)