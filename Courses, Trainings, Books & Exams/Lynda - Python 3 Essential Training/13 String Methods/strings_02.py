#!/usr/bin/python3
# strings.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    a, b = 5 ,42
    print (a,b)
    print('this is {}, that is {}'.format(a ,b))
    s = 'this is {}, that is {}'.format(a ,b)
    print(id(s))
    print(s.format(a, b))
    print('this is {1}, that is {0}'.format(a ,b))
    print('this is {bob}, that is a girl {Frida}'.format(bob = a , Frida = b))
    d = dict( bob = a, Frida = b)
    print('this guy is {bob}, that girl is {Frida}'.format(**d))
    
    
    
if __name__ == "__main__": main()
