import time
import gmpy2
import numpy as np
from itertools import count
import eulerlib
from decimal import *
getcontext().prec = 100


def Fibonacci(n):
    iter = 0 		# Number of terms
    #	ORIGINAL Fibonacci with iteration, while loop
    a, b = 0, 1
    while iter < n:
        iter +=1
        a  , b = b, a + b
    return a


def Fibonacci_Binet(n_th) :
    ''':Description:    Returns the Fibonacci corresponding to the number  and uses the Binet Formula.
        http://mathworld.wolfram.com/BinetsFibonacciNumberFormula.html
        :param n_th: F_nth Fibonacci in sequence
        :return: str, first 9 digits of the Fibonacci number
    '''
    phi = Decimal((5**(1/2)+1)/2)
    phi_ = Decimal((1- 5**(1/2))/2)
    # phi = (1+5**(1/2))/2
    # phi_ = (1-5**(1/2))/2
    # a = ( ( phi**n_th-phi_**n_th ) / ( phi - phi_) )%(10**9)
    a = str(((phi**n_th)-(phi_)**n_th)/( phi - (phi_)))[0:10].replace( '.' , '')
    # b =   ( (( 1 + np.sqrt(5))/2)**n_th - ((1 - np.sqrt(5))/2)**n_th  ) /np.sqrt(5)
    return str(a)



print('\n--------------------- Fibonacci Matrix --------------------')

t1  = time.time()


class FIBONACCI():
    # def __init__(self):       # We don't initialize with values

    def zero_matrix( self, m, n):
        return [[0 for row in range(n)] for col in range(m)]

    def matrix_mul(self,  matrix1, matrix2, mod=None):
        if len(matrix1[0]) != len(matrix2[0]):
            raise Exception("Matrices dimension must be m*n and n*p to multiple")

        new_matrix = self.zero_matrix(len(matrix1), len(matrix2[0]))
        # multiply if dimension is correct
        for i in range(len(matrix1)):
            for j in range(len(matrix2[0])):
                for k in range(len(matrix2)):
                    new_matrix[i][j] += matrix1[i][k]*matrix2[k][j]
                # optional modulus
                if mod is not None:
                    new_matrix[i][j] = new_matrix[i][j] % mod

        return new_matrix


    def fibonacci_matrix(self, n, mod=None):
        """
        Calculate large fib value using matrix form in log(n) steps
        """
        from functools import reduce
        def matrix_mul2(m1, m2):
            return self.matrix_mul(m1, m2, mod )

        b = [int(d) for d in bin(n)[2:]]
        b.reverse()
        p = zip(b, range(len(b)))
        m = { 0: [[1,1],[1,0]] }
        for i in range(1, len(b)):
            m[i] = matrix_mul2(m[i-1], m[i-1])
        ms = [m[y] for (x,y) in p if x == 1]
        return reduce(matrix_mul2, ms)[0][1]

nr = 100000000000031
mod = 10**20
print( FIBONACCI().fibonacci_matrix( nr , mod)  )


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


# https://en.wikipedia.org/wiki/Fibonacci_number#Other_identities

print('\n--------------------- Fibonacci Matrix 2 , MODULO 1234567891011 --------------------')

MOD = 1234567891011

def matrix_mul_mod(a, b, mod = MOD):
    return [[sum((i*j) for i,j in zip(r, c))%mod for c in zip(*b)] for r in a]

# def fib_mod(n, mod = MOD):
def fib_mod(n):

    b = bin(n)[2:][::-1]
    Q = ((1, 1), (1, 0))
    fib = ((1, 0), (0, 0))
    for s in b:
        if s == '1':
            fib = matrix_mul_mod(fib, Q, mod)
        Q = matrix_mul_mod(Q, Q, mod)
    return fib[0][1]

print( fib_mod(10**4) )
