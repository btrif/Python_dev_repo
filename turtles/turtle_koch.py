#  Created by Bogdan Trif on 02-11-2017 , 10:57 AM.
import turtle as t

def koch(t, order, size):
    """
       Make turtle t draw a Koch fractal of 'order' and 'size'.
       Leave the turtle facing the same direction.
    """
    if order == 0:          # The base case is just a straight line
        t.forward(size)
    else:
        koch(t, order-1, size/3)   # Go 1/3 of the way
        t.left(60)
        koch(t, order-1, size/3)
        t.right(120)
        koch(t, order-1, size/3)
        t.left(60)
        koch(t, order-1, size/3)


def koch2(t, order, size):
    """
       Make turtle t draw a Koch fractal of 'order' and 'size'.
       Leave the turtle facing the same direction.
    """
    if order == 0:          # The base case is just a straight line
        t.forward(size)
    else:
        for angle in [ 0, 60, -120, 60  ] :
            t.left(angle)
            koch2(t, order-1, size/3)   # Go 1/3 of the way






t.penup()
t.goto(-400, -200)
t.pendown()
koch2(t, 3, 800)

t.exitonclick()




