from turtle import *

# 1. Set rotation angle and coordinates
setheading(45)  # Set heading to 45 degrees
goto(100, 100)  # Move to coordinates (100, 100)

# 2. Show approximate starting position
penup()  # Lift the pen
goto(-200, -200)  # Move to a corner
pendown()  # Lower the pen
dot(10, "red")  # Draw a red dot to mark the starting point

# 3. Use basic turtle functions
forward(100)  # Move forward 100 units
left(90)     # Turn left 90 degrees
right(45)    # Turn right 45 degrees
goto(0, 0)   # Go back to the origin

# 4. Use pen customization functions
pensize(5)   # Set pen size to 5 pixels
color("blue")  # Set pen color to blue
penup()     # Lift the pen
forward(50)  # Move forward without drawing
pendown()   # Lower the pen

# 5. Adjust speed and hide the turtle
speed(10)  # Set the drawing speed (1 is slowest, 10 is fastest)
hideturtle()  # Hide the turtle's shape

# 6. Code loop-based algorithms for complex shapes
def draw_spiral(size, angle):
    for _ in range(100):
        forward(size)
        right(angle)
        size += 1

draw_spiral(5, 25)

# Keep the turtle window open
exitonclick()