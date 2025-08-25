"""
Write a program that calculates a letter grade for students. 
Then have the program calculate the average of three input grades
and provide a letter grade for the average.
"""

def get_valid_grade(prompt):
    while True:
        grade_input = input(prompt)
        if grade_input.isdigit():
            return int(grade_input)
        else:
            print("Please enter numbers only.")

def calculate_letter_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

def main():
    print("Enter three student grades to calculate the average and letter grade.")

    grade1 = get_valid_grade("Enter first grade: ")
    grade2 = get_valid_grade("Enter second grade: ")
    grade3 = get_valid_grade("Enter third grade: ")

    average = (grade1 + grade2 + grade3) / 3
    letter = calculate_letter_grade(average)

    print(f"\nAverage Grade: {average:.2f}")
    print(f"Letter Grade: {letter}")

# Run the program
main()
