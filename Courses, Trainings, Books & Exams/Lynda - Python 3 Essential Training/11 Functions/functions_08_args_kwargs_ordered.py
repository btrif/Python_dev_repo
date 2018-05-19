#!/usr/bin/python3
# This is how you pass named arguments to a function
# Commonly used for settings, flags
# this is how you combine them with the arbitrary tuple arguments and with your normal positional arguments

def main():
    testfunc(5, 6, 7, 8, 9, 10, one = 1, two =2, four = 4)

def testfunc(this, that, other, *args, **kwargs):         # keyword args ( they are actually dictionary)
    for n in args: print(n)

if __name__ == "__main__": main()
