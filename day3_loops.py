# Counting using while loop
count = 1
while count <= 10:
    print (count)
    count += 1

# Guessing loop
secret = 7
guess = int(input("Guess a number 1-10: "))
while guess != secret:
    guess = int(input("Guess a number 1-10: "))

print("Correct!")

# Multiplication Table using for loop
user_number = int(input("Give me a number: "))
for i in range(1,11):
    results = user_number * i
    print (f"{user_number} x {i} = {results}")