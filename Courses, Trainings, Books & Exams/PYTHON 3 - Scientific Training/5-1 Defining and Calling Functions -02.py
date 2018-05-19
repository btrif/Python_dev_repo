
# Script made by bogdan Trif
# Calling a function with two arguments
# first argument when the function is called has no meaning
# But this is a way to call the function with any range y that you want



def f(x, y):
    for x in range(3, y):
# Note use of 'end' on previous line
        print(repr(x).rjust(2), repr(x * x).rjust(3), end=' ')
        print(repr(x * x * x).rjust(4), repr(x ** 4).rjust(5))
        

f(x=3, y=9)

'''
#This one works too

def f(x, y):
    for x in range(y):
# Note use of 'end' on previous line
        print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
        print(repr(x*x*x).rjust(4), repr(x**4).rjust(5))
        

f(3,9)
'''
