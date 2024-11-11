from turtle import *

# 1. Set turtle rotation angle and coordinates
setheading(45)  # Set the turtle's heading to 45 degrees
goto(100, 100)  # Move the turtle to coordinates (100, 100)


# 2. Show the turtle's starting position
dot(10, "red")  # Draw a red dot with a radius of 10 pixels at the turtle's position


# 3. Use basic turtle functions
forward(100)  # Move forward 100 units
left(90)     # Turn left 90 degrees
right(45)    # Turn right 45 degrees
goto(0, 0)   # Go back to the origin


# 4. Use pen customization functions
pensize(5)   # Set the pen size to 5 pixels
color("blue")  # Set the pen color to blue
penup()     # Lift the pen up
forward(50)  # Move forward without drawing
pendown()   # Put the pen down


# 5. Draw a square using a linear algorithm
def draw_square(size):
    for _ in range(4):
        forward(size)
        right(90)

draw_square(100)


# Keep the turtle window open
exitonclick()