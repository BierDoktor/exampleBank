# function = a block of code which only runs when it is called
# You can pass data, known as parameters, into a function
# A function can return data as a result
# Functions are used to perform certain actions, and they are important for reusing code
# Functions are defined using the def keyword
# Functions are called using the function name followed by parenthesis

# https://github.com/BierDoktor/exampleBank

# Creating a Function
def my_function():
    print('Hello from a function')

# Calling a Function
my_function()

# Arguments
def my_function_with_args(username, greeting):
    print('Hello ' + username + ', from my function. I wish you ' + greeting)
    # print('Hello %s, from my function. I wish you %s'%(username, greeting))
    # print(f'Hello {username}, from my function. I wish you {greeting}')

my_function_with_args('John Doe', 'a great year.')

# Return Values
def sum_two_numbers(a, b):
    return a + b

print(sum_two_numbers(5, 10))

# Functions can call other functions
def call_function():
    my_function()

call_function()

# Functions can be assigned to a variable
my_function_variable = my_function
my_function_variable()

# Functions can be passed as arguments to other functions
def call_function_with_args(func):
    func()

call_function_with_args(my_function)

# Functions can be defined inside other functions
def parent_function():
    def child_function():
        print('Hello from the child function')
    child_function()

parent_function()

# Functions can return other functions
def return_function():
    def child_function():
        print("Hello from the child function")
    return child_function

new_function = return_function()

new_function()