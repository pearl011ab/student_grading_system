"""
Student Grading System (Menu-driven)

Features:
1. Allows entering names and scores of multiple students.
2. Calculates total and average score for each student.
3. Assigns grades based on the average score.
4. Displays all students' performance sorted by average score in descending order.
5. Allows searching for a student by name to view their performance.
"""

database = {}


def add_student():
    """Add a new student's data to the database."""
    name = input("Enter student name: ")
    print("Enter scores")
    score_algebra = float(input("Algebra: "))
    score_commSkills = float(input("Comm Skills: "))
    score_TD = float(input("TD: "))

    total_score = score_algebra + score_commSkills + score_TD
    average_score = total_score / 3

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

    database[name] = {
        "Comm Skills": score_commSkills,
        "Algebra": score_algebra,
        "TD": score_TD,
        "Total": total_score,
        "Average": average_score,
        "Grade": grade
    }
    print(f"{name} has been added successfully!\n")


def display_all():
    """Display all students sorted by average score."""
    if not database:
        print("No student data available.\n")
        return

    sorted_students = sorted(
        database.items(),
        key=lambda student: student[1]["Average"],
        reverse=True
    )

    print("\nStudent Performance (Sorted by Average Score):")
    for student, scores in sorted_students:
        print(f"{student}: {scores}")
    print()


def search_student():
    """Search for a student's performance by name."""
    if not database:
        print("No student data available.\n")
        return

    search_name = input("Enter the name of the student to search for: ")
    found = False
    for name, scores in database.items():
        if name.lower() == search_name.lower():
            print(f"\nPerformance for {name}:")
            for subject, score in scores.items():
                print(f"{subject}: {score}")
            found = True
            break
    if not found:
        print("Student not found.\n")


# --------------------------
# Main program loop
# --------------------------
while True:
    print("====== Student Grading System ======")
    print("1. Add student data")
    print("2. Display all students")
    print("3. Search for a student")
    print("4. Quit")
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        add_student()
    elif choice == "2":
        display_all()
    elif choice == "3":
        search_student()
    elif choice == "4":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.\n")
