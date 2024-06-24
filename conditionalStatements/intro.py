# if statement = a block of code that will execute if it's condition is true

age = int(input('How old are you? '))

if (age >= 18):
    print('You are an adult')
# explain why the order of if statements matter and how to fix it by moving it to the top
elif (age >= 65):
    print('You are a senior')
elif (age >= 13):
    print('You are a teenager')
else:
    print('You are a minor')

# Example for the '!=' operator
if (age != 18):
    print('You are not 18 years old')
else:
    print('You are 18 years old')

# Example for the 'and' operator
if (age >= 18 and age < 65):
    print('You are an adult')
elif (age >= 65):
    print('You are a senior')
elif (age >= 13):
    print('You are a teenager')
else:
    print('You are a minor')

# Example for the 'or' operator
if (age < 18 or age >= 65):
    print('You are either a minor or a senior')
elif (age >= 13):
    print('You are a teenager')
else:
    print('You are an adult')

# Example for the 'not' operator
if not (age >= 18):
    print('You are a minor')

# Example for boolean values in if statements
is_adult = age >= 18
if is_adult:
    print('You are an adult')