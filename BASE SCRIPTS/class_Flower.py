import math
import turtle
import random

class FLOWER():

    def toRadians(self, degrees):
        return (degrees / 180.0) * math.pi
    
    def polar_to_X(self, theta, r):
        x = r * math.cos(theta)
        return x
    
    def polar_to_Y(self, theta, r):
        y = r * math.sin(theta)
        return y
    
    def drawPetal(self, turtle, x, y, scale, color, angle):
        turtle.Turtle()
        turtle.speed(1000)
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.color(color)
        
        turtle.begin_fill()
            
        for k in range(101):
            theta = (k / 100.0) * (math.pi / 3.0)
            r = scale * 80 * math.sin(3 * theta)
            
            xv = self.polar_to_X(theta + angle, r)
            yv = self.polar_to_Y(theta + angle, r)
            
            turtle.goto(x + xv, y + yv)
            
        turtle.end_fill()
        turtle.penup()   
    
    def drawFlower(self, turtle, x , y, scale, color_1, color_2):
        
        for i in range(6):
            angle = i * 360.0 / 6
            
            self.drawPetal(turtle, x, y, scale, color_1, self.toRadians(angle))
             
        for i in range(10):
             
            angle = i * (360.0 / 10)
            self.drawPetal(turtle, x, y, scale * 0.1, color_2, self.toRadians(angle))
             

def main():
    turtle.Turtle()
    
    screen = turtle.getscreen()
    screen.tracer(1000)
    screen.update()  
    screen.setworldcoordinates(-100, -100, 100, 100)   
    
    donald = FLOWER()
#    print(donald, donald.drawFlower, donald.drawFlower.color_1)
    
    
    for a in range(500):  
        color1 = "#%06x" % random.randint(0,0xFFFFFF)
        color2 = "#%06x" % random.randint(0,0xFFFFFF)
        donald.drawFlower(turtle, random.randint(-100, 100), random.randint(-100, 100), random.random()/2, color1, color2)
   

    
    
#    donald.drawFlower(turtle, -40, 20, random.random()/2, "#e2c5f7", "orange")   
#    donald.drawFlower(turtle, 40, -40, 0.3, "green", "cyan")
       
    screen.exitonclick()

if __name__ == "__main__": main()

