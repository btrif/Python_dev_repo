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

Find ∑n = 0,1,...,17   10^n× D_A,B   (( 127+19*n )×7^n) .

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

def binary_search(n, List):        # VERY FAST ALGORITHM
    ''':Description: Search for an element in the list and returns the index of it. If it not finds it returns
        the index of the element closest to its left, the smaller number.
    :param: **n**- integer, the number to find
                **List** - lst type, the list to search for
    :returns:   int, the index of the element
    '''
    left = 0
    right = len(List) -1

    while left <= right:
        midpoint = (left+right)//2
        if List[midpoint] == n: return midpoint
        elif List[midpoint] > n: right = midpoint-1
        else: left = midpoint+1
    if n > List[midpoint]: return midpoint
    else: return (midpoint-1)

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

print('inverse fibonacci : \t' , inverse_fib(5702887) )

for n in range(17+1) :
    d = D(n)
    print(str(n)+'       D('+str(n)+')    =' , d ,'     ' , divmod( d, 100)  )

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
    W = dict()
    for i in range( 3, n+1 ) :
        f3 = f1+f2 #+'.'
        f1 = f2
        f2 = f3
        print( f3 , '   ',str(i) +'.    len z= ' , F[i]  )
        W[len(f3)] = f3
    return W

W = fib_words(12)
# print('W: ', W,'\n\n' )

def brute_force_letter( n , F ) :       # @2018-05-25, 11:50        It works good !!!
    if n in F :
        # print('B')
        return 'B'
    else :
        i1 = binary_search(n, F) +1
        # print('i1', i1, '     F[i1] = ', F[i1] )
        # print( 'W[ '+str(F[i1])+'].index( '+str(n)+') = ', W[F[i1]][n-1]  )
        # print( '\nRESULT  n = '+str(n)+' = ', W[F[i1]][n-1]  )
        return W[F[i1]][n-1]

brute_force_letter(28, F)

# print('\n-------------------------------------------')

#
# def decompose_in_Fib_rec( n, F ) :
#     if n in F :
#         return 'B'
#     ind = binary_search(n, F)
#     print('ind = ', ind, '    Fib = ', F[ind])
#     if F[ind] <= 3 :
#
#         return F[n]
#
#     else :
#         r = n- F[ind]
#         print('ind : ', ind,'       Fib =  ', F[ind] , ' ,  remainder : ', r  )
#         return decompose_in_Fib_rec( n-F[ind] ,F )
#
#
# n = 23
# print('\ndecompose_in_Fib_rec ' + str(n)+' :  ' , decompose_in_Fib_rec(n, F)  )



# for i in range(20, 110) :
#     bf = brute_force_letter(i, F)
#     print(str(i) +'.    =  ', bf )


t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')

print('\n================  My FIRST SOLUTION,   ===============\n')
t1  = time.time()


def fib_in_two(n, F):
    i = binary_search(n, F)
    # print(F[i-2], F[i-1] )
    return F[i-2], F[i-1]

def inv_fib(n, F) :
    ind = binary_search(n, F)

    # print('ind = ', ind , '    F[ind] = ', F[ind] )

    X = F[:ind][::-1][:-2 ] #   Reverse Fibonacci & cut the last two elements [1, 0]
    X.append(2)
    # print('X : ', X , '     sum =', sum(X))
    return X




def find_fib_group(n) :
    X = inv_fib(n, F)
    print(X)

    i, S = 0, 0
    while S < n :
        S += X[i]
        print('S = ', S, ' ;      i =', i,' ;       X[i] =', X[i] ,'                  n=', n)
        i+=1
    r = X[i-1] - S + n
    print('\nfinal S = ', S ,'     X[i]=  ', X[i-1],'     r =', r )

    return X[i-1], r, S


find_fib_group(33)



def get_remainder(n, F ) :
    if n in F :
        print('direct res :  B  ' )
        return 'B'
    # if n == 0 : return 'B'

    Y = {1: 'B' , 2 : 'AB'  }

    x, r, up = find_fib_group(n)
    n = n - F[ binary_search(n, F) ]
    a = fib_in_two(x, F)
    print('x =', x ,'     r =', r ,'     up =', up ,'      n = ', n ,'        a = ',  a ,'\n' )

    if n in [ 0, 2] :
        print('B')
        return 'B'
    if n ==1 :
        print('A')
        return 'A'

    # while n >= 2 :
    # print('1:     n= ', n ,'      a= ', a )
    # if n > a[0] :
    #     a = fib_in_two(a[1] , F)
    #     n -= a[0]
    #
    #
    # if n <= a[0] :
    #     a = fib_in_two(a[0] , F)
    #
    # print('2:    n= ', n , '      a= ', a )


    # print(' Y : ', Y[n] )
    # return Y[n]

get_remainder(109, F)

def find_remainder( x , r ) :
    # if x in F :
    #     print('first res :   x, r  = ', x , r  ,'       B '  )
    #     return 'B'

    if x <= 3 :
        Y = {1: 'B' , 2 : 'AB' , 3 : 'BAB'  }
        print('result :   x = ', x, '    r = ',r ,'          ', Y[x][r] )

        return Y[x][r]

    a = fib_in_two(x, F)
    print('start  x = ', x , '    a =', a ,'     r = ', r )

    if r <= a[0] :
        x = a[0]
    if r > a[0] :
        r -= a[0]
        x = a[1]

    print('final   x = ', x , '    a =', a ,'     r = ', r )

    return find_remainder(x, r )


find_remainder(21, 20 )













t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')


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




