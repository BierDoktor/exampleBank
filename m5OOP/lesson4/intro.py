# Define a class
class Car:
    # Constructor: initializes the fields (attributes) of the class
    def __init__(self, brand, model, year):
        self.brand = brand  # Field: brand of the car
        self.model = model  # Field: model of the car
        self.year = year    # Field: year of manufacture
    
    # Method: describes the car
    def describe(self):
        return f"This car is a {self.year} {self.brand} {self.model}."
    
    # Method: calculates the car's age
    def car_age(self, current_year):
        return current_year - self.year

# Create instances of the Car class
car1 = Car("Toyota", "Corolla", 2015)
car2 = Car("Honda", "Civic", 2020)

# Use methods of the Car class
print(car1.describe())  # Output: This car is a 2015 Toyota Corolla.
print(f"Car 1 is {car1.car_age(2025)} years old.")  # Output: Car 1 is 10 years old.

print(car2.describe())  # Output: This car is a 2020 Honda Civic.
print(f"Car 2 is {car2.car_age(2025)} years old.")  # Output: Car 2 is 5 years old.