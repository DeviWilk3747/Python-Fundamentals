# Open the file in append mode so new data is added
file = open("students.txt", "a")

# Writes student information to the file
file.write("Devian, CIS, 2026\n")

# Closes the file and saves changes
file.close()