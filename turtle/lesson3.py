from turtle import *

# Set the reference point
penup()
goto(0, 0)
pendown()
dot(10, "red")
write("Reference Point", font=("Arial", 10, "normal"))

# Conditional drawing
def draw_shape(sides, length):
    angle = 360 / sides
    for _ in range(sides):
        forward(length)
        right(angle)

# Draw a square if the turtle's x-coordinate is positive
if xcor() > 0:
    pensize(3)
    color("green")
    draw_shape(4, 100)

# Draw a triangle if the turtle's y-coordinate is negative
elif ycor() < 0:
    pensize(2)
    color("blue")
    draw_shape(3, 80)

# Draw a circle if both coordinates are zero
elif xcor() == 0 and ycor() == 0:
    pensize(1)
    color("orange")
    circle(50)

# Keep the window open
exitonclick()