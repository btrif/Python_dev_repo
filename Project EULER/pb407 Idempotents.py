#!/usr/bin/python
# Solved by Bogdan Trif @           Completed on Sun, 12 Mar 2017, 11:25
#The  Euler Project  https://projecteuler.net
'''
                            Idempotents     -       Problem 407

If we calculate a**2 mod 6 for 0 ≤ a ≤ 5 we get: 0,1,4,3,4,1.

The largest value of a such that    :   a**2 ≡ a (mod 6)        is = 4.
Let's call M(n) the largest value of a < n such that            :       a**2 ≡ a (mod n).
So M(6) = 4.

Find ∑M(n) for 1 ≤ n ≤ 10**7.


'''
import time, gmpy2, zzz
from math import log, gcd
from itertools import combinations
from functools import reduce
from operator import mul

def primesieve(n):          ### o(^_^)o  FASTEST  o(^_^)o  ###  Highly Efficient !!!
    import numpy as np
    """return array of primes 2<=p<=n"""
    sieve=np.ones(n+1,dtype=bool)
    for i in range(2, int((n+1)**0.5+1)):
        if sieve[i]:
            sieve[2*i::i]=False
    return np.nonzero(sieve)[0][2:]

def get_factors(n):       ### o(^_^)o  FASTEST  o(^_^)o  ###
    ''' Decompose a factor in its prime factors. This function uses the pyprimes module. THE FASTEST  '''
    from pyprimes import factorise
    return [val for sublist in [[i[0]]*i[1] for i in factorise(n)] for val in sublist]

def egcd(a, b):         #Extended Euclidian Algorithm
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)



def modinv(a, m):       # Modular Inverse
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


def sieve_factorization(n):   # Sieve Factorization and Totient Sieve at once
    ''':Description: Sieve Factorization and Totient Sieve at once
        The factorization is done only with the largest prime powers
        This is needed for the Idempotents Euler Problem 407             '''

    from collections import defaultdict
    F = defaultdict(list)
    T = list(range(n+1))
    for p in range(2, n+1):
        if p not in F :
            T[p] = p-1
            for i in range(p+p, n+1, p ) :
                j, k = i, 1
                while j % p == 0 :
                    j //= p
                    k *= p
                F[i].append(k)
                T[i] = T[i] * (p-1)//p

    return  F, T



# OBSERVATION : If modulo n is a prime or a prime ^ some_power ==> a = 1 . Examples :
# 8, 16, 32, 64, 9 , 27 , 81, 25, 125  + all the primes


# ==== GENERAL IDEAS ===========
# So our plan, in pseudocode, is:
#
# 1.      Factorize all the integers up to 10**7 by sieving.
# 2.      For each integer n:
# 3.            - if n is a prime or prime power, then a=1;
# 4.            - otherwise n is a product of two or more distinct primes, so:
# 5.      for each way to factorize n=uv with u, v coprime:
# 6.            -   find w=u**(−1) (mod v)
# 7.     a is the maximum of uw for all such uv.
#
#
# Now at step 6 we have to find the multiplicative inverse of u modulo v.
# There are a couple of algorithms for finding the modular multiplicative inverse:
# normally we would use the extended Euclidean algorithm, but here the method using Euler's theorem
# is attractive because we know that u is coprime to v.
# So u**(−1) = u**(φ(v)−1) (mod v) where φ is Euler's totient function.

# ==== Wed, 30 Jan 2013, 05:40, Bo, USA
# http://math.stackexchange.com/questions/264290/division-into-xx-1/264307#264307
# This post at Stack Exchange Mathematics seems to have been written for this problem, judging by the dates.
#
# It gives a nice explanation of the solution...
# a^2 = a (mod n)
# a * (a - 1) = 0 (mod n)
# Let n = d * e with a = 0 (mod d) , (a - 1) = 0 (mod e) , and gcd(d, e) = 1
# Let a = d * w and then substitute (d * w - 1) = 0 (mod e)
# Re-write as d * w = 1 (mod e) , or w = modinv(d, e)
# Then a = d * modinv(d, e)
#
# So, check all coprime d and e with d * e = n to see which one gives the largest a.
#
# I used a sieve to compute the divisors of n , storing only divisors >= sqrt(n) and skipping 1 .
# I also realized we can use the results of the extended Euclidean algorithm for GCD three times - once to check gcd(d, e) = 1 ,
# once for modinv(d, e) , and once for modinv(e, d). This is faster than calling GCD once and modinv twice.
#
# 104 seconds in Pypy (with hand-written egcd) or 195 seconds in Python 3.3 (with GMPY's gcdext).





# @2017-01-22 , 22:45
# http://www.math.stonybrook.edu/~moira/mat331-spr10/papers/1978%20McLeanGroups%20in%20Modular%20Arithmetic.pdf
# https://en.wikipedia.org/wiki/Idempotent_(ring_theory)#Types_of_ring_idempotents
# http://www.mersenneforum.org/showthread.php?t=21717
# https://crypto.stanford.edu/pbc/notes/numbertheory/exp.html







print('\n--------------------------TESTS------------------------------')
t1  = time.time()

# print('\nmath log function :\t', log(11**5, 11))
# print('math log function :\t', log(11**5, 11) %1 == 0 )


def brute_force_testing(lim):
    Mod = {}
    Sm = 0
    for n in range(2, lim+1 ) :
        if gmpy2.is_prime(n) : Sm += 1
        else :
            gf = get_factors(n)
            if len(set(gf)) == 1 :             Sm +=1
            else :
                for a in range(n-1, 0, -1):
                    if pow(a, 2, n  ) == a%n :
                        print(str(n)+'.     M('+str(n)+')= a=', a ,  '     a%n=', a%n  ,'    mod : ' , pow(a, 2, n),'     a*(a-1))%n=' , (a*(a-1))%n  , '   n=',get_factors(n) , '        a=', get_factors(a) ,'    gcd=',gcd(n,a) )
                        Sm += a
                        Mod[n] = a
                        # if a not in Mod : Mod[a] = [n]
                        # else :  Mod[a].append(n)
                        break
        print('-----------')

    return Mod, print('\nAnswer : \t', Sm )         #   Answer : 	First 1000 :  314035
    # print('\nMod :', len(Mod), Mod)

# brute_force_testing(lim = 10**3)
BF = brute_force_testing(10**3)

# print('\n-----Interesting test. See the regularity of 1*2, 2*3, 3*4, 4*5 ... ----------------')
# n=155
# for i in range(n-1,0,-1):
#     print(i,  (i*(i-1))%n ,'   ', n-i, n-i+1   )

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


# import gmpy2, sympy
# # M(90)= a= 81 a%n= 81   mod :  81   a*(a-1))%n= 0    n= [2, 9, 5]
# sympy.totient(9)
# u, v = 15, 8
# w = modinv(u, v )
# w ,  u**(sympy.totient(v)-1) % v, w*u


print('\n================  My FIRST SOLUTION,  18 min ===============\n')
t1  = time.time()

def idempotents (lim) :

    F, T = sieve_factorization( lim )
    S = 0
    for n in range(2, lim+1) :
        if n not in F or len(F[n]) <2 :
            b = 1
            S+=1
            continue

        # C = []            !!!! REALLY BAD PRACTICE. Don't do this kind of CODE AGAIN !!!!!! Watch bellow the good one !
        # for q in range(1, len(F[n) ) :
        #     C.extend( [ reduce(mul, j) for j in list(combinations(F[n], q) ) ] )
        # U = [ u for u in C ]
        # V = [ n//u for u in C ]
        # a =  max([  max( u*(u**(T[v] -1)%v) , v*(v**(T[u]-1)%u) )  for u, v in zip(U, V)] )
        # S+=a
        def a(n):
            max_a = 0
            for q in range(1, len(F[n]) ) :
                for j in combinations(F[n], q ):
                    u = reduce(mul, j)
                    v = n// u
                    a =  u*pow(u, T[v]-1, v)
                    if a > max_a : max_a = a
            return max_a

        b = a(n)
        S += a(n)

        # print(str(n)+'.     ', b , '           '  )
                # if BF[0][n] != a :
        # print(str(n), '  difference  ->  REAL:  ', BF[0][n], '       algo:', a(n)    )

        if n%10**5 == 0 : print(str(n))

    return print('\nAnswer : \t ' , S )             #       Answer : 	  39782849136421


idempotents(10**3)                  #       Completed in : 18.657367 min



t2  = time.time()
print('\nCompleted in :', round((t2-t1)/60,6), 'min\n\n')


print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1,  NICE, 3 min --------------------------')
t1  = time.time()

# ==== Wed, 30 Jan 2013, 05:40, Bo, USA
# http://math.stackexchange.com/questions/264290/division-into-xx-1/264307#264307
# This post at Stack Exchange Mathematics seems to have been written for this problem, judging by the dates.
#
# It gives a nice explanation of the solution...
# a^2 = a (mod n)
# a * (a - 1) = 0 (mod n)
# Let n = d * e with a = 0 (mod d) , (a - 1) = 0 (mod e) , and gcd(d, e) = 1
# Let a = d * w and then substitute (d * w - 1) = 0 (mod e)
# Re-write as d * w = 1 (mod e) , or w = modinv(d, e)
# Then a = d * modinv(d, e)
#
# So, check all coprime d and e with d * e = n to see which one gives the largest a.
#
# I used a sieve to compute the divisors of n , storing only divisors >= sqrt(n) and skipping 1 .
# I also realized we can use the results of the extended Euclidean algorithm for GCD three times - once to check gcd(d, e) = 1 ,
# once for modinv(d, e) , and once for modinv(e, d). This is faster than calling GCD once and modinv twice.
#
# 104 seconds in Pypy (with hand-written egcd) or 195 seconds in Python 3.3 (with GMPY's gcdext).



from array import array
from gmpy2 import gcdext

def solution_1():
    N = pow(10, 7) + 1
    A = [array('I', []) for i in range(N)]
    for n in range(2, N):
      n_squared = n * n
      for m in range(n + n, N, n):
        if n_squared <= m:
          A[m].append(n)

    answer = 0
    for n in range(2, N):
      M_n = 1
      for d in A[n]:
        e = n // d
        g, x, y = gcdext(d, e)
        if g == 1:
          a_1 = d * (x % e)
          a_2 = e * (y % d)
          a = a_1 if a_1 >= a_2 else a_2
          M_n = M_n if M_n >= a else a
      answer += M_n

    return print(answer)

# solution_1()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 2,   --------------------------')
t1  = time.time()

def solution_2() :
    from itertools import combinations
    from functools import reduce

    N = 10**7 + 1
    answer = 0

    euler = [1 for i in range(N)]
    facts = [[] for i in range(N)]

    for i in range(2, N):
        if euler[i] == 1:

            for j in range(i, N, i):
                euler[j] *= i - 1
                facts[j] += [i]

            h = i*i
            while h < N:
                for k in range(h, N, h):
                    euler[k] *= i
                    facts[k][-1] *= i
                h *= i

        f = facts[i]
        if len(f) == 1:
            answer += 1
            continue

        m = 0
        for j in range(1, len(f)):
            for c in combinations(f, j):
                u = reduce(lambda x,y:x*y, c)
                v = i // u
                w = u * pow(u, euler[v] - 1, v)
                if w > m: m = w

        answer += m

    return print(answer)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 3,  7 min --------------------------')
t1  = time.time()

# ==== Sun, 23 Dec 2012, 17:28, Marcus Stuhr, USA
# Recall that based on the functional representation of the remainder operation, a**2 ≡ a mod n is equivalent to
# a=a**2−⌊a**2/n⌋*n, which can be rearranged to a(a−1)/n=⌊a**2/n⌋ .
# This means n is a factor of a(a−1) where 0≤a<n, with the goal being to maximize a.
#
# Consider the M(6) example. The possible values of a(a−1) where a<n are 20, 12, 6, 2, and 0.
# The largest of these that is divisible by n=6 is 12, which corresponds to an aa value of 4.
# Thus, M(6) = 4. However, this process is quite tedious, since it requires many divisibility checks for larger values of nn.
#
# Instead, work in reverse. For each level of a, which values of n does it correspond to?
# If we were to look at the a=4 level where a(a−1) is 12, we note that it would only be the answer
# to values of n that divide 12. In other words, only the divisors of a(a−1) are relevant.
# So what I did was sieve divisors over the entire range a≤10**7.
# The divisors of a(a−1) can be constructed easily from the divisors of a and a−1.
# The combined divisors serve as the candidates for n.
#     For each resulting n, ensure that a<n and n≤10**7,
# then update the value of M(n) with the current a (which will always be maximal
# by the last time M(n) is updated since we iterate a upwards).
#
# Under 3 minutes (~160 seconds) in Python (the same code is about 20s in C++):



def PE407(lim=10**7):
    M=[0,0]+[1]*(lim-1)
    divs = [[0],[1]]+[[] for x in range(2,lim+1)]
    for a in range(2,lim+1):
        for j in range(a,lim+1,a):
            divs[j].append(a)
        for u in divs[a]:
            for v in divs[a-1]:
                n=u*v
                if n>lim: break
                if a<n: M[n]=a
    return sum(M)

# PE407()                 #39782849136421

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

# print('\n--------------------------SOLUTION 4,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
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
