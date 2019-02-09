#  Created by Bogdan Trif on 28-11-2017 , 12:00 PM.
# © o(^_^)o  Solved by Bogdan Trif  @
#The  Euler Project  https://projecteuler.net
'''
                        Special partitions      -       Problem 333

All positive integers can be partitioned in such a way that each and every term
of the partition can be expressed as 2^i x 3^j,  where i,j ≥ 0.

Let's consider only those such partitions where none of the terms can divide any of the other terms.
For example, the partition of 17 = 2 + 6 + 9 = (2^1x3^0 + 2^1x3^1 + 2^0x3^2) would not be valid since 2 can divide 6.
Neither would the partition 17 = 16 + 1 = (2^4x3^0 + 2^0x3^0) since 1 can divide 16.

The only valid partition of 17 would be 8 + 9 = (2^3x3^0 + 2^0x3^2).

Many integers have more than one valid partition, the first being 11 having the following two partitions.
11 = 2 + 9 = (2^1x3^0 + 2^0x3^2)
11 = 8 + 3 = (2^3x3^0 + 2^0x3^1)

Let's define P(n) as the number of valid partitions of n. For example, P(11) = 2.

Let's consider only the prime integers q which would have a single valid partition such as P(17).

The sum of the primes q <100 such that P(q)=1 equals 233.

Find the sum of the primes q <10^6 such that P(q)=1.

'''
import time, zzz
from itertools import combinations



def prime_sieve(n):       # FOURTH      o(^_^)o
    sieve = [True] * n
    for i in range(3, int(n**0.5)+1, 2):
        if sieve[i]:
            sieve[ i*i :: 2*i ] = [False] * ( (n-i*i-1) // (2*i) +1 )
    return [2] + [i for i in range(3, n , 2) if sieve[i] ]

def get_terms(lim) :
    ''':Description: generate a list of  multiples of 2 & 3 of the form 2^i * 3^j
    :param lim: int, maximum number
    :return: list of multiples of 2 & 3     '''
    L , T = [], dict()
    i = 0
    while 2**i < lim :
        j = 0
        while 2**i * 3**j < lim :
            n = 2**i * 3**j
            L.append(n)
            T[n] = (i,j)
            # print( 'i, j = ', i, j , '    n =', n ,'       L = ', L)

            j+=1
        i+=1

    L.sort()
    # print('L = ', len(L),'  ', L )
    # print('T = ', T)
    return T, L



S = [1,4, 9 ]

def partition_nr_into_given_set_of_nrs(nr, S,  lim=10 ):
    ''' :Description: partition a number into a custom set of integers with a limit maximum number of terms
    :param n: number to partition
    :param S: integer set
    :return: list of partitions             '''
    nrs = sorted(S, reverse=True)
    def inner(n, i, lim ):
        if lim >= 0 :
            if n == 0:
                yield []
            for k in range(i, len(nrs)):
                if nrs[k] <= n:
                    for rest in inner(n - nrs[k], k , lim-1 ):

                        yield [nrs[k]] + rest
    return list(inner(nr, 0, lim))


def partition(n, S):
    S = sorted(S, reverse=True)

    def inner(n, i) :
        if n == 0 :
            yield set()

        for k in range(i, len(S) ):
            if S[k] <= n :
                for rest in inner( n - S[k] , k ):
                    if S[k] not in rest :
                        yield {S[k]}.union(rest)

    return list(inner( n , 0  ) )


def partition2(n, S):
    S = sorted(S, reverse=True)

    def inner(n, i) :
        if n == 0 :
            yield set()

        for k in range(i, len(S) ):
            if S[k] <= n :
                for rest in inner( n - S[k] , k ):
                    flag = False
                    if S[k] not in rest :
                        for a in rest :
#                             print(S[k], rest)
                            if S[k]%a == 0 :
                                flag = True
                                break
                        if flag == False :
                            yield {S[k]}.union(rest)

    return list(inner( n , 0  ) )


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


def subset(array, num):
    result = []
    def find(arr, num, path=()):
        if not arr:
            return
        if arr[0] == num:
            result.append(path + (arr[0],))
        else:
            find(arr[1:], num - arr[0], path + (arr[0],))
            find(arr[1:], num, path)
    find(array, num)
    return result




print('\n-------------------------- BRUTE FORCE TESTS------------------------------')
t1  = time.time()

def first_solution_BF(lim):         #   Work correctly , but VERY VERY SLOW

    T = get_terms( lim )[1]
    T = T[1:]
    print(len(T), T[:250])

    primes = prime_sieve(lim)[0:]
    # primes = [ 1831 ]
    P = set()

    Sum = 0
    for p in primes :
        up = binary_search(p, T)
        # if p > 20 :   down = binary_search(p/8, T)
        # else : down = 1
        S = T[  : up+1 ]
        Part = partition_nr_into_given_set_of_nrs(p, S, 5 )
        # Part = partition(p, S )
        # Part = partition2(p, S )

        # print('p= ', p ,'    S=  ', S ,'        ',   len(Part) ,'    '    ,Part[-2::] )
        # print('p= ', p , '             ',   len(Part)  )

        cnt, B = 0, []
        for part in Part :
            c0 = 0
            part = list(part)

            for i in range(len(part) ):
                if c0 > 0 : break
                for j in range(i+1, len(part)) :
                    # print(part[i] , part[j] )
                    if  part[i] % part[j] ==0 :
                        c0 +=1

            if c0 == 0 :
                cnt +=1
                B = part
                print('p= ' ,p , '    ',part, '    S= ',sum(part) )             # VALID PARTITION

        if cnt == 1 :
            Sum += p
            P.add(p)
            print(' ----------- chosen prime =  ', p,'         ', B )

    print('\n' ,sorted(P) )
    print('\nSum of primes = ' , Sum)
    return Sum

# first_solution_BF(1*10**3)

'''

  ----------- chosen prime =   2           [2]
 ----------- chosen prime =   3           [3]
 ----------- chosen prime =   5           [3, 2]
 ----------- chosen prime =   7           [4, 3]
 ----------- chosen prime =   13           [9, 4]
 ----------- chosen prime =   17           [9, 8]
 ----------- chosen prime =   23           [9, 8, 6]
 ----------- chosen prime =   43           [27, 16]
 ----------- chosen prime =   59           [32, 27]
 ----------- chosen prime =   61           [27, 18, 16]
 ----------- chosen prime =   113           [81, 32]
 ----------- chosen prime =   181           [81, 64, 36]
 ----------- chosen prime =   193           [81, 64, 48]
 ----------- chosen prime =   199           [81, 64, 54]
 ----------- chosen prime =   241           [96, 81, 64]
 ----------- chosen prime =   467           [243, 128, 96]
 ----------- chosen prime =   479           [243, 128, 108]
 ----------- chosen prime =   499           [256, 243]
 ----------- chosen prime =   593           [512, 81]
 ----------- chosen prime =   643           [256, 243, 144]
 ----------- chosen prime =   661           [256, 243, 162]
 ----------- chosen prime =   691           [256, 243, 192]

RESULTS for 10^3 :
 [2, 3, 5, 7, 13, 17, 23, 43, 59, 61, 113, 181, 193, 199, 241, 467, 479, 499, 643, 661, 691]
Sum of primes =  4600
'''

print('---------------')



# @2017-11-30 -  Must do a recursive approach, build a function which generates recursively and via
# backtracking lists of non-divisors of each other !

### @2018-04-04 - Taken from http://euler.stephan-brumme.com/333/
# KEY OBSERVATION : Example : All the numbers must have this property :
# If we take two numbers n1 = 2^a * 3^b &  n2 = 2^c * 3^d : in order to not have terms divisible :
# if a > c , then => b < d        &
# if a < c , then => b > d
#     IT IS IMPOSSIBLE that either a == c or b ==d because they will be divisor and divident
# Example :  17 = 8 + 9 = 2^3* 3^0 + 2^0 * 3^ 2   is valid and respects the above RULE

# @2018-05-16 :  STRATEGY :
# 1. Build a stack with all the powers of 2^i*3^j  and put them in a data structure, Dictionary with elem of the form :
#     Example 1 :      8 : (3, 0 ) where the first term is i, j from the powers of 2^i and 3^j
#     Example2 :    48 : (4, 1)           72 :(3, 2) ... and so on  to the limit 10^6
#
# 2.  Make combinations of numbers such that their suma < 10^6 and put them in a sieve of the form :
#  [0, 1, 2, 1, 2, 3, 4, 4 ] where indexes represent the actual numbers and the values represent how many representations
# an index number has.
#
# 3. Select the primes indexes with values of 1 . Sum them.

t2  = time.time()
print('\n# Completed in :', round((t2-t1), 4 ), 's\n\n')

print('\n======  My FIRST SOLUTION, EXPONENTIAL, Must improve it, ,  SUPER SLOW, 4 hours  =======\n')
t1  = time.time()


# @2019-01-13 - Use SETS like in the problem 201 !!! ---- hmmmm ... NOT  EXACTLY !
# IDEA :
# 1.  Iterate over all valid power of the type 2^i*3^j -->[1, 2, 3, 4, 6, 8, 9, 12, 16, 18, 24, 27, 32, 36, 48, 54, 64, ... ] <- 143 numbers
# 2. Make valid subsets of 2, 3, 4, ... elements

# 2nd IDEA :
# 1.  Form all the numberswith 2 elements. Put them in an array.
# 2. Then successively formlists of 3, 4, 5 , ... elements


def check_new_elem(L , nr, T ) :
    ''':Description: Checks whether it is safe to add a new element to the list L
        :Example1: if L = [ 16 ,  24  ] and the new elem is 96 it is INVALID since 96 | 16
            but the elem 27 is VALID since 27  do not divide neither 16 neither 24
        :Example2: if L = [ 4 ,  9  ] and the new elem is 18 it is INVALID since 18 | 9
            but the elem 6 is valid since 6  do not divide neither 4 neither 9    '''

    c, d = T[nr]
    for i in L :
        a , b = T[ i ]
        # print( '.       ' , i , '    a, b =' , T[ i ] ,'        c, d = ',  T[nr] ,'      nr= ' , nr )
        if  (a <= c)  and (b > d) == False :                 return False
        if ( a >= c ) and (b < d )== False :                 return False
    return True


# print(' check_new_elem :', check_new_elem( [ 36,  27 ] , 16, T )  )


def solution_special_partitions(lim) :

    Primes= set( prime_sieve(lim) )

    W = [0] * (lim+1)                   # SIEVE used to store how many 2^i* 3^j numbers are

    T, V = get_terms( lim )
    V = V[1:]
    # print('T : ', T)
    # print('V : ', V)


    A = [ [i] for i in V  ]
    print('A : ', A)
    X = { (lim+2):{1234} }               # Dictionary used for doubles like : elem =  [2, 3] & elem =  [3, 2] = 5
    w= 2

    while len(X) > 0 :
        B, X = [], {}              # B will serve as the temp array
        print('\n - - - -   nr. of elemets = ', w )
        for s in A :
            for j in range( len(V) ) :          # V will be unchanged
                if check_new_elem( s  , V[j], T ) :
                    elem = s + [ V[j]]
                    if sum(elem) <= lim :
                        if sum(elem) not in X :
                            X[ sum(elem) ] = []
                        S = sum(elem)
                        seta = set(elem)
                        # print( s, j , '      ', s,'    ', V[j] ,'      elem = ', elem,'     sum = ', S )

                        if seta not in X[ sum(elem) ] :
                            X[S ].append(seta)
                            B.append(elem)
                            W[S] += 1          # The Main SIEVE

        A = [i for i in B]


        # print('\nX : ',  X )
        print('A :   length = ',  len(A),'     ' ,A[:10] )


        w+=1

    print('\nW : ',  len(W), W[:50] )

    SP = [ p for p in Primes if W[p] == 1 ]
    print('SP : ', SP)
    print('\nANSWER :       SP sum =  ', sum(SP)+5 )


'''
 - - - -   nr. of elemets =  2
A :   length =  5633       [[2, 3], [2, 9], [2, 27], [2, 81], [2, 243], [2, 729], [2, 2187], [2, 6561], [2, 19683], [2, 59049]]
 - - - -   nr. of elemets =  3
A :   length =  93866       [[4, 6, 9], [4, 6, 27]
 - - - -   nr. of elemets =  4
A :   length =  773881       [[8, 12, 18, 27]
 - - - -   nr. of elemets =  5
A :   length =  3440916       [[16, 24, 36, 54, 81]
 - - - -   nr. of elemets =  6
A :   length =  8612200       [[32, 48, 72, 108, 162, 243]
 - - - -   nr. of elemets =  7
A :   length =  12303612       [[64, 96, 144, 216, 324, 486, 729]
 - - - -   nr. of elemets =  8
A :   length =  9927062       [[128, 192, 288, 432, 648, 972, 1458, 2187], [128, 192, 288, 432, 648, 972, 1458, 6561]
 - - - -   nr. of elemets =  9
A :   length =  4349817       [[256, 384, 576, 864, 1296, 1944, 2916, 4374, 6561]
 - - - -   nr. of elemets =  10
A :   length =  952137       [[512, 768, 1152, 1728, 2592, 3888, 5832, 8748, 13122, 19683]
 - - - -   nr. of elemets =  11
A :   length =  87695       [1024, 1536, 2304, 3456, 5184, 7776, 11664, 17496, 26244, 39366, 59049]
 - - - -   nr. of elemets =  12
A :   length =  2169       [2048, 3072, 4608, 6912, 10368, 15552, 23328, 34992, 52488, 78732, 118098, 177147]
 - - - -   nr. of elemets =  13
A :   length =  0       []

SP :  [5, 7, 13, 17, 23, 43, 59, 61, 113, 181, 193, 199, 241, 467, 479, 499, 
643, 661, 691, 1753, 1889, 5387, 5531, 5693, 10657, 13249, 13729, 
14753, 15031, 418811, 36067, 308219, 49891, 54499, 448187, 
494843, 118061, 122921, 518171, 391163]

'''

solution_special_partitions(10**6)          #    ANSWER :       SP sum =   3053105

t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')        #   Completed in : 1395.13 s


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

