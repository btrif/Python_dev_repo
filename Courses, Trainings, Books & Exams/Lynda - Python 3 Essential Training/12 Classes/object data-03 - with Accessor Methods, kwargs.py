#!/usr/bin/python3
# classes.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

class Duck:
    def __init__(self, **kwargs):
        self._color = kwargs.get('color', 'white')
        '''
        # I use _color because I need to remind me that this attribute will be used locally
        # but will be not
        # used directly. Otherwise said, will not access this variable from outside this object
        # All the access will be done from methods within the object 
        '''
    
    def quack(self):
        print('Quaaack!')

    def walk(self):
        print('Walks like a duck.')
    
    def feathers(self):
        print('The color of the feathers is: ' + self.get_color())
    
    def set_color(self, color):  # This method sets the color overall
        self._color = color  # this i very useful when I need color to be changed overall 
    
    def get_color(self):  # This method gets the color
        return self._color  
            

def main():
    donald = Duck(color='orange')
    
    print(donald.get_color())
    donald.feathers()
    
    

if __name__ == "__main__": main()
