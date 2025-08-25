"""
Create a Program: Instructions

Write a program that captures a string containing a person’s first, middle, and last names, and then display their first, middle, and last initials.

For example, if the user enters John William Smith, the program should display J. W. S.
"""

# Ask the user to enter their full name
full_name = input("Enter your first, middle, and last name: ")

# Split the name into parts
name_parts = full_name.strip().split()

# Extract the first letter of each part and capitalize it
initials = [part[0].upper() + '.' for part in name_parts]

# Join and display the initials
print(' '.join(initials))