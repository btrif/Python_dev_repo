#!/usr/bin/python3
# Solved by Bogdan Trif @   Completed on Mon, 17 Oct 2016, 17:35
#The  Euler Project  https://projecteuler.net/thread=78
'''
                                Coin partitions     -       Problem 78
Let p(n) represent the number of different ways in which n coins can be separated into piles.
For example, five coins can be separated into piles in exactly seven different ways, so p(5)=7.

                                                        OOOOO
                                                        OOOO   O
                                                        OOO   OO
                                                        OOO   O   O
                                                        OO   OO   O
                                                        OO   O   O   O
                                                        O   O   O   O   O
            Find the least value of n for which p(n) is divisible by one million.
'''

import time
t1  = time.time()

print('\n--------------  MY SOLUTION , SLOW, with the indian fast algorithm for generating partition numbers Pb076-------------------------')

print('From what I read on the forum the 10 divisible numbers must be also pentagonal. Has something to do with pentagonal numbers.')

number = 100000

def pent(n):
    return (n * (3 * n - 1)) / 2

def dyf(num):
    if num < 0:
        return 0
    elif num in memo:
        return memo[num]
    else:
        f = 0
        for a in range(len(L)):
            f += L[a][0] * dyf(num - L[a][1])
    memo[num] = f
    return f

global L, memo
memo = {0:1}
n = 1
L = []

while True:
    sign = 1
    if n % 2 == 0:
        sign = -1
    if number - pent(n) >= 0:
        L.append((sign , pent(n)))
    else:
        break
    if number - pent(-1 * n) >= 0:
        L.append((sign , pent(-1 * n)))
    else:
        break
    n += 1
L = L[::-1]

print(dyf(100))

part_nrs=[]
for i in range(1,number+1):
    if str(dyf(i))[-6::] == '0' * 6 :
        print(str(i)+'.   ', dyf(i))
        break

print('\n The answer is:  ', i)                             # Answer : 55374


#     #for s in range(5, 7):
#     if str(part_nrs[i])[-s::] == '0' * s :
#         print(str(i+1)+'.  -->   ',s,'   ',part_nrs[i])



t2  = time.time()
print('\nCompleted in :', round((t2-t1),6), 's\n\n')          # Completed in : 35449.027538 ms


print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1 , SLOW  ilan, Germany--------------------------')

t1  = time.time()

class Memoize:
    def __init__(self, func):
        self.func = func
        self.cache = {}
    def __call__(self, arg):
        if arg not in self.cache:
            self.cache[arg] = self.func(arg)
        return self.cache[arg]

@Memoize
def p(n):
    if n<0: return 0
    if n<2: return 1
    sm=0
    for k in range(1, n+1):
        n1 = n-k*(3*k-1)/2
        n2 = n-k*(3*k+1)/2
        sm += (-1)**(k+1) * (p(n1) + p(n2))
        if n1 <= 0:
            break
    return sm%1000000

n=0
while p(n)!=0: n += 1
print (n)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 2 , SLOW  , MrDrake, Australia--------------------------')

t1  = time.time()
#
# limit = 10 ** 5
# divisor = 1000000
#
# p = [0] * limit
# p[0] = 1
#
# for i in range(1, limit):
# 	j = 1; k = 1; s = 0
# 	while j > 0:
# 		j = i - (3 * k * k + k) // 2
# 		if j >= 0: s -= p[j] * (-1) ** k
# 		j = i - (3 * k * k - k) // 2
# 		if j >= 0: s -= p[j] * (-1) ** k
# 		k += 1
# 	p[i] = s % divisor
# 	if not p[i]:
# 		print (i)
# 		break

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 3 , VERY FAST , STILL CONFUSED about the approach , jraymond--------------------------')

t1  = time.time()


def generalize_pentagonals(n):
    ps = []
    i = 1
    while len(ps) < n:
        ps.append((3 * i * i - i) // 2)
        if i < 0:
            i -= 1
        i *= -1
    return ps

def run(n):
    memo = [1]
    ps = generalize_pentagonals(1000)
    signs = [1, 1, -1, -1]
    i = 0
    while memo[-1] % n != 0:
        i += 1
        t, ki = 0, 0
        while ps[ki] <= i:
            t += signs[ki%4] * memo[i-ps[ki]]
            ki += 1
        memo.append(t)
    return i, memo[-1]

print(run(100))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 4 , SLOW SLOW --------------------------')

t1  = time.time()
#
# array = [0, 1]
# n = 1
#
# while array[n] != 0:
# 	n += 1
# 	array.append(0)
#
# 	n1 = 1.0/6.0 - ((1+24*n)**0.5)//6.0
# 	n2 = 1.0/6.0 + ((1+24*n)**0.5)//6.0
#
# 	for k in range(int(n1), int(n2)+1):
# 		if k != 0:
# 			array[n] += ((-1)**(k-1))*array[n - k*(3*k-1)//2]
# 			array[n] %= 1000000
#
# print (n)






t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 5 , still SLOW --------------------------')

t1  = time.time()

#Euler Project 78
#Thinginitself

# div = 10 ** 6
# mymax = 10 ** 7
# p = []
# p.append(1)
#
# n = 1
# while True:
# 	k = 1
# 	ans = 0
# 	while True:
# 		sign = int((-1) ** (k+1%2))
# 		g1 = (3*k-1)*k//2
# 		g2 = (3*k+1)*k//2
# 		if g1>n:
# 			break
# 		ans += p[n-g1] * sign
# 		ans %= div
# 		if g2>n:
# 			break
# 		ans += p[n-g2] * sign
# 		ans %= div
# 		k += 1
# 	if ans%div == 0:
# 		print (n)
# 		break
# 	p.append(ans)
# 	n += 1

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')      # Completed in : 32082.834959 ms


print('\n--------------------------SOLUTION 6 ,  SLOW, mmaximus, Portugal --------------------------')

# Using the recursion formula plus memoization.
# Also, calculates the boundary at which the pentagonal numbers go negative in the summation

t1  = time.time()
#
# from math import ceil, sqrt
#
# memo = {0: 1, 1: 1, 2: 2, 3: 3, 4: 5, 5: 7}
#
#
# def partition_mod_million(n):
#     if n < 0:
#         return 0
#     if n not in memo:
#         lower_bound = ceil((1-sqrt(1+24*n))/6)-1
#         upper_bound = ceil((1+sqrt(1+24*n))/6)+2
#         memo[n] = sum(pow(-1,k-1) * partition_mod_million(n-k*(3*k-1)/2)
#                       for k in [i for i in range(lower_bound,upper_bound) if i != 0]) % 1000000
#     return memo[n]
#
# answer = 1
# i = 3
# while answer != 0:
#     answer = partition_mod_million(i)
#     i += 1
#
# print(i-1)


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 7 ,  SLOW, scar, USA --------------------------')

# As I learn Python, I'm trying early problems that I didn't do earlier.
# I found a paper on using Euler's recurrence relation and pentagonal numbers and wrote the code to solve.  Took about 38s.

t1  = time.time()

'''
Project Euler Problem 78
Find the value of 'n' for which the number of partitions p(n)
is divisible by 1,000,000
Date:	16 APR 2015
'''
#
# from math import sqrt
#
# def f(k):
# # function to compute pentagonal numbers
# 	return k*(3*k-1)//2
#
# def kMax(n):
# # function to determine limit of sum
# 	x = sqrt(24*n+1)
# 	return int((1+x)/6)
#
# # create hash to store previous results
# p={}
# p[0]=1
# p[1]=1
#
# n = 2
# while (True):
# 	tmp = 0
# 	for k in range(1, kMax(n)+1):
# 		term1 = p[n - f(k)]
# 		test = n - f(-k)
# 		if test < 0:
# 			term2 = 0
# 		else:
# 			term2 = p[test]
#
# 		tmp += (-1)**(k+1)*( term1 + term2 )
# 	p[n] = tmp
#
# 	trial = p[n]%1000000
# 	if trial == 0:
# 		# print n, p[n]
# 		break
# 	n += 1
#
# print("The answer is", n)




t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')      # Completed in : 27996.601343 ms


print('\n--------------------------SOLUTION 8 ,  FASTEST SOLUTION, Frexxia, Norway  --------------------------')

# I had to give up doing a more brute force approach here (took way too long even using modular arithmetic everywhere),
# so I ended up reading on the Wikipedia page.
# Python, runs in 2.18 s, or 0.21 s if I use PyPy (I was surprised about the speed-up). Pretty compact code as well.

t1  = time.time()

from itertools import chain
from bisect import bisect_right as br

p = [1]
a, b = [k*(3*k-1)//2 for k in range(1,259)], [k*(3*k+1)//2 for k in range(1,259)]
pos, neg = list(chain(*zip(a[::2],b[::2]))), list(chain(*zip(a[1::2],b[1::2])))
for n in range(1,10**5):
    p.append((sum(p[n-k] for k in pos[:br(pos,n)]) - sum(p[n-k] for k in neg[:br(neg,n)])) % 10**6)
    if p[n] == 0:
        print(n)
        break

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')      # Completed in : 5815.332413 ms


print('\n--------------------------SOLUTION 9 ,  SLOW,  anumoshsad, Bangladesh --------------------------')

#    Euler's pentagonal number theorem.

t1  = time.time()
#
# p=[1,1,2,3]
# def generate(n):
# 	if n<4:return p[n]
# 	s=0
# 	for k in range(1,n+1):
# 		if n<k*(3*k-1)//2:
# 			break
# 		s+=(-1)**(k+1)*p[n-k*(3*k-1)//2]
# 		if n<k*(3*k+1)//2:
# 			break
# 		s+=(-1)**(k+1)*p[n-k*(3*k+1)//2]
# 	p.append(s%10**6)
#
# def pe78():
#
# 	l=4
# 	while True:
# 		generate(l)
# 		if p[-1]==0:break
# 		l+=1
# 	print(l)
#
# pe78()


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')      # Completed in : 28342.621088 ms

print('\n--------------------------SOLUTION 10 , SLOW  --------------------------')

#    Euler's pentagonal number theorem.

t1  = time.time()
#
# from itertools import *
#
# def P(n):
#     return n*(3*n - 1)//2
#
# Partitions = {}
# GP = sorted(map(P, range(-250, 250)))[1:]
#
# def Partition(n):
#     if n <= 1: return 1
#     if n not in Partitions:
#         signs = cycle([1, 1, -1, -1])
#         Ps = takewhile(lambda p: p <= n, GP)
#         Partitions[n] = sum(sign * Partition(n - p) for (sign, p) in zip(signs, Ps))
#     return Partitions[n]
#
# M = 10**6
#
# for n  in count(0):
#     if Partition(n) % M == 0:
#        print(n)
#        break

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')      # Completed in : 24902.424335 ms

print('\n--------------------------SOLUTION 11 ,  McMath, Canda --------------------------')
t1  = time.time()

def pent(n):
    return (3 * n**2 - n) // 2

def pExt(pList):
    total = 0; n = len(pList); i = 1
    while True:
        x = n - pent(i)
        if 0 <= x:
            if i % 2 == 1: total += pList[x]
            else: total -= pList[x]
        else: break
        i = -i if 0 < i else 1 - i
    pList.append(total)

def pDiv(d):
    L = [1]
    while L[-1] % d != 0: pExt(L)
    return len(L) - 1

print ('Answer: ' + str(pDiv(1000000)))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')      #  Completed in : 32114.836931 ms
