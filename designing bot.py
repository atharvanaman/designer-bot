import turtle
import random

# Set up the turtle window
turtle.setup(800, 600)
window = turtle.Screen()
window.bgcolor('black')
turtle.speed(0)
turtle.hideturtle()
turtle.colormode(255)

# L-system rules and axiom
rules = {'F': "FF+[+F-F-F]-[-F+F+F]"}
axiom = "F"
iterations = 4
angle = 25

# Function to generate the L-system string
def generate_lsystem(axiom, rules, iterations):
    for _ in range(iterations):
        next_axiom = ""
        for char in axiom:
            next_axiom += rules.get(char, char)
        axiom = next_axiom
    return axiom

# Function to draw the L-system
def draw_lsystem(axiom, angle, length=5):
    stack = []
    for char in axiom:
        if char == 'F':
            turtle.forward(length)
        elif char == '+':
            turtle.right(angle)
        elif char == '-':
            turtle.left(angle)
        elif char == '[':
            position = turtle.position()
            heading = turtle.heading()
            stack.append((position, heading))
        elif char == ']':
            position, heading = stack.pop()
            turtle.penup()
            turtle.setposition(position)
            turtle.setheading(heading)
            turtle.pendown()

# Function to randomize turtle color
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

# Generate the L-system string and draw it
lsystem_string = generate_lsystem(axiom, rules, iterations)
turtle.color(random_color())
draw_lsystem(lsystem_string, angle)

# Hide the turtle and display the window
turtle.hideturtle()
window.exitonclick()
