# Objects can also contain methods. Methods in objects are functions that belong to the object.

# Let us create a method in the Person class:


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()

#we can have methods in class and we can call them using the object methods.
