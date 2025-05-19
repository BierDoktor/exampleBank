# A list is an ordered data structure that can store objects of different types
my_list = [42, "hello", 3.14, True]

# Accessing list items using indexing (starts from 0)
first_item = my_list[0]  # 42
second_item = my_list[1]  # "hello"
print("First item:", first_item)
print("Second item:", second_item)

# Using list methods
my_list.append("new item")  # Add to the end
my_list.insert(1, "inserted item")  # Insert at index 1
my_list.remove(3.14)  # Remove the first occurrence of 3.14
my_list.sort(key=str)  # Sort items (converted to strings for compatibility)
occurrences = my_list.count("hello")  # Count how many times "hello" appears
print("Updated list:", my_list)
print("Occurrences of 'hello':", occurrences)

# Demonstrating different data types
mixed_list = [123, "Python", 3.5, False]
print("Mixed list:", mixed_list)

# Iterating over the list
print("Items in mixed_list:")
for item in mixed_list:
    print("-", item)

# Strings are iterable like lists
word = "Python"
print("Characters in word:")
for char in word:
    print(char)

# Accessing characters in a string by index
print("Third character in 'Python':", word[2])

# Comparing string and list methods
sample_list = ["a", "b", "a", "c"]
sample_string = "banana"

# Both have count method
print("Count of 'a' in list:", sample_list.count("a"))
print("Count of 'a' in string:", sample_string.count("a"))

# Strings are immutable; lists are mutable
# sample_string[0] = "B"  # This would raise an error
sample_list[0] = "z"  # This is allowed
print("Modified list:", sample_list)
