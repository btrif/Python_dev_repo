#  Created by Bogdan Trif on 27-09-2017 , 9:22 AM.

# Write a decorator which decorates simple function :

# A simple function :

def say_hello(name):
    print('Hello')
    return 'Hello'

# We see that the function works properly without decorator
say_hello('')

print('\n### METHOD 1 - calling the function without the decorator  syntax')


# Now we make a decorator which adds the name after the output of the function
def deco( func ) :
    def wrapper( name ) :
        print( str( func(name) ) + ' ' + name )
        return func(name) + ' ' + name
    return wrapper

deco1 = deco(say_hello)
deco1('Bogdan')


print('\n### METHOD 2 - THE DECORATOR WAY  (@deco) : ')

@deco
def say_hello(name):
    print('Hello')
    return 'Hello'

say_hello('Bogdan')



print('\n ----------    ### SECOND EXAMPLE  -   A very basic decorator :    ----------------')

### SECOND EXAMPLE  -   A very basic decorator :

def decorator(func):
    def wrapper(ceva):
        func(ceva)
        print("and this is supposed to be funny ?")

    return wrapper

@decorator
def say_something(acel_ceva):
    print("just another brick in the wall, " + str(acel_ceva) )

say_something("Hugo")



print('\n--------------           two decorator functions -----------------------')
# https://wiki.python.org/moin/FunctionWrappers
# http://wiki.c2.com/?FunctionWrapper
'''
FunctionWrapper is a design pattern used when dealing with relatively complicated functions. 
The wrapper function typically performs some prologue and epilogue tasks like

allocating and disposing resources
checking pre- and post-conditions
caching / recycling a result of a slow computation
but otherwise it should be fully compatible with the wrapped function, so it can be used instead of it. 
(This is related to the DecoratorPattern.)

As of Python 2.1 and the introduction of nested scopes, wrapping a function is easy:
'''

def wrap(pre, post):
    def decorate(func):
        def call(*args, **kwargs):
            pre(func, *args, **kwargs)
            result = func(*args, **kwargs)
            post(func, *args, **kwargs)
            return result
        return call
    return decorate



def trace_in(func, *args, **kwargs):
    print("Entering function",  func.__name__)

def trace_out(func, *args, **kwargs):
    print( "Leaving function", func.__name__)

@wrap(trace_in, trace_out)
def calc(x, y):
    print(' x + y = ' , x+y )
    return x + y


# Calling the function call :
calc(3, 4)




