import turtle

# Call the Turtle Constructor to create a turtle object.
t = turtle.Turtle()

# getscreen is an accesor method on turtle objects
screen = t.getscreen()

# mutator methods, they change the object

def Star():
    for i in range(5):
        t.pensize(4)
        t.forward(250)
        t.left(144)

Star()
screen.exitonclick()



