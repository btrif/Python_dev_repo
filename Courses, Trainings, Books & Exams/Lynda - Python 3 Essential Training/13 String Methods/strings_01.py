#!/usr/bin/python3
# strings.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    s = '   this is a string   \n'
    print(s.capitalize())
    print(s.title())
    print(s.upper())
    print(s.swapcase())     #swapcase
    print(s.find('is'))
    print(s.replace('this', 'I remember you THIS'))         #replace
    print(s.strip())        #removes any whitespace from the beginning and the end
                            # useful for removing new lines, but also removes the leading space
    print(s.rstrip())        #removes any whitespace from  the end of the string
    print(s.isalnum())      # checks only alphanumeric characters in it
    print(s.isalpha())      # checks for alpha characters a-z,A-Z
    print(s.isdigit())      # checks for digits
    print(s.isprintable())  # if the string is printable
    print(len(s))
    print('This is a string {}'.format(42))
    print(id(s))

if __name__ == "__main__": main()
