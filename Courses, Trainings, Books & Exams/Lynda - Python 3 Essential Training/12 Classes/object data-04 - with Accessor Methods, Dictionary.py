#!/usr/bin/python3
# classes.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

class Duck:
    def __init__(self, **kwargs):
        self.variables = kwargs
        '''
 # I use _color because I need to remind me that this attribute will be used locally but will be not
 # used directly. Otherwise said, will not access this variable from outside this object
# All the access will be done from methods within the object  
        '''
    def quack(self):
        print('Quaaack!')

    def walk(self):
        print('Walks like a duck.')
    
#    def set_color(self, color):     # This method sets the color overall
#        self.variables['color'] = color         # this i very useful when I need color to be changed overall 
    
#    def get_color(self):            # This method gets the color
#        return self.variables.get('color', None)  

    def set_variable(self, k, v):
        self.variables[k] = v
        
    def get_variable(self, k):
        return self.variables.get(k, 'Orange')

def main():
    donald = Duck(feet=2)
    donald.set_variable('color', 'blue')
    print(donald.get_variable('color'))
    print(donald.get_variable('feet'))
    

if __name__ == "__main__": main()
