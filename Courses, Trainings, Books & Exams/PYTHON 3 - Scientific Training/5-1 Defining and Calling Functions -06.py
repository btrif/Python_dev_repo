
# Plot a function using Turtle

import math
import turtle

def f(x):
    return x ** 3
    
t = turtle.Turtle()
screen = t.getscreen()

screen.setworldcoordinates(-10, -10, 10, 10)

t.penup()
t.goto(-20, -20)
t.pendown()

for k in range(-30  , 30, 1):
    myx = k / 10
    myy = f(myx)
    
    t.goto(myx, myy)
    
screen.exitonclick()



