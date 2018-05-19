#!/usr/bin/python3
# variables.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    n = 42
    s = 'This is a {} string!'.format(n)   # format is a method of the string object
                                # 
    print(s)
    
    
    
    # in Python2 (old way)
    s2 = 'This is a %s string!' %n      # in Python 2 
    print(s2)
    
if __name__ == "__main__": main()
