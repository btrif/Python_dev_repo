#  Created by Bogdan Trif on 23-05-2018 , 8:29 PM.
import turtle
import random

def leaf(branchlen, t):
    t. forward(branchlen)



# branchLen = 60
def tree(branchlen, t, w) :
    if branchlen > 25 :
        # color = random.choice(['blue', 'green',  'red' ,'purple','cyan' , 'magenta'  ])
        # color = random.choice(['blue',   'red' , 'indigo' , 'purple' ])
        # color = random.choice(['black', 'red'  ])
        # color = random.choice(['blue'])

        t.pensize(w)
        # t.color(color)

        t.forward(branchlen)
        t.right(20)

        tree(branchlen-35, t, w-0.5)

        t.left(20)
        tree(branchlen-35, t, w-0.5)

        t.left(20)
        tree(branchlen-35, t, w-0.5)

        t.right(20)
        t.backward(branchlen)




def main() :
    t = turtle.Turtle()
    t.speed(1)
    t.left(90)
    t.up()
    t.backward(300)
    myWin = turtle.Screen()

    t.down()

    tree(140, t, 4)


    myWin.exitonclick()

main()



# t.forward( branchLen )
# t.right(20)
# t.forward( branchLen )
# t.left(40)


