# 1. Dictionary creation with different types of immutable keys
my_dict = {
    "name": "Steven",           # string key
    180: "height",              # integer key
    (1, 2): [10, 20],           # tuple key (immutable)
}

# 2. Accessing a value using its key
print("Name:", my_dict["name"])       # Output: Name: Steven
print("Tuple key value:", my_dict[(1, 2)])  # Output: Tuple key value: [10, 20]

# 3. Adding a new key-value pair
my_dict["age"] = 30
print("After adding 'age':", my_dict)

# 4. Removing a key-value pair
del my_dict[180]
print("After removing key 180:", my_dict)

# 5. Using dictionary methods

# .keys() returns all keys
print("Keys:", list(my_dict.keys()))

# .values() returns all values
print("Values:", list(my_dict.values()))

# .items() returns key-value pairs
print("Items:", list(my_dict.items()))

# 6. Searching for a key
key_to_check = "name"
if key_to_check in my_dict:
    print(f"'{key_to_check}' is in the dictionary.")

# 7. Showing values can be of any type (string, int, list, dict, etc.)
my_dict["details"] = {
    "height": 182,
    "hobbies": ["mma", "coding"]
}
print("Nested dictionary value:", my_dict["details"])
