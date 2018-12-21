#  Created by Bogdan Trif on 30-06-2018 , 3:16 PM.


import turtle

myTurtle = turtle.Turtle()
myWin = turtle.Screen()
myTurtle.speed(10)

def drawTriangle( points , color , myTurtle ):
    myTurtle.fillcolor(color)
    myTurtle.up()

    myTurtle.goto(points[0][0],points[0][1])        # ( -100, -50 )
    myTurtle.down()
    myTurtle.begin_fill()
    myTurtle.goto(points[1][0],points[1][1])        # (0 , 100)
    myTurtle.goto(points[2][0],points[2][1])        #  [100,-50]
    myTurtle.goto(points[0][0],points[0][1])      # ( -100, -50 )
    myTurtle.end_fill()



def triangle(line_len):
    for i in range(3) :
        myTurtle.forward(line_len)
        myTurtle.left(120)
    myTurtle.forward(line_len//2)
    myTurtle.left( 60 )


side_len = 400
myPoints = [ [-side_len , -side_len//2 ] , [ 0, side_len ],[ side_len,-side_len//2 ] ]


# triangle(300)

drawTriangle(myPoints, 'olive', myTurtle)



myWin.exitonclick()