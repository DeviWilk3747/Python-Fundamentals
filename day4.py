# Greet function
def greet(name):
    print(f"Hello {name}! How are you doing today?")
greet("Devian")
greet("Alex")
greet("Amanda")

# Add function
def add(a, b):
    return a + b
    
a = int(input("Give me a value for a: "))
b = int(input("Give me a value for b: "))
result =  add(a, b)
print(result)

# Even or Odd Function
def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
num = int(input("Give me a random number: "))
answer = even_or_odd(num)
print(answer)