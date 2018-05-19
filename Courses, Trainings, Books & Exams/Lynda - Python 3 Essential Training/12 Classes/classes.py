#!/usr/bin/python3
# classes.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

class Duck:
    def quack(self):
        print('Quaaack!')
        '''
Encapsulation:
When the donald object calls a method that self variable gets passed and that;s a
reference to the object. All the things that are attached to the object, its other
methods, its attributes, its data, is all carried there.

self is passed implicitly by the DOT sign
    '''

    def walk(self):
        print('Walks like a duck.')

def main():
    donald = Duck()
    donald.quack()
    donald.walk()

if __name__ == "__main__": main()
