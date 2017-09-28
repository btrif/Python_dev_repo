#  Created by Bogdan Trif on 28-09-2017 , 8:59 PM.

# © o(^_^)o  Solved by Bogdan Trif  @
#The  Euler Project  https://projecteuler.net
'''
                Fibonacci Words         -           Problem 230

For any two strings of digits, A and B, we define FA,B to be the sequence (A,B,AB,BAB,ABBAB,...)
in which each term is the concatenation of the previous two.

Further, we define DA,B(n) to be the nth digit in the first term of FA,B that contains at least n digits.

Example:

Let A=1415926535, B=8979323846. We wish to find DA,B(35), say.

The first few terms of FA,B are:
1415926535
8979323846
14159265358979323846
897932384614159265358979323846
14159265358979323846897932384614159265358979323846

Then DA,B(35) is the 35th digit in the fifth term, which is 9.

Now we use for A the first 100 digits of π behind the decimal point:

14159265358979323846264338327950288419716939937510
58209749445923078164062862089986280348253421170679

and for B the next hundred digits:

82148086513282306647093844609550582231725359408128
48111745028410270193852110555964462294895493038196 .

Find ∑n = 0,1,...,17   10n× DA,B((127+19n)×7n) .

'''
import time, zzz

from math import floor, sqrt, log

A='1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679'
B ='8214808651328230664709384460955058223172535940812848111745028410270193852110555964462294895493038196'

print(len(A), len(B) ,'\n')

def Fibonacci(n):
    iter = 0 		# Number of terms
    #	ORIGINAL Fibonacci with iteration, while loop
    FIB = [0, 1]
    a, b = 0, 1
    while iter < n:
        iter +=1
        a  , b = b, a + b
        FIB.append(b)
    return FIB

# Construct the Fibonacci Dictionary :
F = Fibonacci(100)
print(F[100])
print(' Fib(10) = ' ,F[10])
print(F ,'\n')

# for n in range(2, 100 ):
#     print('n=',n,'     Fib(n) = ', Fibonacci(n))

D = lambda n : ((127+19*n)*7**n)

# n(F) = Floor[ Log(F Sqrt(5))/Log(Phi) + 1/2]
# phi = (1+5**(1/2))/2
# phi_ = (1-5**(1/2))/2

def inverse_fib( F ):
    Phi = (1+5**(1/2))/2

    return floor(   (log(F, sqrt(5))/log(Phi) ) +1/2  )

print('inverse fibonacci : \t' , inverse_fib(28) )

for n in range(17+1) :
    d = D(n)
    print(str(n)+'       D('+str(n)+')    =' , d ,'     ' , d//100  )

print('\n--------------------------TESTS------------------------------')
t1  = time.time()

# @2017-09-28, 21:23 - the question reduces what letter is at the desired position : either A or B.
# The difficulty of the problem resides in this fact, determining the letter.
# After we have the letter we do a modulo and we determine the digit
# ==> RECURSION
# actually the thing is to decompose in Fibonacci numbers recursively ( backtracking )
# and find precisely the letter by going backwards !


def fib_words(n):
    f1, f2 = 'A' , 'B'
    for i in range( 3, n+1 ) :
        f3 = f1+f2
        f1 = f2
        f2 = f3
        print( f3 , str(i) +'.    len= ' , len(f3)  )
    return f3

fib_words(10)


t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')

print('\n================  My FIRST SOLUTION,   ===============\n')
# t1  = time.time()





# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')


# print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
# print('\n--------------------------SOLUTION 1,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 2,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 3,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 4,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 5,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 6,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 7,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 8,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 9,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 10,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 11,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 12,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')




