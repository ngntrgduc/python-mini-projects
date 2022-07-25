from turtle import *
import random

setup(900,600) # Turtle screen size
speed(0) # Drawing speed
colormode(255) # Enable RGB color in turtle

# Move cursor
def move(x, y):
    penup()
    goto(x, y)
    pendown()

def generate_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color(r, g, b)

def tree(size, levels, angle):
    if (levels == 0):
        return

    generate_color()
    forward(size)
    right(angle)
    tree(size * 0.85, levels - 1, angle)
    left(angle * 2)
    tree(size * 0.85, levels - 1, angle)
    right(angle)
    backward(size)

def square_spiral(size, levels):
    if (levels == 0):
        return
    
    generate_color()
    forward(size)
    right(90)
    square_spiral(size - 2, levels - 1)

def draw_square(size):
    forward(size)
    right(90)
    forward(size)
    right(90)
    forward(size)
    right(90)
    forward(size)
    right(90)

def square(size, levels, space):
    if (levels == 0):
        return

    # generate_color()
    draw_square(size)
    if (levels > 1):
        penup()
        goto(xcor() + space/ 2, ycor() - space/ 2)
        pendown()

    square(size - space, levels - 1, space)

def random_squares(numbers):
    if (numbers == 0):
        return 
    
    move(random.randint(-450, 450), random.randint(-300, 300))
    draw_square(random.randint(0, 200))
    random_squares(numbers - 1)


def generate_dots(size, numbers):
    if (numbers == 0):
        dot(size)
        return

    generate_color()
    dot(size)
    penup()
    goto(random.randint(-450, 450), random.randint(-300, 300))  
    generate_dots(size, numbers - 1)
    

def random_draw(lines):
    if (lines == 0):
        return

    generate_color()
    num = random.randint(0, 11)
    forward(random.randint(0, 50))
    if (xcor() > 450 or ycor() > 300 or xcor() < -450 or ycor() < -300):
        backward(random.randint(0, 50))
    if (num % 2 == 0):
        right(random.randint(0, 90))
    else: 
        left(random.randint(0, 90))

    random_draw(lines - 1)

def triangle(numbers):
    if (numbers == 0):
        return 

    generate_color()
    forward(100)
    left(120)
    forward(100)
    left(120)
    forward(100)
    left(120)
    move(random.randint(-450, 450), random.randint(-300, 100))
    triangle(numbers - 1)

# Fractal tree
# left(90)
# tree(60, 10, 20)

# Spiral
# move(-300, 300)
# square_spiral(600, 300)

# Square
# move(-300, 300)
# square(600, 70, 20)

# Dots
# generate_dots(20, 500)

# Random draw
# random_draw(1000)

# Random square
# random_squares(100)

# Triangle
# triangle(50)

mainloop()