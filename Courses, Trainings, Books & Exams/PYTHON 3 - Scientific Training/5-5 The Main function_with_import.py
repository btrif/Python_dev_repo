import 'TheMainfunction_with_import.py'
import turtle

def main():
    t = turtle.Turtle()
    screen = t.getscreen()
    draw_Flower_2.drawFlower(t, 0 , 0 , 2, "blue")
    
    draw_Flower_2.drawFlower(t, 50 , 50, 0.5, "pink")
    
    draw_Flower_2.drawFlower(t, 150 , -150, 0.8, "yellow")
    
    screen.exitonclick()
    
if __name__ == "__main__":
    main()
