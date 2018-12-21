#  Created by Bogdan Trif on 16-06-2018 , 11:41 AM.

import turtle

myTurtle = turtle.Turtle()
myWin = turtle.Screen()
myTurtle.speed(10)

# def triangle(line_len):
#     for i in range(3) :
#         myTurtle.forward(line_len)
#         myTurtle.left(120)
#     myTurtle.forward(line_len//2)
#     myTurtle.left( 60 )

# def sierpinsky2(myTurtle,  line_len ) :
#     if line_len > 10 :
        # triangle( line_len )

        # sierpinsky(myTurtle , line_len//2 )

        # myTurtle.backward(line_len//2)
        # myTurtle.left( 60 )
        # sierpinsky(myTurtle , line_len//2 )
        # myPoints = [[-100,-50],[0,100],[100,-50]]
        # drawTriangle(myPoints , 'blue', myTurtle  )


# myTurtle.penup()
# myTurtle.goto(-300,-250)
# myTurtle.pendown()


def getMid( p1 , p2 ):
    return ( (p1[0]+p2[0]) / 2, (p1[1] + p2[1]) / 2)



def drawTriangle( points , color , myTurtle ):      # NOT exactly an equilateral Triangle, but close to ...
    myTurtle.fillcolor(color)
    myTurtle.up()

    myTurtle.goto(points[0][0],points[0][1])        # ( -100, -50 )
    myTurtle.down()
    myTurtle.begin_fill()
    myTurtle.goto(points[1][0],points[1][1])        # (0 , 100)
    myTurtle.goto(points[2][0],points[2][1])        #  [100,-50]
    myTurtle.goto(points[0][0],points[0][1])      # ( -100, -50 )
    myTurtle.end_fill()


def sierpinski( points, degree, myTurtle):
    #   main execution code for the recursive algorithm
    colormap = [ 'brown' , 'peru', 'olive' , 'darkolivegreen', 'darkgreen', 'green', 'forestgreen' , 'lightgreen' ]
    drawTriangle( points, colormap[degree], myTurtle )

    if degree > 0:
        #   1-st recursive call
        sierpinski([points[0], getMid(points[0], points[1]),  getMid(points[0], points[2])],  degree-1, myTurtle)
        #   2-nd recursive call
        sierpinski([points[1], getMid(points[0], points[1]), getMid(points[1], points[2])],  degree-1, myTurtle)
        #   3-rd recursive call
        sierpinski( [points[2],  getMid(points[2], points[1]), getMid(points[0], points[2])], degree-1, myTurtle)



def main():
   # myTurtle = turtle.Turtle()
   # myWin = turtle.Screen()
   side_len = 400
   myPoints = [ [-side_len , -side_len//2 ] , [ 0, side_len ],[ side_len,-side_len//2 ] ]
   sierpinski( myPoints , 5 , myTurtle)
   myWin.exitonclick()

main()