#!/usr/bin/python
# Solved by Bogdan Trif @   Completed on Tue, 4 Oct 2016, 00:09
#The  Euler Project  https://projecteuler.net
'''
                    Consecutive prime sum       -      Problem 50
The prime 41, can be written as the sum of six consecutive primes:
41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.
The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.
Which prime, below one-million, can be written as the sum of the most consecutive primes?
'''
import time

def gen_primes(limit): # derived from
                      # Code by David Eppstein, UC Irvine, 28 Feb 2002
    D = {}            # http://code.activestate.com/recipes/117119/
    q = 2
    while q <= limit:
        if q not in D:
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1

def is_prime(n):
    # Function which checks if a number is prime
    for i in range(2, int(pow(n,1.0/2))+1):
        if n%i==0:
            return False
    return True

p = gen_primes(10000)
primes = [i for i in p]
print(primes[-10::])

print('---------------- TESTS--------------------')

X=997651             # Type the  number you want to check
if is_prime(X) == True : print(X ,' is a prime !')
else : print(X,'  Not a prime ')

twentyones = primes[3:24]
print(len(twentyones), sum(twentyones), twentyones)

test_million=primes[0:546]
print(len(test_million), sum(test_million), test_million[-10::])
print(primes.index(3947))
print(is_prime(sum(test_million)))
print(sum(primes[11:30]))

print('\n----------------------MY SOLUTION, RECURSION ALGORITHM ----------------------------')

t1  = time.time()

p = gen_primes(10000)
primes = [i for i in p]


def func(a, i):
    S = sum(primes[a: i])
    print(S)
    if S > 10**6:
        func(a, i-1)
    elif (S < 10**6 and is_prime(S) != True )  :
        func(a+1, i)

func(0, 550)

t2  = time.time()
print('\n' ,' the primes were generated in :', round((t2-t1)*1000,4), 'ms\n')

print('\n-------------------- MY SECOND SOLUTION, BETTER, RECURSION ALGORITHM ----------------------------')

t1  = time.time()
p = gen_primes(5000)       # Generate prime numbers < 5000 are more than enough
primes = [i for i in p]

def pb050(a, i):
    S = sum(primes[a: i])
    if S > 10**6:
        pb050(a, i-1)                               #   shifts last index left, decrease Sum
    elif (S < (10**6 - primes[i]) )  :
        pb050(a, i+1)                               #   shifts last index right, increase Sum
    elif ( is_prime(S) != True )  :
        pb050(a+1, i)                               # shift first index right, removes lowest primes
    else:
        print(S)

pb050(0, 550)               # Start with the index of the first prime, approx index of the last prime

t2  = time.time()
print('\n' ,' the primes were generated in :', round((t2-t1)*1000,4), 'ms\n')



print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')

print('\n--------------------------SOLUTION 1, zhuifengmu from China --------------------------')

t1  = time.time()

def is_prime(x):        ## justify whether an x is prime
    for n in range(2, int(pow(x,1.0/2))+1):
        if x%n==0:
            return 0
    return 1

n = 2
l = []
l2 = []
Sum = 0
while Sum < 1000000:
    if is_prime(n)==1:
        l.append(n)
        Sum += n
        l2.append(Sum)
    n += 1
Sum -= n-1
for j in l:
    Sum -= j
    if is_prime(Sum)==1 and Sum < 1000000:
        print (Sum)
        break

t2  = time.time()
print('\n' ,' the primes were generated in :', round((t2-t1)*1000,4), 'ms\n')


print('\n--------------------------SOLUTION 2, INTERESTING  iranic --------------------------')

t1  = time.time()

from math import log

longest = 1
prime_sum_primes = 1 #we initiate these values at 1 to avoid ZeroDivisionErrors
primes = []
n = 2 #the number we're currently checking
N = 1000000 #our limit

def is_prime(n):
    if n <=1:
        return False
    for p in primes:
        if p > (n**0.5):
            return True
        if n%p==0:
            return False
    else:
        return True

while True:
    #calculate our approximate limit
    E = N/float(longest)
    E_hat = prime_sum_primes/float(longest)
    l_bar = N/E_hat
    a_0 = E/log(E)
    a_1 = (log(E)**2)/(log(E)-1)
    x = a_1*(l_bar - a_0) + E

    if n > x:
        #our approximate limit is exceeded
        break

    if is_prime(n):
        primes.append(n)

        for k in range(len(primes)):
            #check the sums in our current list
            primes_to_sum = primes[k:]
            length = len(primes_to_sum)

            if length < longest:
                break

            prime_sum = sum(primes_to_sum)
            if prime_sum >= N:
                continue
            elif is_prime(prime_sum):
                #we have a new list
                prime_sum_primes, longest = prime_sum, length
    if n == 2:
        n+=1
    else:
        n+=2

print (prime_sum_primes, longest)

t2  = time.time()
print('\n' ,' the primes were generated in :', round((t2-t1)*1000,4), 'ms\n')

