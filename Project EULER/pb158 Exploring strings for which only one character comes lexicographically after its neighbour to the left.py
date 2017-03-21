#!/usr/bin/python                   ( ͡° ͜ʖ ͡°)
# Solved by Bogdan Trif @       Completed on Mon, 6 Mar 2017, 23:25
#The  Euler Project  https://projecteuler.net
'''
Exploring strings for which only one character comes lexicographically after its neighbour to the left      -       Problem 158

Taking three different letters from the 26 letters of the alphabet, character strings of length three can be formed.
Examples are 'abc', 'hat' and 'zyx'.
When we study these three examples we see that for 'abc' two characters come lexicographically after its neighbour to the left.

For 'hat' there is exactly one character that comes lexicographically after its neighbour to the left.
For 'zyx' there are zero characters that come lexicographically after its neighbour to the left.

In all there are 10400 strings of length 3 for which exactly one
character comes lexicographically after its neighbour to the left.

We now consider strings of n ≤ 26 different characters from the alphabet.

For every n, p(n) is the number of strings of length n for which
exactly one character comes lexicographically after its neighbour to the left.

What is the maximum value of p(n)?


'''
import time, string
from itertools import combinations, permutations
import gmpy2, math



print('\n--------------------------TESTS------------------------------')
t1  = time.time()

S = string.ascii_lowercase
print(S, '   \t ', len(S) ,'\n')

def brute_force_test( S, nr_letters ) :
    C = list( combinations ( S, nr_letters ) )
    print(len(C))

    Scnt=0
    for i in C :
        J = list( permutations(i) )
        for i in J :
            cnt = 0
            for j in range( len(i)-1 ) :
                if i[j] < i[j+1] :
                    cnt+=1
            if cnt == 1 : Scnt += 1

    return print('\nResult : \t', Scnt )

brute_force_test(S, 2)

# 2 --> 325
# 3 --> 10400
# 4 --> 164450
# 5 --> 1710280

print('  Combinations Test :    \n', gmpy2.comb(26, 3 )  )


def test_valid_permutations( my_string ) :
    Scnt=0
    J = list(permutations(my_string))
    for i in J :
        cnt = 0
        for j in range( len(i)-1 ) :
            if i[j] < i[j+1] :
                cnt+=1
        if cnt == 1 : Scnt += 1

    return print('\nThere are :\t', Scnt ,'  available permutations !')


test_valid_permutations('abcdef')




t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n================  My FIRST SOLUTION,  VERY FAST  ===============\n')
t1  = time.time()


def generate_coefficients( up ) :
    Max, letters = 0, 0
    for i in range(1, up ) :
        c =  gmpy2.comb( 26, i+1 )
        k = (2**(i+1) -i-2 )
        comb = c*k
        print('Letters : \t   ' + str(i+1)+'          ' ,  comb )
        if comb > Max :
            Max, letters = comb, i+1

    return print('\nAnswer, maximum value : \t', Max,'     corresponding to '+str(letters)+ '  letters' )

generate_coefficients( 26)      # 409511334375      corresponding to 18  letters


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

#### OTHER IDEAS ########
# https://en.wikipedia.org/wiki/Eulerian_number
# EULERIAN NUMBER

print('\n================  My SECOND SOLUTION,   ===============\n')
t1  = time.time()


def strings( up ) :
    M = [ gmpy2.comb( 26, i+1 )*(2**(i+1) -i-2 ) for i in range(1, up ) ]

    return print('\nAnswer, maximum value :  ', max(M),'  corresponding to '+str(M.index(max(M))+2)+ '  letters' )

strings( 26)


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')




print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1,   --------------------------')
t1  = time.time()

# === Thu, 19 Nov 2015, 15:24, hornemann55, Denmark
# Rather simple combinatorial problem, runs in 8ms:

from math import factorial

def combinations(n, r):
    return factorial(n) // factorial(r) // factorial(n-r)

smax=0
for n in range(2,26):
    s = 0
    for i in range (2,n+1):
        s+=combinations(26,i)*combinations(26-i,n-i)

    if s < smax:
        break
    smax = s
print(smax)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 2,   --------------------------')
t1  = time.time()

# ==== Wed, 3 Feb 2016, 19:21, fox016 , USA

import math, functools

high = 0
for i in range(1, 26+1):
        n = (2**i - i - 1) * (functools.reduce(lambda a,b: a*b, map(lambda x: 26-x, range(i)), 1) // math.factorial(i))
        if n > high:
                high = n
print (high)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 3,   --------------------------')
t1  = time.time()

# ==== Thu, 19 Nov 2015, 15:24, hornemann55, USA
# Rather simple combinatorial problem, runs in 8ms:

from math import factorial

def combinations(n, r):
    return factorial(n) // factorial(r) // factorial(n-r)

smax=0
for n in range(2,26):
    s = 0
    for i in range (2,n+1):
        s+=combinations(26,i)*combinations(26-i,n-i)

    if s < smax:
        break
    smax = s
print(smax)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 4,   --------------------------')
t1  = time.time()


# ==== Wed, 25 Sep 2013, 18:08, ChopinPlover , Taiwan
# Find patterns.
import math

def C(m, n):
    return int(math.factorial(m)/(math.factorial(n)*math.factorial(m-n)))

def sol():
    primitive_ways = 0
    ways = []
    for n in range(26):
        primitive_ways = primitive_ways * 2 + n
        ways.append(primitive_ways * C(26, n+1))
    print(max(ways))

sol()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 5,   --------------------------')
t1  = time.time()

# ==== Mon, 4 Mar 2013, 00:22, Ben Ruijl, Netherlands
# I used combinatorics to solve this problem. Let the increase happen at position x in the string and let the value
# of the chosen letter by y. Then: C {(26−y , x−1)}⋅ C{(26−x, N−x)} is the number of ways to do this.

from math import factorial

def ncr(n, k):
	if n < 0 or k > n or k < 0:
		return 0
	return factorial(n) // (factorial(k) * factorial(n - k))

K = 26
N = 26
maxval = 0

for n in range(1, N):
	count = 0
	for x in range(1, n): # position of increase
		for y in range(K): # value at increase
			count += ncr(K - y - 1, x) * ncr(K - x - 1, n - x - 1)

	if count > maxval:
		maxval = count

print(maxval)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 6,   --------------------------')
t1  = time.time()

# ==== Fri, 22 Apr 2011, 18:42, GeoffScrace, England
# I have trouble with combinatorial problems.
# For strings of length 3 and 4 I wrote a program to find the numbers of monotonic strings.
# I noticed that this number was 26Cn and that there was a relationship between this value
# and the number of strings with the required configuration. I arrived at 2^n -n -1.

from sympy import binomial
b=binomial
for i in range(3,27):
    print (b(26,i)*(2**i -i-1))


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 7,   --------------------------')
t1  = time.time()

# ====Sat, 10 Jan 2009, 03:15, tolstopuz, Russia

import functools, operator

def fact(n):
    return functools.reduce(operator.mul, range(1, n + 1), 1)

e = 0
c = 0
for n in range(1, 27):
    e = 2 * e + n - 1
    c = max(c, e * fact(26) // fact(n) // fact(26 - n))

print(c)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 8,   --------------------------')
t1  = time.time()

# ====Sat, 5 Dec 2009, 17:00, Australia
# Same as everyone else:
# If we were working with an alphabet of 1000 characters, then the maximum value of p(n) would be 3.537076 E 475

def p(n, a=26):
    return gmpy2.comb(a, n) * (2 ** n - (n + 1))

print (max([p(n) for n in range(27)]))



t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

