#  Created by Bogdan Trif on 02-11-2017 , 10:43 AM.

#  Created by Bogdan Trif on 02-11-2017 , 10:28 AM.
import turtle as t


def sierpinski(l, n ):
    if n==0 :
        t.begin_fill()
        t.forward(l)
        t.left(120)
        t.forward(l)
        t.left(120)
        t.forward(l)
        t.left(120)
        t.end_fill()
    else:
        sierpinski(l/2, n-1)                    # recursion call
        t.forward(l/2)
        sierpinski(l/2, n-1)                # recursion call
        t.left(120)
        t.forward(l/2)
        t.right(120)
        sierpinski(l/2, n-1)            # recursion call
        t.right(120)
        t.forward(l/2)
        t.left(120)

t.speed(0)
t.penup()
t.goto(-300, -200)
t.pendown()
rang = input('Choose a range: ', )
rang = int(rang )
sierpinski(400, rang)
t.exitonclick()






