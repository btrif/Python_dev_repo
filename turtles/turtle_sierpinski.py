#  Created by Bogdan Trif on 02-11-2017 , 10:43 AM.

#  Created by Bogdan Trif on 02-11-2017 , 10:28 AM.
from  turtle import *

def sierpinski(l, n ):
    if n==0 :
        begin_fill()
        forward(l)
        left(120)
        forward(l)
        left(120)
        forward(l)
        left(120)
        end_fill()
    else:
        sierpinski(l/2, n-1)                    # recursion call
        forward(l/2)
        sierpinski(l/2, n-1)                # recursion call
        left(120)
        forward(l/2)
        right(120)
        sierpinski(l/2, n-1)            # recursion call
        right(120)
        forward(l/2)
        left(120)

speed(0)
penup()
goto(-300, -200)
pendown()
rang = input('Choose a range: ', )
rang = int(rang )
sierpinski(400, rang)
exitonclick()






