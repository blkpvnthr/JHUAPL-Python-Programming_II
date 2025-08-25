"""
Create a Python script that uses classes and attributes with the following directions.

Dog is a class. (instance attributes and instance methods)

1. init method initializes the instance attributes for new dog object created.

2. The description and speak methods are examples of instance methods on object’s attributes.

    - species, name, and breed are attributes.

    - species is a class attribute, while name and breed are instance attributes.

    - bark is a method.

    - dog1 and dog2 are instances (objects) of the Dog class.
"""

# -------------------------
# Define the Dog class
# -------------------------
class Dog:
    # Class attribute (shared by all dogs)
    species = "Canis familiaris"

    # Instance attributes (unique for each dog)
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    # Instance method: describes the dog
    def description(self):
        return f"{self.name} is a {self.breed}."

    # Instance method: makes the dog bark
    def speak(self, sound):
        return f"{self.name} says {sound}!"

# -------------------------
# Create two dog instances (objects)
# -------------------------
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Luna", "German Shepherd")

# -------------------------
# Print information about each dog
# -------------------------
print(f"{dog1.name} belongs to species {dog1.species}.")
print(dog1.description())
print(dog1.speak("Woof Woof"))

print("\n" + "-"*40 + "\n")

print(f"{dog2.name} belongs to species {dog2.species}.")
print(dog2.description())
print(dog2.speak("Bark Bark"))


### Classes and init ###

