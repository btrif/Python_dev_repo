'''
A regular polygon has n number of sides. Each side has length s.
The area of a regular polygon is: 0.25∗n∗s**2/tan(π/n)
The perimeter of a polygon is: length of the boundary of the polygon
Write a function called polysum that takes 2 arguments, n and s.
This function should sum the area and square of the perimeter of the regular polygon.
The function returns the sum, rounded to 4 decimal places.

'''
from math import tan as tan
from math import pi as pi
# n- the number of sides,       s - length of the side

def polysum(n , s):
    squared_perim = (n*s)**2
    area = (0.25*n*(s**2))/(tan(pi/n))
    return round((squared_perim+area),4)


print(polysum(42,21))