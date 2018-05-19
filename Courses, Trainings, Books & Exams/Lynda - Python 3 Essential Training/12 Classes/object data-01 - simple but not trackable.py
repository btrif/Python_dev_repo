#!/usr/bin/python3
# classes.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

class Duck:
    def __init__(self, color='white'):
        self._color = color 
        '''
         # I use _color because I need to remind me that this attribute will be used locally but will be not
        # used directly. Otherwise said, will not access this variable from outside this object
         # All the access will be done from methods within the object 
        '''
    
    def quack(self):
        print('Quaaack!')

    def walk(self):
        print('Walks like a duck.')

def main():
    donald = Duck()
    print(donald._color)
    donald._color = 'blue'
    print(donald._color)
    

if __name__ == "__main__": main()
