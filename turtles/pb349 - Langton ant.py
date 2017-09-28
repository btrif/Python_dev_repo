#  Created by Bogdan Trif on 27-09-2017 , 5:01 PM.

import turtle

# wn = turtle.Screen()
# # wn.bgcolor("lightgreen")  # set the window background color
#
t = turtle.Turtle()


# t.exitonclick()

def drawSquare(color):
    # turtle.pencolor("red")
    t.speed(3)
    # turtle.begin_fill()


    t.pensize(10)
    t.left(90)
    t.forward(150)
    t.left(90)
    t.forward(75)


    # turtle.end_fill()

    # t = turtle.Turtle()
    # screen = t.getscreen()

drawSquare("black")
t.exitonclick()

turtle.begin_fill() # Begin the fill process.
turtle.down() # "Pen" down?
for i in range(squares):  # For each edge of the shape
    turtle.forward(40) # Move forward 40 units
    turtle.left(angle) # Turn ready for the next edge
turtle.up() # Pen up
turtle.end_fill() # End fill.