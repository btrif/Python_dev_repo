#  Created by Bogdan Trif on 17-05-2018 , 8:43 AM.  ### ( ͡° ͜ʖ ͡°)    ( ͡° ͜ʖ ͡°)  ###
# © o(^_^)o  Solved by Bogdan Trif  @
#The  Euler Project  https://projecteuler.net
'''
                Counting primitive Pythagorean triples          -           Problem 540


A Pythagorean triple consists of three positive integers a,b and c satisfying a^2+b^2=c^2.
The triple is called primitive if a,b and c are relatively prime.

Let P(n) be the number of primitive Pythagorean triples with a<b<c≤n.

For example P(20) = 3, since there are three triples: (3,4,5), (5,12,13) and (8,15,17).

You are given that P(10^6) = 159139.

Find P(3141592653589793).

'''
import time, zzz
from math import gcd, sqrt, floor, ceil
from gmpy2 import is_prime

from  itertools import combinations
from functools import reduce
from operator import mul
from pyprimes import factorise

def gcd3(x, y, z):
    return gcd(gcd(x, y), z)

def get_single_factors(n):       ### o(^_^)o  FASTEST  o(^_^)o  ###
    ''' Decompose a factor in its prime factors. This function uses the pyprimes module. THE FASTEST  '''
    return [ i[0] for i in factorise(n) ]

class PrimeTable():    #  ( ͡° ͜ʖ ͡°)  ### !! FIRST FASTEST
    def __init__(self, bound):
        self.bound = bound
        self.primes = []
        self._sieve()

    def _sieve(self):       # FOURTH      o(^_^)o
        sieve = [True] * self.bound
        for i in range(3, int(self.bound**0.5)+1, 2):
            if sieve[i]:
                sieve[ i*i :: 2*i ] = [False] * ( (self.bound-i*i-1) // (2*i) +1 )
        self.primes = [2] + [i for i in range(3, self.bound , 2) if sieve[i] ]
        print('Prime count:', len(self.primes) ,'           ATTENTION , LARGEST PRIME Included = ', self.primes[-1] ,'       !!!!!!!!!!!! ' )

class Factorization():
    ''' Based on a prebuilt prime sieve, and we must pay attention that the prime up range is not
    to low, so that we don't miss a prime when we first factor . As default the value is set to 10.000
      So we need uprange /2         '''
    def __init__(self, bound):
        self.prime_table = PrimeTable(bound)

    def get_factors(self, n):
        d = n
        f = {}
        L = set()
        for p in self.prime_table.primes:
            if d == 1 or p > d:
                break
            e = 0
            while d % p == 0:
                d = d // p
                e += 1
            if e > 0:
                # f[p] = e
                L.add(p)
        if d > 1:
            f[d] = 1
            #raise Exception('prime factor should be small', d)
        return sorted(L)


    def get_divisors(self, n) :
        f = self.get_factors(n)
        unpacking = [[p**e for e in range(f[p] + 1)] for p in f]
        return sorted([self._product(divisor) for divisor in itertools.product(*unpacking)])


    def _product(self, list):
        result = 1
        for number in list:
            result *= number
        return result



def Pythagorean_primitive_triplets_gen_test( side_lim ):    # by Bogdan Trif @ 2018-05-17, 09:30     ### ( ͡° ͜ʖ ͡°)  FASTEST  ( ͡° ͜ʖ ͡°)  ###
    ''':Usage:      >>> pyt = Pythagorean_primitive_triplets_gen()
                        # >>> next(pyt)
                        # >>> for i in Pythagorean_primitive_triplets_gen(): print(i)
    :param i:   i
    :param j:   j
    :return:    a,b,c - primitive pythagorean triplet
    '''
    m = 2
    while m*m < side_lim :
        if m%2 == 1 :            n = 2                 # m - ODD
        if m%2 == 0 :            n = 1                 # m - EVEN


        while n < m :                      ### range(1,m) as we need only a > 0 !!!!!!!!
            if gcd( m,n ) ==1 :           #   Assure that we generate ONLY primitive Pythagorean triplets
                c = m**2 + n**2

                if c > side_lim : break

                a = m**2-n**2
                b = 2*m*n

                p = 2*m* (m + n )           # = 2*m^2 + 2*m*n

                # print(' m, n = \t',m, n,'            a,b,c =\t', a, b, c  ,'      gcd3(a,b,c) = ', gcd3(a,b,c),'     gcd(m,n) = ', gcd(m,n) ,'             p = ',  p )
                yield a, b, c

            n+=2
        m+=1


# F = Factorization(10**6)
# print( F.get_factors(510) )




print('\n--------------------------TESTS------------------------------')
t1  = time.time()



##### CASE 15 : n =  4  TERMS   => I need only EVEN terms :
 # m, n = 	 15 2             a,b,c =	 [60, 221, 229]       gcd3 =  1              p =  510
 # m, n = 	 15 4             a,b,c =	 [120, 209, 241]       gcd3 =  1              p =  570
 # m, n = 	 15 8             a,b,c =	 [161, 240, 289]       gcd3 =  1              p =  690
 # m, n = 	 15 14             a,b,c =	 [29, 420, 421]       gcd3 =  1              p =  870
 # Totients of 15 :   1, 2, 4, 7, 8, 11, 13, 14 = 8 numbers         from which only  4 are even  +
 # All EVEN of 15 are : [2, 4, ..., 14] = 7 terms
# because always odd * prime(odd) = odd => 5*13 = 65 , 9 * 11 = 99
# 15 = [3, 5] => even multiples of 3, 5 excluded  for 3 : => 2*3 = 6, 4*3 = 12 and for 5 : => 2*5=10 => 3 terms out
# => from [2, 4, 6, 8, 10, 12, 14] = 7 we substract 3 => 4 terms (CORRECT ! )



##### CASE 18 : n =  6  TERMS   => I need only ODD terms :
# m, n = 	 18 1             a,b,c =	 [36, 323, 325]       gcd3 =  1              p =  684
#  m, n = 	 18 3             a,b,c =	 [108, 315, 333]       gcd3 =  9              p =  756
#  m, n = 	 18 5             a,b,c =	 [180, 299, 349]       gcd3 =  1              p =  828
#  m, n = 	 18 7             a,b,c =	 [252, 275, 373]       gcd3 =  1              p =  900
#  m, n = 	 18 9             a,b,c =	 [243, 324, 405]       gcd3 =  81              p =  972
#  m, n = 	 18 11             a,b,c =	 [203, 396, 445]       gcd3 =  1              p =  1044
#  m, n = 	 18 13             a,b,c =	 [155, 468, 493]       gcd3 =  1              p =  1116
#  m, n = 	 18 15             a,b,c =	 [99, 540, 549]       gcd3 =  9              p =  1188
#  m, n = 	 18 17             a,b,c =	 [35, 612, 613]       gcd3 =  1              p =  1260
# All odds of 18 are : [1, 3, ..., 17] = 9 terms
# 18 = [2, 3] => odd multiples of 2, 3 MUST BE excluded !
# for 2 :=> because 2 = EVEN = > we already excluded it ( BECAUSE 2 is the ONLY EVEN PRIME !!! )
# for 3 :=> 1*3=3 , 3*3=9, 5*3 = 15 => 3 terms => 9-3 terms = 6 which is CORRECT !!!

# CASE 3 : n = PRIME => consider n-1 terms

print('factorise :', list(factorise(510))  )



PT = Pythagorean_primitive_triplets_gen_test( 10**3 )           #   159139.      (996065, 87912, 999937)   CORRECT

X = set()
for cnt, PPT in enumerate(PT) :
    a=1

    X.add(PPT)
    print(str(cnt+1)+'.     ', PPT )


print('X : ', len(X), X)



t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')

print('\n================  My FIRST SOLUTION,  5 hours  ===============\n')
t1  = time.time()




def Counting_PPT_solution( side_lim ):    # by Bogdan Trif @ 2018-05-17, 18:30
    '''  Solution to problem 540
    '''

    # Primes = PrimeTable( int(sqrt( side_lim )) +1 )
    # Prime_set = set(Primes.primes)
    # print( len( Prime_set)  )
    F = Factorization( int(sqrt( side_lim )) +10 )

    m = 3
    count = 1
    separate_cnt = 1
    while m*m < side_lim :

        n_lim =    floor( sqrt (side_lim - m**2 ) )
        up_lim = min( m-1, n_lim )

        if m% (10**6) ==0 :
            print( 'm =  ', m   , '        n_lim = ', n_lim  , '        up_lim =' ,   up_lim,'     time = ' , round(time.time() - t1) )

        # CASE 1 : m is prime => add all  EVEN terms  n = m-1 / 2 UP TO n_lim
        if is_prime(m) :
        # if m in Prime_set :
            terms = min( (m-1)//2 , n_lim//2  )
            count += terms
            # print('case PRIME :    m= ' , m  ,'      (m-1)//2 = ', (m-1)//2,'      n_lim//2 = ', n_lim//2  , '     terms = ' , terms,'       count = ', count   )

        else :
            # CASE 2 : m is EVEN => substract multiples of odd items of factors
            if m%2 == 0 :
                init_terms = up_lim//2+(up_lim)%2
                terms = init_terms
                f = get_single_factors(m)[1:]
                # G = []
                # print(m ,' f =', f)
                for j in range(1, len(f) +1 ) :
                    prefactor = (-1)**(j)       #### VERY NICE : This elliminates the need for two cases like : j % 2 == 0 && j % 2 == 1
                    I = [ reduce(mul, i) for i in list(combinations(f, j)) ]
                    # print(' I = ', I)
                    # G.extend(I)
                    for i in I :
                        if i < m :
                            odd = up_lim//i//2 + (up_lim//i)%2

                            terms += prefactor * odd

                            # print('factor = ', i, '      odd =  ',  odd ,'     ', up_lim//i//2  )

                count += terms
                # print(' G = ', G)
                # print('case EVEN :    m= ' , m , f ,'      initial_tems = ', init_terms  , '     terms = ' , terms,'       count = ', count   )



            # CASE 3 : m is ODD =>
            if m%2 == 1 :
                init_terms = up_lim//2
                terms = init_terms
                f = get_single_factors(m)
                # G = []
                # print(' f =', f)
                for j in range(1, len(f) +1 ) :
                    prefactor = (-1)**(j)
                    I = [ reduce(mul, i) for i in list(combinations(f, j)) ]
                    # print(' I = ', I)
                    # G.extend(I)
                    for i in I :
                        if i < m :
                            even = up_lim//i//2
                            terms += prefactor * even
                            # print('factor = ', i, '      odd =  ',  even ,'     ', up_lim//i//2  )

                count += terms
                # print('case ODD :    m= ' , m , f ,'      initial_tems = ', init_terms  , '     terms = ' , terms,'       count = ', count   )


        ### PROBLEM PART  II ONLY FOR CHECKING    ###

        # if m%2 == 1 :                n = 2                 # m - ODD
        # if m%2 == 0 :                n = 1                 # m - EVEN
        #
        # while n < m :                      ### range(1,m) as we need only a > 0 !!!!!!!!
        #
        #     c = m**2 + n**2
        #     if gcd( m, n ) == 1 :           #   Assure that we generate ONLY primitive Pythagorean triplets
        #         if c< side_lim : separate_cnt += 1
        #
        #     if c > side_lim : break
        #
        #     a = m**2-n**2
        #     b = 2*m*n
        #
        #
        #     # if count !=  separate_cnt :
        #     print(' m, n = \t',m, n,'            a,b,c =\t', (a, b, c)  ,'      gcd3(a,b,c) = ', gcd3(a,b,c),'     gcd(m,n) = ', gcd(m,n) ,'        separate_cnt=  ', separate_cnt  )
        #
        #     # print( a, b, c )
        #
        #     n+=2
        #
        #

        m+=1

    # print('\nSeparate cnt = ', separate_cnt )


    print('\nANSWER = ', count )
    return count



Counting_PPT_solution( 10**6 )                # 10**6  =  159139
# Counting_PPT_solution( 3141592653589793 )                   #   ANSWER =  500000000002845




# @2018-05-17, 13:00 --> Must find the error !!!


t2  = time.time()
print('\n# Completed in :', round((t2-t1) , 2 ), 's\n\n')               # Completed in : 19905.62 s



#### IDEAS ###
# ====Tue, 29 Dec 2015, 10:59, Animus
# The development team found an O(n37) algorithm based on a different approach:
#
# Every pythagorean triple a2+b2=c2 with c≤n (nonprimitive and with unsorted legs a,b)
# corresponds to a lattice point in the complex area in the first quadrant with a maximal distance
# to the origin of n−−√, since by squaring the number z=x+iy, z2 represents a pythagorean triangle with a=|x2−y2|,
# b=2xy and c=x2+y2≤n.
# Thus the number of pythagorean triples can be calculated by determining the lattice points within
# a circle around the origin with radius n−−√.
#
# Based on a suggestion of Lucy_Hedgehog this can be done in O(n^(1/3) ),
# by calculating the convex hull of the circle points by incrementing the slope using steps based on the Stern-Brocot-tree.
# My Python implementation below just counts lattice points with uneven x- and even y-coordinates greater than 0
# to avoid duplicates and degenerated triples.
# By recursivly excluding points representing nonprimitive triples the complete algorithm reaches the indicated runtime behavior.
#
# Needs 2.44 sec in PyPy for P(⌊1015π⌋)=P(3141592653589793)
# and 47.4 sec for P(⌊1018π⌋)=P(3141592653589793238)=499999999999982329.



print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')

print('\n--------------------------SOLUTION 1,   --------------------------')
t1  = time.time()



def CP(n):
    '''
    return the points in the circle hull for x²+y²<=n, with x odd and y even
    vy/vx is the slope of the last (valid) line segment worked on, starting with 0/2
    cy/cx is the slope bigger than vy/vx, starting formally with 2/0
    cy/cx is gradually getting closer to vy/vx via cx=cx+vx, cy=cy+vy, as long as x+cx, y+cy are still within the circle,
     old values, being reused later, are stored on the stack

    Then vy/vx is approximated towards cy/cx via vx=vx+cx and vy=vy+cy ect. until the best
     possible next slope is found (via testing wether a smaller slope would possible reach
     the circle again)

    Thus vy/vx, cy/cx and the stack stk represent a stack based Stern-Brocot-tree

    A and B are used to count the points enclosed on the fly

    '''
    if n<5:
        return 0
    r=int(sqrt(n-1))
    while r*r>n-1:
        r-=1
    x,y=1,r/2*2
### points=[(x,y)]
    stk=[(0,2)]
    vx,vy=2,0
    A=0
    B=y
    while stk:
        while (x+vx)**2+(y-vy)**2<=n:
            x+=vx
            y-=vy
###         points.append((x,y))
            A+=vx*(2*y+vy)
            B+=2
        fnd=False
        cx,cy=stk.pop()
        while not fnd:
            while (x+cx)**2+(y-cy)**2<=n:
                stk.append((cx,cy))
                cx+=vx
                cy+=vy
            vx,vy=cx,cy
            if not stk:
                fnd=True
                break
            cx,cy=stk.pop()
            while True:
                if (x+vx+cx)**2+(y-vy-cy)**2<=n:
                    #next point reached still within the circle
                    stk.append((cx,cy))
                    cx+=vx
                    cy+=vy
                    break
                #can the circle still be hit with a lesser slope from the outside point
                 # x+vx, y+vy that would be reached with the last cy/cx slope?
                if cx*(x+vx+cx)>=cy*(y-vy-cy):
                    #no, therefore take the last valid value for vx,vy
                    vx,vy=cx,cy
                    fnd=True
                    break
                #not yet optimal? proceed
                vx+=cx
                vy+=cy
    B+=y-x+1
    return (A+2*B)/8
### return points


# @cached( { 0:0 , 1:0 , 2:0 , 3:0 , 4:0 } )
def P(n):
    res=CP(n)
    sn=int(n**0.36)
    for i in range(1,sn+1):
        res-=P(n/(2*i+1)**2)
    i2=i
    for j in range(n/(2*i+1)**2,0,-1):
        i=int(sqrt(n/j)-1)/2
        res-=(i-i2)*P(j)
        i2=i
    return res

# P(10**6)

t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')


print('\n--------------------------SOLUTION 2,   --------------------------')
t1  = time.time()



t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')


print('\n--------------------------SOLUTION 3,   --------------------------')
t1  = time.time()



t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')


print('\n--------------------------SOLUTION 4,   --------------------------')
t1  = time.time()



# Sun, 27 Dec 2015, 17:27, ChopinPlover, Taiwan
#
# By Diophantus parametrization, we can write a=x^2−y^2,b=2xy,c=x^2+y^2
# where gcd(x,y)=1 and x,y are of odd parity.
#
# Now we need to remove two conditions: gcd(x,y)=1 and odd parity.
#
# First we rewrite
# P(n)Q(n)={(x,y)∈A(n):gcd(x,y)=1,odd parity},={(x,y)∈A(n):gcd(x,y)=1}
# where A(n)={(x,y)|x2+y2≤n,0<x<y}.
#
# For any (x,y) in Q(n), there are two possible cases: (i) odd parity, (ii) two odd numbers.
# For case (i), (x,y)∈P(n). For case (ii), gcd(a,b,c)=2gcd(x2,xy,y2)=2, or (x,y)∈P(n/2).  Hence Q(n)=P(n)+P(n/2).
#
# Therefore we can get rid of odd parity,
# P(n)=∑k≥0(−1)kQ(n/2k).
#
#
# To get rid of gcd(x,y)=1, we can introduce Möbius function μ.  Similar to previous problem,
# Q(n)=∑1≤k≤⌊n√⌋μ(k)A(n/k2).
#
#
# Runtime is super bad because I bruteforce A(n).

import math
import sys

class Problem():
    def __init__(self):
        self.mu_values = None
        self.lattice_count_cache = { }
        self.coprime_count_cache = { 1 : 0 }

    def solve(self):
        assert(self.get(10**6) == 159139)

        for n in [3141592653589793]:
            print(n, '=>', self.get(n))

    def get(self, n):
        # Prepare Möbius function for computing coprime lattice count
        self.__init_mu_values(math.floor(math.sqrt(n)))

        # P(n) = sum_{k >= 0} (-1)^k Q(n/2^k) where
        #     P(n) = {(x,y) in A(n) : x, y coprime and odd parity},
        #     Q(n) = {(x,y) in A(n) : x, y coprime}
        total_count = 0
        k = 0
        while 2**k <= n:
            coprime_count = self.__get_coprime_lattice_count(n // 2**k)
            total_count += (-1)**k * coprime_count
            print('get =>', k, coprime_count, total_count)
            k += 1
        return total_count

    def __init_mu_values(self, n):
        prime_sieve = [False for i in range(n + 1)]
        m = math.floor(math.sqrt(n))
        for i in range(2, m + 1):
            if prime_sieve[i] is True:
                continue
            for j in range(i * i, n + 1, i):
                prime_sieve[j] = True

        values = [1 for i in range(n + 1)]
        for i in range(2, n + 1):
            if prime_sieve[i] is True:
                continue
            for j in range(i, n + 1, i):
                values[j] *= -1
            for j in range(i**2, n + 1, i**2):
                values[j] = 0
        self.mu_values = values

    def __get_lattice_count(self, n):
        # Let A(n) = #{(x,y) : x^2 + y^2 <= n, 0 < x < y}.
        if n not in self.lattice_count_cache:
            total_count = 0
            x = 1
            while True:
                max_y = math.floor(math.sqrt(n - x**2))
                min_y = x + 1
                if max_y < min_y:
                    break
                else:
                    total_count += (max_y - min_y + 1)
                x += 1
            self.lattice_count_cache[n] = total_count
        return self.lattice_count_cache[n]

    def __get_coprime_lattice_count(self, n):
        # Q(n) = sum_{d <= sqrt[n]} mu(d) A(floor[n/d^2])
        if n not in self.coprime_count_cache:
            total_count = 0
            m = math.floor(math.sqrt(n))
            for i in range(1, m + 1):
                mu = self.mu_values[i]
                if mu != 0:
                    total_count += mu * self.__get_lattice_count(n // i**2)
            self.coprime_count_cache[n] = total_count
        return self.coprime_count_cache[n]

def main():
    problem = Problem()
    problem.solve()

# main()

t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')


print('\n--------------------------SOLUTION 5,   --------------------------')
t1  = time.time()


# === Sun, 27 Dec 2015, 16:15, Thierry Machicoane, Switzerland
# Wow!!!! First time I'm in the first fifty. So happy!

def euler_totient( dict_list_int ):           # Remark : For large array better use Sieve approach
    """ **©** Made by Bogdan Trif @ 2017-02-08 .
    returns Euler totient (phi) of n = Φ (n)
        Uses the formula of the Totient  : Φ (n) =  Π {p | n}  n *(1 - 1/p) ;
        where p are each prime factors and n is the number  for which we compute
        In number theory, Euler's totient function counts the positive integers up to a given integer n
        that are relatively prime to n. It is written using the Greek letter phi as φ(n) or ϕ(n),
        and may also be called Euler's phi function.
        Example : Φ (12) = 4 =   [1,5,7,11]
        https://en.wikipedia.org/wiki/Euler's_totient_function
        http://marcharper.codes/2015-08-07/totients.html
        :D: is a dictionary of the form {p1:k1, p2:k2...}. E.g : for 90 = {2:2, 3:2, 5:1 }
        or it is a list of the form 180 = [2, 2, 3, 3, 5 ]
        or it is an INT number
        """
    if type(dict_list_int) == dict :
        pfs = [ i for i in dict_list_int ]
        phi = 1
        for a in  [ i**j for i,j in dict_list_int.items() ] :
            phi *= a
    if type(dict_list_int) == list :
        pfs = set(dict_list_int)
        phi = 1
        for a in dict_list_int :
            phi *= a
    if type(dict_list_int) == int :
        pfs = [ i[0] for i in factorise(dict_list_int)]
        phi = dict_list_int

    for pf in pfs:
        phi *= (1-1/pf)
    return int(phi)

def prime_sieve(n):       # FOURTH      o(^_^)o
    sieve = [True] * n
    for i in range(3, int(n**0.5)+1, 2):
        if sieve[i]:
            sieve[ i*i :: 2*i ] = [False] * ( (n-i*i-1) // (2*i) +1 )
    return [2] + [i for i in range(3, n , 2) if sieve[i] ]



def compute(n, factors, Qin=1, index=0):
    S = 0
    for i in range(index,len(factors)):
        Qout = Qin * factors[i]
        S += n // Qout - compute(n, factors, Qout, i+1)
    return S

F = Factorization(int(sqrt( 10**6 ))  )

def count(n, B):
    dec = F.get_factors(n)
    dec.append(2)
    return B - compute(B,dec)

def P540(N):
    global PRIMES

    A = int(N**0.5)
    PRIMES = (A)

    S = 0
    k = 3
    while k <= A:
        S += euler_totient(k) // 2
        k += 2

    A = int((2*N)**0.5)
    while k <= A:
        B = int((2*N - k*k)**0.5)
        S += count(k,B)
        k += 2
    print('\nSolution = ', S )
    return S

# P540(10**6)

t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')


# print('\n--------------------------SOLUTION 6,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
print('\n--------------------------SOLUTION 7,  NICE, Similar to mine but optimized  --------------------------')
t1  = time.time()

# ==== Sun, 10 Apr 2016, 21:36, wakkadojo, USA

# What? I'm still on first page?
#
# This problem is about counting all of the coprimes m less than n where n - m is odd.
# The way I tackled this was by focusing on n even, since in that case all of the coprimes satisfy the parity condition above.
# Tabulate all of the prime factors of a number, and use inclusion / exclusion on the combinations to count
# the numbers that are NOT coprime.
# Runs in a few minutes, though it's embarrassingly parallel,
# so it might be a fun exercise to get it running fast on multiple processors.

import itertools

def prime_sieve (n):
    s = [ False if i % 2 == 0 else True for i in range (n) ]
    yield 2
    for i in range (3, n):
        if s[i]:
            for j in range (i*i, n, i):
                s[j] = False
            yield i


def factorize (M, s):
    f = [ [] for _ in range (M) ]
    for p in s:
        for x in range (p, M, p):
            f[x] += [p]
    return f

def product (l):
    out = 1
    for x in l:
        out *= x
    return out

# coprime to k less than m
def count_coprime (k, m, f):
    total = 0
    for i in range (1, len (f)+1):
        prefactor = (-1)**(i+1)
        for x in itertools.combinations (f, i):
            total += prefactor*(m//product (x))
    return m - total

def count_triples (M, f):
    total = 0
    for i in range (2, int ((M)**0.5) + 1, 2):
        total += count_coprime (i, int ((M - i*i)**0.5), f[i])
    return total


M0 = 3141592653589793
M0 = 10**12
M = int(M0**0.5)+1
s = prime_sieve(M)
f = factorize(M, s)
print (count_triples (M0, f))

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

