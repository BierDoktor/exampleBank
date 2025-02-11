import random  # Import the random module
import time  # Import the time module

# Generate a random integer between 1 and 10
random_number = random.randint(1, 10)
print(f"Random Number: {random_number}")

# Pause the execution for 2 seconds
print("Waiting for 2 seconds...")
time.sleep(2)

# Get the current time
current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print(f"Current Time: {current_time}")

# Handling potential errors
try:
    # Attempt to generate a random float between two values
    random_float = random.uniform(1, '10')  # Incorrect usage (string instead of int/float)
    print(f"Random Float: {random_float}")
except TypeError as e:
    print(f"Error: {e}. Ensure both arguments are numbers.")

try:
    # Incorrect sleep time
    time.sleep(-1)  # Negative sleep time will cause an error
except ValueError as e:
    print(f"Error: {e}. Sleep time must be non-negative.")
