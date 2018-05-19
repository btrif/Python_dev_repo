#!/usr/bin/python3
# variables.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    x = (1,2,3,4,5)
    y = 'Bogdanel'
    for (i) in (x,y):   
        print(i )        # this is a tuple, an immutable object, can't insert, can't append, can't del

if __name__ == "__main__": main()
