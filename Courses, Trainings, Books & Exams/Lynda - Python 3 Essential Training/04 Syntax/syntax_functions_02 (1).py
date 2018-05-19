#!/usr/bin/python3
# syntax.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    func(3)
    func()
    func(11)
    
def func(a=7):
    for i in range(a, 20):
        print(i, end=' ')
    print()  
    
    
    
if __name__ == "__main__": main()
