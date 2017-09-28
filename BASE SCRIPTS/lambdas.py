'''
We can assign a variable to a lambda expression and then invoke the lambda with parentheses.
We call it like any other function. To get the value 6 in this program, we invoke x. We then print the value it returns (stored in y).
So:
Lambdas can be passed to other methods. They can be stored in variables. And those variables can be called like methods.
'''

#Python program that uses lambda, no arguments
# Assign variable to lambda expression.
x = lambda: sum(range(1, 10))

# Invoke lambda expression.
y = x()
print(y)
##########################################################
'''
None
None
Many statements in Python,
like print(),
return None. This is a valid return value for a lambda expression.
 We can specify a lambda with side effects, and a None return value, like print (which writes to the screen).

None
Print
'''
#Python program that uses None, lambda

# This lambda has a side effect.
# ... Print returns None.
p = lambda x: print(x)

p("Hello")
p("World")

#######################################################
'''
Nested
Expression
A lambda can call another lambda. This can help simplify complex computations—we can assign
 names to the parts of the computation. The order the lambdas appear in the file does not matter.

With nested lambdas:
Recursion can occur. This may result in a RuntimeError: maximum recursion depth exceeded error.
'''
#Python program that uses lambda in lambda
add_two = lambda n: n + 2
multiply_add_two = lambda n: add_two(n * 2) # Call lambda in lambda.

print(multiply_add_two(3))
print(multiply_add_two(5))
########################################################

'''
Discussion
Concept
The lambda syntax in Python has serious limitations. But these limitations make sense.
You cannot have multiple statements in a lambda expression. So if you want many statements, please instead use a def.

Def
Conceptually:
A lambda is an expression of behavior. It is a small function meant to do a well-defined task.

Thus:
We have no need to write an entire program in lambda syntax. Lambda supplements, but does not replace, the def method syntax.

Tip:
The word "lambda" is simply the name of a letter in the Greek alphabet. It is similar to the letter "L."
'''
######################################################
'''
Performance
Performance
In some languages lambdas cause performance loss. They slow down programs.
 In the Python documentation I found that lambdas should not cause this problem. They behave just like def methods.

The expression lambda yields a function object. The unnamed object behaves like a function object defined with [def].

Expressions: python.org
But in this program, I test this statement with a simple benchmark.
The square() method above is rewritten in the def method syntax. We then benchmark the methods against each other.

Def is a method keyword
First:
The program tests the performance of the def method call. We call it ten million times.

Second:
The program times the lambda expression method call. We also call it ten million times.

The results show that methods written with the def keyword and with the lambda keyword are close in performance.
In this test the difference was small. No performance loss is caused by lambda expressions.
'''

#Python program that times lambda expressions

import time

# Method.
def square1(n):
    return n ** 2

# Lambda method.
square2 = lambda n: n ** 2

print(time.time())

# Use def method.
i = 0
while i < 10000000:
    square1(1)
    i += 1

print(time.time())

# Use lambda method.
i = 0
while i < 10000000:
    square2(1)
    i += 1

print(time.time())

'''
Summary

Function objects provide many possibilities.
We specify these objects with the lambda syntax form.
 And when we pass them to other functions, we develop higher-order procedures.
 We construct functions that act on other functions.

Thus:
Functional programming is a style of programming. It is not based on the order of statements and loops.

Instead:
It is based on the input and output of functions. In it, recursive functions are often used.
'''


print('----------- Finding consecutive numbers in a list -----------------')

import itertools
from operator import itemgetter
# Find runs of consecutive numbers using groupby.  The key to the solution
# is differencing with a range so that consecutive numbers all appear in
# same group.
L = [ 1,  4,5,6, 10, 15,16,17,18, 22, 25,26,27,28]
for k, g in itertools.groupby( enumerate(L), lambda x_i: x_i[1]-x_i[0] ) :
    print (list(map(itemgetter(1), g)))
