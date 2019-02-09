#  Created by Bogdan Trif on 18-09-2017 , 7:20 PM.
#!/usr/bin/python                   o(^_^)o         ( ͡° ͜ʖ ͡°)
# © Solved by Bogdan Trif @
#The  Euler Project  https://projecteuler.net
'''
            Solving the diophantine equation 1/a+1/b= p/10**n     -       Problem 157

Consider the diophantine equation 1/a+1/b= p/10**n with a, b, p, n positive integers and a ≤ b.
For n=1 this equation has 20 solutions that are listed below:

1/1+1/1=20/10	        1/1+1/2=15/10	        1/1+1/5=12/10	        1/1+1/10=11/10	    1/2+1/2=10/10
1/2+1/5=7/10	        1/2+1/10=6/10	        1/3+1/6=5/10	        1/3+1/15=4/10	        1/4+1/4=5/10
1/4+1/20=3/10	        1/5+1/5=4/10	        1/5+1/10=3/10       	1/6+1/30=2/10	        1/10+1/10=2/10
1/11+1/110=1/10	    1/12+1/60=1/10	    1/14+1/35=1/10	    1/15+1/30=1/10	    1/20+1/20=1/10

How many solutions has this equation for 1 ≤ n ≤ 9?

'''
import time, zzz, itertools
from gmpy2 import mpq
from pyprimes import factorise
from functools import reduce
from operator import mul
from itertools import combinations, chain


def get_factors(n):       ### o(^_^)o  FASTEST  o(^_^)o  ###
    ''' Decompose a factor in its prime factors. This function uses the pyprimes module. THE FASTEST  '''

    return [val for sublist in [[i[0]]*i[1] for i in factorise(n)] for val in sublist]

class PrimeTable():    #  ( ͡° ͜ʖ ͡°)  ### !! FIRST FASTEST
    def __init__(self, bound):
        self.bound = bound
        self.primes = []
        self._sieve()

    def _sieve(self):
        visited = [False] * (self.bound + 1)
        visited[0] = visited[1] = True
        for i in range(2, self.bound + 1):
            if not visited[i]:
                self.primes.append(i)
            for j in range(i + i, self.bound + 1, i):
                visited[j] = True
        print('Prime count:', len(self.primes))

class Factorization():
    ''' Based on a prebuilt prime sieve, and we must pay attention that the prime up range is not
    to low, so that we don't miss a prime when we first factor . As default the value is set to 10.000   '''
    def __init__(self):
        self.prime_table = PrimeTable(10**4)

    def get_divisors(self, n):
        d = n
        f = {}
        for p in self.prime_table.primes:
            if d == 1 or p > d:
                break
            e = 0
            while d % p == 0:
                d = d // p
                e += 1
            if e > 0:
                f[p] = e
        if d > 1:
            f[d] = 1
            #raise Exception('prime factor should be small', d)
        unpacking = [[p**e for e in range(f[p] + 1)] for p in f]
        return sorted([self._product(divisor) for divisor in itertools.product(*unpacking)])

    def _product(self, list):
        result = 1
        for number in list:
            result *= number
        return result


F  = Factorization()
print( F.get_divisors(180180) )







print('\n--------------------------TESTS------------------------------')
t1  = time.time()

footprint = lambda a, b : a*b + (a+b)/ 10**(len(str(a+b)))

Uniq = set()
def the_brutest_of_forces( n ) :

    cnt=0
    for b in range(1, 51*n +1 ) :
        for a in range(1, b+1 ) :
            c = mpq( 1 , a ) + mpq( 1 , b )
            if (  n % c.denominator   == 0  ):
                cnt+=1
                Uniq.add(footprint(a, b)  )
                print(str(cnt)+'.   a = ', a,'  ', get_factors(a) ,'        b = ', b ,'    ', get_factors(b) ,'  ;       p=', c.numerator , ' ;     denom = ' , c.denominator )

# the_brutest_of_forces(10**2 )

print('\n Len Uniq = ', len(Uniq))
print(Uniq)

# OBSERVATION :
# 3 appears on both sides : Examples :
# 571.   a =  15    [3, 5]         b =  7500      [2, 2, 3, 5, 5, 5, 5]   ;       p= 167  ;     denom =  2500
# 560.   a =  540    [2, 2, 3, 3, 3, 5]         b =  6750      [2, 3, 3, 3, 5, 5, 5]   ;       p= 1  ;     denom =  500
# 667.   a =  516    [2, 2, 3, 43]         b =  16125      [3, 5, 5, 5, 43]   ;       p= 1  ;     denom =  500
# 691.   a =  1050    [2, 3, 5, 5, 7]         b =  21000      [2, 2, 2, 3, 5, 5, 5, 7]   ;       p= 1  ;     denom =  1000
# 311.   a =  525    [3, 5, 5, 7]         b =  10500      [2, 2, 3, 5, 5, 5, 7]   ;       p= 1  ;     denom =  500
# 326.   a =  144    [2, 2, 2, 2, 3, 3]         b =  18000      [2, 2, 2, 2, 3, 3, 5, 5, 5]   ;       p= 7  ;     denom =  1000
# 266.   a =  21    [3, 7]         b =  2625      [3, 5, 5, 5, 7]   ;       p= 6  ;     denom =  125

### DOUBLE CASES :
# 324.   a =  1064    [2, 2, 2, 7, 19]         b =  16625      [5, 5, 5, 7, 19]   ;       p= 1  ;     denom =  1000
# In this case [5, 5, 5] + [2,2,2] must be a multiple of 7*19 => Verification :  125+8 = 133 = 7*19 => TRUE !!

# Question :
# 1.  What combination of primes when summed makes another prime number or a multiple of prime number ?


# def a_add_b_over_a_x_b(a, b):




t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')

print('\n================  My FIRST SOLUTION,  1 second   ===============\n')
t1  = time.time()

'''
2019-01-22 - ALGORITHM IDEA :
Very nice and interesting problem. I obtained for n=9 the value 23058 and could not understand why my answer is wrong. 
I investigated my code, nothing wrong. In the end I realized that I must sum all the n=1,...,9. Funny. Yes, this happens.
Anyway, I looked at the solutions here on forum and I do not know how, 
but I managed to find the most complicated solution from the entire forum, which is my opinion a bad performance. 
However, my solution is efficient, interesting and I think it worth a look.

I will briefly explain my algorithm which I constructed it by hand, pen & paper first before implementing it in python :
Basically I started to solve the equation $(a+b)/(a*b) = p/(2^i*5^j)$. Find all rational solutions of this form.
               ==  STEPS OF THE ALGORITHM == :
1.	Generate all the numbers which are of the form : $2^i*5^j$ with $i, j <= 9$ :
: 1, 2, 4, 5, 8, 10, ...
2.	Loop over and choose $a, b = 2^i*5^j, 2^i*5^j$ . This will be the Base Case
3.	Factorize both $a, b$ and find common factors and differences in factors
4.	Take the common factors as separate and add the differences factors of the a, b
5.      The  sum obtained from difference which will be factored.
6.	Form combinations of this factorization .
7.	Multiply each case to initial values of a, b : $a*factor, b*factor$ and check if the result is within our limits.

  EXAMPLE :
$a =  125 = 5^3     b =  2500 = 2^2 * 5^4$    Will represent the base case:
$(a+b)/(a*b) = [(1+20) *5^3] /(2^2 * 5^7 )  = (3* 5^3 *7) / (2^2 * 5^7 ) = 21 / (2^2 * 5^4)$
The powers of 2 & 5 are within the required range. Next we search for additional cases :

3.  Common factors $C = 5^3 = 125$,     Uncommon factors : $a/C = 1 , b/C = 2^2*5$
4.  $d = a/C + b/C = 1+20 = 21$	# Sum of difference in factors of a & b
5.  Factorize $d = [3*7]$
6.  Generate all combinations of factorization of $d : [ 3, 7, 21 ]$
7.  Take the first element m = 3 : Form new numbers by multiplying with m:

$a_2 = a*3 = 3*5^3, b_2 = b*3 = 2^2*3*5^4$ 
The new case :
$(a_2+b_2)/(a_2*b_2) = [(1+20) *3*5^3] / (2^2*3^2*5^7 ) = 7 / (2^2*5^4) $
Check if the the powers of 2 & 5 are within the range.

repeat the process for 7 , 21, ....


The algorithm without optimizations runs in about 1 second. But can be greatly reduced 
to 0.1 = 0.2 seconds if we eliminate the redundant cases.

'''


def test_powers( denom, x ):
    ''':Description: Given a number of the form **2^x * 5^x** tests whether the power of 2 and
            5 is bigger or smaller than the accepted limit = x.

    :Example1: denom = 5**2 * 2**5, x = 4 => 2 has a larger power than the limit x = 4 => It will return False
    :Example2: denom = 5**4 * 2**4, x = 4 => both 2 & 5 have power =4 which is within the limit range of x = 4. Will return True    '''
    five, two = denom % 5**x, denom % 2**x
    # print('five=', five,  ' ;   two=', two  )
    if two == 0 :
        n2 = denom / 2**x
        # print('n2= ', n2, '   ', n2%2 )
        if n2%2 == 0:  return False

    if five == 0 :
        n5 = denom / 5**x
        # print('n5= ', n5, '   ', n5%5 )
        if n5%5 == 0:  return False

    return True


def unique_combinations(L) :        # Made by Bogdan Trif @ 2019-01-21, 20:00
    ''':Description: Having a list like L = [3, 3, 3, 139] it outputs the unique combinations of elements
    without repeating the same subsets :                    '''

    COMB = [ list(set(combinations(L, i))) for i in range(1, len(L)+1)  ]
    single_flattened = list( chain.from_iterable(COMB) )        # Method I
#     single_flattened = [val for sublist in COMB for val in sublist]   # Method II

    return single_flattened

footprint = lambda a, b : a*b + (a+b)/ 10**(len(str(a+b)))


def gen_twos_fives( pwr ) :
    ''':Description: generate a list of  multiples of 2 & 5 of the form 2^i * 5^j
    :param lim: int, maximum number
    :return: list of multiples of 2 & 5     '''
    L , T = [], dict()
    i = 0
    while i <= pwr :
        j = 0
        while j <= pwr :
            n = 2**i * 5**j
            L.append(n)
            T[n] = (i,j)
            # print( 'i, j = ', i, j , '    n =', n ,'       L = ', L)
            j+=1
        i+=1
    L.sort()

    return T, L


def diophantine_eqn( pwr) :
    M, N = gen_twos_fives( pwr )
    Uniques = set()

    for i in range( len(N) ) :
        for j in range(i, len(N) ) :
            a , b = N[i], N[j]
            A, B = M[a], M[b]
            C = [ min(A[0], B[0]) ,min(A[1], B[1])  ]               # Common factors
            A2, B2 = [ A[0]- C[0], A[1]- C[1] ] , [ B[0]- C[0], B[1]- C[1] ]        # Uncommon factors in A and B
            d = 2**A2[0] * 5**A2[1] + 2**B2[0] * 5**B2[1]                       # Special sum of Uncommon factors
            d_f = get_factors(d)                        # factoring

            nr = mpq(a+b, a*b)
            # print('A= ', A, '    B= ' ,B, ' ;   a = ', a ,'    b = ', b ,'  ;     a*b= ', a*b, '   C= ', C ,'       A2= ', A2, '  B2= ' , B2 ,'    d= ', d, ' = ', d_f , '    nr= ', nr  )
            if  test_powers( nr.denominator, pwr) :
                if (a, b) not in Uniques :
                    Uniques.add( (a, b) )

                Comb = unique_combinations( d_f )
                # print('Comb : ', Comb)
                for K in Comb :
                    c = reduce(mul, K)
                    a2, b2 = a * c , b * c
                    nr2 = mpq( a2 + b2 , a2 * b2 )

                    if  test_powers( nr2.denominator, pwr) :
                        if (a2, b2) not in Uniques :
                            Uniques.add( (a2,b2) )

                    # print('             K = ', K ,' = ' , c , ' ;         a2 = ', a2, ' ,   b2 = ', b2, '\t'*28 ,'nr2 = ', nr2 )

    print('Uniques : ', len(Uniques) )
    # print('\nUniques : ', Uniques )

    return len(Uniques)


def main_solution_Bogdan( up_lim ) :
    S = 0
    for pwr in range(1, up_lim+1) :
        S += diophantine_eqn( pwr )

    print('\nANSWER = ', S)
    return S

# main_solution_Bogdan( 9 )               #   ANSWER =  53490


#  : Uniques for n = 9 :  23058

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')              #       Completed in : 1325.08 ms


print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1,   --------------------------')
t1  = time.time()

''' === Thu, 15 Sep 2016, 16:46, mbh038, England

In the same manner as in problem 110, I recast the given equation as 
y = (10^n * x) / (xp−10^n)
and set k = x*p−10^n, from which it follows that : 
x*p= k+10^n
and that
y*p = 10^n + 10^(2n)/ k

It follows then that k must be a divisor of 10^2n and, if x⩽y, that k⩽10n. 
For each n I go through the allowed values of k and find the number of common prime factors of xp and yp. 
That gives the number of possible solutions for that value of n. Then, we sum over all n.

Thanks to vamsikal3 (below) for the insight that it is just the common prime factors of xp and yp that are needed. 
I had been trying to find the number of values of p that are divisors of both xp and yp. 
That is the same thing in the end, but takes longer to do because there is an extra (and unnecessary)  
task involved - finding the  divisors, given the prime factors.

† With a really slow way of finding divisors that does not use prime factors.
†† With a faster way of finding divisors that does use the prime factors.
††† Without bothering to find divisors at all. Just use the prime factors.

'''

import numpy as np

def p157(nmax):
    """
    prints number of solutions to 1/x + 1/y = p/10^n for 1<=n<=nmax
    x,y,p,n are positive integers, x<=y
    """
    sols=0
    for n in range(1,nmax+1):
        ks=[k for k in [2**i*5**j for i in range(2*n+1) for j in range(2*n+1)] if k<=10**n]
        for k in ks:
            xpfs=pfdic(k+10**n) #prime factors of xp
            ypfs=pfdic(10**n+(10**(2*n))/k)#prime factors of yp
            cpfs={pf:min(expxp,ypfs[pf]) for pf,expxp in xpfs.items() if pf in ypfs} #common pfs
            sols+=np.prod([cpfs[x] + 1 for x in cpfs]) #number of solutions for these values of k,n
    print(sols)

def pfdic(n):
    '''returns the prime factors of n as {prime1:exponent1,...} '''
    i = 2
    factors = {}
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors[i]=factors.get(i,0)+1
    if n > 1:
        factors[n]=factors.get(n,0)+1
    return factors

p157(9)


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')


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

