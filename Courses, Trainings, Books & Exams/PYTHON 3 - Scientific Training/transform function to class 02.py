import math
import turtle

class FLOWER:

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
    
    def drawFlower(self, turtle, x , y, scale, color):
        
        for i in range(6):
            angle = i * 360.0 / 6
            
            self.drawPetal(turtle, x, y, scale, color, self.toRadians(angle))
             
        for i in range(10):
             
            angle = i * (360.0 / 10)
            self.drawPetal(turtle, x, y, scale * 0.1, "cyan", self.toRadians(angle))
             

def main():
    turtle.Turtle()
    
    screen = turtle.getscreen()
    screen.tracer(30)       # sets the speed of the cursor drawing
    screen.update()
    
    
    screen.setworldcoordinates(-100, -100, 100, 100)   
    
    donald = FLOWER()
    print(donald.toRadians(90))
    print(donald.polar_to_X(60 , 1))
    
    donald.drawPetal(turtle, -20, -52, 0.5, "red", 130)
    
    donald.drawFlower(turtle, 20, 20, 0.7, "yellow")
    

    
#    donald.drawFlower(turtle, -40, 20, 0.4, "blue")
    
#    donald.drawFlower(turtle, 40, -40, 0.3, "green")
    

    
    screen.exitonclick()

if __name__ == "__main__": main()  

      


# drawFlower(t, 0, 0, 0.5, "lightblue")

