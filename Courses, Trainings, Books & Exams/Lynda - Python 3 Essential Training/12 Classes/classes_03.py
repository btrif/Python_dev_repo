#!/usr/bin/python3
# classes.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

class Duck:
    def __init__(self, value):         # The CONSTRUCTOR method
        self._v = value             # !!! self._v is attached to the object donald, frank not to the CLASS
                                  # and is Called ENCAPSULATION in OOP
        
    def quack(self):
        print('Quaaack!', self._v)

    def walk(self):
        print('Walks like a duck.', self._v)

def main():
    donald = Duck(47)
    print('This the main Id Object : ',donald)
    donald.quack()
    donald.walk()
    frank = Duck(1555)
    frank.quack()
    frank.walk()

if __name__ == "__main__": main()
