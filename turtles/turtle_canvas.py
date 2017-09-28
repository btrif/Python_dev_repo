#  Created by Bogdan Trif on 27-09-2017 , 6:00 PM.

from tkinter import Tk, Canvas, Frame, BOTH
import turtle

top = Tk()
C = Canvas(top, height=500, width=600)

Doug = turtle.RawTurtle(C)

rectangles = []
rectangles.append(C.create_rectangle(30, 10, 120, 80, outline="#fb0", fill="#fb0"))

Doug.fd(50)
Doug.rt(90)
Doug.fd(50)

# For some reason Doug's y-coord is opposite what Canvas uses, so * -1 to fix it...
overlapping = C.find_overlapping(Doug.xcor(), Doug.ycor() * -1, Doug.xcor(), Doug.ycor() * -1)
for item_id in overlapping:
   if item_id in rectangles:
        print(C.itemcget(item_id, "fill"))

C.pack(fill=BOTH, expand=1)
top.mainloop()


