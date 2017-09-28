class Point:
    """
    Simple class for representing a point in a Cartesian coordinate system.
    """
    
    def __init__(self, x, y):
        """
        Create a new Point at x, y.
        """
        self.x = x
        self.y = y
        
    def translate(self, dx, dy):
        """
        Translate the point by dx and dy in the x and y direction.
        """
        self.x += dx
        self.y += dy
        
    def __str__(self):
        return("Point at [%f, %f]" % (self.x, self.y))

p1 = Point(0, 0) # this will invoke the __init__ method in the Point class

print(p1)         # this will invoke the __str__ method

#To invoke a class method in the class instance p:

p2 = Point(1, 1)
p1.translate(0.25, 1.25)

print(p1)
print(p2)


print('\n---------- Inheriting from named tuples: -----------')
import collections
class Point(collections.namedtuple('PointBase', ['x', 'y'])):
    __slots__ = ()
    def __add__(self, other):
        return Point(x=self.x + other.x, y=self.y + other.y)

p = Point(x=1.0, y=2.0)
q = Point(x=2.0, y=3.0)
print(p+q)

