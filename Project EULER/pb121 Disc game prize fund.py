#!/usr/bin/python
# Solved by Bogdan Trif @   	Completed on Mon, 23 Jan 2017, 23:46
#The  Euler Project  https://projecteuler.net
'''
                            Disc game prize fund        -       Problem 121

A bag contains one red disc and one blue disc.
In a game of chance a player takes a disc at random and its colour is noted.
After each turn the disc is returned to the bag,
an extra red disc is added, and another disc is taken at random.

The player pays £1 to play and wins if they have taken more blue discs than red discs at the end of the game.

If the game is played for four turns, the probability of a player winning is exactly 11/120,
and so the maximum prize fund the banker should allocate for winning in this game would be £10
before they would expect to incur a loss.
Note that any payout will be a whole number of pounds and also includes the original £1 paid to play the game,
so in the example given the player actually wins £9.

Find the maximum prize fund that should be allocated to a single game in which fifteen (15) turns are played.

'''
import time
import gmpy2
from math import factorial, floor
from itertools import combinations
import operator, functools

def unique_permutations(lst):       # VERY EFFECTIVE
    ''':Description: Takes a list and makes ONLY Unique Permutations of a list with repeated elements.
        If one tries itertools.permutations on a list with 14 elements ==> BANG, computer freezes
    :param lst: type list
    :return:    a list of lists containing all the permutations
    '''
    if len(lst) == 1:
        yield (lst[0],)
    else:
        unique_lst = set(lst)
        for first_element in unique_lst:
            remaining_lst = list(lst)
            remaining_lst.remove(first_element)
            for sub_permutation in unique_permutations(remaining_lst):
                yield (first_element,) + sub_permutation

print('\n--------------------------TESTS------------------------------')


# print(gmpy2.comb(4,2))

discs = 5
print( [ i  for i in range(discs-1, discs//2-1, -1) ] )
S, C = 0, 0
C = [gmpy2.comb(discs-1, i)  for i in range(discs-1, discs//2-1, -1) ]

P = factorial(discs)
print(sum(C),  '      Comb :',P,'      ', C )
prob = sum(C)*100 / P

print('Probability of winning : \t', prob, '%', '    ',floor(prob)  )
print('\nthe winning Factor : \t' ,P / sum(C) , floor( P / sum(C) ))


#### GENERAL IDEA ##########
# There are already 2 discs : blue & red. On every turn the disc is returned and a new red is added
# Therefore, blue disk will be 1/2, 1/3, 1/4, 1/5 in 4 turns game
# In game with 4 turns , 4 discs are extracted. The players wins in the following configurations:
# BBBB = 1/2* 1/3* 1/4* 1/5 = 1/120
# BBBr = 1/2* 1/3* 1/4* 4/5 = 4/120
# BBrB = 1/2* 1/3* 3/4* 1/5 = 3/120
# BrBB = 1/2* 2/3* 1/4* 1/5 = 2/120
# rBBB = 1/2* 1/3* 1/4* 1/5 = 1/120
# The Sum of these probabilities is : 11/120

# In a 15 turns-game there will be :
# 8 Blue and 7 red maximum

print('\n================  My FIRST SOLUTION, SLOW, Unique Permutations  ===============\n')
t1  = time.time()


def disc_game_prize( turns =15 ) :
    ### Convention : 1 - blue, 0 - red
    P_sum=0
    for b in range(turns, turns//2, -1) :
        discs = [1]*b +[0]*(turns-b)
        P =  list(unique_permutations(discs))
        # print('Blue : ',b,'   ', '     Red:  ', turns-b , '    ',discs, '    ', P)
        # print('---------------------------')
        for O in P :
            # print(O)
            Prob = 1
            for j in range(len(O)):
                if O[j] == 1 : Prob*= 1/(j+2)
                if O[j] == 0 : Prob*= (j+1)/(j+2)
            # print(O,'     ', Prob)
            P_sum += Prob
    print('\nProbability : \t', P_sum,'        fund to allocate : \t', 1/P_sum)

    return print('\nAnswer  : \t',    floor(1/P_sum))

disc_game_prize(15)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n==========  My SECOND SOLUTION, Learnt on forum, Much BETTER  ===============\n')
t1  = time.time()


discs = 15
P = 0
for reds in range( (discs+1)//2 ) :
    # print(reds, list(combinations( range( 1, discs+1 ) , reds )) )
    for r in combinations( range( 1, discs+1 ) , reds ) :
        P += functools.reduce(operator.mul, r ,1 )
        # print(r,'    ' ,functools.reduce(operator.mul, r , 1), '   total:',P )

print('\n',list ( range(2, discs+2)) )
print('\nAnswer : \t', functools.reduce( operator.mul, range(2, discs+2))//P )

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')



print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1,   --------------------------')
t1  = time.time()

# ===== Thu, 22 Sep 2016, 20:42 , pedrotari7, Portugal
# Find all the combinations, pick the winners, calculate each winner probability and sum it up


from itertools import product
from math import factorial
import functools, operator

def single_prob(case):
	return functools.reduce(operator.mul, [i+1 for i,v in enumerate(case) if v=='R'], 1)

n = 15

winners = [a for a in product(['B','R'], repeat=n) if a.count('B')>a.count('R')]

total = sum([single_prob(w) for w in winners])

print ("total: " + str(int(float(factorial(n+1))/total)))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 2,   --------------------------')
t1  = time.time()

# ===== Tue, 23 Aug 2016, 17:32, gvhl, Netherlands
# runs in 50ms, obviously if we reach 8 blue the rest of the tree doesn't matter and the probability at that point is taken

from math import gcd

def func(blue, red, depth, disks, chance_a, chance_b):
    if blue >= 8:
        return chance_a, chance_b
    if depth == 0:
        return (0, 1)
    a, b = chance_a, chance_b
    #grab blue
    a1, b1 = func(blue+1, red, depth-1, disks+1, a, disks*b)
    #grab red
    a2, b2 = func(blue, red+1, depth-1, disks+1, (disks-1)*a, disks*b)
    r1, r2 = a1*b2+a2*b1, b1*b2
    p = gcd(int(r1), int(r2))
    return (r1/p, r2/p)


a,b = func(0,0,15, 2, 1, 1)
print ("chance = " + str(a) + " / " + str(b))
print ("money = " + str(b//a))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 3,   --------------------------')
t1  = time.time()

# ==== Wed, 16 Nov 2016, 20:44, Khalid. Saudi Arabia
# Doing 4 and 5 by hand, I noticed the pattern. One way to look at it is that it's 1 + the sum of the the probabilities
# for picking 1 (which turns out to be the direct sum of 1 to n) + the sum of the probabilities of picking 2
# (which is the product of each of the numbers 1 to n) ... etc up to ceil(n/2)


from itertools import combinations
from math import ceil

turns = 15
sample_space = 1
for i in range(2, turns+2):
    sample_space *= i

min_to_win = int(ceil(turns / 2.0))

probabilities = 1
for win in range(1, min_to_win):
    combs = combinations(range(1, turns+1), win)
    for c in combs:
        p = functools.reduce(lambda x, y: x*y, c)
        probabilities += p

print (sample_space, "/", probabilities, "=", sample_space / probabilities)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 4,  SIMPLEST &  FAST --------------------------')
t1  = time.time()

# ===== Thu, 19 Jan 2017, 22:41, zinger_13, Canada
# Quick solution using some handy modules.  Runs in 13ms:

from itertools import combinations
from functools import reduce
from operator import mul
turns = 15

num = 0
for reds in range((turns+1)//2):
    for r in combinations(range(1, turns+1),reds):
        num += reduce(mul, r , 1)

print(reduce(mul, range(2, turns+2))//num )



t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 5, Simple & Fast   --------------------------')
t1  = time.time()

# === Fri, 15 May 2015, 00:03, gle_blanc, France
# Very simple


from itertools import combinations

N = 15

def prod(seq):
   prod = 1
   for factor in seq:
      prod *= factor
   return prod

sampleSpaceSize = prod(range(1,N+2))
eventSize = sum(prod(c) for k in range((N+1)//2) for c in combinations(range(1,N+1),k))
print(sampleSpaceSize // eventSize)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 6,  AMAZING, THE FASTEST --------------------------')
t1  = time.time()

# ==== Tue, 18 Aug 2015, 17:02, Haroun, Saudi Arabia

# my python code needed 0.14 milliseconds to work (really fast).
# The idea : Let f(n,k) be the number of ways of obtaining kk blue disks in nn turns.
# At the n-th turn, to obtain kk blue disk we can have k blue disks in n−1 turns and
# The only blue disk on the n-the turn or have k−1 blue disks in n−1 turns  and a red disk on the n-th disk
# (we have nn disk at the n-th disk), then :
#
# f(n,0)=(n−1)!,      f(n,n)=1,           f(n,k) = n⋅f(n−1,k)+f(n−1,k−1).
#
# which is like a pascal triangle, easy to implement. we divide n!
# by the sum of f(n,k) for n≥k≥[n/2]+1.


def f(n):
    s=[1,1]
    for i in range(2, n+1):
        s = [ i*s[0]]+list(s[k]+i*s[k+1 ] for k in range(0, i-1))+[1]
    p =  sum( s[k] for k in range(n//2+1,len(s)) )
    f = 1
    for i in range(1,n+2): f*=i
    return f/p

sol=f(15)

print ("the anwser is :" , sol )

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 7,  THE FASTEST --------------------------')
t1  = time.time()

# ==== Tue, 15 Mar 2016, 16:16, rokusuke, Japan

# Let p_k be the probability that the player takes k blue discs. Then
# G(x) = ∑{k=0, 15} p_k * x**k = ∏ {k=1, 15}  [ k / (1+k) + x/ (1+k)]

# It is easy to calculate this polynomial. The answer is ⌊1 / ∑{k=8, 15}  p_k ⌋ . (floor function )


def mult(p, q):
    r = [0] * (len(p) + len(q) + 1)
    for i in range(len(p)):
        for j in range(len(q)):
            r[i+j] += p[i] * q[j]
    return r

n = 15
p = [1]
for k in range(1, n + 1):
    p = mult(p, (k / (1 + k), 1 / (1 + k)))

print(int(1/sum(p[n // 2 + 1:])))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 8,  GOOD --------------------------')
t1  = time.time()

# ==== Sat, 27 Dec 2014, 12:31, GreenFlu

from itertools import combinations

n = 15
P = [i for i in range(1, n+1)]

nor = 1
den = reduce(lambda x, y: x*y, [i for i in range(2, n+2)])              #(n+1)!

for i in range(1, (n-1)//2 + 1):
	for j in combinations(P, i):
		nor += reduce(lambda x, y: x*y, j)
print (nor, den, den/nor)
#2269

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

