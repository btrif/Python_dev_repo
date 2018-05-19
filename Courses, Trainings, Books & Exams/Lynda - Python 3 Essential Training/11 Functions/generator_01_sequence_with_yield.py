#!/usr/bin/python3
#     A generator function is function that return an iterator object.
# So this is how you create functionality that can be used in a for loop or any
# place an iterator is allowable in Python

def main():
    print("This is the functions.py file.")
    for i in inclusive_range(0 ,25, 1):
        print(i, end =' ')

def inclusive_range(start, stop, step):
    i = start
    while i <= stop:
        yield i         # yield does it return 'i' but because we are using yield instead of return
        i += step                # the next time the function is called execution will continue right after
                        # the yield statement. It will get incremented with step.
        
    
 # Difference between yield and return :
 # as the function gets called over and over again, each time execution begins right after
 # the yield and continues as if the function were running continually
    

if __name__ == "__main__": main()
