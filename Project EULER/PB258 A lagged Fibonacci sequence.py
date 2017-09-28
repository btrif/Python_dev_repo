#  Created by Bogdan Trif on 21-09-2017 , 2:17 PM.

# © o(^_^)o  Solved by Bogdan Trif  @
#The  Euler Project  https://projecteuler.net
'''
                A lagged Fibonacci sequence     -           Problem 258

A sequence is defined as:

g_k = 1, for 0 ≤ k ≤ 1999
g_k = g_k-2000 + g_k-1999, for k ≥ 2000.

Find g_k mod 20092010 for k = 10^18.


'''
import time, zzz


def zero_matrix(m, n):
    return [[0 for row in range(n)] for col in range(m)]

def matrix_mul(matrix1, matrix2, mod=None):
    if len(matrix1[0]) != len(matrix2[0]):
        raise Exception("Matrices dimension must be m*n and n*p to multiple")
    new_matrix = zero_matrix(len(matrix1), len(matrix2[0]))
    # multiply if dimension is correct
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                new_matrix[i][j] += matrix1[i][k]*matrix2[k][j]
            # optional modulus
            if mod is not None:
                new_matrix[i][j] = new_matrix[i][j] % mod

    return new_matrix


def fibonacci_matrix(n, mod=None):
    """
    Calculate large fib value using matrix form in log(n) steps
    """
    from functools import reduce
    def matrix_mul2(m1, m2):
        return matrix_mul(m1, m2, mod)

    b = [int(d) for d in bin(n)[2:]]
    b.reverse()
    p = zip(b, range(len(b)))
    m = { 0: [[1,1],[1,0]] }
    for i in range(1, len(b)):
        m[i] = matrix_mul2(m[i-1], m[i-1])
    ms = [m[y] for (x,y) in p if x == 1]
    return reduce(matrix_mul2, ms)[0][1]

print( len(str(fibonacci_matrix(10**5) )) )


print('\n--------------------------TESTS------------------------------')
t1  = time.time()


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')

print('\n================  My FIRST SOLUTION,   ===============\n')
t1  = time.time()

mod = 20092010
nr = 10**18-1997
F = fibonacci_matrix(nr, 10**3000 )
print( '\nAnswer : \t  ', F , '\n', F%mod , fibonacci_matrix(nr, mod ) )

@2017-09-25,  - Nici asta nu iese ! Cred ca e mai complicat !
https://discuss.codechef.com/questions/49614/linear-recurrence-using-cayley-hamilton-theorem

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')


# print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
# print('\n--------------------------SOLUTION 1,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 2,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 3,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 4,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 5,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 6,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 7,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 8,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 9,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 10,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 11,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 12,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')




