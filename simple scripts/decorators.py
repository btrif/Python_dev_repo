print('----------------------   Decorators   ----------------------' )


# ==== Introduction
#
# decorators Decorators belong most probably to the most beautiful and most powerful design possibilities in Python,
# but at the same time the concept is considered by many as complicated to get into.
# To be precise, the usage of decorates is very easy, but writing decorators can be complicated,
# especially if you are not experienced with decorators and some functional programming concepts.
#
# Even though it is the same underlying concept, we have two different kinds of decorators in Python:
# Function decorators
# Class decorators
# A decorator in Python is any callable Python object that is used to modify a function or a class.
# A reference to a function "func" or a class "C" is passed to a decorator and the decorator returns a modified function or class.
# The modified functions or classes usually contain calls to the original function "func" or class "C".
#
# You may also consult our chapter on memoization with decorators.
#
# If you like the image on the right side of this page and if you are also interested in image processing with Python,
#     Numpy, Scipy and Matplotlib, you will definitely like our chapter on Image Processing Techniques,
#     it explains the whole process of the making-of of our decorator and at sign picture!

print('\n---------------  First Steps to Decorators --------------------')
# ==== First Steps to Decorators
# We know from our various Python training classes that there are some sticking points in the definitions of decorators,
# where many beginners get stuck.
#
# Therefore, we wil will introduce decorators by repeating some important aspects of functions.
# First you have to know or remember that function names are references to functions
# and that we can assign multiple names to the same function:

def succ(x):
    return x + 1

successor = succ
print(successor(10) )
print(succ(10) )

# This means that we have two names, i.e. "succ" and "successor" for the same function.
# The next important fact is that we can delete either "succ" or "successor" without deleting the function itself.
del succ
print(successor(10) )

# ====Functions inside Functions
print('\n---------------  Functions inside Functions --------------------')
# The concept of having or defining functions inside of a function is completely new to C or C++ programmers:
def f():
    def g():
        print("Hi, it's me 'g'")
        print("Thanks for calling me")

    print("This is the function 'f'")
    print("I am calling 'g' now:")
    g()

f()

print('\n"proper" return statements')
# Another example using "proper" return statements in the functions:
def temperature(t):
    def celsius2fahrenheit(x):
        return 9 * x / 5 + 32

    result = "It's " + str(celsius2fahrenheit(t)) + " degrees!"
    return result

print(temperature(20))


# ==== Functions as Parameters
print('\n---------------  Functions as Parameters --------------------')

# If you solely look at the previous examples, this doesn't seem to be very usefull.
# It gets useful in combination with two further powerful possibilities of Python functions.
# Due to the fact that every parameter of a function is a reference to an object and functions are objects as well,
# we can pass functions - or better "references to functions" - as parameters to a function.
# We will demonstrate this in the next simple example:

def g():
    print("Hi, it's me 'g'")
    print("Thanks for calling me")

def f(func):
    print("Hi, it's me 'f'")
    print("I will call 'func' now")
    func()

f(g)

print()
# You may not be satisfied with the output. 'f' should write that it calls 'g' and not 'func'.
# Of course, we need to know what the 'real' name of func is.
# For this purpos, we can use the attribute __name__, as it contains this name:

def g():
    print("Hi, it's me 'g'")
    print("Thanks for calling me")

def f(func):
    print("Hi, it's me 'f'")
    print("I will call 'func' now")
    func()
    print("func's real name is " + func.__name__)

f(g)

print('\n -----------   Another example: -------------- ')

import math

def foo(func):
    print("The function " + func.__name__ + " was passed to foo")
    res = 0
    for x in [1, 2, 2.5]:
        res += func(x)
    return res

print(foo(math.sin))
print(foo(math.cos))


# ======Functions returning Functions
print('\n---------------  Functions returning Functions--------------------')
# The output of a function is also a reference to an object. Therefore functions can return references to function objects.

def f(x):
    def g(y):
        return y + x + 3
    return g

nf1 = f(1)
nf2 = f(3)

print( nf1(1) )
print( nf2(1) )


# We will implement a polynomial "factory" function now. We will start with writing a version which can create polynomials of degree 2.
print('\n------------ polynomial "factory" function  --------------')


# The Python implementation as a polynomial factory function can be written like this:
# p(x) = a*x**2 + b*x + c


def polynomial_creator(a, b, c):
    def polynomial(x):
        return a * x**2 + b * x + c
    return polynomial

p1 = polynomial_creator(2, 3, -1)
p2 = polynomial_creator(-1, 2, 1)

for x in range(-2, 2 ):
    print('x=',x, '      p1(x)=',p1(x), '        p2(x)=',p2(x) )


print('\n------------ polynomials of arbitrary degree  --------------')

# We can generalize our factory function so that it can work for polynomials of arbitrary degree:

# Σ {k=0, n} a_k * x**k = a_n*x**k + a_(n-1)*x**(n-1) +... + a_2*x**2 + a_1*x + a_0

def polynomial_creator(*coefficients):
    def polynomial(x):
        res = 0
        degree = len(coefficients) - 1
        for index, coeff in enumerate(coefficients):
            res += coeff * x**(degree - index)
        return res
    return polynomial

p1 = polynomial_creator(4)
p2 = polynomial_creator(2, 4)
p3 = polynomial_creator(2, 3, -1, 8, 1)
p4 = polynomial_creator(-1, 2, 1)


for x in range(-2, 2, 1):
    print(x, p1(x), p2(x), p3(x), p4(x))


# ===== A Simple Decorator
print('\n------------ A Simple Decorator  --------------')
# Now we have everything ready to define our first simple decorator:

def our_decorator(func):
    def function_wrapper(x):
        print("Before calling " + func.__name__)
        func(x)
        print("After calling " + func.__name__)
    return function_wrapper

def foo(x):
    print("Hi, foo has been called with " + str(x))

print("We call foo before decoration:")
foo("Hi")

print("We now decorate foo with f:")
foo = our_decorator(foo)

print("We call foo after decoration:")
foo(42)











