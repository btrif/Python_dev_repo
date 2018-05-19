#!/usr/bin/python                   o(^_^)o         ( ͡° ͜ʖ ͡°)
# © Solved by Bogdan Trif @
#The  Euler Project  https://projecteuler.net
'''
                Harshad Numbers     -       Problem 387

A Harshad or Niven number is a number that is divisible by the sum of its digits.
201 is a Harshad number because it is divisible by 3 (the sum of its digits.)
When we truncate the last digit from 201, we get 20, which is a Harshad number.
When we truncate the last digit from 20, we get 2, which is also a Harshad number.

Let's call a Harshad number that, while recursively truncating the last digit,
always results in a Harshad number a right truncatable Harshad number.

Also:
201/3=67 which is prime.
Let's call a Harshad number that, when divided by the sum of its digits,
results in a prime a strong Harshad number.

Now take the number 2011 which is prime.
When we truncate the last digit from it we get 201, a strong Harshad number that is also right truncatable.
Let's call such primes strong, right truncatable Harshad primes.

You are given that the sum of the strong, right truncatable Harshad primes less than 10000 is 90619.

Find the sum of the strong, right truncatable Harshad primes less than 10**14.

'''
import time, gmpy2

def primesieve(n):          ### o(^_^)o  FASTEST  o(^_^)o  ###  Highly Efficient !!!
    import numpy as np
    """return array of primes 2<=p<=n"""
    sieve=np.ones(n+1,dtype=bool)
    for i in range(2, int((n+1)**0.5+1)):
        if sieve[i]:
            sieve[2*i::i]=False
    return np.nonzero(sieve)[0][6:]

def Harshad_number(n):
    N= [int(i) for i in str( n) ]
    if n%(sum(N)) == 0 :
        return True
    return False

def strong_Harshad_number(n):
    N= [int(i) for i in str( n) ]
    if Harshad_number(n) == True :
        if  gmpy2.is_prime( n//(sum(N)) ) :
            return True
    return False

def right_truncatable_Harshad_number(n) :       # RECURSION
    if len(str(n)) ==1 :
        if Harshad_number(n) :
            return True
    N= str(n)
    while len(N) > 1 :
        if Harshad_number(n) == True :
            n = int(str(n)[:-1])
            # print(n)
            N = str(n)
            return right_truncatable_Harshad_number(n)
        else :      return False

    return False


def strong_right_truncatable_Harshad_prime(n):
    if gmpy2.is_prime(n)==True and n > 10 :
        n = int(str(n)[:-1])
        if strong_Harshad_number(n) and right_truncatable_Harshad_number(n) :
            return True
    else : return False

    return False


print('primes', gmpy2.is_prime(201), gmpy2.is_prime(2011))

print('\nHarshad_number : \t', Harshad_number(201))
print('\nstrong_Harshad_number : \t', strong_Harshad_number(201))
print('\nright_truncatable_Harshad_number : \t', right_truncatable_Harshad_number(2011))
print('\nstrong_right_truncatable_Harshad_prime : \t', strong_right_truncatable_Harshad_prime(211))



print('\n------------------- Initial TEST was a SUCCESS ------------------------------')
t1  = time.time()

up_lim = 10**6
primes = primesieve(up_lim)
print('Prime sieve len : ', len(primes), primes[:25],'\n')

S=0
for p in primes :
    if strong_right_truncatable_Harshad_prime( int(p)) :
        print(str(p)+'.       len:', len(str(p))  )
        S+=p

print('\nAnswer : \t', S)

print('------Finding the larger Harshad numbers ----')

for length in range( 6, 10) :
    start1 = 40
    start2 = 48
    start3 = 80

    p = gmpy2.next_prime( (start1)*10**(length-1) )
    while p < (start1+1)*10**(length-1) :
        if strong_right_truncatable_Harshad_prime(p) :
            print(p,'        len:', len(str(p)) )
            S+=p
        p = gmpy2.next_prime( p )
    p = gmpy2.next_prime( (start2)*10**(length-1) )
    while p < (start2+1)*10**(length-1) :
        if strong_right_truncatable_Harshad_prime(p) :
            print(p,'        len:', len(str(p)) )
            S+=p
        p = gmpy2.next_prime( p )
    p = gmpy2.next_prime( (start3)*10**(length-1) )
    while p < (start3+1)*10**(length-1) :
        if strong_right_truncatable_Harshad_prime(p) :
            print(p,'        len:', len(str(p)) )
            S+=p
        p = gmpy2.next_prime( p )


2018-03-28 - We must find a way to generate the numbers RECURSIVELY !!!

# 181.       len: 3
# 211.       len: 3
# 271.       len: 3
# 277.       len: 3
# 421.       len: 3
# 457.       len: 3
# 631.       len: 3
# 2011.       len: 4
# 2017.       len: 4
# 2099.       len: 4
# 2473.       len: 4
# 2477.       len: 4
# 4021.       len: 4
# 4027.       len: 4
# 4073.       len: 4
# 4079.       len: 4
# 4231.       len: 4
# 4813.       len: 4
# 4817.       len: 4
# 6037.       len: 4
# 8011.       len: 4
# 8017.       len: 4
# 8039.       len: 4
# 8461.       len: 4
# 8467.       len: 4

# 20071.       len: 5
# 20431.       len: 5
# 40867.       len: 5
# 48091.       len: 5
# 84061.       len: 5
# 84067.       len: 5
# 400237.       len: 6
# 400277.       len: 6
# 4008271.       len: 7
# 4860013.       len: 7
# 40000021.       len: 8
# 80402071.       len: 8
# 400002073         len: 9
# 480006031         len: 9
# 4000008697         len: 10
# 4008200071         len: 10
# 4020800071         len: 10
# 8004000619         len: 10
# 8004600031         len: 10

print('\nAnswer : \t', S)

t2  = time.time()
print('\nCompleted in :', round((t2-t1),6), 's\n\n')

print('\n================  My FIRST SOLUTION,   ===============\n')
# t1  = time.time()







# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


# print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
# print('\n--------------------------SOLUTION 1,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
# print('\n--------------------------SOLUTION 2,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
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
