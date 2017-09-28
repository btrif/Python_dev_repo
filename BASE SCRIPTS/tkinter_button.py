from tkinter import *
def stopProg(e):
    root.destroy()
    
root=Tk()
button1=Button(root,
 text="Hello World click to close")
button1.pack()
button1.bind('<Button-1>',stopProg)
root.mainloop()