#  Created by Bogdan Trif on 23-05-2018 , 11:20 PM.
#  Created by Bogdan Trif on 23-05-2018 , 8:29 PM.
import turtle
import random
from math import cos, acos, sqrt, sin, asin, pi


A = [ acos(4/5)*180/pi , acos(3/5)*180/pi  ]
E = [ 4/5, 3/5 ]
# A = [ acos(sqrt(2)/2)*180/pi , acos(sqrt(2)/2)*180/pi  ]
# E = [ sqrt(2)/2, sqrt(2)/2]

myWin = turtle.Screen()
t = turtle.Turtle()
t.speed(2)

def square(points, color, t) :
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.goto(points[0][0], points[0][0]  )
    t.goto(points[1][0], points[0][0]  )
    t.goto(points[1][0], points[1][1]  )
    t.goto(points[0][0], points[1][0]  )
    t.goto(points[0][0], points[0][0]  )

    # for i in range(4) :
    #     t.forward(sidelen)
    #     t.left(90)
    t.end_fill()


colors = ['brown', 'green']

def pythagorean_tree(points, w, t) :
    color = colors[w%2]
    # side_len=100


    if (points[1][0]-points[0][0]) > 80 :
        square(points, color, t )

        # t.forward(sidelen)
        # t.right( A[1] )
        pythagorean_tree( [ points ,  w+1 , t)

        # t.color('blue')
        # t.left(90)
        #
        # t.backward(sidelen)
        # # t.left(90)


        # pythagorean_tree(E[1] * sidelen,  w+1, t )
        # t.backward( sidelen )

        # t.forward( sidelen )



def main() :

    print('angles : ', A )
    print('sides : ' , E  )

    side_len = 100
    points = [ [0,0] , [side_len, side_len] ]

    # square(points, colors[0] , t )

    t.pensize(1)
    t.penup()
    # t.goto(0, -400 )

    pythagorean_tree(points , 0, t )








    myWin.exitonclick()

main()





