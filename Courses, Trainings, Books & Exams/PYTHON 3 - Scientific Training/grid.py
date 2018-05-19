import turtle

wn = turtle.Screen()
wn.bgcolor("#EBF1F5")  # set the window background color
turtle.screensize(1000, 800)
turtle.resizemode()

tess = turtle.Turtle()
tess.color("blue")  # make tess blue
tess.pensize(3)  # set the width of her pen


wn.exitonclick()  # wait for a user click on the canvas

print(turtle.window_height())
print(turtle.window_width()) 
