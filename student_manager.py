students = []

def add_students():
    name = input("What is your name? ")
    major = input("What is you major? ")
    graduation_year = int(input("What is your anticipated graduation year? "))

    new_student = {"Name": name,
                    "Major": major,
                    "Graduation Year": graduation_year}
    students.append(new_student)
    print("Student added successfully!\n")

def view_students():
    if not students:
        print("No students available")
        return
    for student in students:
            print("Name: ", student["Name"])
            print("Major: ", student["Major"])
            print("Graduation Year: ", student["Graduation Year"])
            print()

def search_students():
    search_name = input("What is the name of the student you are looking for? ")
    found = False
    for student in students:
        if student["Name"] == search_name:
            print("Name: ", student["Name"])
            print("Major: ", student["Major"])
            print("Graduation Year: ", student["Graduation Year"])
            print()
            found = True
    if not found:
        print(f"The student {search_name} could not be found \n")

def delete_students():
    delete_student = input("What is the name of the student you want to delete? ")
    found = False
    for student in students:
        if student["Name"] == delete_student:
            students.remove(student)
            print("Student removed successfully")
            found = True
            break
    if not found:
        print(f"The student {delete_student} could not be found \n")

# Prints a list of options for the user to choose from
print()
while True:
    print("1. Add Students")
    print("2. View Students")
    print("3. Search Students")
    print("4. Delete Students")
    print("5. Exit \n")

    choice = input("Choose an option: ")
    print()
    if choice == "1":
        add_students()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_students()
    elif choice == "4":
        delete_students()         
    elif choice == "5":
        break
    else:
        print("Invalid Option")
