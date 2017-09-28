def myfunc(x, p=2, debug=False):
    if debug:
        print("evaluating myfunc for x = " + str(x) + " using exponent p = " + str(p))
    return x**p

print(myfunc(x= 11, p=3, debug=True))


def addnumbers(a,b):
    result = a + b
    return print(result)

def multiply():
    a=float(input("Input a: "))
    b=float(input("Input b: "))
    result = a * b
    return print(result)

def main():
    print('\nHere we are in the DEF MAIN function calls :   ')
    addnumbers(13,4)
    multiply()


if __name__ == "__main__":  main()


def square(x=1):
    '''    x: int or float.    '''
    # Your code here
    return x**2


def fourthPower(x=3):
   '''
   x: int or float.
   '''
   return square(square(x))

print(fourthPower(3))

##############################

def odd(x=1):
    '''
    x: int or float;     returns: True if x is odd, False otherwise
    '''
    return (x % 2 == 1)
odd(3)

def is_even( i=1):
    """
    Input: i, a positive int;    Returns True if iis even, otherwise False
    """
    print ("hi")
    return (i % 2 == 0)
is_even(3)

print('-----'*25)
#######################################
# ITERATION   ALGORITHM
print('\nIterative Implementation of the multiplication of two numbers : ')
def mult_iter(a=3, b=81):
    result = 0
    while b > 0:
        result += a
        b -= 1
    return print(result)
mult_iter(11,11)

# RECURSION  FUNCTION ALGORITHM
print('\nRecursive Function Implementation of the multiplication of two numbers : ')
def mult_recursive(a=3, b=9):
    if b == 1:
        return a
    else :                                                              #  The Recursive Step
        return (a + mult_recursive(a, b-1))             #

print(mult_recursive(22,89))

print('Power iteration using while')
def iterPower(base, exp):
    '''
    base: int or float.   exp: int >= 0
    returns: int or float, base^exp
    '''
    result = 1
    while exp > 0:
        result *=base
        exp -= 1
    return result

print(iterPower(3,5))

# RECURSION FUNCTION FACTORIAL :
print('\n----------------     Recursive Function Implementation for Factorial : ---------------')
def factorial(n=10):
    if n == 1:
        return 1
    else:
        return (n*factorial(n-1))

print(factorial(12))

# RECURSION FUNCTION for base**POWER :
print('----------------  RECURSION FUNCTION for base**power  :       --------------------')
def recursionPower(base=3, exp=6):
    '''
    base: int or float.    exp: int >= 0
    returns: int or float, base^exp
    '''
    if exp == 1 : return base
    else :
        return (base * recursionPower(base, exp-1))

print(recursionPower(3,5))


#####################################

def gcdIter(a, b):          # The Greatest Common Divisor , CMMDC, c.m.m.d.c.
    '''
    a, b: positive integers
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if b%a == 0 : return a
    else:
        for i in reversed(range(a)):
            if (a%i == 0 and b%i == 0):
                return i
print(gcdIter(1445468, 300173))

# Recursion for the Greatest Common Divisor, CMMDC
def gcdRecur(a, b):              # Recursive CMMDC
    if b == 0:
       return a
    else:
       return gcdRecur(b, a % b)
gcdRecur(144,10)

######################################
print('\n ----------- Is String Palindrom function------------------')
def isPalindrome(s):
    def toChars(s):
        s= s.lower()
        ans= ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans= ans+ c
        return ans
    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1])
    return isPal(toChars(s))

print(isPalindrome('abbcddcbba'))

#################################################

print('\n -------------------     PASCAL s   TRIANGLE    ---------------------')

def pascal(n):
    row = [1]
    for x in range(n):
        row = [l + r for l, r in zip(row + [0], [0] + row)]
    # print row
    return row

print (pascal(4*2))

#################################################

print('\n----------------------- Function which returns another Function ------------------------')

import math
def make_cylinder_volume_func(r):
    def volume(h):
        return math.pi * r * r * h
    return volume

volume_radius_10 = make_cylinder_volume_func(10)
print(volume_radius_10(5))

L=[1,2,7,3,4]
def general_poly(L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """
    def number(x):
        S=0
        for i in range(len(L)):
            S += L[i]* x **(len(L)-i-1)
        return S
    return number

print(general_poly(L)(10))



#######################################

