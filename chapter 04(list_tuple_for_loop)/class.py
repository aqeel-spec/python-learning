# ((((( __ WORKING WITH LISTS __ )))))

# my_list: list[str] = ["a", "b", "c", "e", "f"]

# # Print the first three items from the list without using slicing
# print("Without slicing:")
# for item in my_list[:3]:
#     print(item)

# # Use slicing to print the first three items from the list
# print("\nWith slicing:")
# for item in my_list[0:3]:
#     print(item)

# # List of fruits
# fruits : list[str] = ["apple", "banana", "cherry", "date"]

# # List of vegetables
# vegetables : list[str]  = ["carrot", "eggplant", "fennel", "garlic"]

# # Print fruits using for loop
# print("List of fruits:")
# for fruit in fruits:
#     print(fruit)

# # Print vegetables using for loop
# print("\nList of vegetables:")
# for vegetable in vegetables:
#     print(vegetable)


# # Five simple foods 
# simple_foods : tuple[str] = ("pizza", "pasta", "salad", "steak", "soup")

# # for loop to print each food
# for food in simple_foods:
#     print(food)
# # Change the first food 
# simple_foods[0] = "burger" # Python will reject it

# Five simple foods 
simple_foods : tuple[str] = ("pizza", "pasta", "salad", "steak", "soup")

# for loop to print each food
for food in simple_foods:
    print(food)
# Change the first food 
simple_foods[0] = "burger" # Python will reject the change

# change menu , replacing of two items
# change items : burger , chips 

# rewrite the tuple
simple_foods : tuple[str] = ("burger", "pasta", "salad", "chips", "soup")

# Changed list
# print the tuple
print("\nChanged list is:")
for food in simple_foods:
    print(food.title())

