from turtle import *

# Step 1: Create a turtle object
turtle1 = Turtle()  # Create the first turtle
turtle1.shape("turtle")    # Set its shape to "turtle"
turtle1.color("blue")      # Set its color
turtle1.speed(3)           # Adjust its speed

# Step 2: Create another turtle object
turtle2 = Turtle()  # Create the second turtle
turtle2.shape("circle")    # Set its shape
turtle2.color("red")       # Set its color
turtle2.speed(7)           # Faster speed

# Step 3: Use methods to move the turtles
# Turtle 1 draws a square
for _ in range(4):
    turtle1.forward(100)
    turtle1.left(90)

# Turtle 2 draws a triangle
for _ in range(3):
    turtle2.forward(100)
    turtle2.left(120)

# Keep the window open until clicked
exitonclick()