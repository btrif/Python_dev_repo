#!/usr/bin/python                   o(^_^)o         ( ͡° ͜ʖ ͡°)
# © Solved by Bogdan Trif @     Completed on Sat, 25 Mar 2017, 16:04
#The  Euler Project  https://projecteuler.net
'''
                    Top Dice        -       Problem 240
There are 1111 ways in which five (5)  6-sided dice (sides numbered 1 to 6)
can be rolled so that the top three sum to 15. Some examples are:

D1,D2,D3,D4,D5 = 4,3,6,3,5
D1,D2,D3,D4,D5 = 4,3,3,5,6
D1,D2,D3,D4,D5 = 3,3,3,6,6
D1,D2,D3,D4,D5 = 6,6,3,3,3

In how many ways can twenty (20) !!!!   12-sided dice (sides numbered 1 to 12) be rolled so that the top ten sum to 70?


'''
import time, zzz
from itertools import combinations, permutations, combinations_with_replacement, product
import collections
from math import factorial
from functools import reduce
from operator import mul


def partition(number):
    answer = set()
    answer.add((number, ))
    for x in range(1, number):
        for y in partition(number - x):
            answer.add(tuple(sorted((x, ) + y)))
            #print(answer)
    return answer

def partition_min_max(n,k,l, m):
    ''':Description:  n - is the integer to partition, k -  is the length of partitions,
    l - is the min partition element size, m - is the max partition element size '
   Taken from http://stackoverflow.com/questions/18503096/python-integer-partitioning-with-given-k-partitions
   **©** Modified by Bogdan Trif @ 2017-03-25, 12:20,
    :param n: n is the integer to partition
    :param k: k is the length of partitions
    :param l: l is the min partition element size
    :param m: m is the max partition element size
    :return: list of partition lists                        '''

    if k < 1:
        raise StopIteration
    if k == 1:
        if n <= m and n>=l :
            yield (n,)
        raise StopIteration
    for i in range(l,m+1):
        for result in partition_min_max(n-i,k-1,i,m):
            yield result+(i,)

def calc_perm(lst) :        ### o(^_^)o    o(^_^)o  ###
    '''     **©** Made by Bogdan Trif @ 2016-12-16, 1150.
         The formula is Perm(total_elem_nr) / [ Perm(elem_1) *Perm(elem_2) * ...* Perm(elem_n) ]
        :Description:    Calculates the number of unique permutations of a list.
        :param lst: list
        :return: int, number of permutations                    '''

    total = len(lst)
    elem_nr=[]
    for i in set(lst): elem_nr.append(lst.count(i))
    numerator = factorial(sum(elem_nr))
    denominator =  reduce(mul, [factorial(i) for i in elem_nr] )
    return numerator // denominator

def non_increasing_counter(values, length):
    ''':Description: generates from a list of values all the combinations up to to the maximum value
        in the values list. length is the length of the sequences generated
        https://www.reddit.com/r/learnpython/comments/3dnzap/need_to_generate_all_possible_permutations/
    :param values:   list
    :param length: the length of list
    :return:
    '''
    if length == 1:
        for value in values:
            yield value,
    else:
        for index, value in enumerate(values, 1):
            for rest in non_increasing_counter(values[:index], length - 1):
                yield (value,) + rest

# @2017-03-22 - 00:05 - Easy ! Combinatorics Problem
# it will be , example  : combinations for 663 --> all the combinations of 2 elements up to 3 which is C(...,...) = 190
# Not quite so easy, I must count also the permutations of elements
# Must first use partition of 15 in 3, and then make permutations of the resulted combinationsand only afterwards
# compose it with the remaining list for which the maximum must me <= than the min of the 15 list
#
# Example : for our case study 15 = [6,6,3] with all its permutations against the complete list of five elements
# Then, we take the remaining two factors and take care that max = 3 => min (6,6,3) and also make permutations of that
# In the end we multiply the two cases !
# WELL, THIS NEEDS QUITE SOME WORK !!!! in the end. not an easy problem !
#
# Therefore the problem will be in 4 steps :
# step 1. partition of 70 into 10 pieces ! WOW. DAMAGE here !
# step 2 . find how many permutations against the 20 list there are with those.
# step 3. find the remaining 10 numbers for which the max is <= than the min from the first 10 list
#     and also permutate them . (Fucking shit !!!)
# step 4. put all the pieces together.
# I have emotions for the partition part with its permutations, my algorithms work close to  that limit.



print('\n------------------------ TESTS, understanding the concept ------------------------------')
t1  = time.time()

def brute_force_test():
    cnt, itr = 0, 0
    for a, b, c, d, e in product(range(1, 6+1), repeat=5):

        m1, m2, m3 = sorted([a, b, c, d,e])[-3::]
        if m1+m2+m3 == 15  :
            cnt +=1
            if m1 == 3 and m2 ==6 and m3 == 6 :
                itr+=1
                print(str(cnt)+'.      ',  a, b, c, d, e , '        ', sorted([a, b, c, d,e ])  ,'    ', itr )

brute_force_test()
print()
# print(partition(10))

# =======  STEP 1
# top 10 = 70
#  7  7  7  7  7  7  7  7  7  7  <--- min configuration  => the other side : max conf :  7 7 7 7 7 7 7 7 7 = > 7777777777-1111111111+1 posibilities
# the first part should be merged with the second and only then calculate the permutations
# 12 12 12 12 12 6 1 1 1 1 <---  max configuration => other side : max conf : 1 1 1 1 1 1 1 1 1 1 => 1111111111-1111111111+1 = 1

Z = list(partition_min_max(15 , 3, 1, 6 ))
print(len(Z),'\n', Z[:50],'\n',Z[-50::])

test_lst = (12, 12, 12, 12, 12, 6, 1, 1, 1, 1)
print('calc_perm : \t',calc_perm(test_lst)  )

desc_counter = list( non_increasing_counter( range(1, 4), 4 )  )
print('non_increasing_counter : \t',desc_counter  )

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n================  My FIRST SOLUTION,  30 seconds, Good Enough  ===============\n')
t1  = time.time()

def my_first_solution( n , k, l, m, r   ) :
    S, cnt = 0, 0
    for i in list(partition_min_max(n ,k, l, m )) :
        cnt +=1
        v_min = min(i)
        print( str(cnt)+'.     ',  i ,  v_min )
        for j in non_increasing_counter( range(1, v_min+1), r ) :
            C = list(i)+list(j)
            elem = collections.Counter(C)
            num = factorial(k+r)
            den = reduce(mul, [ factorial(v) for k, v in elem.items() ] )
            res = num//den
            # print(i, v_min, '     ', j,'      ', C,'      ', elem, num , den  , res)
            S += res
    return print('\nAnswer : \t', S)

# my_first_solution(70, 10, 1, 12, 10 )           #       Answer : 	 7448717393364181966


t2  = time.time()
print('\nCompleted in :', round((t2-t1),6), 's\n\n')


print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1,  VERY Similar to mine ,33 sec --------------------------')
t1  = time.time()

# ====== Sat, 10 Jan 2015, 06:06, wakkadojo, USA
#
# Ah, I have been out-clevererred
#
# I split the problem up into two pieces:
# 1. Find out the combinations of dice that summed exactly to the target number
# 2. Find the combinations of dice that wouldn't change (1) (i.e. combs with max <= min of (1))
#
# Then, combine and count.
#
# Not the most glorious piece of code, but I hacked it out quickly and it passes the one minute rule.

import itertools

class count:
    def __init__ (self):
        self.f = [1, 1]
    def fact (self, k):
        if len (self.f) < k+1:
            self.f += [-1]*(k + 1 - len (self.f))
        if self.f[k] < 0:
            self.f[k] = k*self.fact (k-1)
        return self.f[k]
    def __call__ (self, p):
        c = self.fact (sum (p)) # number rolls
        for x in p:
            c //= self.fact (x)
        return c

# sum to a using n elements of max k
def integer_partition (a, n, k, m):
    if n < 1:
        return []
    if n == 1 and k >= a:
        return [[a]]
    if (a, n) not in m:
        m[a, n] = []
        for i in range (1, k+1):
            for r in integer_partition (a-i, n-1, k, m):
                if r[0] >= i:
                    m[a, n] += [[i] + r]
    return m[a, n]

def remap_partition (m, k):
    new = [ [ 0 for _ in range (k) ] for _ in m ]
    i = 0
    for x in m:
        new[i], i = [ x.count (i+1) for i in range (k) ], i+1
    return new

def min_list (p):
    for i in range (len (p)):
        if p[i] != 0:
            return i

def merge (a, b):
    return [ a[i] + b[i] for i in range (len (a)) ]

def solution_1():
    a, m, n, k = 70, 20, 10, 12
    p = remap_partition (integer_partition (a, n, k, {}), k)
    c = count ()

    # for each of the sum rolls, fill in the blanks and count the ways
    s = set ()
    for i in range (k):
        for a in p:
            if i <= min_list (a)+1:
                for b in itertools.combinations_with_replacement(range(1,i+1), m-n):
                    t = tuple (merge (a, remap_partition ([b], k)[0]))
                    s.add (t)
    return print (sum (c (x) for x in s))

# solution_1()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 2,  25 sec --------------------------')
t1  = time.time()

# ====Fri, 19 Dec 2014, 19:22, eidanch, Israel
#
# Huh... few seconds in python for backtracking on all sets (and then using multinomial coefficient for orderings).
# I was a bit surprised it worked that fast.

def factorial(n):
    result = 1
    for k in range(2, n+1):
        result *= k
    return result

def multinomial(xs):
    n,d = 0,1
    for x in set(xs):
        c = xs.count(x)
        n += c
        d *= factorial(c)
    return factorial(n)/d

def bruteDiceCountExtended(sides, count, dsum, rest=None, lst=[]):
    if rest is None:
        rest = 0
    if count == 0 and dsum == 0:
        if rest == 0:
            return multinomial(lst)
        result = 0
        for i in range(1,sides+1):
            result += bruteDiceCountExtended(min(sides,i), count, dsum, rest - 1, lst+[i])
        return result
    if sides*count < dsum:
        return 0;
    if count > dsum:
        return 0
    result = 0
    for i in range(1,sides+1):
        result += bruteDiceCountExtended(min(sides,i), count - 1, dsum - i, rest, lst+[i])
    return result


# assert bruteDiceCountExtended(6, 3,15,2) == 1111
# print (bruteDiceCountExtended(12, 10,70,10))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 3,   --------------------------')
t1  = time.time()

# ==== Mon, 30 Dec 2013, 23:35, gechhesy, USA
# struggled for a while. then figured out to pick a pivot number pick how many times it is in the answer,
# then pick how many of its rolls are in top 10.. then its' super fast:

def P(p, n, s, m):
    # number of ways to roll n s sided dice to get p
    #print("D(", p, n, s, ')')
    if p==0 and n==0:
        return 1

    if n*s<p or n>p:
        return 0
    sm=0
    nn=int((p-n)/s)+1
    #print('Need C(', p, ',', 0, '-', nn-1, ') and C(', [p-s*i-1 for i in range(nn)], ',', n-1,')')
    for i in range(nn):
        sm+= (-1)**i * C(n, i, m) * C(p-s*i-1, n-1, m)
    return sm

def PWithMin(p, n, s, mn):
    """
    num ways to roll p with n s sided dice with the smallest value being mn
    # >>> PWithMin(15, 3, 6, 4)
    1

    """

    return P(p-(mn-1)*n, n, s-(mn-1))


def e240(p, n, s, nt):

    #pivot is die roll that is lowest value of top nt dice that adds to p
    #  can also be in the lower half too, so it is tricky
    #
    #  p = sum we're looking for
    #  n = total number of rolls
    #  s = num sides of die
    #  nt = number of top rolls to add to see if we make p
    #
    #  pivot min value of die in top nt die rolls
    #  np = number of pivot values out of n
    #  nh = number of die rolls higher than pivot (therefor included in sum)
    #  nl = number of die rolls lower than pivot (not included in sum)
    #         n = np + nh + nl
    #  nph = number of pivots included in high (and included in the sum)
    #  ph = target sum for nh dies (all hgher than pivot)

    tot = 0
    for pivot in range(1, s+1):
        for np in range(1, n+1):
            waysToAssignPivots = C(n, np)
            if pivot != s:
                min_nph = max(1, np - (n-nt))
                max_nph = min(nt, np)
            else:
                min_nph = max_nph = nt

            for nph in range(min_nph, max_nph+1):
                nh = nt-nph
                ph = p-nph*pivot
                if ph <0:
                    continue
                nl = n-nh-np

                #print('pre pivot', pivot, 'np', np, 'nph', nph)
                waysToAssignHighsAfterPivots = C(n-np, nh)
                waysToFillHighs = PWithMin(ph, nh, s, pivot+1)
                waysToAssignLows = 1 # because that's all that's left
                waysToFillLows = (pivot-1)**nl

                v = waysToAssignPivots * waysToAssignHighsAfterPivots * waysToAssignLows * \
                    waysToFillHighs * waysToFillLows
                #print('pivot', pivot, 'np', np, 'nph', nph, 'v', v)
                tot += v

    print(p, n, s, nt, '=', tot)
    return tot

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 4,  1 sec, THE FASTEST --------------------------')
t1  = time.time()

# ==== Sat, 16 Jan 2016, 06:51, gclements, England
# 0.635s in Python.
# Enumerate the ways that 10 12-sided dice can sum to 70.
# For each one, calculate the number of ways that 20 dice can produce that result.
# The tricky part was handling the boundary, i.e. dice which are equal to the least of the "top ten" but aren't counted amongst them.


def q240():
    fact = [factorial(i) for i in range(21)]
    def partitions(sofar, total, highest, left):
        if highest == 1:
            if total == left:
                yield sofar + [left]
            return
        highest_ = highest-1
        for i in range(left+1):
            sofar_ = sofar + [i]
            left_ = left - i
            total_ = total - i * highest
            if total_ < 0:
                break
            for p in partitions(sofar_, total_, highest_, left_):
                yield p

    def ways(p, n):
        for i,k in enumerate(p):
            if not k:
                continue
            pp = p[i+1:]
            if any(pp):
                return (fact[n] // (fact[n-k] * fact[k])) * ways(pp, n-k)
            else:
                return sum((fact[n] // (fact[n-kk] * fact[kk])) * ways(pp, n-kk)
                           for kk in range(k,n+1))
        return len(p) ** n

    print (sum(ways(p, 20)              for p in partitions([], 70, 12, 10)))

q240()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 5,  10 sec --------------------------')
t1  = time.time()

# ==== Sat, 28 May 2011, 19:08, DanGoldbach, England
# Dynamic programming as usual -- a surprisingly small amount of maths was necessary.
# The state space is largish and it took a while to work out the intricacies of the problem,
# but solving for small cases first helped a lot.
# Runs in about 5 seconds.

MAX_VALUE    = 12
NUM_TOP      = 10
NUM_OVERALL  = 20
SUM_REQUIRED = 70

cache = {}

def dp(goal, minim, numTop, numFree, numMins):
    if (goal, minim, numTop, numFree, numMins) not in cache:
        t = (goal == numTop == numFree == numMins == 0)

        if numTop > 0:
            for d in range(minim, MAX_VALUE+1):
                if goal - d >= 0:
                    t += dp(goal-d, minim, numTop-1, numFree, numMins-(d==minim))
        if numFree > 0:
            for d in range(1, minim+1):
                if (d == minim and numMins == 0) or d != minim:
                    t += dp(goal, minim, numTop, numFree-1, numMins)

        cache[(goal, minim, numTop, numFree, numMins)] = t
    return cache[(goal, minim, numTop, numFree, numMins)]


# print (sum(sum(dp(SUM_REQUIRED, m, NUM_TOP, NUM_OVERALL-NUM_TOP, numMins)
#               for numMins in range(1, SUM_REQUIRED//m+1))
#           for m in range(1, MAX_VALUE+1)))


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 6,  5 sec , Recursive Solution  --------------------------')
t1  = time.time()

# ==== Mon, 23 Jul 2012, 18:57, anythingapplied, USA
# Recursive python solution in 4 seconds.  Fairly short program:

from math import factorial
from fractions import Fraction

def binom(a,b):
  return Fraction(factorial(a))/factorial(b)/factorial(a-b)

def num_dice(tot,sides,sum_cnt,tot_cnt):
  #Reframes the problem as dice that can roll between 0 and sides-1 instead of 1 to sides
  return num_dice2(tot-sum_cnt,sides-1,sum_cnt,tot_cnt)

def num_dice2(tot,sides,sum_cnt,tot_cnt):
  #Figures out how many dice should have a face value of sides
  #then reframes the problem with max sides of sides-1
  if tot-sides*sum_cnt == 0:
    ret = 0
    for x in range(sum_cnt,tot_cnt+1):
      ret += binom(tot_cnt,x) * sides**(tot_cnt-x)
    return ret
  elif tot-sides*sum_cnt > 0:
    return 0
  else:
    ret = 0
    for cur in range(0,min(tot//sides+1,sum_cnt)):
      ret += binom(tot_cnt,cur)*num_dice2(tot-sides*cur,sides-1,sum_cnt-cur,tot_cnt-cur)
    return ret

# print (num_dice(70,12,10,20))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 7, 600 ms, the FASTEST  --------------------------')
t1  = time.time()

# ===== Mon, 8 Mar 2010, 18:45, yurip  , USA

sides=12
dices=20
N=10
sumN=70

def f(n):
    if n <= 1: return 1
    return reduce(lambda a,b:a*b, range(1,n+1))

def b(n,m): return f(n)//f(m)//f(n-m)

def allcomb(remdices, remsum, mindice):
    if remsum < 0 or remdices*sides < remsum:
        return []
    if remsum == 0 and remdices == 0:
        return [1]
    ret = []
    for d in range(mindice, sides+1):
        for n in range(1, remdices+1):
            comb = allcomb(remdices-n, remsum-d*n, d+1)
            for v in comb:
                ret.append(v*f(n))
    return ret

cnt = 0
for d in range(1, sides+1):
    for n in range(1, N+1):
        comb = allcomb(N-n, sumN-d*n, d+1)
        if comb:
            r = dices - N + n
            R = f(dices)//f(r)*sum([b(r,i)*(d-1)**(r-i)
                               for i in range(n, r+1)])
            cnt += sum([R//g for g in comb])

print (cnt)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 8,   --------------------------')
t1  = time.time()

# from gmpy2 import comb
#
# def binomial(n,k):
#     if(B.get((n,k))):
#         return B[(n,k)]
#     else:
#         c=comb(n,k,exact=1)
#         B[(n,k)]=c
#         return c
#
# B={}
# D={}
# dice_side = 12
# throws = 20
# top = 10
# top_sum = 70
#
# def dice(sides,throws,given_sum):
#     if(sides == 0):
#         return sum==0
#     if(given_sum == 0 and throws ==0):
#         return 1
#     if(D.fromkeys((sides,throws,given_sum))):
#         return D[(sides,throws,given_sum)]
#     else:
#         c=sum([(-1)**n*binomial(throws,n)*binomial(given_sum-sides*n-1,throws-1) for n in range((given_sum-throws)//sides+1)])
#         D[(sides,throws,given_sum)]=c
#         return c
#
# total = 0
# for c in range(1,dice_side+1):
#     for k1 in range(1,top+1):
#         for k2 in range(0,throws-top+1):
#             total += dice(dice_side-c,top-k1,top_sum - c*top)*(c-1)**(throws-top-k2)* \
#                         binomial(throws,top-k1)*binomial(throws-top+k1,k1+k2)
#
# print(total)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


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

