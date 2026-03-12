students = [
    {"name": "Devian", "major": "CIS", "graduation_year": 2026}
]
# Print current students
for student in students:
    print("Name:", student["name"])
    print("Major:", student["major"])
    print("Graduation Year:", student["graduation_year"])
    print()

name = input("What is your name? ")
major = input("What is your major? ")
grad_year = int(input("What is your graduation year? "))

new_student = {
    "name": name,
    "major": major,
    "graduation_year": grad_year
}

students.append(new_student)

print("\nUpdated Student List:")

for student in students:
    print("Name:", student["name"])
    print("Major:", student["major"])
    print("Graduation Year:", student["graduation_year"])
    print()