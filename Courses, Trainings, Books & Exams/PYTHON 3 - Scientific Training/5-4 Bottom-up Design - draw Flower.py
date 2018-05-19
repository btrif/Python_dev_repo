import math
import turtle

def toRadians(degrees):
    return (degrees / 180.0) * math.pi

def polar_to_X(theta, r):
    x = r * math.cos(theta)
    return x

def polar_to_Y(theta, r):
    y = r * math.sin(theta)
    return y

def drawPetal(t, x, y, angle):
    t.penup()
    t.goto(x, y)
    t.pendown()
    
    for k in range(101):
        theta = (k / 100.0) * (math.pi / 3.0)
        r = 80 * math.sin(3 * theta)
        
        xv = polar_to_X(theta + angle, r)
        yv = polar_to_Y(theta + angle, r)
        
        t.goto(x + xv, y + yv)
        
def drawFlower(t, x , y):
    for i in range(6):
        angle = i * 360.0 / 6
        
        drawPetal(t, 0, 0, toRadians(angle))
        
t = turtle.Turtle()
screen = t.getscreen()
screen.setworldcoordinates(-100, -100, 100, 100)

drawFlower(t,0,0)


screen.exitonclick()


        
        
        
print(toRadians(360))
print(polar_to_X(math.pi / 3, 1))
