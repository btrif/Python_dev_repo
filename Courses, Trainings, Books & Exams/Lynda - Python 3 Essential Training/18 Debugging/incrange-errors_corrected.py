#!/usr/bin/python3
# incrange-errors.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

class inclusive_range:
    def __init__(self, *args):
        numargs = len(args)
        if numargs < 1: raise TypeError('Requires at least one argument')
        elif numargs == 1:
            self.start = 0
            self.stop = args[0]
            self.step = 1
        elif numargs == 2:
            (self.start, self.stop) = args
            step = 1
        elif numargs == 3:
            (self.start, self.stop, self.step) = args
        else: raise TypeError('inclusiveRange expected at most 3 arguments, got {}'.format(numargs))

    def __iter__(self):
        i = self.start
        while i <= self.stop:
            yield i
            i += self.step

def main():
    
    o = inclusive_range(3, 25, 5)
 #   o = range(3,25, 4)
    print(inclusive_range, 'Start: ', o.start, 'Stop: ', o.stop, 'Step: ',o.step)
    
#    j = 4
    for j in o: print(j, end=' ')
  
    
#    for a in range(13, 34, 3): print (a, end=' ')
    

        
        
#    for a in range(113, 134, 3): print (a, end=' ') 
    
'''    
    while j < 20 : 
        print(j, end=' ')
        j += 1
'''
if __name__ == "__main__": main()
