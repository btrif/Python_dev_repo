#  Created by Bogdan Trif on 05-04-2018 , 7:04 PM.
'''      In this example I will exercise Recursion .
The problem is as follows :
As a more complex example of the
use of recursion, consider how to draw the markings of a typical English ruler. For
each inch, we place a tick with a numeric label. We denote the length of the tick
designating a whole inch as the major tick length. Between the marks for whole
inches, the ruler contains a series of minor ticks, placed at intervals of 1/2 inch,
1/4 inch, and so on. As the size of the interval decreases by half, the tick length
decreases by one. Figure 4.2 demonstrates several such rulers with varying major
tick lengths (although not drawn to scale).
----- 0
-
--
-
---
-
--
-
----
-
--
-
---
-
--
-
----- 1

This is a more complex recursion and we need to cut the problem into three parts :
1.  draw_line function - function which simply prints a line mark
2.   draw_interval - here we will have our recursion implemented
3.  draw_ruler - this is the main general function

OBSERVATION : As we have two ways of going after we split the ruler, we need to make two recursion calls

'''

def draw_line(tick_length, tick_label='') :
    ''' Draw one line with given tick length (followed by optional label).'''
    line = '-'*tick_length
    if tick_label :
        line += ' ' + str(tick_label)
    print(line)

# draw_line(4, '0')

def draw_interval( center_length ) :
    ''' Draw tick interval based upon a central tick length.'''
    if center_length > 0:                           # stop when length drops to 0
        draw_interval(center_length-1)      # recursively draw top ticks
        draw_line( center_length )              # draw center tick

        draw_interval(center_length-1)      # recursively draw bottom ticks


draw_interval( 3 )

print('-----------')

def draw_ruler(num_inches, major_length) :
    '''    Draw English ruler with given number of inches, major tick length. '''
    draw_line(major_length, '0' )               #   draw inch 0 line
    for i in range(1, num_inches+1 ) :
        draw_interval(major_length -1)          # draw interior ticks for inch
        draw_line(major_length, str(i) )            # draw inch i line and label


draw_ruler(4, 2)






