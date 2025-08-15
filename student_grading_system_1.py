"""
Student Grading System

Features:
1. Allows entering names and scores of multiple students.
2. Calculates total and average score for each student.
3. Assigns grades based on the average score:
4. Displays all students' performance sorted by average score in descending order.
5. Allows searching for a student by name to view their performance.
"""

# Dictionary to store all student records
# Structure: { "Name": { "Subject1": score, "Subject2": score, ... } }
database = {}

# --------------------------
# Input loop for multiple entries
# --------------------------
while True:
    # Get the student's name
    name = input("Enter student name: ")

    # Get the student's scores for 3 subjects
    print("Enter scores")
    algebra = input("Algebra: ")
    score_algebra = float(algebra)  # convert user input to float

    # same conversion to float happens here
    score_commSkills = float(input("Comm Skills: "))
    score_TD = float(input("TD: "))

    # Calculate total
    total_score = score_algebra + score_commSkills + score_TD

    # Calculate average score
    average_score = total_score / 3

    # Assign a grade based on the average score
    if average_score >= 80:
        grade = "A"
    elif average_score >= 70:
        grade = "B"
    elif average_score >= 60:
        grade = "C"
    elif average_score >= 50:
        grade = "D"
    else:
        grade = "F"

    # Store the student's data in the database
    database[name] = {
        "Comm Skills": score_commSkills,
        "Algebra": score_algebra,
        "TD": score_TD,
        "Total": total_score,
        "Average": average_score,
        "Grade": grade
    }

    # Ask if the user wants to add another student
    more = input(
        "Do you want to add another student? (yes/no): ").strip().lower()
    if more != "yes":
        break  # Exit the loop if user types anything other than "yes"

# Sort students by average (descending)
#
# sorted() will rearrange the items in the database based on "Average"
# key=lambda student: student[1]["Average"] → fetches the "Average" from the value (scores dictionary)
# reverse=True → sorts in descending order
sorted_students = sorted(
    database.items(),
    key=lambda student: student[1]["Average"],
    reverse=True
)

# Display sorted results
print("\nStudent Performance (Sorted by Average Score):")
for student, scores in sorted_students:
    print(f"{student}: {scores}")

# Search for a specific student by name
search_name = input("\nName of student you want to search for: ")
found = False

# Loop through each student in the database
for name, scores in database.items():
    # Compare names in lowercase to make search case-insensitive
    if name.lower() == search_name.lower():
        print(f"\nPerformance for {name}:")
        for subject, score in scores.items():
            print(f"{subject}: {score}")
        found = True
        break  # Stop searching once the student is found

# If student is not found
if not found:
    print("Student not found in the database.")
