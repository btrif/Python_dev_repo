#  Created by Bogdan Trif on 22-11-2017 , 10:52 AM.
# © o(^_^)o  Solved by Bogdan Trif  @
#The  Euler Project  https://projecteuler.net
'''
            Factorisation triples           -           Problem 418

Let n be a positive integer. An integer triple (a, b, c) is called a factorisation triple of n if:

1 ≤ a ≤ b ≤ c
a·b·c = n.
Define f(n) to be a + b + c for the factorisation triple (a, b, c) of n

which minimises c / a. One can show that this triple is unique.

For example, f(165) = 19, f(100100) = 142 and f(20!) = 4034872.

Find f(43!).
'''

import operator, functools
import time, zzz
from itertools import combinations
from math import factorial, sqrt
import itertools
from pyprimes import factorise


def get_factors(n):       ### o(^_^)o  FASTEST  o(^_^)o  ###
    ''' Decompose a factor in its prime factors. This function uses the pyprimes module. THE FASTEST  '''

    return [val for sublist in [[i[0]]*i[1] for i in factorise(n)] for val in sublist]


# === Same result can be achieved with the following approach
def all_factors_combinations(lst) :     # !!!!!!!!!!! function not utilized here
    ''' Returns the combinations of all elements from a list, preferable a prime factor list'''
    L =[1]
    for i in range(1, len(lst)+1 ) :
        c = list(combinations(lst, i))
        for j in c :
            L.append( functools.reduce(operator.mul, j) )
            # print(L)
    # print(L)
    return sorted(set(L))

def _prod(L):
    s = 1
    for i in  L:
        s*= i
    return s

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



print('43! = ' ,factorial(43) )
print('cubic_root of 43!  = '  ,   (factorial(43))**(1/3)   )

print('\n--------------------------TESTS------------------------------')
t1  = time.time()

def test1( n_) :

    n = factorial(n_)
    print(str(n_)+'! = ' , n)

    F = list(factorise(n))
    # F = [(2, 39), (3, 19), (5, 9), (7, 6), (11, 3), (13, 3), (17, 2), (19, 2), (23, 1), (29, 1), (31, 1), (37, 1), (41, 1), (43, 1)]      #  43!
    # F = [(2, 18), (3, 8), (5, 4), (7, 2), (11, 1), (13, 1), (17, 1), (19, 1)]               #  20!
    print('F = ', F )

    Bs = [ i[0] for i in F ]
    Pwr = [ i[1]+1  for i in F ]
    print('Bases : ', Bs)
    print('Powers : ', Pwr ,'\n')

    ####    Buld the divisors list , GET DIVISORS from a list of factors
    # Use this to obtain all the divisors :

    Div = []
    c=0
    for x in itertools.product(*map(range, Pwr )) :
        divisor = _prod( [ b**p for b, p in zip(Bs , x ) ] )
        if n**(8/27) < divisor < n**(10/27) :
            Div.append(divisor)
            c+=1
            if c%10**4 ==0 :
                print(str(c)+'.      Base : ', Bs , '     Powers : ', x ,'       divisor = ', divisor )

        # print(Div)

    Div.sort()
    print('\n', len(Div) , Div[:100], '\n')        # Only first 100

    result = 0
    ind_b = binary_search( n**(1/3), Div )

    b = Div[ind_b]
    print('\n  b = ', b, '      ind_b = ', ind_b )

    min_ca = 10**8
    for k in range(-30, 30) :
        for i in range( 0, -200, -1 ) :
            for j in range( 0, 200, 1 ) :
                ind_a, ind_c = ind_b + i+k , ind_b + j +k
                a, c = Div[ind_a], Div[ind_c]
                if a*b*c == n :
                    if c/a < min_ca :
                        min_ca = c/a
                        result = a+b+c
                        print('ind_a, ind_b_ind_c = ' ,ind_a, ind_b,  ind_c ,'     a= ' , a, '   b= ' , b , '    c= ', c , '    result = ' , result,'    c/a = ', c/a )
                        print('  a= ' , get_factors(a), '   b= ' , get_factors(b) , '    c= ', get_factors(c)  )


    print('\nResult = ', result)
    return result

# test1(29)


t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')

print('\n================  My FIRST SOLUTION,   ===============\n')
t1  = time.time()

# @2017-11-22 - I know what to do. I must get the divisors list and then get the numbers closest to :
# a <= b <= c
# 0.9999 * cubic_root(n! ) <= b <= 1.0001 * cubic_root(n!)
# The problem is to build this divisors list . Even for 20 ! it takes toooo loooooong  !


def first_solution( n_) :

    n = factorial(n_)
    print(str(n_)+'! = ' , n)

    F = list(factorise(n))
    # F = [(2, 39), (3, 19), (5, 9), (7, 6), (11, 3), (13, 3), (17, 2), (19, 2), (23, 1), (29, 1), (31, 1), (37, 1), (41, 1), (43, 1)]      #  43!
    # F = [(2, 18), (3, 8), (5, 4), (7, 2), (11, 1), (13, 1), (17, 1), (19, 1)]               #  20!
    print('F = ', F )

    Bs = [ i[0] for i in F ]
    Pwr = [ i[1]+1  for i in F ]
    print('Bases : ', Bs)
    print('Powers : ', Pwr ,'\n')

    ####    Buld the divisors list , GET DIVISORS from a list of factors
    # Use this to obtain all the divisors :

    Div = []
    c=0
    for x in itertools.product(*map(range, Pwr )) :
        divisor = _prod( [ b**p for b, p in zip(Bs , x ) ] )
        if n**(242/729) < divisor < n**(244/729) :
            Div.append(divisor)
            c+=1
            if c%10**5 ==0 :
                print(str(c)+'.      Base : ', Bs , '     Powers : ', x ,'       divisor = ', divisor )

        # print(Div)

    Div.sort()
    print('\n', len(Div) , Div[:100])        # Only first 100
    print( len(Div) , Div[-100::], '\n')        #  LAST 100

    result, ai, bi,ci  = 0, 0, 0, 0
    cut = binary_search( n**(1/3), Div )
    init_b = Div[cut]

    min_ca = 10**8
    k = 10
    ind_b = cut -k

    print('\n  initial cut = ', cut, '    init_b = ', init_b, '    ref =  ', n**(1/3) ,'   start ind_b = ', ind_b )
    while ind_b <= cut + 2*k :
        ind_a = ind_b - 1*k
        b = Div[ind_b]
        while ind_a <= ind_b :
            a = Div[ind_a]
            c = n/(a*b)
            if c >= b and c%1 ==0  :
                c = int(c)
                # print(' ind_a, ind_b  =    ', ind_a, ind_b,'          a =', a ,'      b=', b, '      c=', c , '         ', c/a, min_ca , a*b*c, n)
                if c/a < min_ca :
                    if a*b*c == n :
                        ind_c = Div.index(c)
                        min_ca = c/a
                        result = a+b+c
                        ai, bi, ci  = ind_a, ind_b, ind_c
                        A, B, C = a, b, c
                        print('ind_a, ind_b_ind_c = ' ,ind_a, ind_b,  ind_c ,'     a= ' , a, '   b= ' , b , '    c= ', c , '    result = ' , result,'    c/a = ', c/a )
                        print('  a= ' , get_factors(a), '   b= ' , get_factors(b) , '    c= ', get_factors(c)  )

            ind_a += 1
        ind_b += 1

    print('\nResult = ', result,'       a, b, c = ', A, B, C,'           ind_a, ind_b, ind_c = ', ai, bi, ci)
    print('\nResult = ', result   )
    return result


# first_solution(43)

#  Result =  1177163565297340320        a, b, c =  392386762388275200 392388272221065120 392388530688000000
#  ind_a, ind_b, ind_c =  18718567 18718586 18718589


t2  = time.time()
print('\n# Completed in :', round((t2-t1)/60,2 ), 'mins\n\n')


print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1, AMAZING, 3 sec, Must study it  --------------------------')
t1  = time.time()

# ==== Fri, 15 Mar 2013, 19:48, ving, USA
# Pretty much the same as the very first post, only in Python.  Runs under 3 seconds.

from math import factorial

def solution_1( fact_nr ) :
    F = factorial(fact_nr)

    # product(prime[i]^expon[i]) = 43!
    primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43)
    expons = (39, 19, 9, 6, 3, 3, 2, 2, 1, 1, 1, 1, 1, 1)

    # Make a sorted list of divisors with factors 5, 7, ..., 43:
    lst1 = [1]
    for i in range(2, 14):
        lst1 = [x * primes[i]**k for x in lst1 for k in range(expons[i]+1)]
    lst1.sort()

    # Make a sorted list of divisors with factors 2 and 3:
    lst2 = [1]
    for i in range(2):
        lst2 = [x * primes[i]**k for x in lst2 for k in range(expons[i]+1)]
    lst2.sort()

    n1, n2 = len(lst1), len(lst2)

    # Merge the lists together, keeping only divisors that are close to F^(1/3):
    epsilon = 1.0001
    m = F**(1/3)
    M1, M2 = round(m/epsilon), round(m*epsilon)
    i, j = 0, n1 - 1
    divs = []

    while i < n2 and j >= 0:
        x = lst2[i]
        while j >= 0 and lst1[j] * x > M2:
            j -= 1;
        for k in range(j, -1, -1):
            z = lst1[k] * x
            if z >= M1:
                divs.append(z)
            else:
                break
        i += 1

    divs.sort()
    n = len(divs)

    # Examine all pairs of divisors x, y, such that N! is divisible by xy:
    rMin, f = 2, None
    for i in range(n):
        x = divs[i]
        for j in range(i, n):
            y = divs[j]
            z = x*y
            if F % z != 0:
                continue
            z = F//z
            if x <= z and z <= y:
                r = y/x
                if r < rMin:
                    rMin = r
                    f = x + y + z

    return print(f)                # Answer: 1177163565297340320           # Completed in : 3383.19 ms

solution_1(43)

t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')


print('\n--------------------------SOLUTION 2,   --------------------------')
t1  = time.time()

# ==== Sat, 9 Mar 2013, 22:01, Peter de Rivaz, England
# I used a meet in the middle technique to find factors near a target value, first for a target of the cube root,
# and then for a target of the sqrt of the remainder.
#
# To do the meet in the middle I split the prime factors into 2 sets, and for each set
#     generate all possible values of multiplying the factors together.
#
# I then sort these lists and run a single pass over both lists finding values near the target.
# The search for the sqrt target will be optimal, but the initial search may not be so I tried a few
# factors below the cube root to find the smallest.  Takes a second in Python.

D= { 2 : 39 , 3 : 19 ,  5 : 9 ,  7 : 6 ,  11 : 3 ,  13 : 3 ,  17 : 2 ,  19 : 2 ,  23 : 1 ,  29 : 1 ,  31 : 1 ,  37 : 1 ,  41 : 1 ,  43 : 1 }
n = factorial(43)


def find_close_factor(D, target):
   """Given a dictionary of primes, return a factor below (or at) the target"""
   # Split into two
   n = _prod(p**c for p,c in D.items())
   n2=int(sqrt(n))
   m=1
   A=[1]
   B=[1]
   for p,c in D.items():
      A2=A[::]
      B2=B[::]
      m=m*p**c
      if len(A)<len(B):
         for k in range(c):
            A2=A2+[p**(k+1)*a for a in A]
      else:
         for k in range(c):
            B2=B2+[p**(k+1)*a for a in B]
      A=A2
      B=B2
   A=sorted(A)
   B=sorted(B,reverse=True)
   b=0
   best=0
   for a in A:
      while b<len(B) and a*B[b]>target:
         b+=1
      if b>=len(B):
         break
      best=max(best,a*B[b])
   return best


print( find_close_factor(D, n**(1/3) ) )

t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')


print('\n--------------------------SOLUTION 3,  2 min --------------------------')
t1  = time.time()

# === Mon, 11 Mar 2013, 18:37, bobrovsky.serj, Russia
# Eats memory like crazy. Fast.


from math import factorial

def getfactors(x):
    factors = []
    for p in 2,3,5,7,11,13,17,19,23,29,31,37,41,43:
        y, rest = divmod(x, p)
        while rest == 0:
            factors.append(p)
            x = y
            y, rest = divmod(x, p)
        if x == 1:
            return factors

def gensubproducts(factors, top):
    l = [1]
    for p in factors:
        for i in range(len(l)):
            x = l[i] * p
            if x < top:
                l.append(x)
            else:
                break
        l.sort()
        x = 0
        newl = []
        for y in l:
            if x < y:
                x = y
                newl.append(x)
        l = newl
    return l


def euler418(limit):
    fac43 = factorial(limit)
    factors = getfactors(fac43)

    def trya(a):
        nonlocal fac43, top
        bestbc = fac43
        fac43div_a = fac43 // a

        l = gensubproducts(getfactors(fac43div_a), top)

        for b in reversed(l):
            if b < a:
                return bestbc
            c = fac43div_a // b
            if c < a:
                continue
            bc = max(b,c)
            if bestbc > bc:
                bestbc = bc
        return bestbc

    top = int(fac43**(1/3))

    l = gensubproducts(factors,top)

    gap = top >> (limit * 18 // 43) # some arbitrary value
    bottom = top - gap
    top += gap

    besta, bestc = 1, fac43
    for a in reversed(l):
        if a < bottom:
            break
        c = trya(a)
        if c * besta < a * bestc:
            besta, bestc = a, c

    bestb = fac43 // besta // bestc
    return besta + bestb + bestc


# print(euler418(43))

t2  = time.time()
print('\n# Completed in :', round((t2-t1) , 2), 's\n\n')


print('\n--------------------------SOLUTION 4,  1 min  --------------------------')
t1  = time.time()

# ==== Wed, 10 Jul 2013, 21:14, Bo, USA
# I found myself writing a lot of new code, which is usually a sign that I've failed to understand the problem fully...
#
# Like most others, I initially got the solution by searching for divisors "around" (n!)^(1 / 3).
# This was slow and it feels wrong to just throw in arbitrary bounds.
# To get under a minute I implemented wrongrook's meet-in-the-middle algorithm and RobArthan's non-arbitrary
# bounds method (thanks RobArthan!).
#
# Still a lot of code, so there's probably room to improve.


def gen_primes(limit):                                  # EIGHTH
    ''' SIEVE of ERATOSTHENES :  Efficient PRIME GENERATOR algorithms
    Code by David Eppstein, UC Irvine, 28 Feb 2002,     http://code.activestate.com/recipes/117119/ '''
    D = {}
    i = 2
    while i <= limit:
        if i not in D:
            yield i
            D[i * i] = [i]
        else:
            for p in D[i]:
                D.setdefault(p + i, []).append(p)
            del D[i]
        i += 1


from gmpy2 import fac, iroot, isqrt


def sub_products(factors):
  # Helper function for the meet-in-the-middle function, closest_divisors
  L = len(factors) // 2
  F_1 = factors[:L]
  F_2 = factors[L:]

  P_1 = [1]
  for p in F_1:
    P_1.extend([x * p for x in set(P_1)])
  P_1 = sorted(set(P_1))

  P_2 = [1]
  for p in F_2:
    P_2.extend([x * p for x in set(P_2)])
  P_2 = sorted(set(P_2), reverse=True)

  return P_1, P_2

def closest_divisor(factors, target, P_lists):
  # Returns the largest divisor of the number with the given factors that is
  # at most equal to the target
  P_1, P_2 = P_lists
  L_1 = len(P_1)
  L_2 = len(P_2)

  i = 0
  j = 0
  answer = 0
  while (i < L_1) and (j < L_2):
    x = P_1[i] * P_2[j]
    if x > target:
      j += 1
    elif x < target:
      if x > answer:
        answer = x
      i += 1
    else:
      answer = x
      break

  return answer

def fpf(n, prime_factors):
  # Returns the prime factorization of n! given n and the primes <= n
  for p in prime_factors:
    e = 0
    q = p
    while q <= n:
      e += n // q
      q *= p
    for _ in range(e):
      yield p

def remaining_primes(n, prime_factors):
  # Given n and a list of prime factors, return the list of prime factors
  # with n's prime factors removed. Assumes n's prime factors are a subset
  # of the given list.
  distinct_primes = sorted(set(prime_factors))
  ret = prime_factors[:]
  x = n
  for p in distinct_primes:
    while x % p == 0:
      x //= p
      ret.remove(p)

  return ret

limit = 43
N = fac(limit)
factors = list(range(2, limit + 1))
prime_factors = list(fpf(limit, gen_primes(limit)))
n_cbrt = iroot(N, 3)[0]
sp_1, sp_2 = sub_products(factors)


def get_triple(x_target):
  # Returns a factorization triple x, y, z such that x * y * z = N
  x = closest_divisor(factors, x_target, (sp_1, sp_2))
  yz_primes = remaining_primes(x, prime_factors)
  yz = N // x
  y = closest_divisor(yz, isqrt(yz), sub_products(yz_primes))
  z = yz // y

  return x, y, z

# Compute the lower bound for a
x, y, z = get_triple(n_cbrt)
a, b, c = sorted((x, y, z))
m = (a * a * N) // (c * c)
m_cbrt = iroot(m, 3)[0]

# Search for the best triple
best = c / a
answer = (a, b, c)
while x > m_cbrt:
  x, y, z = get_triple(x - 1)
  a, b, c = sorted((x, y, z))
  ratio = c / a
  if ratio < best:
    best = ratio
    answer = (a, b, c)

print(sum(answer))

t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')


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

