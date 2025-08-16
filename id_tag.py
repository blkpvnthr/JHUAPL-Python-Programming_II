"""
Write a program demonstrating a string split and indexing.
- Prompt the learner for one line in the format.

FirstName LastName Grade
Example input: Ana Gomez 92

- Use str.split() to break that line into a list of three tokens.
Use indexing to extract:
- the first letter of the first name (tokens[0][0])
- the first letter of the last name (tokens[1][0])
- Combine those two letters with the grade to make a simple “ID tag”, e.g., AG-92.

Print the ID tag.
"""

# Prompt the user to enter a line with FirstName LastName Grade
user_input = input("Enter FirstName LastName Grade (e.g., Ana Gomez 92): ")

# Split the input into a list of tokens
tokens = user_input.strip().split()

# Extract the first letters of the first and last names
first_initial = tokens[0][0].upper()
last_initial = tokens[1][0].upper()

# Get the grade
grade = tokens[2]

# Combine to form the ID tag
id_tag = f"{first_initial}{last_initial}-{grade}"

# Print the result
print("ID Tag:", id_tag)
