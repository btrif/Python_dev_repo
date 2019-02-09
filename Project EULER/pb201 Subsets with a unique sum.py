#  Created by Bogdan Trif on 07-11-2017 , 6:42 PM.
# © o(^_^)o  Solved by Bogdan Trif  @   Completed on Mon, 14 Jan 2019, 16:20
#The  Euler Project  https://projecteuler.net
'''
                            Subsets with a unique sum               -           Problem 201

For any set A of numbers, let sum(A) be the sum of the elements of A.

Consider the set B = {1,3,6,8,10,11}.
There are 20 subsets of B containing three elements, and their sums are:

sum({1,3,6}) = 10,
sum({1,3,8}) = 12,
sum({1,3,10}) = 14,
sum({1,3,11}) = 15,
sum({1,6,8}) = 15,
sum({1,6,10}) = 17,
sum({1,6,11}) = 18,
sum({1,8,10}) = 19,
sum({1,8,11}) = 20,
sum({1,10,11}) = 22,
sum({3,6,8}) = 17,
sum({3,6,10}) = 19,
sum({3,6,11}) = 20,
sum({3,8,10}) = 21,
sum({3,8,11}) = 22,
sum({3,10,11}) = 24,
sum({6,8,10}) = 24,
sum({6,8,11}) = 25,
sum({6,10,11}) = 27,
sum({8,10,11}) = 29.

Some of these sums occur more than once, others are unique.
For a set A, let U(A,k) be the set of unique sums of k-element subsets of A,
in our example we find U(B,3) = { 10, 12, 14, 18, 21, 25, 27, 29 } and sum(U(B,3)) = 156.

Now consider the 100-element set S = {1^2, 2^2, ... , 100^2}.
S has 100891344545564193334812497256 50-element subsets.

Determine the sum of all integers which are the sum of exactly one of the 50-element subsets of S,
i.e. find sum(U(S,50)).


'''
import time, zzz
# from gmpy2 import comb
from itertools import combinations
import random

# print('Comb( 100, 50 ) = ', comb(100, 50) )

L = [ i*i for i in range(1,101) ]
S = set(L)
print(L)

smallest_set_sum = sum( [  i*i for i in range(1, 51)] )
greatest_set_sum = sum( [  i*i for i in range(51, 101)] )

print('smallest_set_sum = ', smallest_set_sum, ' ;   greatest_set_sum = ', greatest_set_sum )
print(' There are no more than ', greatest_set_sum-smallest_set_sum , '    unique sums' )


'''
https://stackoverflow.com/questions/12533302/project-euler-201
VERIFICATION :
10 5        =       15785
20 10       =       152110

'''

print('\n--------------------------TESTS------------------------------')
t1  = time.time()

# What is the recursive solution for finding all subsets of a given array?
def subsets( nums ):      # Returns all the subsets of the main set
    if nums is None: return None
    subsets_ = [[]]
    next = []
    for n in nums:
        for s in subsets_ :
            next.append(s + [n])
        subsets_ += next
        next = []
    return subsets_

print(subsets( [ 2, 3, 5, 7, 11, 13 ] ) )



# def existsRepresentation( nr, max_nr ,nr_of_elem ):
#     n = 0
#     for i in range(nr_of_elem) :

def just_a_test(lim) :
    # lim = 20

    A, B = dict(), [0 for i in range(10*lim*lim+1)]
    for i in range(1, lim+1):
        for j in range(i+1, lim+1):
            print('i,j = ', i, j, '      ', i*i+j*j )
            B[i*i+j*j] += 1
            if i*i+j*j not in A :
                A[i*i+j*j] = []
                A[i*i+j*j].append({i, j})
            else : A[i*i+j*j].append({i, j})

    print('B :', len(B), B )
    print()
    A_ = dict()
    for k,v in A.items():
        if len(A[k]) == 1 :
            for i in range(1, lim +1) :
                if i not in v[0] :
                    S = v[0].union({i})
                #     print(S)
                    s_ = sum([i*i for i in S])
                    B[s_] += 1
                    if s_ not in A_ :
                        A_[s_] = []
                    if S not in A_[s_] :
                        A_[s_].append(S)

                    print(k, v , '      ', i,'     ' , S,'   ',s_ )

    cnt = 0
    for k,v in A_.items():
        if len(A_[k]) != 1 :
            cnt +=1
            print(' k, v = ', k, '    ',v, '    cnt = ', cnt)

    return A_

# just_a_test(20)

print('\n-------------- Using Combinations,  Hard Brute Force, Exponential ALGO -----------------------')
def hard_brute_force(lim, elem) :           #### @2018-05-28, 14:10        IT WORKS FINE !!!

    Y = dict()
    cnt = 0
    I = list(range(1, lim+1) )
    print(I)
    # I = [1,3,6,8,10,11]
    for cnt, i in enumerate(combinations( I, elem ) ):

        J = [ x*x for x in i  ]
        s = sum( J )
        if s not in Y :
            Y[s] = []
            # print(str(cnt+1)+ '.    ' , i,'      ', J, '       ', s)

        # else :
            # print('duplicate :     ' , i , '     cnt=', cnt ,'     ', J , '      s =', s )
        Y[s].append( set(J) )

    W =  [ k for k,v in Y.items() if len(v) ==1 ]

    print('W :',  W  )
    print( '\n Total sum = ', sum(W) )
    return set(W)

# W = hard_brute_force(20, 10 )

t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')

print('\n-------  My FIRST SOLUTION, Exponential Algorithm , Correct, but it takes a lifetime   ---------\n')
# Used only for VERIFICATION & Checks
t1  = time.time()

def subsets_unique_sum_exponential_algo(lim, elem_nr, visual ) :
    # elem_nr = 2             # number of elements in the set
    # lim = 20                    # maximum number to consider
    A = { k*k: [{k*k}] for k in range(1, lim+1)   }
    Aplus = dict()
    print('A :', A)
    elem = 1
    while elem < elem_nr :
        print('\n-------- elem =', elem ,'   ------   len(A )=  ', len(A) ,'    -------    ' +str( round( time.time() -t1 , 4 )) +' s' )
        # A_ = { k:v for k,v in Aplus.items() if v }
        A_ = dict()
        Aplus = dict()

        for k,v in A.items():
            if len(v) == 1 :
                for i in range(1, lim +1) :
                    if i*i not in v[0] :
                        S = v[0].union({i*i})

                        s_ = sum([i for i in S])

                        if s_ not in A_ :
                            A_[s_] = []

                        if S not in A_[s_] :
                            A_[s_].append(S)
                            # print('k=', k ,'  v= ' ,v , '      ', i*i,'     ' , S,'    s_= ', s_ , '       A_[s_] =   ' , A_[s_] )

            if len(v) > 1 :
                # print('k=', k ,'  v= ' ,v , '      ', i*i,'     ' , S,'    s_= ', s_ , '       A_[s_] =   ' , A_[s_] )
                for j in range(len(v)) :
                    Z = v[:j] + v[j+1:]
                    U = list(set().union(*Z))
                    W = set(U).difference( v[j] )
                    # print( v[j], '     Z =', Z,'        U :', U ,'      W :', W )
                    for el in W :
                        S2 = v[j].union({el})
                        s_2 = sum([i for i in S2])

                        if s_2 not in Aplus :
                            Aplus[s_2] = []

                        if S2 not in Aplus[s_2] :
                            Aplus[s_2].append(S2)
                            # print( v[j], '     Z =', Z,'        U :', U ,'      W :', W , '    just added S2 : ' , S2 )

        A = { k:v for k,v in A_.items() if v }
        # print('\nA : elements = ', elem ,'\n' , len(A), A )
        # print('\nAplus : \n' , len(Aplus), Aplus )
        ### Extend further A with Aplus :
        for k2, v2 in Aplus.items() :
            if k2 not in A :
                A[k2] = v2
            if k2 in A :
                for f in v2 :
                    if f not in A[k2]:
                        A[k2].append(f)
        elem+=1

    if visual == True :
        print('\n------------    Visualize  elements     ----------')
        cnt = 1
        S = 0
        for k,v in A.items():
            if len(v) == 1 :
                S += k
                print('k = ', k, '    v = ',  v, '        cnt = ', cnt ,'     S=', S )
                cnt +=1


    result = [ k  for k,v in A.items() if len(v) ==1 ]
    print('\n-------- elem =', elem ,'   ------   len(A )=  ', len([ k  for k,v in A.items() if len(v) ==1 ]) ,'    -------    ' +str( round( time.time() -t1 , 4 )) +' s' )

    print('\nFinal SETS : ',  { k: v  for k,v in A.items() if len(v) ==1 } )
    print('\nANSWER : ',  sum(result) )
    return set(result)

# result = subsets_unique_sum_exponential_algo( 16, 8   , False  )

# print('W :', len(W), W)
# print('result :', len(result), result)
#
# print('\n Set dif : ', result.difference(W) )
# print('\n Set dif 2 : ', W.difference(result) )


# @2018-05-28 : 74:
# [{8, 1, 3}, {3, 4, 7}] <--- Here is the problem ! I neglected the fact that I must combine all elements of the two sets :
# to form set of 4 elements with them !! And I have seen this in the start but I neglected it !!!
# I must do the following :
# make set diff between each set in the list like :
# S1, S2 = {8, 1, 3} ,{3, 4, 7}
# S2.difference(S1)
# for i in S2.difference(S1) :
#     print(S1.union({i}) )
#
# for i in S1.difference(S2) :
#     print(S2.union({i}) )
#
# {8, 1, 3, 4}
# {8, 1, 3, 7}
# {8, 3, 4, 7}
# {1, 3, 4, 7}



t2  = time.time()
print('\n# Completed in :', round((t2-t1), 2 ), 's\n\n')


print('\n============   My SECOND SOLUTION,  FAIL  ===============\n')
t1  = time.time()

#           @2019-01-03, 20:00          IDEA :
# 1.  form sets of 1 elements {1}, {2}, {3}, {4}, {5}, {6}
# 2.  check for duplicates. Obviously no duplicates
# 3.  Form sets of 2 elements : {1, 4}, {1, 9}, {1, 16}, {1, 25}, .... {99^2, 98^2  }, {99^2, 100^2}
# 4.  Check for duplicates and eliminate those sets
# ... repeat the process until you reach sets of 50-ellemets
# The  General Idea is the following :
# Because we have a finite nr of sets, There are no more than  252500     unique sums =>
# The subsets sums will not grow exponentially; they will always reduce to a finite nr of subsets.
# That is why we can eliminate the duplicates.Obviously
# OBS: We must also have a dictionary of sets of the form :
# SETS = {100: {36, 100} ,13: {4, 9} ,41: {16, 25} ,85: {36, 49} , ... }
# to keep track of the elements we have already in the previous sets

def Sum_squared(k, n) :
    ''':Description: returns Sum{k, n} (k^2)
        :Example: Sum{4, 7} (k^2) = Sum{1, 7} (k^2) - Sum{1, 3} (k^2)
    :param k:  int, the starting k number
    :param n: int, ending number
    :return: int, Sum{k, n} (k^2)           '''
    Sum_squared_basic = lambda n :  n*(n+1)*(2*n+1) // 6
    S1 = Sum_squared_basic(k-1)
    S2 = Sum_squared_basic(n)
    return S2 -  S1







def solution_attempt2_( max_nr, Set_size ) :

    square_sum = Sum_squared(Set_size, max_nr )
    print('square_sum ('+str(Set_size) +' ,' +str(max_nr) +' )= ', square_sum )

    SETS = { k*k : {k*k} for k in range(1, max_nr+1)  }
    DUPLIQ = dict()


    print('SETS : ',SETS)

    for set_size in range(2, Set_size+1 ) :
        print('\nset_size = ', set_size)
        SETS2 = {}

        # print('SETS2 : ', SETS2 )

        print('before DUPLIQ , length= ', len(DUPLIQ), '   ' ,DUPLIQ )
        for nr in range(1, max_nr +1) :
            for k, v in DUPLIQ.items() :
                for sset in v  :           #   DUPLIQ[v]  is a list of sets, of the form 65: [{1, 64},{ 16, 49 } ] where k=65 and v = [ {1, 64},{ 16, 49 } ]
                    # print('sset : ', sset)
                    if nr*nr not in sset :
                        sbset = sset | {nr*nr}
                        if sum(sbset) not in SETS2 :
                            SETS2[ sum(sbset)] = sbset
                            # print('DUPLIQ : ',  DUPLIQ[s] )

                    v.remove(sset)

        DUPLIQ =  {k:v for k,v in DUPLIQ.items() if len(v) >0 }

        print('--- after  DUPLIQ : ',  DUPLIQ )


        for subset_sum, subset_vals in SETS.items():
            for nr in range(1, max_nr +1) :
                if nr*nr not in SETS[ subset_sum ] :    # We don't want to add the add a number to a set more than once
                    # print('---    subset_sum = ', subset_sum+nr*nr , '   ' ,subset_vals , '      nr^2=  ', nr*nr)

                    if (subset_sum+nr*nr)  not in SETS2 :
                        temp_set = set()
                        temp_set.update(SETS[subset_sum])
                        temp_set.add(nr*nr)
                        SETS2[ subset_sum+nr*nr ] = temp_set

                        # print('after :  temp_set =  ', temp_set  , '      ',SETS2 )
                    elif (subset_sum+nr*nr) in SETS2 :
                        if nr*nr not in SETS2[subset_sum+nr*nr] :
                            dupliq_set = set()
                            dupliq_set.update(SETS[subset_sum])
                            dupliq_set.add(nr*nr)
                            if subset_sum+nr*nr not in DUPLIQ :
                                DUPLIQ[subset_sum+nr*nr]= [ dupliq_set ]
                            elif dupliq_set not in DUPLIQ[subset_sum+nr*nr] :
                                DUPLIQ[subset_sum+nr*nr].append(dupliq_set)
                            DUPLIQ[subset_sum+nr*nr].append(SETS2[subset_sum+nr*nr]  )
                            SETS2.pop( subset_sum+nr*nr )

                                # print('Duplicates :  len= ', len(DUPLIQ),'  ', DUPLIQ )


        #                 print('subset_sum: ', subset_sum+nr*nr , '     subset_vals : ' , SETS2[ subset_sum+nr*nr ] ,'    nr*nr = ', nr*nr )
        key, val = random.choice(list(SETS2.items()))
        print('---------- next_SETS : len= ', len(SETS2)   ,'   ;  random key, val = ' ,  key,' : ' ,val   )
        # print('next_SETS : ', len(SETS2)   , SETS2 )
        #   Make a copy of the previous SET :
        SETS = SETS2.copy()

    ### final Step is to POP OUT the last duplicates :
    for k, v in DUPLIQ.items():
        if k in SETS :
            SETS.pop(k)

    print('\nFINAL SETS : ', len(SETS), SETS)

    UNIQUE_SUM = sum( k for k, v in SETS.items() )
    print('\nUNIQUE_SUM = ', UNIQUE_SUM)


# solution_attempt2_(10, 5)


t2  = time.time()
print('\n# Completed in :', round((t2-t1), 2 ), 's\n\n')

print('\n==========   My THIRD SOLUTION,  not mine  ===============\n')
t1  = time.time()


def solution(max_nr, Set_size) :


    S = [ i*i for i in range(1, max_nr+1) ]
    print(S)
    T = { k:{} for k in range(len(S)+1 ) }
    T[0][0] = 1
    print(T)

    for i in range(len(S)) :
        U = {}
        for subset_size in T:
            if subset_size < Set_size :

                for subset_sum in T[subset_size] :
                    new_size = subset_size + 1
                    new_sum = subset_sum + S[i]

                    if new_size not in U :
                        U[new_size] = {}

                    if new_sum not in U[new_size] :
                        U[new_size][new_sum] = 0

                    U[new_size][new_sum] += T[subset_size][subset_sum ]

        for subset_size in U :
            for subset_sum in U[subset_size] :
                if subset_sum not in T[subset_size] :
                    T[subset_size][subset_sum] = 0
                T[subset_size][subset_sum] += U[subset_size][subset_sum]

        # print('U : ', U)
    # print(T)

    X = { k for k,v in T[Set_size].items() if v == 1 }
    # print('X : ', X )

    print('\nANSWER :      ' , sum(X )  )           #   115039000


max_nr = 10
Set_size = 5

solution( max_nr = 10 , Set_size = 5  )

t2  = time.time()
print('\n# Completed in :', round((t2-t1),2), 's\n\n')

'''                 =====   GENERAL IDEAS       =====
===  Sun, 18 Mar 2012, 02:52, viv_ban, India
I have learnt four things from this problem:
1)Never use python to solve problems that use brute force.
2)Most of the time it is just my mental block that stops me to solve problem.
3)Always think simple
4)Every problem - no matter how apparently difficult it may be - looks simple once you solve it.

'''

print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 0,  DYNAMIC PROGRAMMING --------------------------')
t1  = time.time()

''' ====    Mon, 29 Sep 2008, 02:04, drw, Russia
Another solution using generating functions.
'''

from numpy import array, polyadd, zeros, concatenate

N = 100
M = 50

l = [array([1])] + [array([0])]*M

def mul(a, cutoff=0):
    zr = zeros(a)
    for i in reversed(range(cutoff,M)):
        l[i+1] = polyadd(l[i+1], concatenate((l[i], zr)))

for x in range(1,N+1):
    mul(x**2, max(x-(N-M+1), 0))

m = len(l[M])
print(sum(m-1-i for i in range(m) if l[M][i] == 1))


t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')

print('\n--------------------------SOLUTION 1,  DYNAMIC PROGRAMMING --------------------------')
t1  = time.time()

''' ====    Tue, 14 Jul 2015, 21:38, cburschka, Switzerland

DP, but a fairly inefficient implementation (1-2 minutes).
'''

def dp(S, k):
    D = [{} for i in range(k+1)]
    D[0][0] = 1
    N = len(S)
    for j,x in enumerate(S):
        print(j)
        E = [d.copy() for d in D]
        for i in range(max(k-N+j,0),k):
            for s in D[i]:
                if s+x not in E[i+1]:
                    E[i+1][s+x] = 0
                E[i+1][s+x] += D[i][s]
        D = E
    return sum(x for x in D[k] if D[k][x] == 1)


def main():
    set_size = 10
    max_nr = 20
    print(dp({ i*i for i in range( 1, max_nr+ 1 )}, set_size ))

# main()


t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')


print('\n--------------------------SOLUTION 2, 6 seconds,  OUTSTANDING SOLUTION  --------------------------')
t1  = time.time()

'''
Sat, 24 Oct 2015, 19:02, yigalzeg, ISrael
I implemented a (somewhat) vectorized python+numpy version of the simple DP solution.
My code runs in about 3.5 seconds on my i5-2.5Ghz laptop.

I estimate that a pure python implementation would run in about 1-2 minutes.

I thought of another solution that could have been faster, but i did not implement it due to laziness:

Given a set S, consider the polynomial f_S(x,y) with coefficient c(i,j) equals the number of subsets of size i and sum j.

Now, divide S into two subsets, and compute recursively the matching polynomials for each one.

You get that if S=S1∪S2 => f_S=f_S1×f_S2. 

The important thing here, is that the product can be computed efficiently using fft. 
If my calculations are correct, i estimate that this would take about 2**27 operations all in all, 
    which is much less than the 2**31 solution i ended up implementing.

'''

def matrix_numpy() :
    import numpy as np

    my_set = [i**2 for i in range(1, 101)]
    max_size = 50
    max_sum = sum(sorted(my_set)[-max_size-1:])


    my_data = [np.array([0 for i in range(max_sum)], dtype='uint16') for i in range(max_size + 1)]
    my_data[0][0] = 1

    for i in my_set:
        for j in range(max_size, 0, -1):
            my_data[j][i:] += (my_data[j-1][:-i])


    print( sum([i for i in range(max_sum) if my_data[max_size][i] == 1]) )

# matrix_numpy()


t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')


print('\n--------------------------SOLUTION 3,  THE BEST --------------------------')
t1  = time.time()

'''  ===Tue, 31 May 2016, 09:53, lord.sidious
Dynamic programming using numpy in python.  Takes about 8 seconds on an old Core 2 Duo P8600 2.40GHz
'''

from numpy import zeros, int32

def euler201(numbers, deg):
    numbers.sort()
    min_sum = sum(numbers[:deg])
    max_sum = sum(numbers[deg:])

    x = zeros((deg + 1, max_sum + 1), dtype=int32)
    y = zeros((deg + 1, max_sum + 1), dtype=int32)
    y[0, 0] = 1

    for e in numbers:
        e2 = max_sum - e + 1
        e3 = e + e2

        x[0, 0] = 1

        x[1:deg + 1, 0:e] = y[1:deg + 1, 0:e]
        x[1:deg + 1, e:e3] = y[0:deg, 0:e2]
        x[1:deg + 1, e:e3] += y[1:deg + 1, e:e3]

        x, y = y, x

    ans = 0
    for s in range(min_sum, max_sum + 1):
        if y[deg, s] == 1:
            ans += s

    return ans


assert euler201([1, 3, 6, 8, 10, 11], 3) == 156

print( euler201([n**2 for n in range(1, 101)], 50)  )

t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')


print('\n--------------------------SOLUTION 4,   --------------------------')
t1  = time.time()

''' === Mon, 25 Dec 2017, 05:41, fakesson, Sweden
1.0 s using Python / numpy. 

As most people, I used DP to keep track of the number of ways each possible sum can be constructed 
by x terms only using the first y terms of 12,22,….
 
 I used numpy's matrix operations make the code faster. 
 The trick (which I've used for several other DP PE problems) is to use indexes in the reverse order, 
 which ensures that elements are processed in the right order, 
 without overriding any element by accident. 
 Unfortunately, this make the code a bit harder to read.

(For the general case, it's possible that there is a minuscule risk that my code will 
give the wrong answer, as I'm allowing int64 to overflow and then assume that I won't get 1 by a coincide.)

'''

def euler201(L=100,t=50):
    import numpy as np
    sLst = [i*i for i in range(L+1)]
    sLstSum = sum(sLst)
    xLst = np.zeros((sLstSum+1,t+1), dtype=np.int64)
    xLst[sLstSum-0,t-0] = 1
    L1 = 0
    L2 = 1
    for s in sLst:
        xLst[sLstSum-L1-s:-s,-L2-1:-1] += xLst[sLstSum-L1:,-L2:]
        L1 += s
        if L2 < t:
            L2 += 1
    r = 0
    for i in range(sLstSum+1):
        if xLst[sLstSum-i,0] == 1:
              r += i
    return r

euler201()

t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')


print('\n--------------------------SOLUTION 5,  CRAZY SPEED  --------------------------')
t1  = time.time()

import numpy as np
import time

def main():

    N=100
    L=50
    elements = np.arange(1, N+1)**2
    M=elements.sum()

    nb_subsets = np.zeros( (M+1,L+1), dtype=int)
    nb_subsets[0,0]=1
    E=0

    for n,e in enumerate(elements):
        n = max(0,L-N+n) #min length
        E += e #max sum
        nb_subsets[e:E+1,1+n:L+1] += nb_subsets[:E+1-e,n:L].copy()

    sums = np.arange(M+1)
    return np.sum (sums[nb_subsets[:,L]==1] )



if __name__=='__main__':

    start = time.process_time()
    result = main()
    end = time.process_time()

    print("result : {} in {:.2f}s".format(result,end-start))

t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')


print('\n--------------------------SOLUTION 6, VERY SIMPLE    --------------------------')
t1  = time.time()

''' ===Sat, 14 Apr 2012, 06:40, ving, USA.

A more streamlined and faster version with a sparce-matrix representation of the sum-counts table:
'''

N = 10  # Answer: 15785
N = 50  # Answer: 7383100
N = 100  # Answer: 115039000

def get_sum_counts(nums, m):
    cnts = [{0:1}]
    for x in nums:
        k = len(cnts)
        if k <= m:
            cnts.append({})
            k += 1
        for j in range(k-1, 0, -1):
            prevsums, sums = cnts[j-1], cnts[j]
            for s in prevsums:
                sx = s + x
                if sx in sums:
                    sums[sx] += prevsums[s]
                else:
                    sums[sx] = prevsums[s]
    return cnts[-1]

def solution6():
    nums = [x*x for x in range(1, N+1)]
    sums = get_sum_counts(nums, N//2)
    print(sum(s for s in sums if sums[s] == 1))




t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')


print('\n--------------------------SOLUTION 7, VERY SIMPLE SOL  --------------------------')
t1  = time.time()


''' === Tue, 26 Jun 2012, 04:38,  MrDrake
Wow... this was easier than I thought... 15.5s on a crappy MacBook.
'''

solution7() :
    sets = [{} for i in range(51)]
    sets[0][0] = 1

    for i in range(1, 101):
        for j in range(49, max(-1, i-52), -1):
            for k in sets[j]:
                z = k+i**2
                if z not in sets[j+1]: sets[j+1][z] = 0
                sets[j+1][z] += sets[j][k]


    print( sum([i for i in sets[50] if sets[50][i] == 1]))

t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')


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




