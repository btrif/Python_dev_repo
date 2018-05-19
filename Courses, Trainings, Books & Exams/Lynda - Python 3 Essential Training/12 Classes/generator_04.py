#!/usr/bin/python3
# classes.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

class inclusive_range:
    def __init__(self, *args):  # special method in python, the CONSTRUCTOR !!
        numargs = len(args)
        if numargs < 1 : raise TypeError('requires at least one arguemnt')
        elif numargs == 1:
            self.stop = args[0]
            self.start = 0
            self.step = 1
        elif numargs == 2:
            (self.start, self.stop) = args
            self.step = 1
        elif numargs == 3:
            (self.start, self.stop, self.step) = args
        else: raise TypeError('expected at most 3 arguments, got {}'.format(numargs))
    
    def __iter__(self):  # this method makes the object an iterable object !!
        i = self.start
        while i <= self.stop:
            yield i
            i += self.step

def main():
#    o = range(4,25, 4)
#    o = range(4,25, 1)
#    o = range(2,45, 3)
    o = inclusive_range(30, 130, 4)
    for i in o: print(i, end=' ')

if __name__ == "__main__": main()
