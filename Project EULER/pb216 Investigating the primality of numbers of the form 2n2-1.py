#!/usr/bin/python
# Solved by Bogdan Trif @       Completed on Sat, 7 Jan 2017, 23:07
#The  Euler Project  https://projecteuler.net
'''
                Investigating the primality of numbers of the form 2n2-1        -           Problem 216

Consider numbers t(n) of the form t(n) = 2n^2-1 with n > 1.
The first such numbers are 7, 17, 31, 49, 71, 97, 127 and 161.
It turns out that only 49 = 7*7 and 161 = 7*23 are not prime.

For n ≤ 10000 there are 2202 numbers t(n) that are prime.

How many numbers t(n) are prime for n ≤ 50,000,000 (  5*10**7 )   ?

'''
import time, gmpy2

def primesieve(n):          ### o(^_^)o  FASTEST  o(^_^)o  ###  Highly Efficient !!!
    import numpy as np
    """return array of primes 2<=p<=n"""
    sieve=np.ones(n+1,dtype=bool)
    for i in range(2, int((n+1)**0.5+1)):
        if sieve[i]:
            sieve[2*i::i]=False
    return np.nonzero(sieve)[0][2:]


print('\n--------------------------TESTS, BRUTE FORCE , 7 min , Completed in : 420.13203 s ------------------------------')
t1  = time.time()


def brute_force(limit = 5*10**7) :
    primes = primesieve(  int( limit* pow(2, 1/2))+1 )
    # print(primes[0:10])

    cnt=0
    for n in range(2, limit+1 ) :
        t = 2*n**2-1
        if gmpy2.is_prime(t):
            cnt+=1
            # print(str(cnt)+'.    ', n, t )
        if n % 10**6 == 0 :        print(n)
    return print('\nAnswer :\t', cnt)

# brute_force( limit = 5*10**7 )                    #  Answer :	 5437849


t2  = time.time()
print('\nCompleted in :', round((t2-t1),6), 's\n\n')            #   Completed in : 420.13203 s  -- 7 minutes

# ====        GENERAL IDEA :
# http://math.stackexchange.com/questions/403519/primality-of-the-numbers-in-the-form-of-2n2-1



print('\n================  My FIRST SOLUTION,   ===============\n')
# t1  = time.time()

















# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1,  2 min  --------------------------')
t1  = time.time()

# === Tue, 3 Jan 2017, 04:57, mbh038, England
# About 50s in Python. It has taken me a few days to get a solution that works in under a minute.
# Along the way I have learned a lot about modular square roots, quadratic residues and the like.
#
# I start with the premise that if n=ak+b, then if a prime p divides a and 2b**2≡1 mod p, 2n**2−1 is composite for all k.
# This is easy to show. Next, we find that there will only be solutions for bb if p mod 8=7 or 1.
# The fun bit was to realise, using modular arithmetic,  that 2b**2≡1 mod p implies that b=8–√×(4)**(−1) mod p,
# where the root is mod pp and (4)−1 means the multiplicative inverse of 4 mod p.
# Thus the problem has two parts. First solve the modular square root x**2≡8 mod p for each of our candidate primes p,
# then solve the linear diophantine equation ap−4b=1a.
# I used the Tonelli-Shanks algorithm to solve the modular square root,
# and a recursive algorithm stolen from John Carlson to solve the linear diophantine equation.
#
# That apart, I use a sieve method and avoid any primality testing.
# Using pow(x,y,p) in the modular square root code instead of x**y%p speed things up by a factor of 50 or so.


import numpy as np

def p216(limit):
    primes=primesieve(int(1.5*limit))
    primes=np.array([x for x in primes if x%8==1 or x%8==7])
    az=np.ones(limit,dtype=bool)
    for a in primes:
        b=bsolve(int(a))
        az[a-b::a]=False
        az[a+b::a]=False
    trials=np.nonzero(az)[0][2:]
    print (len(trials))

def bsolve(prime):
    """returns solution b to 2b^2=1 mod prime"""
    x=ts(8,prime)
    y=isolve(prime,-4,1)[1]
    solution= x*y%prime
    if solution>prime/2:
        return prime-solution
    return solution

def legendre_symbol(a,p):
    return pow(a,(p-1)//2,p)

def ts(n,p):
    """Tonnelli-Shanks algorithm. returns R: R^2=n mod p"""
    #check first that a solution exists. Return 0 if not.
#    if legendre_symbol(n,p)==-1:
#        return 0
    if p%4==3:
        return  pow(n,(p+1)//4,p)
    # this means p%4==1...
    #find Q,S: Q.2^s=p-1
    Q=p-1
    S=0
    while not Q%2:
        S+=1
        Q//=2

    #find z - lowest quadratic non-residue of p, using Euler's criterion
    z=2
    while pow(z,(p-1)//2,p)==1:
        z+=1

    c=pow(z,Q,p)
    R=pow(n,(Q+1)//2,p)
    t=pow(n,Q,p)
    M=S
    while not t%p==1:
        i=1
        while not pow(t,pow(2,i),p)==1:
            i+=1
        b=pow(c,pow(2,M-i-1),p)
        R=b*R%p
        t=t*pow(b,2)%p
        c=pow(b,2,p)
        M=i
    return R

def isolve(a,b,c):
    """code by John Carlson"""
    q, r = divmod(a,b)
    if r == 0:
        return( [0,c//b] )
    else:
        sol = isolve( b, r, c )
        u = sol[0]
        v = sol[1]
        return( [ int(v), int(u - q*v) ] )

def primesieve(n):
    """return array of primes 2<=p<=n"""
    sieve=np.ones(n+1,dtype=bool)
    for i in range(2, int((n+1)**0.5+1)):
        if sieve[i]:
            sieve[2*i::i]=False
    return np.nonzero(sieve)[0][2:]


# p216(5*10**7)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 2, Modular Square Roots , 2 min --------------------------')
t1  = time.time()

# === Fri, 27 May 2016, 14:52, FJ_Sevilla, Spain
# Python 3  Modular Square Roots.


from math import sqrt


def modular_sqrt(n, p):
    a = n%p
    if p%4 == 3: return pow(a, (p+1) >> 2, p)
    elif p%8 == 5:
        v = pow(a << 1, (p-5) >> 3, p)
        i = ((a*v*v << 1) % p) - 1
        return (a*v*i)%p
    elif p%8 == 1: # Shank's method
        q, e = p-1, 0
        while q&1 == 0:
            e += 1
            q >>= 1
        n = 2
        while legendre_symbol(n, p) != -1: n += 1
        w, x, y, r = pow(a, q, p), pow(a, (q+1) >> 1, p), pow(n, q, p), e
        while True:
            if w == 1: return x
            v, k = w, 0
            while v != 1 and k+1 < r:
                v = (v*v)%p
                k += 1
            if k == 0: return x
            d = pow(y, 1 << (r-k-1), p)
            x, y = (x*d)%p, (d*d)%p
            w, r = (w*y)%p, k
    else: return a # if p == 2


def Eratosthenes_sieve(lim):
    sieve = [True] * lim
    sieve[0:2]=[False]*2
    sieve[2]=True
    sieve[4::2]=[False]*len(sieve[4::2])
    for num in range(3,int(sqrt(lim))+1,2):
        if sieve[num]:
            sieve[num*num::2*num]=[False]*int((lim-num*num-1)/(2*num)+1)
    return sieve



def legendre_symbol(n, p):
    ls = pow(n, (p - 1) // 2, p)
    return -1 if ls == p - 1 else ls


def main():
    L = 5*10**7
    primes = Eratosthenes_sieve(int(sqrt(2*L**2-1)))
    sieve = [False, False] + [True] * (L-1)

    n = 2
    for p in [pr for pr, b in enumerate(primes) if b and legendre_symbol((pr+1)//2, pr)==1]:
        mr = modular_sqrt((p+1)//2, p)
        sieve[mr::p] = [False] * ((L - mr) // p + 1)
        sieve[p-mr::p] = [False] * ((L - (p - mr)) // p + 1)
        if n * n * 2 - 1 == p:
                sieve[n] = True
                n += 1
                while sieve[n] == False: n += 1
    print(sum(sieve))

if __name__ == '__main__':
    main()


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

# print('\n--------------------------SOLUTION 3,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
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
