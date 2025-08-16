# Parent Class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "This animal makes a sound."

# Child Class - Dog
class Dog(Animal):
    def speak(self):
        return f"{self.name} says: Woof! Woof!"

# Child Class - Cat
class Cat(Animal):
    def speak(self):
        return f"{self.name} says: Meow!"

# Create objects of Dog and Cat
dog1 = Dog("Buddy")
cat1 = Cat("Whiskers")

# Demonstrating polymorphism
print(dog1.speak())  # Output: Buddy says: Woof! Woof!
print(cat1.speak())  # Output: Whiskers says: Meow!
