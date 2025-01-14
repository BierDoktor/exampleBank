# Demonstrating various looping constructs and control structures in Python

# Using a while loop to count down
count = 5
print('Using while loop:')
while count > 0:
    print(f'Count is: {count}')
    count -= 1  # Decrement the count
print('Done with while loop!\n')

# Using for loop with range to repeat an action n times
print('Using for loop with range:')
for i in range(1, 6):  # Range from 1 to 5 because we always start from 0
    print(f'This is iteration {i}')
print('Done with for loop using range!\n')

# Using for loop to iterate over characters in a string
text = 'Python'
print('Iterating over characters in a string:')
for char in text:
    print(f'Character: {char}')
print('Done iterating over string!\n')

# Demonstrating nesting: loop within a loop
print('Nested loops:')
for i in range(1, 4):  # Outer loop
    for j in range(1, 4):  # Inner loop
        print(f'Outer: {i}, Inner: {j}')
print('Done with nested loops!\n')

# Conditional statement inside a loop
print('Conditional statement in a loop:')
for num in range(1, 11):
    if num % 2 == 0: # Modulus operator is used to find the remainder of a division
        print(f'{num} is even')
    else:
        print(f'{num} is odd')
print('Done with conditional in a loop!\n')