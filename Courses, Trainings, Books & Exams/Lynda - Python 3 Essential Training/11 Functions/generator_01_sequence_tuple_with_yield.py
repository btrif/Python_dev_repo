#!/usr/bin/python3
#     A generator function is function that return an iterator object.
# So this is how you create functionality that can be used in a for loop or any
# place an iterator is allowable in Python

def main():
    print("This is the functions.py file.")
    for i in inclusive_range(2, 125, 4):            
        print(i, end =' ')

def inclusive_range(*args):             # we make an inclusive range function
    numargs = len(args)
    if numargs < 1: raise TypeError('requires at least one argument')
    elif numargs == 1:
        start = 0
        step = 1
        stop = args[0]
    elif numargs == 2:
        (start, stop) = args
        step = 1
    elif numargs == 3:
        (start, stop, step) = args
    else: raise TypeError('inclusive_range expected at most 3 arguments, got {}'.format(numargs))
    i = start
    while i <= stop:
        yield i         # yield does it return 'i' but because we are using yield instead of return
        i += step                # the next time the function is called execution will continue right after
                        # the yield statement. It will get incremented with step.
        
    
 # Difference between yield and return :
 # as the function gets called over and over again, each time execution begins right after
 # the yield and continues as if the function were running continually
    

if __name__ == "__main__": main()
