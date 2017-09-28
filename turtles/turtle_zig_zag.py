# made by Bogdan Trif @ 2014-10-06 14:00

import turtle

window = turtle.Screen()

def simpleLoop(a, b, c):
    for i in range(a, b, c):
        print (i)
    
simpleLoop(4, 400, 44)

turtle.setpos(-40, -30)
def ZigZag(turtle, rng, ya, x, yb, w, speed, color, t):
    for i in range(rng):
        turtle.speed(speed)
        turtle.color(color)
        turtle.pensize(t)

        turtle.forward(ya)
        turtle.left(x)
        turtle.color("blue")
        turtle.forward(yb)
        turtle.right(w)
       

ZigZag(turtle, 25 , 68, 40, 18, 9, 4, '#ee1199#', 5)

window.exitonclick()
    
'''
wn = turtle.Screen()
wn.bgcolor("blue")
jamal = turtle.Turtle()
jamal.color("white")
jamal.pensize(10)
jamal.right(90)
jamal.forward(150)
jamal.left(90)
jamal.forward(75)


def makeSquare(turtle, size):
    for i in range(4):
        turtle.pensize(5)
        turtle.speed(0)
        turtle.color('#dddd33')
        
        turtle.forward(size)
        turtle.left(90)


wn.exitonclick()
'''
