# Lists
favorite_foods = ["Pizza", "Tacos", "Spaghetti", "Cheeseburger"]
print(favorite_foods[0])

# Add an item to the list
add_food = input("What food do you want to add? ")
favorite_foods.append(add_food)
print(favorite_foods)

# Loop through the list
for i in range(len(favorite_foods)):
    print(i + 1, favorite_foods[i])