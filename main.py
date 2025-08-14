"""
Student Grading System

Features:
1. Allows entering names and scores of multiple students.
2. Calculates total and average score for each student.
3. Assigns grades based on the average score:
4. Displays all students' performance sorted by average score in descending order.
5. Allows searching for a student by name to view their performance.
"""

database = {}

# --------------------------
# Input loop for multiple entries
# --------------------------
while True:
    name = input("Enter student name: ")
    print("Enter scores")

    score_algebra = float(input("Algebra: "))
    score_commSkills = float(input("Comm Skills: "))
    score_TD = float(input("TD: "))

    # Calculate total and average
    total_score = score_algebra + score_commSkills + score_TD
    average_score = total_score / 3

    # Assign grade
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

    # Store in database
    database[name] = {
        "Comm Skills": score_commSkills,
        "Algebra": score_algebra,
        "TD": score_TD,
        "Total": total_score,
        "Average": average_score,
        "Grade": grade
    }

    # Ask if user wants to continue
    more = input(
        "Do you want to add another student? (yes/no): ").strip().lower()
    if more != "yes":
        break

# Sort students by average (descending)
sorted_students = sorted(
    database.items(),
    key=lambda student: student[1]["Average"],
    reverse=True
)

# Display sorted results
print("\nStudent Performance (Sorted by Average Score):")
for student, scores in sorted_students:
    print(f"{student}: {scores}")


search_name = input("\nName of student you want to search for: ")
found = False
for name, scores in database.items():
    if name.lower() == search_name.lower():
        print(f"\nPerformance for {name}:")
        for subject, score in scores.items():
            print(f"{subject}: {score}")
        found = True
        break

if not found:
    print("Student not found in the database.")
