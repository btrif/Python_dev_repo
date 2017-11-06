# Create A Game Board
#
# Create an 8 x 8 game board using a 2D array.
#
# Make sure to have read and practised your 2D arrays first.
#
# Start by building a 2D array filled with 0’s or 1’s. Use for loop to generate the array or list comprehension.
#
# Draw a board using a for loop running through the array by row and then by column.
# Increment and reset x and y variables to track where on the screen you should be.
# Check what the value of the array is to determine the fill colour.
#
# Create a mouse pressed function to find out where the user is clicking.
# Use integer division to generate the position in terms of the array. Try changing the value in the array based on clicks.


grid = [ [-1]*8  for n in range(8)] # list comprehension
grid[0][0] = 1
grid[7][7] = 1



w = 70 # width of each cell

def setup():
    size(800,600)
    
def draw():
    
    x,y = 0,0 # starting position

    for row in grid:
        for col in row:
          if col == 1:
              fill(250,0,0)
          else:
              fill(255)
          rect(x, y, w, w)
          x = x + w  # move right
        y = y + w # move down
        x = 0 # rest to left edge
        
        
def mousePressed():
    grid[mouseY/w][mouseX/w] = -1 * grid[mouseY/w][mouseX/w]  
    # integer division is good here!

