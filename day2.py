number = int(input("Give me a random number: "))
if number > 0:
    print("Positive")
else:
    print("Zero or Negative")

age = int(input("What is your age? "))
if age >= 16:
    print("You can drive.")
else:
    print("You cannot drive.")

password = input("What is your password: ")
if password == "python123":
    print("Access granted")
else:
    print("Access denied")