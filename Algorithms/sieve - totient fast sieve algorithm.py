import time

#############   EULER TOTIENT SIEVE FAST ALGORITHM    ##############
#### TOTIENT SIEVE IS VERY GOOD !!!! the Prime sieve may be improved
# http://marcharper.codes/2015-08-07/totients.html

import time, math

t1  = time.time()

def primes_up_to(n):
    # http://code.activestate.com/recipes/576640/
    nroot = int( n**(1/2) )
    sieve = [True] * (n+1)# range(n+1)
    sieve[0] = False
    sieve[1] = False

    for i in range(2, nroot+1):
        if sieve[i]:
            m = n/i - i
            sieve[i*i: n+1:i] = [False] * (int(m)+1)

    return [i for i in range(n+1) if sieve[i]]

def multiple_gen(modulus):
    """Generates the list of multiples of modulus."""
    count = 1
    while True:
        yield modulus * count
        count += 1

def fast_compute_totients(bound):
    """Simultaneously compute totients for all numbers
    up to and including n."""

    # Populate the initial list with the leading factor of n.
    results = list(range(0, bound+1))

    # Get the list of primes up to the bound.
    primes = primes_up_to(bound)

    for p in primes:
        for m in multiple_gen(p):
            if m > bound:
                break
            results[m] = (results[m] // p) * (p - 1)
    return print(sum(results), '\n',results[:100])



n = 10**6
fast_compute_totients(n)


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n')





###    EULER TOTIENT SIEVE FAST ALGORITHM  2 TIMES FASTER  #########



t1  = time.time()

def Euler_Totient_Sieve(n):
    phi = list(range(n+1))
    for i in range(2,n+1):
        if phi[i]==i:
            for x in range(i,n+1,i):
                phi[x]-=phi[x]//i
    return print(sum(phi[1:]) , '\n',phi[1:][:100] )

Euler_Totient_Sieve(n)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n')


###    EULER TOTIENT SIEVE FAST ALGORITHM   3,  SUPER FAST  #########

import math

t1  = time.time()

#from overview for pe351 by Marcus Stuhr
#used by TotientSum7 - recursive version of O((n/(log(log(n))))^(2/3)) algorithm
def v7(n,L,sieve,memo):
    if n<=L:
        return sieve[n]
    else:
        try:
            return memo[n]
        except KeyError:
            res=n*(n+1)//2

            for g in range(2,int(n**0.5)+1):
                res-=v7(n//g,L,sieve,memo)

            for z in range(1,int(n**0.5)+1):
                if n//z!=z:
                    res-=(n//z-n//(z+1))*v7(z,L,sieve,memo)

            memo[n]=res
            return res

#from overview for pe351 by Marcus Stuhr
#recursive version of O((n/(log(log(n))))^(2/3)) algorithm
#if use instead of my totientSum(), gives a x5 speed up for n=10^8
def TotientSum7(n):
    L=int((n/(math.log(math.log(n))))**(2/3))
    sieve =list(range(L+1))
    memo={}
    for p in range(2,L+1):
        if p==sieve[p]:
            k=p
            while k <= L:
                sieve[k]-=sieve[k]//p
                k+=p
        sieve[p]+=sieve[p-1]
    return v7(n,L,sieve,memo)


print(TotientSum7(n) )

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n')





###    EULER TOTIENT SIEVE FAST ALGORITHM   4,  THE FASTEST !!!!!!   ######### !!!!!!!!!!!!!   MUST STUDY IT !!

import math

t1  = time.time()

#Algorithm 8 from the p351 overview
#iterative version of O((n/(log(log(n))))^(2/3)) algorithm
#if use instead of my totientSum(), gives a x6 speed up for n=10^8
def TotientSum8(n):
    L=int((n/(math.log(math.log(n))))**(2/3))
    sieve =list(range(L+1))
    bigV=[0]*(n//L+1)

    for p in range(2,L+1):
        if p==sieve[p]:
            k=p
            while k <= L:
                sieve[k] -= sieve[k]//p
                k+=p
        sieve[p] += sieve[p-1]

    for x in range(n//L,0,-1):
        k=n//x
        res=k*(k+1)//2

        for g in range(2,int(k**0.5)+1):
            if k//g<=L:
                res-=sieve[k//g]
            else:
                res-=bigV[x*g]

        for z in range(1,int(k**0.5)+1):
            if z != k//z:
                res -= (k//z-k//(z + 1))*sieve[z]

        bigV[x]=res

    return bigV[1]


print(TotientSum8(n) )

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n')




