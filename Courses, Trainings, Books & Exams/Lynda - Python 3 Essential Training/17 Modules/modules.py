#!/usr/bin/python3
# modules.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

import sys


def main():
    print('Python version {}.{}.{}'.format(*sys.version_info))
    print(sys.platform)
    
    import os
    print(os.name)
    print(os.getenv('PATH'))
    print(os.getcwd())
    print(os.urandom(26))
    print('----'*25)
    
    import urllib.request
    page = urllib.request.urlopen('http://bw.org' )
#    for line in page: print(str(line, encoding = 'utf_8'), end= '')
    
    import random
    print(random.randint(1, 1000))
    x = list(range(34))
    print(x)
    random.shuffle(x)
    print(x)
    random.shuffle(x)
    print(x)
    random.shuffle(x)
    print(x)
    
    

if __name__ == "__main__": main()
