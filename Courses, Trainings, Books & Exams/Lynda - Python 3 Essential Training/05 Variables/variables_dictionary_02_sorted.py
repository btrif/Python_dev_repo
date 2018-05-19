#!/usr/bin/python3
# variables.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    d = dict(
        one = 1, two = 2, three = 3, four = 4, five = 5, nine = 9
             )
    d['seven'] = 7    #because dictionary are mutuable objects we can add other ojects, del, etc
    for k in sorted(d.keys()):
        print(k, d[k])

if __name__ == "__main__": main()

