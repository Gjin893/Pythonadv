from pydantic import BaseModel, conint, constr
from typing import Optional


#class User(BaseModel):
 #name: str
  #  age: int
   # email: str

#user = User(id=1, name="John Doe", age=30, email="johndoe@gmail.com")
#print(User)

class User(BaseModel):
    id: int
    name: str
    age: int =0
    email: str = "noemail@example.com"

user1 = User(id=2, name="John Doe")
print(user1)

user2 = User(id= 3, name="Alice", age=23)
print(user2)

user4 = User(id=4, name="Bob")
print(user4)

class another_user(BaseModel):
    id : conint (gt = 0)
    name:constr(min_length=2, max_length=50)

valid_user = another_user(id=1, name="Alice")
print(valid_user)