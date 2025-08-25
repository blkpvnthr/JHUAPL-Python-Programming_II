"""
Create a Python script that uses classes and objects using the init method.

For this program:

The Dog class has an __init__ method that initializes.

The name and breed attributes when a new Dog object is created.

The bark method is also defined within the class. Two Dog objects, my_dog and another_dog, are created with different names and breeds.

The program then accesses the attributes of these objects and calls the bark method."""

### Define Dog class ###

class Dog:
    # The __init__ method initializes name and breed attributes
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    # Method for the dog to bark
    def bark(self):
        print(f"{self.name} says Woof! Woof!")



### Create two Dog objects ###

my_dog = Dog("Buddy", "Golden Retriever")
another_dog = Dog("Luna", "German Shepherd")



### Access and display the attributes of each dog ###

print(f"My dog's name is {my_dog.name} and it is a {my_dog.breed}.")
my_dog.bark()

print(f"Another dog's name is {another_dog.name} and it is a {another_dog.breed}.")
another_dog.bark()
