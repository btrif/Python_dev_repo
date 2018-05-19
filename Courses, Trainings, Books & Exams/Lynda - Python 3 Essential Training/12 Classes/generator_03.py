#!/usr/bin/python3
# classes.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

class inclusive_range:
    def __init__(self):  # special method in python, the CONSTRUCTOR !!
        pass
    
    def __iter__(self):  # this method makes the object an iterable object !!
        pass

def main():
#    o = range(4,25, 4)
#    o = range(4,25, 1)
#    o = range(2,45, 1)
    o = range(4, 35)
    for i in o: print(i, end=' ')

if __name__ == "__main__": main()
