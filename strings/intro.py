name = 'john'

print(len(name))  # 4
print(name.find('o'))  # 1
print(name.capitalize())  # John
print(name.upper())  # JOHN

name = 'JOHN'
print(name.lower())  # john
print(name.isdigit())  # False
print(name.isalpha())  # True

name = 'John Doe'
print(name.isalpha())  # False
print(name.count('o'))  # 2
print(name.replace('o', 'a'))  # Jahn Dae
print(name.split(' '))  # ['John', 'Doe']
print(name.startswith('J'))  # True
print(name.endswith('e'))  # True

