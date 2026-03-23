contact_info={
    "Alice": "555-1234",
    "Bobby":"555-5678",
}

print(contact_info["Alice"])

contact_info["Alice"] = "555-999"
print(contact_info)

contact_info["Ana"]="123-234"
print(contact_info)

del contact_info["Alice"]
print(contact_info)

keys = contact_info.keys()
print(keys)

values = contact_info.values()
print(values)

print(contact_info.items())

contact_information ={
    "Bobby":{
        "phone-number": "554-234",
        "email": "Bobby@gmail.com",
        "birthday":"20/11/2000"
    },
    "Alice": {
        "phone-number": "555-234",
        "email": "Alice@gmail.com",
        "birthday": "20/11/2005"
    },
    "Eve": {
        "phone-number": "556-234",
        "email": "Eve@gmail.com",
        "birthday": "20/11/2010"
    },
}
print(contact_information)
print(contact_information["Alice"])

grades ={
    ("John", "Math"): 5,
    ("Alice", "Biology"): 2,
    ("Bobby", "Physics"): 5

}

john_math = grades[("John", "Math")]
print(john_math)
print("John's grade in math is:",john_math)

grades[("Bob","Math")]=5
print(grades)