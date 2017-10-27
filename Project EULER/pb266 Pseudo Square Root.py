#!/usr/bin/python                   o(^_^)o
# Solved by Bogdan Trif @       Completed on Fri, 13 Oct 2017, 22:34
#The  Euler Project  https://projecteuler.net
'''
Pseudo Square Root      -       Problem 266

The divisors of 12 are: 1,2,3,4,6 and 12.
The largest divisor of 12 that does not exceed the square root of 12 is 3.
We shall call the largest divisor of an integer n that does not exceed the square root of n the pseudo square root (PSR) of n.

It can be seen that PSR(3102)=47.

Let p be the product of the primes below 190.
Find PSR(p) mod 10**16.


'''
import operator
import time, math, zzz
import  itertools
from functools import reduce
from operator import mul
from itertools import combinations, cycle
from math import sqrt, log2, log10, log

import sys

from decimal import Decimal

import functools


def prime_generator(lower, upper):      #THIRD FASTEST
    """  Sieve of Eratosthenes              !!!!!!!!! THE FASTEST SIEVE. It won the battle with sieve
    Create a candidate list within which non-primes will be marked as None.         """
    cand = [i for i in range(3, upper + 1, 2)]
    end = int(upper ** 0.5) // 2

    # Loop over candidates (cand), marking out each multiple.
    for i in range(end):
        if cand[i]:
            cand[cand[i] + i::cand[i]] = [None] * ( (upper // cand[i]) - (upper // (2 * cand[i])) - 1 )

    # Filter out non-primes and return the list.
    return [2] + [ i for i in cand if i and i > lower ]

def get_factors(n):       ### o(^_^)o  FASTEST  o(^_^)o  ###
    ''' Decompose a factor in its prime factors. This function uses the pyprimes module. THE FASTEST  '''
    from pyprimes import factorise
    return [val for sublist in [[i[0]]*i[1] for i in factorise(n)] for val in sublist]

def get_divisors(n):      ### ( ͡° ͜ʖ ͡°)  FASTEST  ( ͡° ͜ʖ ͡°)  ### !! FIRST FASTEST
    from math import sqrt
    factors = set()
    for x in range(1, int(sqrt(n)) + 1):
        if n % x == 0:
            factors.add(x)
            factors.add(n//x)
    return sorted(factors)

def binary_search(n, List, direction ):        # VERY FAST ALGORITHM
    ''':Description: Search for an element in the list and returns the index of it. If it not finds it returns
        the index of the element closest to its left, the smaller number.
        :OBSERVATION:  direction argument +1 means to the right ; -1 to the left
    :param: **n**- integer, the number to find
                **List** - lst type, the list to search for
    :returns:   int, the index of the element               '''
    if direction == -1 : alpha = 0
    if direction == 1 : alpha = +1

    left = 0
    right = len(List) -1

    while left <= right:
        midpoint = (left+right)//2
        if List[midpoint] == n: return midpoint
        elif List[midpoint] > n: right = midpoint-1
        else: left = midpoint+1
    if n > List[midpoint]: return midpoint + alpha
    else: return (midpoint-1+alpha )

P_primes = prime_generator(1,190)
print(len(P_primes) ,P_primes)

def rotate(l, n):     return l[-n:] + l[:-n]

# Q : How to find the divisors of a very huge number ?
# Q2 : How to find the midle divisor, closest to the square root ?
# A2 : You try to equilibrate all the factors. For example : in 3102 with factors [2,3,11, 47]
# they are best equilibrated wheh  pair 1 is [2*3*11] = 66   and pair 2 is 47 .  abs(diff) = 66-47 = 19
# No other pairs can have a smaller diff :

print('\n-------------------------- TESTS  ------------------------------')

# p = reduce( mul , P_primes )
# print('p : \t' ,len(str(p)), p, '\n' )


def build_pairs( ordered_lst ) :
    pair1, pair2 = [], []
    for i in range( len(ordered_lst)//2 ) :
        if len(pair1) %2 == 0 :
            pair1.append( ordered_lst[2*i] ) ;
            pair2.append( ordered_lst[2*i+1] )
        else :
            pair1.append( ordered_lst[2*i+1] )
            pair2.append( ordered_lst[2*i] )
    return pair1, pair2


BP = build_pairs(P_primes)
print('\nbuild_pairs : \t ',  BP )



print('\n--------------------------BRUTE FORCE  TESTING ------------------------------')
t1  = time.time()

test_A =  [2,3,5,7,11,13,17,19,23,29, 31,37]
sqr = (reduce(mul, test_A) )**(1/2)

def brute_force_testing( lst, sqr ) :
    A, B = 0, 0
    C = list(combinations(test_A, len(test_A)//2   ))
    print(len(C))

    mmin = 10**8
    for i in C :
        r = reduce(mul, i)
        if abs(sqr - r) <= mmin :
            mmin = abs(sqr - r)
            print(r , i , sqr-r , '    ', sqr)
            A, B = i, list( set(lst)-set(i) )
    return A, B

A, B = brute_force_testing(test_A, sqr )

print('\n',A, B)
a, b = reduce(mul, A), reduce(mul, B)
print('\nList 1 : \t' , a, len(str(a)), '\nList 2 : \t' ,  b , len(str(b)) ,'\nDIFF = \t' ,abs(a-b), len(str(abs(a-b))) )
print( 'sqrt(test_A): \n',len(str(round(sqr) )), round(sqr) )


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n================  My UGLY INEFFICIENT FIRST SOLUTION,   ===============\n')
t1  = time.time()

# My idea is to use logarithm to all the numbers because we can treat then the problem as a
# SUBSET SUM PROBLEM which has solutions because of the logarithms properties :
# log(a_1 + a_2 +...+ a_n ) = log(a_1) * log(a_2)* ... * log(a_n)


P = prime_generator(1,190)
print ( len(P_primes) ,P_primes)


# def balanced_pair_lists_products(lst ) :
#     U = lst[ : len(lst)//2 ]
#     V = lst[  len(lst)//2 : ]
#     print('Initial lists : \nList 1 :\t',U, '\nList 2 : \t',V,'\n')
#     REF = 10**48
#     for zz in range(2) :
#         print('\n ++++++++++  Main Iteration : ', zz ,'   +++++++++++')
#         u, v = reduce(mul, U), reduce(mul, V)
#         if u < v :
#             i = 0
#             while u < v :       # CASE  1
#                 t = binary_search( U[i] ,V , 1)
#
#                 if t >= len(V)  :
#                     print('Special : ' ,t, '   ',i ,V[i])
#                     t = binary_search( U[i] ,V , -1 )
#                 # if  U[i] < V[t] :
#                 print( '\nList 1 : ' , i, U[i] ,  '        List 2 : ' ,t, V[t]  , '  <------------ CASE 1','       ' )
#                 print('',U, reduce(mul, U) ,'        ',V  , reduce(mul, V), '        ', REF )
#                 temp_U = U[:] ; temp_U.remove(U[i] ) ; temp_U.append(V[t]) ; temp_U.sort()
#                 temp_V = V[:] ; temp_V.remove(V[t]) ; temp_V.append(U[i]) ; temp_V.sort()
#                 u_temp, v_temp = reduce(mul, temp_U), reduce(mul, temp_V)
#
#                 if (abs( u_temp - v_temp ) <  abs( u - v ) ) :
#                     # if (abs( u_temp - v_temp ) < REF) :
#                     U, V = temp_U[:], temp_V[:]
#                     REF = abs( u_temp - v_temp )
#                     print(U, reduce(mul, U) ,'        ',V  , reduce(mul, V) , '        ', REF)
#                     u, v = reduce(mul, U), reduce(mul, V)
#
#
#                 i+=1
#                 if i >=len(U) : break
#
#
#         if u > v :      #CASE 2
#             i = 0
#             while u > v :
#                 t = binary_search( V[i] ,U , 1 )
#                 if t >= len(V)  :
#                     print('Special : ' ,t, '   ',i ,V[i])
#                     t = binary_search( V[i] ,U , -1 )
#                 print( '\nList 1 : ' , t, U[t] ,  '        List 2 : ' ,i, V[i]  , '  <------------ CASE 2','       ' )
#                 print('',U, reduce(mul, U) ,'        ',V  , reduce(mul, V),  '        ', REF )
#                 temp_U = U[:] ; temp_U.remove(U[t] ) ; temp_U.append(V[i]) ; temp_U.sort()
#                 temp_V = V[:] ; temp_V.remove(V[i]) ; temp_V.append(U[t]) ; temp_V.sort()
#                 u_temp, v_temp = reduce(mul, temp_U), reduce(mul, temp_V)
#
#                 if (abs( u_temp - v_temp ) <  abs( u - v ) ) :
#                     # if (abs( u_temp - v_temp ) < REF) :
#                     U, V = temp_U[:], temp_V[:]
#                     REF = abs( u_temp - v_temp )
#                     print(U, reduce(mul, U) ,'        ',V  , reduce(mul, V) , '        ', REF )
#                     u, v = reduce(mul, U), reduce(mul, V)
#
#                 i+=1
#                 if i >= len(V) : break
#     return U , V

# A, B = balanced_pair_lists_products(W)
# A, B = balanced_pair_lists_products(P_primes)

def balanced_pair_lists_products(lst , alpha) :
    U = lst[ : len(lst)//2 ]
    V = lst[  len(lst)//2 : ]
    print('Initial lists : \nList 1 :\t',U, '\nList 2 : \t',V,'\n')
    DIFF, A, B = 10**48, [], []
    u, v = reduce(mul, U), reduce(mul, V)
    key=[   -2, -1, 1, 2, 3 ]
    Cyc = cycle(key)
    for loop in range(20) :
        c = next(Cyc)
        U = rotate(U, 2)

        for lup in range(alpha) :
            # print(U, reduce(mul, U) ,'        ',V  , reduce(mul, V) , '        ', REF )
            a, b = U[0], V[0]
            # if a < b :
            t_U = U[:] ; t_U.remove(a ) ; t_U.insert(0, b)
            t_V = V[:] ; t_V.remove(b ) ; t_V.insert(0, a)
            u_check, v_check = reduce(mul, t_U), reduce(mul, t_V)
            val = abs(u_check - v_check)
            # if  val < abs(u-v)  :
            U, V = t_U[:], t_V[:]
            u, v = reduce(mul, U), reduce(mul, V)

            if abs(u-v) < DIFF :
                DIFF = abs(u-v)
                A, B = U[:], V[:]
                print(U, reduce(mul, U) ,'        ',V  , reduce(mul, V) , '        ', DIFF )
            d = next(Cyc)
            V = rotate(V, -1)
    return sorted(A), sorted(B), DIFF


print('\nAlgorithm to find which number in a list sum up to a certain number')

'''
http://stackoverflow.com/questions/3420937/algorithm-to-find-which-number-in-a-list-sum-up-to-a-certain-number
'''

def stackoverflow(x_list, target):
    memo = dict()
    result, _ = g(x_list, x_list, target, memo)
    return (sum(result), result)


def g(v, w, S, memo):
    subset = []
    id_subset = []
    for i, (x, y) in enumerate(zip(v, w)):
        # Check if there is still a solution if we include v[i]
        if f(v, i + 1, S - x, memo) > 0:
            subset.append(x)
            id_subset.append(y)
            S -= x
    return subset, id_subset


def f(v, i, S, memo):
    if i >= len(v):
        return 1 if S == 0 else 0
    if (i, S) not in memo:    # <-- Check if value has not been calculated.
        count = f(v, i + 1, S, memo)
        count += f(v, i + 1, S - v[i], memo)
        memo[(i, S)] = count  # <-- Memoize calculated result.
    return memo[(i, S)]       # <-- Return memoized value.


def find_partition(int_list):
    "returns: An attempt at a partition of `int_list` into two sets of equal sum"
    A = set()
    B = set()
    for n in sorted(int_list, reverse=True):
        if sum(A) < sum(B):
           A.add(n)
        else:
           B.add(n)
    return A, B


# P = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181]
print(P)
Log = [ log2(i ) for i in P ]
# print('\nLog : ',Log)

target = sum(Log)/2
print('target = ', target )

# log_res = stackoverflow(Log, target)
# print('\nresult : ', log_res )

# X = find_partition(Log)

# With 10 combinations I arrived here :
X1 = [5, 11, 17, 23, 29, 31, 37, 47, 53, 59, 67, 71, 83, 89, 97, 103, 107, 127, 157, 163, 181]
X2 = [2, 3, 7, 13, 19, 41, 43, 61, 73, 79, 101, 109, 113, 131, 137, 139, 149, 151, 167, 173, 179]

LOG_OP = lambda lst : [ log2(i) for i in lst ]

print('\nX1 = ',X1)
print('X2 = ',X2,'\n')

Y1 = set(LOG_OP(X1))
Y2 = set(LOG_OP(X2))


X = lambda lst : sorted([round(2 **i) for i in lst ])

# X1 =X(Y1)
# X2 =X(Y2)



print(' Sum Y1 =',sum(Y1) , '     Sum Y2 = ',sum(Y2)  , '     Diff =',abs(sum(Y1) - sum(Y2) ) )

Prod = lambda lst : reduce(mul, lst)

x1, x2 = Prod(X1), Prod(X2)
print('x1 = ', x1 )
print('x2 = ', x2  )

print('\nX1   len=' , len(X1),'    ' ,X1, '      ',  x1,'           ', x1%(10**16) )
print('X2    len=' , len(X2), '   ',X2 , '    ',  x2 ,'           ', x2%(10**16) )


print('-------'*20)

def some_solution(Y1, Y2, nr_of_repetitions) :
    if nr_of_repetitions == 0 :
        return Y1, Y2

    for i in range(7, 22) :
        c1 = list(itertools.combinations(Y1, i ))
        cnt = 0
        for j1 in c1 :
            cnt += 1
            sys.stdout.write('\r' + str(cnt)+'.   ' +  '          i =   ' + str(i)  )   # Font Segoe UI Semibold
            sys.stdout.flush()
            c2 = list(itertools.combinations(Y2, i ))
            for j2 in c2 :
                if abs( sum(j1)- sum(j2) ) < abs( sum(Y1)-sum(Y2) )/ 2 :
                    print(' =========   ', i,'  ====    ',nr_of_repetitions,'   =======')
                    if sum(j1)-sum(j2) < 0 and sum(Y1) < sum(Y2) :
                        print('case1 :    n1= ' , sum(j1) ,'   n2= ',sum(j2), '       Diff=   ' , abs( sum(Y1)-sum(Y2) )/2 ,'     ', j1, j2)
                        Y1= Y1.union(set(j2)) ; Y1 =Y1.difference(set(j1))
                        Y2 =Y2.difference(set(j2)) ; Y2 =Y2.union(set(j1))
                        print('\nX1 :' ,X(Y1))
                        print('X2 :' ,X(Y2))
                        print('x1 = ', Prod(X(Y1)) ,  Prod(X(Y1)) %(10**16) )
                        print('x2 = ', Prod(X(Y2)),  Prod(X(Y2)) %(10**16) )
                        return some_solution(Y1, Y2, nr_of_repetitions-1)

                    if sum(j1)- sum(j2) > 0 and sum(Y1) > sum(Y2) :
                        print('case2 :     n1= ' ,sum(j1),'    n2= ' ,sum(j2), '       Diff=   ' , abs( sum(Y1)-sum(Y2) )/2 ,'     ', j1, j2)
                        Y1= Y1.union(set(j2)) ; Y1 =Y1.difference(set(j1))
                        Y2 =Y2.difference(set(j2)) ; Y2 =Y2.union(set(j1))

                        print('\nX1 :' ,X(Y1))
                        print('X2 :' ,X(Y2))
                        print('x1 = ', Prod(X(Y1)) ,  Prod(X(Y1)) %(10**16) )
                        print('x2 = ', Prod(X(Y2)),  Prod(X(Y2)) %(10**16) )
                        return some_solution(Y1, Y2, nr_of_repetitions-1)

# A = some_solution(Y1, Y2, 1000)             # Answer : 1096883702440585

# 9212.             i=   7 =========    7   ====     1000    =======
# case1 :    n1=  36.334425583725015    n2=  36.33442558617261        Diff=    2.461518988639e-09       (1.0, 3.700439718141092, 5.357552004618084, 5.930737337562887, 6.303780748177103, 7.383704292474052, 6.658211482751795) (2.321928094887362, 3.4594316186372973, 4.954196310386875, 5.554588851677638, 6.149747119504682, 6.599912842187128, 7.294620748891627)
# X1 : [5, 11, 17, 23, 29, 31, 37, 47, 53, 59, 67, 71, 83, 89, 97, 103, 107, 127, 157, 163, 181]
# X2 : [2, 3, 7, 13, 19, 41, 43, 61, 73, 79, 101, 109, 113, 131, 137, 139, 149, 151, 167, 173, 179]
# x1 =  2323218950659046189161096883702440585 1096883702440585
# x2 =  2323218950703910704013480747339996674 3480747339996674



# https://www.google.ro/search?q=subset+product+problem&*&cad=h
# https://www.google.ro/search?q=subset+sum+problem&oq=subset+sum+problem&gs_l=psy-ab.3..0i67k1j0l9.23197.23475.0.23876.3.3.0.0.0.0.132.361.0j3.3.0....0...1.1.64.psy-ab..0.3.359...0i7i30k1.0.gvpvfqlCaa4

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n========  My SECOND SOLUTION,  O(2^n)  After learning on Euler Forum, 12 sec ===============\n')
t1  = time.time()

def closest_product_subset_list_algorithm() :

    primes = prime_generator(2, 190)
    print(primes)
    P1 = primes[:len(primes)//2]
    P2 = primes[len(primes)//2:]

    print(P1)
    print(P2)

    Q1, Q2 = [1], [1]
    for i in P1 :
        Q1 += [ i*j for j in Q1 ]

    for i in P2 :
        Q2 += [ i*j for j in Q2 ]


    Q1 = sorted(Q1, reverse=False)
    Q2 = sorted(Q2, reverse=True)
    print(Q1[:50])
    print(Q2[:50])

    # === Same result can be achieved with the following approach
    def all_factors_combinations(lst) :
        ''' Returns the combinations of all elements from a list, preferable a prime factor list'''
        L =[1]
        for i in range(1, len(lst)+1 ) :
            c = list(combinations(lst, i))
            for j in c :
                L.append( functools.reduce(operator.mul, j) )
                # print(L)
        print(L)
        return L
    # all_factors_combinations(P1)

    l1, l2, = len(Q1), len(Q2)
    print('---- Those two approaches are also equivalent ---- NICE !! ---')
    target = sqrt( functools.reduce(operator.mul, P1+P2) )
    target2 = sqrt( Q1[-1] * Q2[0] )
    print('target1 = ',target ,'      target2 = ', target2)

    ### Main solution
    i, j, best = 0, 0, 0
    while i< l1 and j < l2 :
        curr_prod = Q1[i]*Q2[j]
        # print(curr_prod)
        if curr_prod > target :
            j += 1
        elif curr_prod < target :
            if curr_prod > best :
                best = curr_prod
                print('best = ', best)
            i += 1

    print('\nResult : \t',best)

    R1 = get_factors(best)
    print('the primes of the first half list are : ', R1)

    R2 = (set(primes)).difference(set(R1))
    print('the primes of the second half list are : ', sorted(list(R2)))



    return print('\nthe last 16 digits are : ', best%(10**16))

# closest_product_subset_list_algorithm()

t2  = time.time()
print('\nCompleted in :', round((t2-t1) ,4), 's\n\n')


print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n-------------------- SOLUTION 1,  FLAWLESS MAGIC SOLUTION, Must study it --------------------------')
t1  = time.time()

# ==== Sat, 28 Nov 2009, 15:32, Obergscheidle, Luxembrourg
# Third!
# 16 seconds in Python, essentially the same as wrongrook's second scheme

def solution1() :
    prods1,prods2 = [1],[1]

    for p in [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73]:
        prods1 += [x*p for x in prods1]

    for p in [79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181]:
        prods2 += [x*p for x in prods2]

    prods1.sort()
    prods2.sort(reverse=True)
    target = (prods1[-1]*prods2[0])**0.5
    l1,l2 = len(prods1),len(prods2)

    i=j=best=0
    while i<l1 and j<l2:
        current = prods1[i]*prods2[j]
        if current>target:
            j+=1
        elif current<target:
            if current>best: best=current
            i+=1

    return print(best, best%(10**16) )

# solution1()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000, 6), 'ms\n\n')



t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------- SOLUTION 2   --------------------------')
t1  = time.time()

print('\n--------------- SOLUTION 2,  WORSE SCHEME ,  1 min --------------------------')
# WORSE SCHEME
# The first approach I tried was scanning back from the sqrt looking for values which
# could be constructed from the known primes.  However, this seems to take a very long time
# (order distance between the sqrt and the actual answer) so is definitely not to be recommended!

import bisect

def makeprods(ps):
    t=len(ps)
    S=[]
    for n in range(2**t):
        p=1
        for b in range(t):
            if n&(1<<b):
                p*=ps[b]
        S.append(p)
    S.sort()
    return S


def euler266():
    ps=prime_generator(2, 190 )
    s=1
    for p in ps:
        s*=p
    a=Decimal(s)
    start=int(a.sqrt())
    S=makeprods(ps[0:21])
    S2=makeprods(ps[21:])
    print( 'searching')
    maxt=0

    for s2 in S2:
        t=start//s2
        s1=bisect.bisect(S,t)
        while (s1<len(S)-1) and (S[s1]*s2)**2<s:
            s1+=1
        if s1>=len(S): continue

        while (s1>0) and (S[s1]*s2)**2>s:
            s1-=1
        s1=S[s1]
        if (s1*s2)**2>s: continue

        if (s1*s2>maxt):
            maxt=s1*s2
            print (maxt,s-maxt*maxt)

# euler266()

print('\n---------------- IMPROVED SOLUTION , 45 sec------------------')

# BETTER SCHEME
# A better scheme is to scan the lists in parallel, one going forward,
# and one backward based on whether the current product was above or below the target.
# (Would be even faster if I trusted the precision of sqrt as could avoid the squaring operation in the loop)

def second_euler266():
    ps=prime_generator(2, 190)
    s=1
    for p in ps:
        s*=p
    S=makeprods(ps[0:21])
    S2=makeprods(ps[21:])
    maxt=0
    j=len(S2)-1

    for s1 in S:
        while j>0 and (s1*S2[j])**2>s:
            j-=1
    if j==0:
        return
    if s1*S2[j] > maxt:
        maxt=s1*S2[j]
        print (maxt)

# second_euler266()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 3,   --------------------------')
t1  = time.time()

#!/usr/bin/env python

from math import sqrt, ceil
from operator import mul
# import psyco
#
# psyco.full()

p = prime_generator(2, 190)
N = reduce(mul, p, 1)
sqn = int(sqrt(N))
lp = len(p)//2
p1 = p[:lp]
p2 = p[lp:]

def products(v):
    r = set([1])
    for vv in v:
        r = r.union(set([w * vv for w in r if w * vv <= sqn]))
    return sorted(r)

def search(v, prod):
    t = sqn // prod
    lo, hi = 0, len(v)
    while lo < hi:
        m = (hi+lo)//2
        if v[m] <= t:
            lo = m+1
        else:
            hi = m
    return v[lo-1]


def p266():
    prod1 = products(p1)
    prod2 = products(p2)
    r = 0
    for v in prod1:
        t = search(prod2, v)
        if r < v*t:
            r = v*t
    print( 'Complete solution : %d' % r)
    print( 'Modular solution  : %d' % (r % 10**16))

# p266()

# Complete solution : 2323218950659046189161096883702440585
# Modular solution  : 1096883702440585
# p266 took 20.6450029 s

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 4,  SLOW  --------------------------')
t1  = time.time()

# ====Tue, 1 Dec 2009, 20:07, Yuval Dor, Israel
# It's similar to what I did at first. It finds good solutions instantly, but not the result
# (I found a '232188' after a minute, the result is '232189').
# By bruteforce what I think is meant is simply searching for results recursively,
# stopping when the result is bigger than max,
# and making sure that it's still bigger than the best you have if you use all the primes left.
#
# I added logs, made it iterative, and by using a heap made sure values close to square root are investigated first.
# Another small optimization is to use the big primes first to make results more balanced.
#
# Frankly, I have no idea how come it works in C++. But consider the fact there are only 10^12 divisors or so,
# and you filter them out, and use a rather simple operation - adding floats. So it is not completely impossible.

def solution4() :

    import heapq
    import math

    n = 190
    primes = [p for p in range(2, n + 1) if all(p % d for d in range(2,p))]
    plogs = [math.log(p) for p in range(2, n + 1) if all(p % d for d in range(2,p))]
    dmax = math.fsum(plogs) / 2
    s = 1 << (len(plogs) + 1)
    lefts = [0] * len(plogs)
    lefts[0] = plogs[0]
    for i in range(1,len(plogs)):
        lefts[i] = lefts[i-1] + plogs[i]

    diffbest = dmax
    xbest = 0
    heap = [(dmax, 0, s, len(primes))]
    while heap:
        diff, x, ss, i = heapq.heappop(heap)
        if diff < diffbest:
            diffbest = diff
            c = 1
            xbest = x
            for ii in range(len(primes)):
                if ss & (1 << ii):
                    c *= primes[ii]
            print(c)

        for ii in range(i - 1,-1,-1):
            if x + plogs[ii] < dmax:
                if x + lefts[ii] > xbest:
                    heapq.heappush(heap, (dmax - x - plogs[ii], x + plogs[ii], ss | (1 << (ii)), ii))


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 5, A Little SLOW  --------------------------')
t1  = time.time()

def solution5() :
    from itertools import compress, product
    from functools import reduce
    from operator import mul

    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181]
    goal = (reduce(mul, primes))**0.5
    arr1, arr2 = primes[:23], primes[23:]

    a = sorted(reduce(mul, compress(arr1, pattern), 1) for pattern in product(*[(0,1)]*len(arr1)))
    b = sorted(reduce(mul, compress(arr2, pattern), 1) for pattern in product(*[(0,1)]*len(arr2)))

    best = 0
    pa, pb = 0, len(b)-1
    while pa < len(a):
        while a[pa] * b[pb] > goal: pb -= 1
        best = max(best, a[pa] * b[pb])
        pa += 1
    print( best % 10**16 )

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
#
print('\n--------------------------SOLUTION 6,  30 sec  --------------------------')
t1  = time.time()

def solution6():
    from itertools import chain, combinations
    from bisect import bisect
    from math import log10


    primes = prime_generator(2, 190)
    logp = {p: log10(p) for p in primes}
    target = sum(logp.values())/2

    divs = [(0,(1,))]
    for c in chain.from_iterable((combinations(primes[21:],r) for r in range(1,22))):
        divs.append((sum(logp[p] for p in c),c))
    divs = sorted(divs)

    maxlog = 0
    factors = (0,)
    for c in chain.from_iterable((combinations(primes[:21],r) for r in range(1,22))):
        a = sum(logp[p] for p in c)
        ind = bisect(divs, (target-a,))-1
        if a+divs[ind][0] > maxlog:
            maxlog = a+divs[ind][0]
            factors = c + divs[ind][1]

    ans = 1
    for p in factors:
        ans *= p

    return print(ans%10**16)

# solution6()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

