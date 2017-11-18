
import turtle

david = turtle.Turtle()
david.color('red')
david.penup()
david.goto(100,0)

david.pendown()
david.begin_fill()
num_sides = 6
side_length = 70
angle = 360.0 / num_sides

def triangle(length, angle , direction) :
    for i in range(3):
        if direction == 'left' :
            david.left(angle*2)
        elif direction == 'right' :
            david.right(angle*2)
        david.forward(length)

triangle(side_length*3, 120  ,'right' )

david.end_fill()
david.color('blue')
david.begin_fill()

david.penup()
david.left(90)
david.forward(side_length*40/23)
david.right(30)
david.pendown()
triangle(side_length*3, 120  ,'right' )
david.end_fill()

david.penup()
turtle.done()




