#!/usr/bin/python

def f():
    for x in range(10):
        # Note use of 'end' on previous line
        print(repr(x).rjust(2), repr(x * x).rjust(3), end=' ')
        print(repr(x * x * x).rjust(4), repr(x ** 4).rjust(5))

f()


def g():  # Loop with range going backwards
    print('\n A loop going backwards :')
    for t in range(11, 0, -1):
        if t > 1:
            print(t, end=',  ')
        if t == 1:
            print(t, end='.')

g()
