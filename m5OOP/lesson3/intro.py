import turtle

# Create screen and turtle objects
screen = turtle.Screen() 
screen.bgcolor("lightblue")

t = turtle.Turtle()
t.shape("turtle")
t.color("green")
t.speed(1)

# Event Handlers

# Move the turtle to the clicked position on the screen
def on_screen_click(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

# Move the turtle forward on pressing 'Up'
def move_forward():
    t.forward(20)

# Move the turtle backward on pressing 'Down'
def move_backward():
    t.backward(20)

# Turn the turtle left on pressing 'Left'
def turn_left():
    t.left(30)

# Turn the turtle right on pressing 'Right'
def turn_right():
    t.right(30)

# Drag the turtle to follow the mouse
def drag_turtle(x, y):
    t.ondrag(None)  # Disable ondrag temporarily to avoid recursion
    t.setheading(t.towards(x, y))
    t.goto(x, y)
    t.ondrag(drag_turtle)  # Re-enable ondrag

# Subscribe to Events

# Screen click event
screen.onscreenclick(on_screen_click)

# Keyboard events
screen.listen()  # Activate keyboard event listening
screen.onkey(move_forward, "Up")
screen.onkey(move_backward, "Down")
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")

# Turtle dragging event
t.ondrag(drag_turtle)