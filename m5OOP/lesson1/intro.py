# Explain what an object is, and what methods and properties of an object are:
    # Object: An object is like a "thing" in the program that has data (properties) and behaviors (methods). 
    # For example, a car object can have properties like color, speed, and model, and methods like drive or stop.



# Define a Car class
class Car:
    def __init__(self, brand, color, speed):
        # Properties (attributes) of the Car object
        self.brand = brand
        self.color = color
        self.speed = speed
    
    # Method to display car details
    def display_details(self):
        print(f"Car Brand: {self.brand}, Color: {self.color}, Speed: {self.speed} km/h")
    
    # Method to accelerate the car
    def accelerate(self, amount):
        self.speed += amount
        print(f"The car accelerates by {amount} km/h. New speed is {self.speed} km/h.")
    
    # Method to brake the car
    def brake(self, amount):
        self.speed -= amount
        if self.speed < 0:
            self.speed = 0
        print(f"The car slows down by {amount} km/h. New speed is {self.speed} km/h.")

# Create a Car object
my_car = Car("Toyota", "Red", 50)

# Accessing properties
print("Car Details:")
print(f"Brand: {my_car.brand}")
print(f"Color: {my_car.color}")
print(f"Speed: {my_car.speed} km/h")

# Using methods
print("\nActions:")
my_car.display_details()
my_car.accelerate(30)  # Increase speed
my_car.brake(60)       # Reduce speed
