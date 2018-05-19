#!/usr/bin/python3
# functions.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    testfunc(5, 6, 7, 8, 9, 10, one = 1, two =2, four = 43)

def testfunc(this, that, other, *args, **kwargs):         # keyword args ( they are actually dictionary)
    print('This is a test function', 
          this, that, other,'\n', args,'\n',
          kwargs['one'], kwargs['two'], kwargs['four'])

if __name__ == "__main__": main()
