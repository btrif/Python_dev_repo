#!/usr/bin/python                   o(^_^)o         ( ͡° ͜ʖ ͡°)
# © Solved by Bogdan Trif @     Completed on Sun, 26 Mar 2017, 22:12
#The  Euler Project  https://projecteuler.net
'''
                Alexandrian Integers        -       Problem 221

We shall call a positive integer A an "Alexandrian integer", if there exist integers p, q, r such that:

A = p · q · r    and  	    1 / A = 1 / p - 1 / q - 1 / r

For example, 630 is an Alexandrian integer (p = 5, q = −7, r = −18).
In fact, 630 is the 6th Alexandrian integer,
the first 6 Alexandrian integers being: 6, 42, 120, 156, 420 and 630.

Find the 150000th Alexandrian integer.

'''
import time, zzz
from gmpy2 import mpq, is_prime
import heapq
# from _primes_work_tool import get_divisors

def get_factors(n):       ### o(^_^)o  FASTEST  o(^_^)o  ###
    ''' Decompose a factor in its prime factors. This function uses the pyprimes module. THE FASTEST  '''
    from pyprimes import factorise
    return [val for sublist in [[i[0]]*i[1] for i in factorise(n)] for val in sublist]

def get_divisors(n):      ### ( ͡° ͜ʖ ͡°)  FASTEST  ( ͡° ͜ʖ ͡°)  ### !! FIRST FASTEST !! Must be improved !!
    from math import sqrt
    factors = set()
    for x in range(1, int(sqrt(n)) + 1):
        if n % x == 0:
            factors.add(x)
            factors.add(n//x)
    return sorted(factors)

print('\n--------------------------TESTS------------------------------')
t1  = time.time()

listForTree = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
heapq.heapify(listForTree)             # for a min heap

print('Minimum element is always first :\t',listForTree)
heapq.heappop(listForTree)


def brute_force(lim,nth):
    AI = []
    heapq.heapify(AI)
    # heapq._heapify_max(AI)
    cnt = 0
    for p in range(1, lim+1 ):
        for q in range(p+1,lim+1 ) :
            for r in range(q+1, lim+1 ):
                A = p * q * r
                if mpq(1, A) == mpq(1, p) - mpq(1, q) - mpq(1, r) :
                    cnt +=1
                    AI.append(A)
                    print(str(cnt)+'.      ', 'p=',p,'  q=',q,'  r=',r , '       k=',q-p ,'     A=', A,'       1/A = ', mpq(1,A),'     p= ',get_factors(p) , '   q=',get_factors(q), '   r=', get_factors(r) )
    print( heapq.nsmallest(nth, AI) )
    return print('\n'+str(nth)+'-th Alexandrian Integer is : \t', heapq.nsmallest(nth, AI)[-1] )


# brute_force(5*10**2, 150)


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n================  My FIRST SOLUTION,  10 min  ===============\n')
t1  = time.time()

# =====    SOLUTION =========
#
# 0.          A = pqr                                                                                                               (eqn 0)
# 1.          1/A = ( qr + pr+ pq) /pqr
# 2.          A = pqr = A * ( qr + pr+ pq) )    =>   we simplify to   : qr + pr + pq = 1                  (eqn 1)
# 3.          Without loss of generality we note that 0 < p < q< r
# 4.          From (1) we rewrite r as :  -r = (pq -1 )/ (p+q)                                                        (eqn 2)
# 5.          We introduce a new variable k such that  1<=k <=p
#                                                      and q = p+k                                                                       (eqn 3)
# 6.          Introducing  (3) into (2) => -r = (-p(p+k)-1) / (p-p-k) = (-p**2-1)/k - pk/k =>
#                     => r = ( p**2+1) /k + p                                                                             (eqn 4)
# 7.          But r is integer and therefore (p**2+1) / k is integer,  therefore k | (p**2+1)         or  (p**2+1) %k ==0
# 8.          Substituting (4) ,  (3) into (0) we get that :
#                 A = pqr =  p * (p+k) *  (( p**2+1) /k + p  )
#
# 9.          Last observation  : we iterate over p and take only k for which (p**2+1) % 3 ==1 or 2
#             k - is never a multiple of 3. The full explanation is found here :
#     http://math.stackexchange.com/questions/630742/whats-the-explanation-for-why-n21-is-never-divisible-by-3



def my_first_solution( lim ) :
    AI = []
    heapq.heapify(AI)
    p, cnt = 1, 0
    while cnt  < 4*lim  :
        K = get_divisors(p**2+1)
        i=0
        while K[i] <= p :
            k = K[i]
            q, r = p+k ,  ((p*p+1)//k) +p
            A = p*q*r
            AI.append(A)
            cnt+=1
            if cnt % 1000 == 0 :
                print(str(cnt)+'.      ', 'p=',p,'  q=',q,'  r=',r , '       k=',k ,'     A=', A,'       1/A = ', mpq(1,A)  )

            i+=1
        p+=1
    # AI.sort()
    # print( AI[lim-1] )
    return print('\n'+str(lim)+'-th Alexandrian Integer is : \t', heapq.nsmallest(lim, AI)[-1] )

# my_first_solution(150000 )      #       150000-th Alexandrian Integer is : 	 1884161251122450

# CORRECT VALUES:         10000-th Alexandrian Integer is : 	 628833933090


t2  = time.time()
print('\nCompleted in :', round((t2-t1), 6), 's\n\n')               #       Completed in : 659.715734 s


print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1,  22 sec --------------------------')
t1  = time.time()

# ====Fri, 17 Oct 2014, 00:36, umu , Germany
# First arrived at 1 = pq + qr +pr, than at 1 + pq = r(p-q). With d=p-q this results in:
#
# A = q + 2 q³ + q² ( d + (1+q²)/d )
#
# As p,q,r must be coprime, so must be q,d, so d must be a divisor of 1+q². Then iterated over q,
# and over the divisors of (1+q²). For efficiency precalculated prime decomposition of all (1+q²)
# with a sieve and generated each list of divisors from this.
#
# So far fine. But the main problem seemed for me when to stop iterating q.
# For any q the worst case is for d=1 or d=1+q²  =>  A = q + 2 q^3 + 2q^2 + q^4 , what is polynom of order 4.
# The best case for another (bigger) Q would be for d close to sqrt(1+q²):  A ~ Q + 2 Q^3 + Q^2 * 2Q.
# What is of order 3. So if we are unlucky, some solution for Q near 5000000 could still beat solutions for q near 150000.
#
# Fortunately enough I found 150000 solutions for q<=28037 already.
# Corresponding Q where we can be sure that it won't have better solutions is "only" around 650000.
# So even if stated in some earlier post, that checking until ~80000 will be enough,
# as mathematician we SHOULD check further until 650000, getting a list of more than 4 million candidates to sort...
#
# Still quite fast, thanks to sieve, 10s Python.

N = 150000
Q = int( (30000**4/3.)**(1./3) )

fs = [0]*Q
for i in range(Q): fs[i] = [ i*i+1,[] ]

for i in range(Q):
  if fs[i][0]>1:
    p = fs[i][0]
    for j in range(i, Q, p):
      k=0
      while fs[j][0]%p==0:
        k += 1
        fs[j][0] //= p
      fs[j][1].append((p,k))
    if p-i!=i:
      for j in range(p-i,Q,p):
        k=0
        while fs[j][0]%p==0:
          k += 1
          fs[j][0] //= p
        fs[j][1].append((p,k))

def divisors(f):
  div = [1]
  for (p,k) in f:
    l = len(div)
    m = 0
    for i in range(k):
      for j in range(l):
        div.append(div[m]*p)
        m += 1
  div.sort()
  return div

print (fs[:2])
print (divisors(fs[7][1]))

q = 0
na = 0
As = []
while q<Q-1:
  q += 1
  div = divisors(fs[q][1])
  ndiv = len(div)
  for i in range(ndiv//2-1,-1,-1):
    d = div[i] + div[ndiv-1-i]
    A = q + 2*q**3 +q**2*d
    As.append(A)

    na += 1
    if na==N:
      print (q)
      # continue checking up to Q with Q+4*Q^3 > q+2*q^3+2*q^2+q^4

print ("q=",q)
print ("na",na)

print (As[:30])
As.sort()
print (As[:30])
print (As[N-1])

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 2,   --------------------------')
t1  = time.time()

# ==== Fri, 7 Jun 2013, 13:23, tom.wheldon, England
# Quite easy to get the answer using the formula from oeis A147811: by finding divisors of n^2+1
# generate what you hope will be enough numbers, sort them, check the 150,000th against the answer,
# and if it's wrong use a higher limit next time. My first version was about 8 lines of Python (not counting utility functions).
# Rather more difficult to generate just enough numbers to guarantee getting the right answer first time.
# I produced better looking versions of the code but they took longer to run (note that various minus signs
# in the code occur because the heap module from the Python standard library
# is a min heap and the value I'm interested in is a maximum).




from heapq import *

def prime_factors(n,primes):
    c = Counter()
    for p in primes:
        if p*p > n: break
        if n%p: continue
        while not n%p:
            n //= p
            c[p] += 1
    if n > 1:
        c[n] += 1
    return c

def divisors(n,primes):
    c = prime_factors(n,primes)
    divs = []
    ps = list(c.keys())
    r = len(ps)
    for exps in product(*[range(v+1) for v in c.values()]):
        d = 1
        for i in range(r):
            d *= ps[i]**exps[i]
        divs.append(d)
    return sorted(divs)


limit = 10**6
N = 150000
primes = [2] + primeslist(N,1) # Second argument = 1  produces primes of form 4k+1

hq = []
for n in range(1,limit):
    if len(hq) >= N:
        nextn = n
        break
    divs = divisors(n*n + 1, primes)
    for i in range((len(divs)+1)//2):
        a = n*(n+divs[i])*(n+divs[-(i+1)])
        heappush(hq,-a)

while len(hq) > N:
    heappop(hq)

maxn = 0
for n in range(nextn,limit):
    divs = divisors(n*n + 1, primes)
    for i in range((len(divs)-1)//2,-1,-1):
        a = (n*(n+divs[i])*(n+divs[-(i+1)]))
        if -a < hq[0]:
            break
        else:
            heapreplace(hq,-a)
            maxn = int((-hq[0]/4)**(1/3))
    if n > maxn : break
else:
    print('maxn greater than limit')

print(-heappop(hq),maxn)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 3,   --------------------------')
t1  = time.time()



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

