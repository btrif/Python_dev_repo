#  Created by Bogdan Trif on 13-01-2019 , 8:41 PM.
# © o(^_^)o  Solved by Bogdan Trif  @   Completed on Mon, 14 Jan 2019, 19:03
#The  Euler Project  https://projecteuler.net
'''
                            Summation of primes             -               Problem 10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.


'''
import time, zzz
import numpy

print('\n--------------------------TESTS------------------------------')
t1  = time.time()



t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')

print('\n================  My FIRST SOLUTION,   ===============\n')
t1  = time.time()


def prime_sieve_numpy(n):                       ### o(^_^)o  FASTEST  o(^_^)o  ###  Highly Efficient !!!
    """ Input n>=6, Returns a array of primes, 2 <= p < n
    http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n/3035188#3035188 """
    sieve = numpy.ones(n//3 + (n%6==2), dtype = numpy.bool)
    for i in range(1,int(n**0.5)//3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[       k*k//3    :: 2*k ] = False
            sieve[ k*(k-2*(i&1)+4)//3 :: 2*k ] = False
    return numpy.r_[ 2, 3, (( 3*numpy.nonzero(sieve)[0][1:]+1)|1) ]

lim = 2*10**6
Primes = prime_sieve_numpy(lim)

print('\nANSWER :     ',  sum(Primes)  )        #       ANSWER :      142913828922



t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')        # Completed in : 226.01 ms


print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 0,   OUTSTANDING  , Lucy_Hedgehog   --------------------------')
t1  = time.time()

'''     ==== Fri, 3 May 2013, 21:14, Lucy_Hedgehog , Switzerland

Here is a solution that is more efficient than the sieve of Eratosthenes. 
It is derived from similar algorithms for counting primes. 
The advantage is that there is no need to find all the primes to find their sum.

The main idea is as follows: Let S(v,m) be the sum of integers in the range 2..v that remain 
after sieving with all primes smaller or equal than m. 
That is S(v,m) is the sum of integers up to v that are either prime or the product of primes larger than m. 

S(v, p) is equal to S(v, p-1) if p is not prime or v is smaller than p*p. 
Otherwise (p prime, p*p<=v) S(v,p) can be computed from S(v,p-1) 
by finding the sum of integers that are removed while sieving with p. 

An integer is removed in this step if it is the product of p with another integer that has no divisor smaller than p. 
This can be expressed as

S(v,p) = S(v,p−1) − p( S(v/p,p−1)−S(p−1,p−1) ).

Dynamic programming can be used to implement this. It is sufficient to compute S(v,p) 
for all positive integers v that are representable as floor(n/k) for some integer k and all p≤v√.

The complexity of this algorithm is about O(n0.75) and needs 9 ms to find the solution. 
Computing the sum of primes up to different bounds n gives:

n = 2*10**7: 12272577818052  0.04 s
n = 2*10**8: 1075207199997334  0.2 s
n = 2*10**9: 95673602693282040  1 s
n = 2*10**10: 8617752113620426559  6.2 s
n = 2*10**11: 783964147695858014236  34 s
n = 2*10**12: 71904055278788602481894  3 min

I also have a C++ version of this algorithm. This one solves the problem in 700μs.
 It needs 10 hours to compute the sum of primes up to 10^17 which is 129408626276669278966252031311350.

It is also possible to improve the complexity of the algorithm to O(n2/3), but the code would be more complex.

'''

def P10(n):
    r = int(n**0.5)
    assert r*r <= n and (r+1)**2 > n
    V = [n//i for i in range(1,r+1)]
    V += list(range(V[-1]-1,0,-1))
    S = {i:i*(i+1)//2-1 for i in V}
    for p in range(2,r+1):
        if S[p] > S[p-1]:  # p is prime
            sp = S[p-1]  # sum of primes smaller than p
            p2 = p*p
            for v in V:
                if v < p2: break
                S[v] -= p*(S[v//p] - sp)
    return S[n]

lim = 2*10**6

print( 'Answer = ' ,P10( lim )   )


t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')

print('\n--------------------------SOLUTION 1,  WTF ?  --------------------------')
t1  = time.time()

'''     ====Mon, 2 Jan 2012, 22:09,     Francky
I ever post my optimized Python3 code a few month ago, but it had been lost in the wave. 
I think it's the fastest Python'one, so I post again.

Recently I rewrote a genSieve : a program that write my sieve-program with a wheel 
with the size I want : 2, 6, 30 or 210. (or even more)
The last one is 7000 lines of code and 5% faster than the 30-wheel. 
So I prefer the 30-wheel (less than 200 lines).

It's a 30-whell and use bytearray. (and quite cryptic)

'''

def primes(lim):
  # cas particuliers
  if lim<7:
    if lim<2: return []
    if lim<3: return [2]
    if lim<5: return [2, 3]
    return [2, 3, 5]
  #  Crible
  n = (lim-1)//30
  m = n+1
  BA = bytearray
  prime1 = BA([1])*m
  prime7 = BA([1])*m
  prime11 = BA([1])*m
  prime13 = BA([1])*m
  prime17 = BA([1])*m
  prime19 = BA([1])*m
  prime23 = BA([1])*m
  prime29 = BA([1])*m
  prime1[0] = 0
  i = 0
  try:
    while 1:
      if prime1[i]:
        p = 30*i+1
        l = i*(p+1)
        prime1[l::p] = BA(1+(n-l)//p)
        l += i*6
        prime7[l::p] = BA(1+(n-l)//p)
        l += i*4
        prime11[l::p] = BA(1+(n-l)//p)
        l += i*2
        prime13[l::p] = BA(1+(n-l)//p)
        l += i*4
        prime17[l::p] = BA(1+(n-l)//p)
        l += i*2
        prime19[l::p] = BA(1+(n-l)//p)
        l += i*4
        prime23[l::p] = BA(1+(n-l)//p)
        l += i*6
        prime29[l::p] = BA(1+(n-l)//p)
      if prime7[i]:
        p = 30*i+7
        l = i*(p+7)+1
        prime19[l::p] = BA(1+(n-l)//p)
        l += i*4+1
        prime17[l::p] = BA(1+(n-l)//p)
        l += i*2+1
        prime1[l::p] = BA(1+(n-l)//p)
        l += i*4
        prime29[l::p] = BA(1+(n-l)//p)
        l += i*2+1
        prime13[l::p] = BA(1+(n-l)//p)
        l += i*4+1
        prime11[l::p] = BA(1+(n-l)//p)
        l += i*6+1
        prime23[l::p] = BA(1+(n-l)//p)
        l += i*2+1
        prime7[l::p] = BA(1+(n-l)//p)
      if prime11[i]:
        p = 30*i+11
        l = i*(p+11)+4
        prime1[l::p] = BA(1+(n-l)//p)
        l += i*2
        prime23[l::p] = BA(1+(n-l)//p)
        l += i*4+2
        prime7[l::p] = BA(1+(n-l)//p)
        l += i*2
        prime29[l::p] = BA(1+(n-l)//p)
        l += i*4+2
        prime13[l::p] = BA(1+(n-l)//p)
        l += i*6+2
        prime19[l::p] = BA(1+(n-l)//p)
        l += i*2+1
        prime11[l::p] = BA(1+(n-l)//p)
        l += i*6+2
        prime17[l::p] = BA(1+(n-l)//p)
      if prime13[i]:
        p = 30*i+13
        l = i*(p+13)+5
        prime19[l::p] = BA(1+(n-l)//p)
        l += i*4+2
        prime11[l::p] = BA(1+(n-l)//p)
        l += i*2+1
        prime7[l::p] = BA(1+(n-l)//p)
        l += i*4+1
        prime29[l::p] = BA(1+(n-l)//p)
        l += i*6+3
        prime17[l::p] = BA(1+(n-l)//p)
        l += i*2+1
        prime13[l::p] = BA(1+(n-l)//p)
        l += i*6+3
        prime1[l::p] = BA(1+(n-l)//p)
        l += i*4+1
        prime23[l::p] = BA(1+(n-l)//p)
      if prime17[i]:
        p = 30*i+17
        l = i*(p+17)+9
        prime19[l::p] = BA(1+(n-l)//p)
        l += i*2+1
        prime23[l::p] = BA(1+(n-l)//p)
        l += i*4+3
        prime1[l::p] = BA(1+(n-l)//p)
        l += i*6+3
        prime13[l::p] = BA(1+(n-l)//p)
        l += i*2+1
        prime17[l::p] = BA(1+(n-l)//p)
        l += i*6+3
        prime29[l::p] = BA(1+(n-l)//p)
        l += i*4+3
        prime7[l::p] = BA(1+(n-l)//p)
        l += i*2+1
        prime11[l::p] = BA(1+(n-l)//p)
      if prime19[i]:
        p = 30*i+19
        l = i*(p+19)+12
        prime1[l::p] = BA(1+(n-l)//p)
        l += i*4+2
        prime17[l::p] = BA(1+(n-l)//p)
        l += i*6+4
        prime11[l::p] = BA(1+(n-l)//p)
        l += i*2+1
        prime19[l::p] = BA(1+(n-l)//p)
        l += i*6+4
        prime13[l::p] = BA(1+(n-l)//p)
        l += i*4+2
        prime29[l::p] = BA(1+(n-l)//p)
        l += i*2+2
        prime7[l::p] = BA(1+(n-l)//p)
        l += i*4+2
        prime23[l::p] = BA(1+(n-l)//p)
      if prime23[i]:
        p = 30*i+23
        l = i*(p+23)+17
        prime19[l::p] = BA(1+(n-l)//p)
        l += i*6+5
        prime7[l::p] = BA(1+(n-l)//p)
        l += i*2+1
        prime23[l::p] = BA(1+(n-l)//p)
        l += i*6+5
        prime11[l::p] = BA(1+(n-l)//p)
        l += i*4+3
        prime13[l::p] = BA(1+(n-l)//p)
        l += i*2+1
        prime29[l::p] = BA(1+(n-l)//p)
        l += i*4+4
        prime1[l::p] = BA(1+(n-l)//p)
        l += i*2+1
        prime17[l::p] = BA(1+(n-l)//p)
      if prime29[i]:
        p = 30*i+29
        l = i*(p+29)+28
        prime1[l::p] = BA(1+(n-l)//p)
        l += i*2+1
        prime29[l::p] = BA(1+(n-l)//p)
        l += i*6+6
        prime23[l::p] = BA(1+(n-l)//p)
        l += i*4+4
        prime19[l::p] = BA(1+(n-l)//p)
        l += i*2+2
        prime17[l::p] = BA(1+(n-l)//p)
        l += i*4+4
        prime13[l::p] = BA(1+(n-l)//p)
        l += i*2+2
        prime11[l::p] = BA(1+(n-l)//p)
        l += i*4+4
        prime7[l::p] = BA(1+(n-l)//p)
      i+=1
  except:
    pass
  #  Génération
  RES = [2, 3, 5]
  A = RES.append
  ti=0
  try:
    for i in range(n):
      if prime1[i]: A(ti+1)
      if prime7[i]: A(ti+7)
      if prime11[i]: A(ti+11)
      if prime13[i]: A(ti+13)
      if prime17[i]: A(ti+17)
      if prime19[i]: A(ti+19)
      if prime23[i]: A(ti+23)
      if prime29[i]: A(ti+29)
      ti+=30
  except:
    pass
  if prime1[n] and (30*n+1)<=lim: A(30*n+1)
  if prime7[n] and (30*n+7)<=lim: A(30*n+7)
  if prime11[n] and (30*n+11)<=lim: A(30*n+11)
  if prime13[n] and (30*n+13)<=lim: A(30*n+13)
  if prime17[n] and (30*n+17)<=lim: A(30*n+17)
  if prime19[n] and (30*n+19)<=lim: A(30*n+19)
  if prime23[n] and (30*n+23)<=lim: A(30*n+23)
  if prime29[n] and (30*n+29)<=lim: A(30*n+29)
  return RES

# from time import time
# primes(10**7)
# for e in range(6, 9):
#   st=time()
#   print("2×10^", e, " --> ", sum(primes(2*10**e)), " in ", time()-st, "s", sep="")


t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')


print('\n---------------------SOLUTION 2, VERY GOOD, bytearray   --------------------------')
t1  = time.time()

from itertools import compress
def primes(lim):
    BA = bytearray
    prime = BA([1])*(lim+1)
    prime[0]=prime[1]=0

    for p in range(2, int(lim**0.5)+1):
        if prime[p]: prime[p*p::p] = BA(1 + lim//p - p)

    return compress(range(lim+1), prime)

lim = 2*10**6
print( sum(primes( lim )) )



t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')


print('\n--------------------------SOLUTION 3, OUTSTANDING  --------------------------')
t1  = time.time()

from itertools import compress
def primes(lim):
    "generateur de premier impair"
    assert lim>2
    BA = bytearray
    n = (lim-1)//2
    prime = BA([1])*(n+1)
    prime[0] = 0 # 2*0+1 = 1 n'est pas premier
    # Crible
    for i in range((int(lim**0.5)+1)//2):
        if prime[i]:
            p = 2*i+1 # p est premier
            i2 = i*(i+1)<<1
            prime[i2::p]=BA(1+ (n-i2)//p )
    return compress(range(1,lim+1,2),prime)

for i in range(3, 30):  # tests
  print(i, list(primes(i)))

lim = 2*10**6
print('\nPrimes sum up to ' +str(lim) + '  = ',2+sum(primes( lim )) )

t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')


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

