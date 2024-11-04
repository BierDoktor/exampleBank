import random

# Generate a random integer between 1 and 10
random_integer = random.randint(1, 10)
print(random_integer)

# Generate a random floating-point number between 0 and 1
random_float = random.random()
print(random_float)

# Choose a random element from a list
my_list = ['apple', 'banana', 'cherry']
random_choice = random.choice(my_list)
print(random_choice)


# Import the greet function from my_module.py
import my_module

# Call the greet function
my_module.greet('Stefan')