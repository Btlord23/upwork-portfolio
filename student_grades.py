
print("STUDENT GRADE MANAGEMENT SYSTEM")
print("=" * 35)

name = input("Enter student name: ")

subjects = ["English", "Mathematics", "Science"]
scores = []

for subject in subjects:
    while True:
        try:
            score = float(input(f"Enter {subject} score (0-100): "))

            if score < 0 or score > 100:
                print("Score must be between 0 and 100.")
                continue

            scores.append(score)
            break

        except ValueError:
            print("Please enter a valid number.")

average = sum(scores) / len(scores)

if average >= 70:
    grade = "A"
elif average >= 60:
    grade = "B"
elif average >= 50:
    grade = "C"
elif average >= 45:
    grade = "D"
else:
    grade = "F"

print("\n" + "=" * 35)
print("STUDENT REPORT")
print("=" * 35)

print(f"Student Name: {name}")

for i in range(len(subjects)):
    print(f"{subjects[i]}: {scores[i]}")

print("-" * 35)
print(f"Average Score: {average:.2f}")
print(f"Final Grade: {grade}")

print("\nThank you for using the system!")
