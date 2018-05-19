
# Script made by Bogdan Trif
# Calling a function with more arguments
# first argument x when the function is called has no meaning
# But this is a way to call the function with any range values that you want
# x value needs to be passed because x stands in the for loop and x is the temporary value
# actually the value of the x value does not matter when you call the function 



def f(x, y, z, w):
    for x in range(y, z, w):
# Note use of 'end' on previous line
        print(repr(x).rjust(2), repr(x * x).rjust(3), end=' ')
        print(repr(x * x * x).rjust(4), repr(x ** 4).rjust(5))
        

f(x=3555, y=9, z=24, w=2)


