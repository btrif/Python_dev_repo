#  Created by Bogdan Trif on 17-07-2018 , 3:34 PM.

# I noticed that in Python, people initialize their class attributes in two different ways.

# The first way is like this:

class MyClass:
    __element1 = 123                     #   static element, it means, they belong to the class
    __element2 = "this is Africa"       #   static element, it means, they belong to the class
    def __init__(self):
        pass
        #   pass or something else

# The other style looks like:

class MyClass:
    def __init__(self):
        self.__element1 = 123
        self.__element2 = "this is Africa"

# Which is the correct way to initialize class attributes?
# ANSWER :
'''
Both ways aren't correct or incorrect, they are just two different kind of class elements:

1.  Elements outside __init__ method are static elements, it means, they belong to the class.

2.  Elements inside the __init__ method are elements of the object (self ), they don't belong to the class.
 
You'll see it more clearly with some code:
'''

class MyClass:
    static_elem = 123
    def __init__(self):
        self.object_elem = 456


c1 = MyClass()
c2 = MyClass()

# Initial values of both elements
print('# Initial values of both elements')
print( ' c1 class : ',c1.static_elem, c1.object_elem)
# 123 456
print( ' c2 class : ', c2.static_elem, c2.object_elem )
# 123 456

# Nothing new so far ...
# Let's try changing the static element
print('\n# Lets try changing the static element')
MyClass.static_elem = 999

print( ' c1 class : ',c1.static_elem, c1.object_elem)
# 999 456
print( ' c2 class : ', c2.static_elem, c2.object_elem )
# 999 456

# Now, let's try changing the object element
print('\n# Now, let s try changing the object element')
c1.object_elem = 888
print( ' c1 class : ',c1.static_elem, c1.object_elem)
# 999 888
print( ' c2 class : ', c2.static_elem, c2.object_elem )
# 999 456

# As you can see, when we changed the class element, it changed for both objects. But, when we
# changed the object element, the other object remained unchanged.



