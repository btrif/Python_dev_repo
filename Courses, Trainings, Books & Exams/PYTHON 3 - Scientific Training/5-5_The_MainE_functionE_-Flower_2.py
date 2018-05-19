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

def drawPetal(turtle, x, y, scale, color, angle):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    
    turtle.begin_fill()
        
    for k in range(101):
        theta = (k / 100.0) * (math.pi / 3.0)
        r = scale * 80 * math.sin(3 * theta)
        
        xv = polar_to_X(theta + angle, r)
        yv = polar_to_Y(theta + angle, r)
        
        turtle.goto(x + xv, y + yv)
        
    turtle.end_fill()   

def drawFlower(turtle, x , y, scale, color):
    
    screen = turtle.getscreen()
    
    screen.tracer(100)
    
    for i in range(6):
        angle = i * 360.0 / 6
        
        drawPetal(turtle, x, y, scale, color, toRadians(angle))
    
    for i in range(10):
        angle = i * (360.0 / 10)
        drawPetal(turtle, x, y, scale * 0.1, "orange", toRadians(angle))
    
    screen.update()

def main():        
    t = turtle.Turtle()
    screen = t.getscreen()
    screen.setworldcoordinates(-100, -100, 100, 100)
    
    drawFlower(t, 0, 0, 0.5, "lightblue")
    
    screen.exitonclick()

if __name__ == "__main__":
    main()
