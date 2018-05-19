#!/usr/bin/python3
# classes.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

class Duck:
    def __init__(self, value):  # The init is a CONSTRUCTOR - a special METHOD, used to set up data, open databases
        self.abc = value  # Creates a local variable which is an attribute of the donald object (in this case)
                            # then I can use that value in the methods
    '''
Encapsulation:
When the donald object calls a method that self variable gets passed and that;s a
reference to the object. All the things that are attached to the object, its other
methods, its attributes, its data, is all carried there.

self is passed implicitly by the DOT sign
    '''    
    def quack(self):
        print('Quaaack!', self.abc)

    def walk(self):
        print('Walks like a duck.', self.abc)

def main():
    donald = Duck(247)
    frank = Duck(53)
    donald.quack()
    donald.walk()
    frank.quack()
    frank.walk()

if __name__ == "__main__": main()
