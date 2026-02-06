def greet():
    name = input("Hello! What is your name? ")
    print(f"Welcome {name}! I hope you are having a great day")

def add():
    a = int(input("Give me a value for a: "))
    b = int(input("Give me a value for b: "))
    sum = a + b
    print(sum)

def even_or_odd():
    number = int(input("Give me a random number: "))
    if number % 2 == 0:
        print ("Even")
    else:
        print("Odd")

def guessing_game():
    secret = 7
    guess = int(input("Guess a number 1-10: "))
    while guess != secret:
        guess = int(input("Guess a number 1-10: "))
    print("Correct!")

while True:
    print("1. Greet someone \n2. Add two numbers \n3.Even or Odd checker \n4. Number guessing game \n5. Exit")
    choice = int(input("Choice and option 1-5: "))

    if choice == 1:
        greet()
    elif choice == 2:
        add()
    elif choice == 3:
        even_or_odd()
    elif choice == 4:
        guessing_game()
    elif choice == 5:
        break