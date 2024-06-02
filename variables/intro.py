# variable = container for a value. Behaves as the value that it contains.

# Like in algebra, variables can be assigned to values.
# 10 = 5 * x
# x = 2


# string = a series of characters
firstname = 'John'
lastname = "Doe"

print(firstname)
print(lastname)

# when you print your variable, make sure you don't use quotes
print('firstname')

# we can combine strings using the + operator
print('Hello ' + firstname)
fullname = firstname + ' ' + lastname

# we can check the type of a variable using the type() function
print(type(firstname))

# we can not use strings for math
# that's what the int and float types are for

# int = integer = whole number
age = 25
age = age + 1 # age += 1
print(age)
print(type(age))

# let's combine strings and numbers
print('Your age us:' + age) # this will cause an error
print('Your age us:' + str(age)) # this will work

# float = floating point number = decimal number
height = 1.82
print(height)
print(type(height))
print('Your height is: ' + str(height) + 'm')

# boolean = True or False
is_student = True
print(is_student)
print(type(is_student))
print('Are you a student? ' + str(is_student))

# user input = input() function
input('What is your name? ')
name = input('What is your name? ')
print('Hello ' + name)

# input() always returns a string
age = input('What is your age? ')
age = age + 1 # this will cause an error
age = int(age) + 1

print('You will be ' + str(age) + ' in a year')

age = int(input('What is your age? '))
print('You will be ' + str(age + 1) + ' in a year')