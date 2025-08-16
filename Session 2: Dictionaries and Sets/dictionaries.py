### Dictionaries ###

"""
1. Create a Python dictionary by enclosing the elements inside a set
 of curly braces {} and add the following keys and values:"""

dict = {"name": "Tim", "age": 25, "city": "Los Angeles"}


"""
2. Write a program that does the following:

Add elements to the dictionary using square bracket notations.

Retrieve values from a dictionary using the get() method.

Use the following to help create this program:

my_dict

apple, banana, cherry

key-value pairs = name, age, city
"""

# Step 1: Create an empty dictionary
my_dict = {}

# Step 2: Add elements using square bracket notation
my_dict["name"] = "Alice"
my_dict["age"] = 30
my_dict["city"] = "New York"

# Adding some fruits
my_dict["apple"] = "red"
my_dict["banana"] = "yellow"
my_dict["cherry"] = "dark red"

# Step 3: Retrieve values using the get() method
print("Name:", my_dict.get("name"))
print("Age:", my_dict.get("age"))
print("City:", my_dict.get("city"))
print("Apple color:", my_dict.get("apple"))
print("Banana color:", my_dict.get("banana"))
print("Cherry color:", my_dict.get("cherry"))

# Retrieving a non-existing key (returns None instead of an error)
print("Orange color:", my_dict.get("orange"))



### Mixed data types ###

"""
3. Create a Python script that creates mixed data types in a dictionary. Use the following input:

mixed_dict = name, age, is student, grades, address, city, is student

key-value pairs = name, age, is student, grades, address, city, favorite number

favorite_number = 3.14

print(mixed_dict) = name, age, is student, grades, address, city, favorite number

Introduction to Classes: str, int, bool, list, dict, float"""

mixed_dict = {
    "name": "Alice",                      # str
    "age": 25,                            # int
    "is_student": True,                   # bool
    "grades": [90, 85, 92],               # list
    "address": {"street": "123 Main St", "zipcode": "10001"},  # dict
    "city": "New York",                   # str
    "favorite_number": 3.14               # float
}

# Print the dictionary
print("Mixed Dictionary:", mixed_dict)

