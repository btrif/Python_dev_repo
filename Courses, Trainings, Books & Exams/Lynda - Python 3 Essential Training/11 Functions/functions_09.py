#!/usr/bin/python3
# functions.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    print(testfunc())

def testfunc():
#    return('This is a test function')   # the return keyword is the way the values are returned
#    return 42        # we can return a number
    return range(12)             # return an object (example:range)

if __name__ == "__main__": main()
