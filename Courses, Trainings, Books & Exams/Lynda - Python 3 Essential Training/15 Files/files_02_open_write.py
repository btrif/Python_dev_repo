#!/usr/bin/python3
# files.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    infile = open('lines.txt','r')
    outfile = open('new.txt', 'w')
    
    '''
    it could be : 
    f = open('lines.txt', 'r')
    r -read, w -write, a -append
    r+ = read and write in the same file handle object
    t - text file mode
    b - for binary mode
    
    '''
    
    for line in infile:
        print(line, file = outfile, end='')
    print('Done.')

if __name__ == "__main__": main()
