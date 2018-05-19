#!/usr/bin/python3
# variables.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    x = [1,2,3]
    x.append(5)
    x.insert(0, 57)
    x.insert(3,23)
    print(type(x),x)        # this is a list, an mutable object, insert, append, del work

if __name__ == "__main__": main()
