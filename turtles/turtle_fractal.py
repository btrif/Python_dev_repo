#  Created by Bogdan Trif on 02-11-2017 , 10:28 AM.
import turtle
loadWindow =  turtle.Screen()
t = turtle.Pen()
t.speed(0)
t.penup()
t.goto(0, -100)
t.pendown()

#defining recursive function

def draw_fractal(length, depth) :
    t.forward(length)
    if depth > 1 :
        t.backward(length/2)
        t.left(90)
        draw_fractal(length/2.1, depth-1)
        t.forward(length/2.1)
        t.right(180)
        draw_fractal(length/2.1, depth-1)
        t.forward(length/2.1)
        t.right(90)
        # draw_fractal(length/2.1, depth-1)
        t.forward(length/2)



    t.right(180)
    t.forward(length)

# run function
draw_fractal(400, 6)
t.right(180)
draw_fractal(400, 6)

# exit
turtle.exitonclick()



