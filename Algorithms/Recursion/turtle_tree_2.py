#  Created by Bogdan Trif on 23-05-2018 , 8:29 PM.
import turtle
import random

def simple_tree( branch_len , t ) :
    if branch_len > 10 :

        t.forward(branch_len)
        t.right(20)

        simple_tree( branch_len-20, t )

        t.left(40)

        simple_tree( branch_len-20, t )

        t.right( 20 )
        t.backward(branch_len)



colors = [ 'brown' , 'peru', 'olive' , 'darkolivegreen', 'darkgreen', 'green', 'forestgreen'  ]
def nice_tree( branch_len , thickness , colo ,  t ) :
    if branch_len > 10 :
        t.pensize(thickness)
        t.color( colors[colo] )
        t.forward(branch_len)
        t.right(20)

        nice_tree( branch_len-20 , thickness-1, colo+1 ,  t )

        t.left(40)

        nice_tree( branch_len-20 , thickness-1, colo+1 , t )

        t.right( 20 )
        t.color( colors[colo] )
        t.backward(branch_len)






def main() :
    t = turtle.Turtle()
    t.speed(9)
    t.left(90)
    t.up()
    t.backward(300)
    myWin = turtle.Screen()

    t.down()

    # simple_tree( 140, t )
    nice_tree( 140, 6 , 0 , t )


    myWin.exitonclick()

main()



# t.forward( branchLen )
# t.right(20)
# t.forward( branchLen )
# t.left(40)


