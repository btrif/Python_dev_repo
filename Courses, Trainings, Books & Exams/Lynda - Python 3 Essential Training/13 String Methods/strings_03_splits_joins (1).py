#!/usr/bin/python3
# strings.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    
    s = 'this is a string of words'
    print(s.split())
    words = s.split()
    print(s.split('i'))         #split about the 'i' character
    for c in words:
        print(c)
    
    new = ':'.join(words)       #join the words already split words
    print(new)
    new2 = '_'.join(words)
    print(new2)
    
    
    
if __name__ == "__main__": main()
