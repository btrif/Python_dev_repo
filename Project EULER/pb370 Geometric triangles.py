#  Created by Bogdan Trif on 02-11-2017 , 11:39 PM.
# © o(^_^)o  Solved by Bogdan Trif  @
#The  Euler Project  https://projecteuler.net
'''
                    Geometric triangles         -           Problem 370

Let us define a geometric triangle as an integer sided triangle with sides a ≤ b ≤ c so
that its sides form a geometric progression, i.e. b^2 = a · c .

An example of such a geometric triangle is the triangle with sides :
a = 144, b = 156 and c = 169.

There are 861.805 geometric triangles with perimeter ≤ 10^6 .

How many geometric triangles exist with perimeter ≤ 2.5·10^13   ?


'''
import time, zzz
from pyprimes import factorise
from gmpy2 import is_prime, gcd, mpq


phi = (1+5**(1/2))/2
phi_ = (1-5**(1/2))/2

def get_factors(n):       ### o(^_^)o  FASTEST  o(^_^)o  ###
    ''' Decompose a factor in its prime factors. This function uses the pyprimes module. THE FASTEST  '''

    return [val for sublist in [[i[0]]*i[1] for i in factorise(n)] for val in sublist]


#print(list(i[0] for i in list(factorise(3932273))))


import itertools

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
        print('Prime count:', len(self.primes) ,'           ATTENTION , LARGEST PRIME Included = ', self.primes[-1] ,'       !!!!!!!!!!!! ' )

class Factorization():

    ''' Based on a prebuilt prime sieve, and we must pay attention that the prime up range is not
    to low, so that we don't miss a prime when we first factor . As default the value is set to 10.000
      So we need uprange /2         '''
    def __init__(self, bound):
        self.bound = bound
        self.prime_table = PrimeTable(bound)

    def get_factors(self, n):
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
        return f


    def get_divisors(self, n) :
        f = self.get_factors(n)
        unpacking = [[p**e for e in range(f[p] + 1)] for p in f]
        return sorted([self._product(divisor) for divisor in itertools.product(*unpacking)])


    def _product(self, list):
        result = 1
        for number in list:
            result *= number
        return result


F  = Factorization( 10**6 )
print( F.get_divisors(36) )


print('\n--------------------------TESTS------------------------------')
t1  = time.time()


def brute_force_testing(lim):           # @2017-11-07 - Algorithm confirmed for small limits
    cnt = 1
    b=2
    max_ca = 0
    while b < lim/3 :
        if b % 10**5 == 0 : print(b)

        cnt+=1          # We add triangles like 3,3,3 ; 6, 6, 6,

        if not is_prime(b) :
            Dvs = F.get_divisors(b*b)
            # print( str(b)+'.         ', b*b   , '          ',  Dvs  )

            e = 0
            while Dvs[e] < b :
                a  =  Dvs[e]
                c = b*b//a
                if a+b+c <= lim and a+b > c :
                    cnt+=1
                    div_A = Factorization().get_divisors(a)
                    print(str(cnt)+ '.         ' ,a,'  ' , b, '  ',c ,'      mpq(b,a)=' ,   mpq(b,a) ,  '    div_A = ', div_A  , '       a= ' , get_factors(a)  ,'        b=',  get_factors(b) ,'        c=', get_factors(c) ,'   ratio r= ' , c/b   )


                e+=1

        b+=1

    return print('\nGeom Triangles = ', cnt)

# brute_force_testing(10**6)                    #           Geom Triangles =  861805        CORRECT !
brute_force_testing(10**4)

#### REFERENCE VALUES :
# lim = 10^4 there are 6427 triangles
# lim = 10^5 there are 75243 triangles

# @2017-11-07- This problems needs a sublinear algorithm ( < O(n) => O(sqrt(n))   or O ( n * log(n) ).
# KEY OBSERVATION :
# 1.          Numbers with huge prime factors differences must be ignored .
# 2.           b - is a COMPOSITE number ( its prime factorisation is composed of at least 2 primes)
# 3.          Generate b - But see that for each b there are multiple (a, c) pairs . Example :
# 72.          48 72 108      a=  [2, 2, 2, 2, 3]         b= [2, 2, 2, 3, 3]         c= [2, 2, 3, 3, 3]
# 72.          54 72 96        a=  [2, 3, 3, 3]         b= [2, 2, 2, 3, 3]         c= [2, 2, 2, 2, 2, 3]
# 72.          64 72 81        a=  [2, 2, 2, 2, 2, 2]         b= [2, 2, 2, 3, 3]         c= [3, 3, 3, 3]

# OBSERVATION 2 : limit of c/a ratio approaches e - natural base algorithm c/a =  2.6180073311352206  ( e =2.7182 )

# Must do some kind of pre-build SMART factorization !

# 2018-05-05 - b contain terms from both a, c
# CONDITION a+b < c : IS  MANDATORY    !!!!!


# ==== PROCEDURE ==== :
# 1.  Generate all COMPOSITE b's from prim factors . --> [2, 3], [2, 5], [2,2,3], [3, 5] ,[2, 3, 3  ]
# 2.     Balance the square of b , a range is --> [b/2, b] maximum such that a+b > c  ---> ALGORITHM STRONG !!!
#
# 3.          2018-06-18, 12:30 - KEY OBSERVATION :          !!!!!!!!!!!!
# BOTH a & c ARE having at least a factor square or more . Example :
# 81 108 144        a=  [3, 3, 3, 3]         b= [2, 2, 3, 3, 3]         c= [2, 2, 2, 2, 3, 3] =>
# This reduces our span search TO  sqrt(25 *10^12) = 5 * 10 ^ 6 = 5.000.000
# which is  O( n^(1/2) ) algorithm     AND LESS BECAUSE :
#  in this example :   363 429 507        a=  [3, 11, 11]         b= [3, 11, 13]         c= [3, 13, 13]
# 11*11= 121 so we iterate to 11 and multiply by 3 = 363
# More than that if we raise the bigger power the remaining factor decreases :

# STRATEGY :
# 1. Find a way to generate all "a" terms :
# 2. construct "a" from taking care that b >= a and that by forming b it will  result   b <=  c = b^2/a < (a+b)
# HERE I must find a NICE ALGO !
#
#
# 304 380 475        a=  [2, 2, 2, 2, 19]         b= [2, 2, 5, 19]         c= [5, 5, 19]
# 304 456 684        a=  [2, 2, 2, 2, 19]         b= [2, 2, 2, 3, 19]         c= [2, 2, 3, 3, 19]
#
# 144 156 169        a=  [2, 2, 2, 2, 3, 3]         b= [2, 2, 3, 13]         c= [13, 13]            mpq(b,a)= 13/12
# 144 168 196        a=  [2, 2, 2, 2, 3, 3]         b= [2, 2, 2, 3, 7]         c= [2, 2, 7, 7]          mpq(b,a)= 7/6
# 144 180 225        a=  [2, 2, 2, 2, 3, 3]         b= [2, 2, 3, 3, 5]         c= [3, 3, 5, 5]          mpq(b,a)= 5/4
# 144 192 256        a=  [2, 2, 2, 2, 3, 3]         b= [2, 2, 2, 2, 2, 2, 3]         c= [2, 2, 2, 2, 2, 2, 2, 2]            mpq(b,a)= 4/3
# 144 204 289        a=  [2, 2, 2, 2, 3, 3]         b= [2, 2, 3, 17]         c= [17, 17]                mpq(b,a)= 17/12
# 144 216 324        a=  [2, 2, 2, 2, 3, 3]         b= [2, 2, 2, 3, 3, 3]         c= [2, 2, 3, 3, 3, 3]         mpq(b,a)= 3/2
# 144 228 361        a=  [2, 2, 2, 2, 3, 3]         b= [2, 2, 3, 19]         c= [19, 19]                mpq(b,a)= 19/12
#
#
# if a = [2, 2, 2, 2, 19] contains a single prime factor  like here   => b mandatory that will contain [ 19 ]

t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')

print('\n================  My FIRST SOLUTION,   ===============\n')
# t1  = time.time()





# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')


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




