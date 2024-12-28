# Initialize an array to store grades of 5 students
grades = []

# Input grades for 5 students
print("Enter the grades for 5 students:")
for i in range(5):
    while True:
        try:
            grade = float(input(f"Enter grade for Student {i + 1}: "))
            if 0 <= grade <= 100:  # Ensure valid grade range
                grades.append(grade)
                break
            else:
                print("Grade must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Display all grades
print("\nGrades of all students:")
for i in range(5):
    print(f"Student {i + 1}: {grades[i]}")

# Compute the average grade
total = 0
for grade in grades:
    total += grade
average = total / len(grades)
print(f"\nThe average grade is: {average:.2f}")

# Find the highest grade
highest = grades[0]
for grade in grades:
    if grade > highest:
        highest = grade
print(f"The highest grade is: {highest}")

# Find the lowest grade
lowest = grades[0]
for grade in grades:
    if grade < lowest:
        lowest = grade
print(f"The lowest grade is: {lowest}")
