database = {
    "Alice": {"Comm Skills": 85, "Algebra": 90, "TD": 88, "Total": 263, "Average": 87.67, "Grade": "A"},
    "Bob": {"Comm Skills": 70, "Algebra": 75, "TD": 72, "Total": 217, "Average": 72.33, "Grade": "B"},
    "Charlie": {"Comm Skills": 60, "Algebra": 65, "TD": 62, "Total": 187, "Average": 62.33, "Grade": "C"}
}

print(database.items())

# See what the lambda produces for each item
for student in database.items():
    print(student[0], "-> lambda output:",
          (lambda s: s[1]["Average"])(student))
