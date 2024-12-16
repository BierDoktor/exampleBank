import turtle

# Concepts Explanation:
#    - Event: An event is an action or occurrence recognized by a program, such as a mouse click or key press.
#    - Subscription to an Event: Subscription means registering a function (event handler) to respond when a specific event occurs.
#    - Event Handler: A function or method executed when an event occurs, reacting to the event.

# Example program demonstrating these concepts:

def change_color_on_click(x, y):
    """Event handler: Change the color of the clicked turtle."""
    if red_turtle.distance(x, y) < 20:  # Check if click is near red turtle
        red_turtle.color("blue")
        print(red_turtle.color())
        print("Red turtle clicked! Now it's blue.")
    elif green_turtle.distance(x, y) < 20:  # Check if click is near green turtle
        green_turtle.color("yellow")
        print("Green turtle clicked! Now it's yellow.")

# Program selects significant events and reacts to them:
#    - Significant events (mouse clicks) are filtered based on their location.
#    - The program determines which turtle was clicked by calculating the distance between the click point and the turtles.

# Create the screen
screen = turtle.Screen()

# Create two turtle objects
red_turtle = turtle.Turtle()
green_turtle = turtle.Turtle()

# Set turtle properties
red_turtle.shape("turtle")
red_turtle.color("red")
red_turtle.penup()
red_turtle.goto(-100, 0)  # Position turtle

green_turtle.shape("turtle")
green_turtle.color("green")
green_turtle.penup()
green_turtle.goto(100, 0)  # Position turtle

# Handle mouse clicks on one of the turtles
# Bind the onclick event to the screen, passing the event handler
screen.onclick(change_color_on_click)

# Keep the window open
screen.mainloop()