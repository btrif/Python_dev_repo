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

Find the sum of the primes q <1000000 such that P(q)=1.

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
    T = []
    i =0
    while 2**i < lim :
        j = 0
        while 2**i * 3**j < lim :
            n = 2**i * 3**j
            # print(n)
            T.append(n)
            j+=1
        i+=1

    T.sort()
    return T


S = [1,4,9]

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




print('\n--------------------------TESTS------------------------------')
t1  = time.time()

def first_solution(lim):

    T = get_terms( lim )
    T = T[1:]
    print(len(T), T[:250])

    primes = prime_sieve(lim)[0:]
    P = set()

    Sum = 0
    for p in primes :
        up = binary_search(p, T)
        # if p > 20 :   down = binary_search(p/8, T)
        # else : down = 1
        S = T[  : up+1 ]
        Part = partition_nr_into_given_set_of_nrs(p, S, 6 )
        # Part = partition(p, S )
        # Part = partition2(p, S )

        # print('p= ', p ,'    S=  ', S ,'        ',   len(Part) ,'    '    ,Part[-2::] )
        # print('p= ', p , '             ',   len(Part)  )

        cnt, B = 0, []
        for part in Part :
            c0 = 0
            part = list(part)
            # print(part)
            for i in range(len(part) ):
                if c0 > 0 : break
                for j in range(i+1, len(part)) :
                    # print(part[i] , part[j] )
                    if  part[i] % part[j] ==0 :
                        c0 +=1


            if c0 == 0 :
                cnt +=1
                B = part

        if cnt == 1 :
            Sum += p
            P.add(p)
            print(' ----------- chosen prime =  ', p,'         ', B )

    print('\n' ,sorted(P) )
    print('\nSum of primes = ' , Sum)
    return Sum

first_solution(10**2)



print('---------------')

# J = partition_nr_into_given_set_of_nrs(233, primes  , 10)
# for I in J:
#     if len(I) == len(set(I)) and 17 in I  :
#         print(I)


# @2017-11-30 -  Must do a recursive approach, build a function which generates recursively and via
# backtracking lists of non-divisors of each other !

t2  = time.time()
print('\n# Completed in :', round((t2-t1), 4 ), 's\n\n')

print('\n================  My FIRST SOLUTION,   ===============\n')
t1  = time.time()

def generate_two__three_non_divisible(nr, power, lim) :
    L = [  ]
    S = {2, 3}
    S  -= {nr}
    x = sum(S)
    print(x)

    for j in range( power) :
        i = 1
        while x**i * nr**j  < lim :
            print('x= ',x, '      ' , j , i , '    '  , x**i * nr**j  )
            L.append( x**i * nr**j )

            i+=1

    print(nr**power ,L )
    return nr**power, L


generate_two__three_non_divisible(3, 1, 10**2)

T = get_terms( 10**5 )
T = T[1:]  [ :: -1 ]
print(len(T), T ,'\n\n')

for i in range(11, 14 ) :       # for 10**6 limit is 11+1 with elements < 10**5
    comb =  combinations(T, i)
    # print(comb)
    for J in comb :
        c = 0
        for x in range(len(J) ) :
            if c > 0 :
                break
            for y in range(x+1, len(J) ) :
                # if J[y] % J[x] == 0 :
                if J[x] % J[y] == 0 :
                    c+=1
        if c == 0 :
            print(J ,'          ', len(J) , sum(J) )



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

