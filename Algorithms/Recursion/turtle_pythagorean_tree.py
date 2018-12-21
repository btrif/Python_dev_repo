#  Created by Bogdan Trif on 23-05-2018 , 11:20 PM.
#  Created by Bogdan Trif on 23-05-2018 , 8:29 PM.
import turtle
import random
from math import cos, acos, sqrt, sin, asin, pi


A = [ acos(4/5)*180/pi , acos(3/5)*180/pi  ]
E = [ 4/5, 3/5 ]
# A = [ acos(sqrt(2)/2)*180/pi , acos(sqrt(2)/2)*180/pi  ]
# E = [ sqrt(2)/2, sqrt(2)/2]

def square(sidelen, t, color) :
    t.pendown()
    t.color(color)
    t.begin_fill()
    for i in range(5) :

        t.forward(sidelen)
        t.left(90)
    # t.left(180)
    # t.penup()
    # t.forward(sidelen)

    t.end_fill()


colors = ['brown', 'green']

def pythagorean_tree(sidelen, t, w) :
    color = colors[w%2]

    if sidelen > 80 :

        square(sidelen, t, color )

        # t.forward(sidelen)
        # t.right( A[1] )

        pythagorean_tree(E[1] * sidelen, t, w+1 )
        t.color('blue')

        t.left(A[1])
        # t.left(90)

        t.backward(sidelen)
        t.left(90)


        # pythagorean_tree(E[1] * sidelen, t, w+1 )
        # t.backward( sidelen )

        # t.forward( sidelen )









def main() :
    myWin = turtle.Screen()
    t = turtle.Turtle()

    t.speed(2)

    print(' angles : ', A )
    print('sides : ' , E  )

    side = 100


    t.pensize(1)
    t.left(90)
    t.up()
    t.backward(300)
    t.left(90)
    t.down()

    # pythagorean_tree(side , t, 3  )

    # square(120, t, 'orange' )
    t.setheading(90)
    # t.goto(30, 400)

    # t.penup()
    # t.forward(side)

    pythagorean_tree(140, t, 4)




    myWin.exitonclick()

main()



# t.forward( branchLen )
# t.right(20)
# t.forward( branchLen )
# t.left(40)


