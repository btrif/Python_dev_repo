#!/usr/bin/python3
# modules.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

import sys


def main():
    print('Python version {}.{}.{}'.format(*sys.version_info))
    print(sys.platform)
    
    import datetime
    now = datetime.datetime.now()
    print(now)
    print(now.year, now.month, now.hour, now.minute, now.second, now.microsecond)
    
    
    

if __name__ == "__main__": main()
