#  Created by Bogdan Trif on 27-09-2017 , 5:56 PM.
# Set dot color based on where they are in Python turtle?


from turtle import Turtle, Screen
from random import randint

AREA_SIZE = 800
MAX_COORD = AREA_SIZE / 2
SQUARE_SIZE = 200
DOT_SIZE = 4
NUM_DOTS = 300
STAMP_SIZE = 20

screen = Screen()
screen.setup(AREA_SIZE, AREA_SIZE)

turtle = Turtle(shape="circle")
turtle.shapesize(DOT_SIZE / STAMP_SIZE)
turtle.speed("fastest")

for _ in range(4):
    turtle.forward(SQUARE_SIZE)
    turtle.left(90)

turtle.left(45)
turtle.goto(SQUARE_SIZE, SQUARE_SIZE)
turtle.penup()

black, red, green = 0, 0, 0

for _ in range(NUM_DOTS):

    color = "black"

    x = randint(-MAX_COORD, MAX_COORD)
    y = randint(-MAX_COORD, MAX_COORD)

    turtle.goto(x, y)

    # color dot if it's in the square but not smack on any of the lines
    if 0 < x < SQUARE_SIZE and 0 < y < SQUARE_SIZE:
        if x < y:
            color = "green"  # easier to distinguish from black than blue
            green += 1
        elif y < x:
            color = "red"
            red += 1
        else : black += 1  # it's on the line!
    else:
        black += 1  # it's not in the square

    turtle.color(color)
    turtle.stamp()

turtle.hideturtle()

print("Black: {}\nRed: {}\nGreen: {}".format(black, red, green))

screen.exitonclick()


