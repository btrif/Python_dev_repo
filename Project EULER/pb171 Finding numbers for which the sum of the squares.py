#!/usr/bin/python                   o(^_^)o         ( ͡° ͜ʖ ͡°)
# © Solved by Bogdan Trif @
#The  Euler Project  https://projecteuler.net
'''
        Finding numbers for which the sum of the squares of the digits is a square      -           Problem 171

For a positive integer n, let f(n) be the sum of the squares of the digits (in base 10) of n, e.g.

f(3) = 3^2 = 9,
f(25) = 2^2 + 5^2 = 4 + 25 = 29, --> this is not valid, 29 not a square !
f(442) = 4^2 + 4^2 + 2^2 = 16 + 16 + 4 = 36

Find the last nine digits of the sum of all n, 0 < n < 10**20,   such that f(n) is a perfect square.
'''


import time, zzz, gmpy2

import itertools

import math


def f(n):
    l = sum([ int(i)**2 for i in str(n)])
    return l

print('test f : \t' , f(3) )



def partition_nr_into_given_set_of_nrs2(nr , S):        # Not quite so estetic
    ''' Made by Bogdan Trif @ 2017-10-06, 20:00.
        :Description:  does the partition of a number into the given set of numbers. Example :
        take the number 9, and the set of numbers = {1, 4, 9}. It will yield the following partitions :

        { (1, 1, 1, 1, 1, 1, 1, 1, 1), (1, 1, 1, 1, 1, 4), (1, 4, 4), (9,)}

        No other possible partitions using the set {1, 4, 9} cannot be formed to sum the number 9.
        the partition of the given nu

    :param nr: int, the number to partition
    :param S: the set of integers to use for partitioning
    :return: lst, the list with all partitions
    '''
    lst = set()
    # Build the base case :
    M = [1]*(nr%S[0]) + [S[0]] * (nr //S[0])
    # print(M)
    if set(M).difference(S) == 0  :
        lst.add(M)
        # print('as a result',M)
    else :
        for x in S :
            for j in range(1, len(M)+1):
                for k in range(1, nr//x +1 ) :
                    # print(x, j , '  k=',k)
                    if  k*x ==  sum(M[:j]) :
                        # print( [x]*k , M[:j] ,  '  the partition :    ', tuple(sorted([x]*k + M[j:])) )
                        lst.add(  tuple(sorted([x]*k + M[j:])) )
    return sorted(lst)


S = [1, 4, 9]
print ('\npartition_nr_into_given_set_of_nrs : \n' ,partition_nr_into_given_set_of_nrs2(9, S) )

def partition_nr_into_given_set_of_nrs(nr, S ):
    ''' Recursive function to partition a number into a given set of numbers

    :param nr:
    :param S:
    :return:
    '''
    nrs = sorted(S, reverse=True)
    def inner(n, i):
        if n == 0:
            yield []
        for k in range(i, len(nrs)):
            if nrs[k] <= n:
                for rest in inner(n - nrs[k], k):
                    yield [nrs[k]] + rest
    return list(inner(nr, 0))

# S = [  1, 4, 9, 16 ]
# print(partition_nr_into_given_set_of_nrs(40, S ))


def partition_nr_into_given_set_of_nrs_limit(nr, S, m=10):
    '''Recursive function to partition a number into a given set of numbers
    and also having an upper limit lim of the  partition length.
    :param nr: int, nr to partition, example : 109
    :param S: set of numbers used for partitioning
    :param m: int, limit, example m=10 represents the maximum partition length
    :return: list of partitions , list of lists
    '''
    nrs = sorted(S, reverse=True)
    def inner(n, i, m):
        if m >= 0:
            if n == 0:
                yield []
            for k in range(i, len(nrs)):
                if nrs[k] <= n:
                    for rest in inner(n - nrs[k], k, m - 1):
                        yield [nrs[k]] + rest
    return list(inner(nr, 0, m))

def partition_nr_into_given_set_of_nrs_limit_square_root(nr, S, m=10):
    '''Recursive function to partition a number into a given set of numbers
    and also having an upper limit lim of the  partition length.
    :param nr: int, nr to partition, example : 109
    :param S: set of numbers used for partitioning
    :param m: int, limit, example m=10 represents the maximum partition length
    :return: list of partitions , list of lists
    '''
    nrs = sorted(S, reverse=True)
    def inner(n, i, m):
        if m >= 0:
            if n == 0:
                yield []
            for k in range(i, len(nrs)):
                if nrs[k] <= n:
                    for rest in inner(n - nrs[k], k, m - 1):
                        yield [ int(nrs[k]**(1/2))] + rest
    return list(inner(nr, 0, m))




def unique_permutations(lst):       # VERY EFFECTIVE
    ''':Description: Takes a list and makes ONLY Unique Permutations of a list with repeated elements.
        If one tries itertools.permutations on a list with 14 elements ==> BANG, computer freezes
    :param lst: type list
    :return:    a list of lists containing all the permutations
    '''
    if len(lst) == 1:
        yield (lst[0],)
    else:
        unique_lst = set(lst)
        for first_element in unique_lst:
            remaining_lst = list(lst)
            remaining_lst.remove(first_element)
            for sub_permutation in unique_permutations(remaining_lst):
                yield (first_element,) + sub_permutation

def multiple_permutations(*args ) :
    ''' **©** Made by Bogdan Trif @ 2017-09-03, 12:15.
        Uses the formula Perm(total_elem_nr) / [ Perm(elem_1) *Perm(elem_2) * ...* Perm(elem_n) ]
    :param args:  the first arg is always the total number of elements, e.g. : for  the list [1, 1, 1, 1, 2, 2, 2 ,3, 3] = 9 elem ;
        The next elements will be in descending order the separate no of elem : 4 elem of '1' s , 3 elem of '2's , 2 elem of '3's
    :Explicit formula:      p = gmpy2.fac(9) // ( gmpy2.fac(4)*gmpy2.fac(3)*gmpy2.fac(2) )
    :return: int, Perm(total) / (Perm(elem_1) *Perm(elem_2) * ...* Perm(elem_n) )
    '''
    den = 1
    S=0          # the sum of all elements
    for i, j in enumerate(args) :
        # print(i,'    ', j,'     ' )
        if i == 0 :
            num = gmpy2.fac(j)
            N = j
        else :
            den *= gmpy2.fac(j)
            S += j
    # assert (N == S ) , "Total number of elements condition is not met !"
    if (N != S) :  raise ValueError ("Total number of elements condition is not met !")

    return (num // den)

print('\nMultiple_permutations of elements : \t' ,multiple_permutations(9,4,3,2) )


class Compute_List_Permutations_Number() :
    ''' o(^_^)o MAde by Bogdan Trif @ 2017-10-11, 13:30
    It has many functions:
    1. factorial
    2. count all the occurences of int elements of a list
    3. computes the nr of permutations of an int list
    4. computes the nr of permutations of a list without leading zeros. Euler pb 171
    '''

#     def __init__(self ):
#         self.lst = lst
#         self.length = len(lst)
#         print(self.lst, self.length)

    def fact(self, n):
        nr = 1
        for i in range(1, n+1):
            nr *= i
        return nr

    def count_elem(self, lst ):        # Nice function, made by Bogdan Trif @ 2017-04-09, 13:30
        X = []
        for i in set(lst):
#             print(i, lst.count(i), end='; ')
            X.append((i, lst.count(i) ))
#         print(X)
        return X

    def compute_permutations( self, lst ) :
        L = self.count_elem(lst)
#         print( L )
        num, den = len(lst), 1
        for x in L :
            den *= self.fact(x[1])
        return self.fact(num)//den

    def compute_permutations_without_leading_zeros( self, lst ) :
        L = self.count_elem(lst)
        if L[0][0] !=0 :
            return self.compute_permutations(lst)
        else :
            o, S = len(L), 0
            for i in range(1, o) :
                P =  [ L[j][1] if i!=j else L[j][1]-1 for j in range(len(L)) ]
#                 print(i, L, ' P=',P)

                den, num = 1, sum(P)
                for k in P :
#                     print('k =', k)
                    den *= self.fact(k)
#                     print('den=  ', den, '  sum(P) = ', sum(P))

                S+= int( self.fact(num)/den )
            return S

print('\n--------------------------TESTS------------------------------')
t1  = time.time()

# # 2017-03-09 - APPROACH : I must identify for a given length of number which is the combination
# of digits whose squares gives another square .
# For example : for a length 2 I would immediately know that wa can use Pytagora. therefore :
# 34, 43 gives the perfect square 25;    68, 86 gives 100, there are also the 10 multiples.
#
# Then we must go to the 3 digit numbers. We already have some from the two's and we add 0, like
# 340 or 430 or 403 or 304 .
#
#
# https://plus.maths.org/content/triples-and-quadruples
# https://en.wikipedia.org/wiki/Pythagorean_quadruple

## IMportant OBSERVATION : maximum number is 10**20 => 20 digits => maximum square will be LESS THAN :
# 9**2 +....+ 9**2 = 81*20 = 1620
# Those numbers must be broken into 2,3,4,.... parts squares such that :
# So the problem reduces to ways to partition a square into squares :) NICE :)
#
# Example : in a 4 digit number, let's say that we have the result, the square is 169
# must broke into 4 squares : how we do it ?
# we try : 169 - 16 = 153 - 36 = 117 - 81 = 36. Therefore we obtained the digits : 4,6,9,6 .
# And from here we make permutations of that number. We must take for the zero case
# and permutate accordingly
#
# make a dictionary of squares
#
# @2017-09-11 - Must do the recursive partition function, NOT YET FINISHED
# In how many ways can we decompose a number into squares, like :
# 9 = 9
# 9 = 4,4,1
# 9 = 4,1,1,1,1,1
# 9 = 1,1,1,1,1,1,1,1,1

Q = [ i*i for i in range(1, 10) ]



def test_to_establish_formula() :
    test = [81, 81, 81, 81, 81, 81, 81, 81, 49, 16, 9, 4, 1, 1, 1]
    test2 = [9, 4, 1, 1, 1]
    test3 = [4, 4, 1, 1, 1]
    test4 = [1, 1 ]

    for i in range( 1,  8-len(test3)+1 ):
        pe = test3 + [0]*i
        Perm = list(unique_permutations(pe))
        v= len(Perm)
        for j in Perm :
            if j[0] == 0 : v -= 1
        # print('Valid permutations : ', l )

        print('0=' , i, '    ', pe ,'     All = ', len(Perm),'      Valid=  ',v ,'       ' ,Perm[:100])




def first_solution(lim):
    SUM = 0
    SP = []
    for i in range(1, lim+1):
        n = i*i
        P = partition_nr_into_given_set_of_nrs_limit( n, Q, 20)
        print(str(n)+'.    nr_of_part= ', len(P) , '    ',P[:50] )
        SP += P
    # print(SP)

    cnt = 0
    for J in SP :
        cnt +=1
        J = [ int(math.sqrt(i )) for i in J ]
        zer = 20 - len(J)
        print(str(cnt) +'.     ', zer  , len(J), '    ',J)
        for k in range( zer+1 ) :
            Z = J + [0]*k
            UP = list(unique_permutations(Z) )[:50]

            print( 'Z= ', Z ,'       UP=      ' , UP)
            # SUM += perm

    print('\nThe SUM of Total numbers=  ', SUM )
    return print('Last 9  digits : \t', SUM%(10**9) )

first_solution(5)





### SOME IDEAS : https://www.quora.com/What-is-a-formula-to-calculate-the-sum-of-all-the-permutations-of-a-given-number-with-repitations

t2  = time.time()
print('\nCompleted in :', round((t2-t1) , 4), 's\n\n')

print('\n======= My FIRST SOLUTION,  Not feasable - 3 DAYS !!! OMG !! ===============\n')
t1  = time.time()

def three_days_some_BRUTE_FORCE_solution() :             ### NO !!! DON'T RUN IT !!!!

    S = [1, 4, 9, 16, 25, 36, 49, 64, 81]
    print('Main Set: ', S)
    m=20

    Part_lim = partition_nr_into_given_set_of_nrs_limit_square_root( 100, S, m)
    print('\npartition_nr_into_given_set_of_nrs_limit : \n', len(Part_lim), Part_lim )

    SUM = 0
    PART =[]
    cnt = 0
    for i in range(1, 40) :
        Partitions = partition_nr_into_given_set_of_nrs_limit_square_root( i*i, S, m=20 )
        print('\ni =',i , '  n = ' ,i*i ,'     Partitions : ', len(Partitions), Partitions[:1000] )
        PART.extend(Partitions)
        for J in Partitions :
            cnt += 1
            zeros = m-len(J)
            J.extend([0]*zeros)
            print(str(cnt) + '.    ' , J , len(J) ,'       ', round((time.time()-t1) , 4), ' s' )
            Comb = itertools.combinations(J, 9)
            for K in Comb :
                nines = int(''.join( str(i) for i in  K ))
                # print(K,'     ', nines)
                SUM += nines

    print('\nTotal nr of partitions : ', len(PART))         #
    print('\nANSWER : TOTAL SUM = ', SUM,'    %9 = ', SUM%(10**9) )
    return SUM%(10**9)

### NOTE : 2018-03-31, 11:50 :  Total nr of partitions :  221372    , With current algorithm it will take  3 DAYS    !!!!!!!!!!!!!!!!!!!!!
# LAst Partition to investigate is    i = 39   n =  1521      Partitions :  1 [[9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 8, 8, 4]]
# i = 36   n =  1296      Partitions :  85 [[9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 8, 4, 1],
# i = 37   n =  1369      Partitions :  28 [[9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 8, 3], [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 8, 2, 2, 1],
# i = 38   n =  1444      Partitions :  6 [[9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 7, 3, 3], [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 8, 8, 4, 2],
# i = 39   n =  1521      Partitions :  1 [[9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 8, 8, 4]]
# i = 40   n =  1600      Partitions :  0 []

### Timing results :
# 150.     [6, 3, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0] 20         192.412  s
# 151.     [6, 3, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0] 20         193.7941  s
# 152.     [6, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] 20         195.1762  s
# 153.     [6, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0] 20         196.5712  s

# three_days_solution()




# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


# print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
# print('\n--------------------------SOLUTION 1,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 2,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 3,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 4,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 5,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 6,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 7,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 8,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 9,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 10,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 11,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 12,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

