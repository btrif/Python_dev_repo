#!/usr/bin/python
# Solved by Bogdan Trif @   Completed on Sat, 10 Dec 2016, 23:25
#The  Euler Project  https://projecteuler.net
'''
            Diophantine reciprocals I           -          Problem 108

In the following equation x, y, and n are positive integers.

                                             1 / x  +  1 / y  =  1 / n

For n = 4 there are exactly three distinct solutions:

                                            1 / 5 + 1 / 20 = 1 / 4

                                            1 / 6 + 1 / 12 = 1 / 4

                                            1 / 8 + 1 / 8 = 1 / 4

What is the least value of n for which the number of distinct solutions exceeds one-thousand?

NOTE: This problem is an easier version of Problem 110; it is strongly advised that you solve this one first.
'''

import time
import math
from  fractions import Fraction
import gmpy2
from itertools import combinations, count, islice
import functools, operator, gmpy2
from pyprimes import factorise

print('\n--------------------------TESTS------------------------------')

print('Check the proximity of a number to another:\t',math.isclose(4, 4.0000000001, rel_tol=10**(-14) ))
print('Check the proximity of a number to another:\t',math.isclose(4, 4.0000000001))

print(5/Fraction(6) + 3/Fraction(12))
print('\n----------------------------')


class GET_DIVISORS(object):
    '''©Made by Bogdan Trif @ 2016-11-15, based on itertools.combinations module
    and with a little help on list(functools.reduce(operator.mul, i) for i in comb)

    :param nr:  int
    :return: a list with the factors ( method factorise) or divisors (method divisors)
    :Usage:  >>> GET_DIVISORS().divisors(90)    # to obtain the divisors   '''

#     def __init__(self, nr):   # We don't want to initialize the class with a number
#     self.nr = nr

    def factorise(self, nr):
        ''' Decompose a factor in its prime factors. This function uses the pyprimes module. THE FASTEST  '''

        return [val for sublist in [[i[0]]*i[1] for i in factorise(nr)] for val in sublist]

    def divisors(self, nr):
        ''':Description: Use the itertools, functools, operator, gmpy2 modules.
        In the case of multiple calls take the module imports outside the class and load only once => improved speed. '''

        if gmpy2.is_prime(nr) == True or nr == 1 :
            return [1]    # Must be adjusted to [1] if you change on list
        else :
            all_factors =  self.factorise(nr)
            # set_factors=list(set(all_factors))
            comb= set()
            # print('all_factors:\t',all_factors)
            for i in range(1, len(all_factors)):
                c = set(combinations(all_factors, i) )
                comb.update(c)
                comb_prod = list(functools.reduce(operator.mul, i) for i in comb)
                comb_prod.sort()
        return  len(comb_prod)+2   # sum([1]+ comb_prod)   !!! Remember to change on  return [1]  for is_prime case !


def lcm(a, b):
    """Return lowest common multiple."""
    return a * b // math.gcd(a, b)




def partitions(n):
    '''     Taken from http://code.activestate.com/recipes/218332-generator-for-integer-partitions/
            Created by David Eppstein on Wed, 27 Aug 2003
    :What it is:    A generator of number partition
    :Usage:     Example:    for i in partitions(5):    print(i)
    :param n:   the number you want the partitions
    :return:    set of lists with all the possible combinations                                                 '''
    # base case of recursion: zero is the sum of the empty list
    if n == 0:
        yield []
        return
    # modify partitions of n-1 to form partitions of n
    for p in partitions(n-1):
        yield [1] + p
        if p and (len(p) < 2 or p[1] > p[0]):
            yield [p[0] + 1] + p[1:]



def primitive_Diophantine(n):   # CHECK FUNCTION ONLY
    cnt = 0
    for i in range(n+1, 2*n+1):
        j = i
        while  (i*j)/(i+j) <= n :
            if (i*j)/(i+j) == n:
                print('n=',n, '\t\t i=', i,'   j=' , j ,'\t' ,(i*j)/(i+j), '     Fractions : ',Fraction(i, j) , '      ',gmpy2.mpq(i, j) )
                cnt+=1
            j+=1
    print('------------------------------')
    return  cnt


def compute_Diophantine_ways(n):
    cnt = 0
    for i in range(n+1, 2*n+1):
        j = lcm(i, n)
        # print(i)
        if (i*j)/(i+j) == n:
            print('n=',n, '\t\t i=', i,'   j=' , j ,'\t' ,(i*j)/(i+j))
            cnt+=1
        # if cnt > 20 :
    print('------------------------------')
    return  cnt

def get_divisors(all_factors) :
    ''':Description: Takes as argument a list of all factors of a number and returns its divisors '''
    comb= set()
    for i in range(1, len(all_factors)):
        c = set(combinations(all_factors, i) )
        # print(c)
        comb.update(c)
        comb_prod = set(functools.reduce(operator.mul, i) for i in comb)
        # print(comb_prod)
    return [1]+sorted(list(comb_prod))+ [functools.reduce(operator.mul, all_factors)]


def  calculate_divisors(nr):
    '''**©** Made by Bogdan Trif @2016-12-08, 16:30.
        :Description: Functions which computes the number of divisors of a number.
                It uses the Numbers of Divisors Theorem :which says : if N=a**x*b**y*c**z => divisors_nr=(x+1)(y+1)(z+1)
            Example: N = 216 = 2**3 * 3**3 => divisors_nr = (3+1)(3+1) = 16
    :param nr: int, nr
    :return: int, divisors_number
    '''
    # import functools, operator
    # from pyprimes import factorise
    def factors(nr):
        ''' Decompose a factor in its prime factors. This function uses the pyprimes module. THE FASTEST  '''
        return [i for i in factorise(nr)]
    N = factors(nr)
    return  functools.reduce( operator.mul , [ (i[1]+1) for i in N ])

print('Factorise 114307200 : ' ,[i for i in factorise(114307200)])
print('calculate_divisors : ' ,calculate_divisors(114307200))

def get_reciprocals(nr) :
    factors =  GET_DIVISORS().factorise(nr)
    div = get_divisors(factors)
    # print(div)
    X = []
    for i in range(1, len(div)-1):
        for j in range(i, len(div)-1):
            frac = gmpy2.mpq(div[i], div[j])
            if frac.numerator != 1 :
                # print(div[i], div[j], '    ', frac , frac.numerator )
                X.append(frac)
    X = list(set(X))
    # print(len(X), X)
    return len(X) + calculate_divisors(nr)



print('\n-----------primitive_Diophantine & compute_Diophantine_ways CORRECTNESS  TESTS ----------------------')

number = 12

print(' ---------- Number to Test is :\t', number, '  -------------\n')
# print('    !!!    TRUE ANSWER from the  Function primitive_Diophantine :\t ' ,primitive_Diophantine(number),'\n' )
# print('Test for the Function compute_Diophantine_ways :\t ' ,compute_Diophantine_ways(number) )       # It's equivalent to divisors number



print('\nFactors of ',number,'are :\t' , GET_DIVISORS().factorise(number))
lst = GET_DIVISORS().factorise(number)
print('\nClass Method for GET_DIVISORS().divisors :\t', GET_DIVISORS().divisors(number),'\n')
print('\nFunction Test for get_divisors :\t', get_divisors(lst) )

print('\n =====  Function get_reciprocals Test : \t',get_reciprocals(number))


# test_factors = (2, 3, 5, 7, 2, 3, 2, 3, 11, 13, 17, 19)
# test_factors = [2]*5+[3]*3+[5]*2+[7]+[11]+[13]+[17]
# n = functools.reduce(operator.mul, test_factors)






print('\n------------------------ TESTS ----------------------')
# 2016-12-06, 16:30, I will retry later
# test_factors = (2, 2, 2, 2, 2, 3, 3, 3, 5, 5, 7, 11, 13, 17)
# print('\nTest for functools.reduce  :\t ', functools.reduce(operator.mul, test_factors), '\n')
# print('Class Method for GET_DIVISORS().divisors :\t', GET_DIVISORS().divisors(number))

print('\n================  My FIRST SOLUTION,   ===============\n')
t1  = time.time()

def solution_iter_pb108():
    for n in count( int(15e4)  ):
        if gmpy2.is_prime(n) == False :
            if len(GET_DIVISORS().factorise(n)) > 7 :
                rec = get_reciprocals(n)
                # print( n, rec)
                if rec > 1000 :
                    ans = n
                    break

    return print('\nAnswer: \t', ans )



solution_iter_pb108()           # Answer : 180180



t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')          # Completed in : 21193.212271 ms



print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
                ##### GENERAL IDEAS ###########

# https://en.wikipedia.org/wiki/Highly_composite_number
# https://oeis.org/A002182
# https://oeis.org/A002182/b002182.txt

# ===== Sun, 6 Nov 2016, 20:10, night.train, USA

# Can show mathematically that number of representations is a function of
# prime factorization exponents. If those exponents are n1, n2, n3, the
# representations will number: ((2n1+1)*(2n2+1)*(2n3+1)+1)/2.




print('\n--------------------------SOLUTION 0,   --------------------------')
t1  = time.time()
# ======Sun, 10 Nov 2013, 15:46, Anthony, England
# I had this function to get the number of solutions given a particular number
def NumberSolutions(n):

    count = 0
    nsquared = n**2
    for i in range(1,n+1):
        if nsquared % i == 0:
            count += 1
    return print(count)

NumberSolutions(180180)

# But what to test in the function? I tried brute forcing and it took forever so started playing with 1260
# and soon saw that was 2^2*3^2*5*7 (ie powers of primes) and tried a few combinations until I found 2^2*3^2*5*7*11*13 worked.
# Not entirely happy that I solved this programmatically but have solved it.
# Now to apply the powers of many primes to solve 110 programmatically.

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')



print('\n--------------------------SOLUTION 1,   --------------------------')
t1  = time.time()
# ====== Tue, 30 Sep 2014, 10:12, sgruenwald, USA
# Fairly straight forward in Python. Takes about 2 seconds calculation time.

a=10**3
a+=1
n=a
while 1:
    t,v= n*n,2
    for i in range(2,n):
        if t%i == 0:
            v+=1
    if v > a-1:
        print (n)
        break
    n +=a

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 2,   --------------------------')
t1  = time.time()
# ========== Sun, 18 Jan 2015, 04:28, Xin, OCaml, China

import sympy as sy
from operator import mul
from functools import reduce

plist = list(sy.primerange(2,100))
p_num = len(plist)
MAX = 1e10
cutoff = 1000
ans = MAX

def cnt_sols(pf):
    return (reduce(mul,[x*2+1 for x in pf])+1)//2

def find_ans(i,pf,n):
    global ans
    if i>=p_num: return
    pf_tmp = pf.copy()
    while True:
        pf_tmp[i] += 1
        n *= plist[i]
        if n>MAX: break
        n_sols = cnt_sols(pf_tmp)
        if n_sols>cutoff:
            if n<ans: ans = n
            break
        find_ans(i+1,pf_tmp,n)

find_ans(0,[0]*p_num,1)
print(ans)



t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 3, VERY fast, aolea, Spain   --------------------------')

t1  = time.time()
# ========= Fri, 7 Oct 2016, 09:09, aolea, Spain

import pyprimes
import sympy

def aolea_sol() :
    n = 10**3
    listResult = [2]
    divisors = 3
    solutions = 2
    flag = False
    i1 = 2
    while flag == False:
        listResult.append(pyprimes.nth_prime(i1))
        num = 1
        for i in listResult:
            num = num*i
        divisors = len(list(sympy.divisors(num**2)))
        solutions =(divisors-1)/2 + 1
        k1 = 0
        k2 = 0
        k3 = 0
        k4 = 0
        if solutions > n:
            while   k1+1<= len(listResult) and listResult[-1] > listResult[k1]*listResult[k1+1] and int(round(solutions*25/27))>=n :
                    listResult.pop()
                    listResult.append(pyprimes.nth_prime(k3+1))
                    listResult.append(pyprimes.nth_prime(k3+2))
                    k3 = k3 + 2
                    k1 = k1 + 4
                    num = 1
                    for i in listResult:
                        num = num * i
                    divisors = len(list(sympy.divisors(num ** 2)))
                    solutions = (divisors - 1) / 2 + 1
                    listResult=sorted(listResult)
            while   k2+1<= len(listResult) and listResult[-1] > listResult[k2]*listResult[k2+1] and int(round(solutions*49/75))>= n :
                    listResult.pop()
                    listResult.append(pyprimes.nth_prime(k4+1))
                    listResult.append(pyprimes.nth_prime(k4+2))
                    k4 = k4 + 2
                    k2= k2 + 4
                    num = 1
                    for i in listResult:
                        num = num * i
                    divisors = len(list(sympy.divisors(num ** 2)))
                    solutions = (divisors - 1) / 2 + 1
                    listResult=sorted(listResult)
            print(n,num,solutions,divisors,listResult)
            flag = True
        i1 = i1 + 1

aolea_sol()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 4,  SLOW --------------------------')
t1  = time.time()
# ===== Thu, 29 Jan 2015, 19:47, jvbelle, SouthAfrica
# Easy but didn't quite get the partitions figured out. Just got to the first level of analysis and brute-forced:
#     for b in range(n+1,2*n):
#         if (b*n)%(b-n) == 0: nr += 1
# Ran it up to 10,000 - found multiples of 60 and 180 and 360 recurring lots so you can run the bruteforce
# on ranges with those steps in 3 separate windows.
# <10 lines

def jvbelle() :
    bestnr, bestn, limit = 0,0,  1000
    #for n in range(3,10000):
    for n in range(180,360000, 180):
        nr = 1  # 1/n = 1/2n + 1/2n
        for b in range(n+1,2*n):
            if (b*n)%(b-n) == 0: nr += 1
        if nr > bestnr:
            bestnr, bestn = nr, n
            print(n,nr)
            if bestnr > limit: break

# jvbelle()


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 5,   --------------------------')
t1  = time.time()
# ===== Tue, 20 Aug 2013, 22:39, Nicolas Patrois, France
# Brute force… and a little help (for verification) in OEIS.

from math import sqrt,floor

def prod(lis):
  p=1
  for i in lis:
    p*=i
  return p

n=3
liste=[{0:0},{1:0},{2:1},{3:1}]
premiers=[2,3]

while prod([c*2+1 for c in (liste[n].values())])<1999:
  n+=1
  nb=n
  d=0
  while n%premiers[d]!=0 and premiers[d]<sqrt(n):
    d+=1
  if n%premiers[d]!=0:
    liste.append({n:1})
    premiers.append(n)
  else:
    liste.append(dict(liste[n//premiers[d]]))
    if premiers[d] in liste[n].keys():
      (liste[n])[premiers[d]]+=1
    else:
      (liste[n])[premiers[d]]=1

print(n)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 6,   --------------------------')
t1  = time.time()
# ===== Mon, 29 Jun 2009, 20:28, PyRangers, Bulgaria
# The way i solved this I just thought of highly composite numbers and checked their number of solutions.
# first 720720, then 360360, and finally the answer 180180.
 # After some research I had this program to justify it.


n = 1260

while 1:
    count = 2   # sq % 1 and sq % n
    sq = n*n
    for x in range(2, n):
        if not sq % x:
            count += 1

    if count > 1000:
        print (n, count)
        break

    n += 1260

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 8,   --------------------------')
t1  = time.time()
# ======= Tue, 13 Sep 2016, 14:41, mbh038, England
# About 2.9 ms in Python on a MacBook Pro 2015.

import itertools as it
import numpy as np
import operator as op

def dr(m):
    """
    returns the minimum value of n for which the diophantine equation 1/x + 1/y = 1/n
    has more than m solutions
    """
    print('Diophantine reciprocal equation: 1/x + 1/y = 1/n')
    primes=[]
    prime=erat2a()
    while 1:
        primes.append(next(prime))
        if np.prod(primes)>m**2:
            break
    primes.append(next(prime))

    pfs=[]
    powers=[]
    solutions=[np.inf]
    pindex=0
    minsol=np.inf
    while len(pfs)<len(primes):
        pfs.append(primes[pindex])
        for pmax in range(1,5):
            powers=pfpowers(pfs,pmax)
            for a in powers:
                if np.prod([2*a[x]+1 for x in range(len(pfs))])>2*m-1:
                    solutions.append(myprod(pfs,a))
                    if solutions[-1]<minsol:
                        minsol=solutions[-1]
                        amin=a
                    break
        pindex+=1
    print('Least value of n for which the number of solutions exceeds',m,'=',minsol)
    print('Prime factors:',amin)
    print('Prime factor powers:',pfs[:len(amin)])
    print('Number of solutions:',(divisibility(amin)+1)//2)


def pfpowers(pfs,maxpow):
    """
    returns list of possible exponents a,b,c,d... where maxpow =a>=b>=c...of a
    list of prime factors 2,3,5,7...in order such that 2^a*3^b*4^c...is an ascending sequence.
    """
    ps=[]
    for a in it.combinations_with_replacement([x for x in range(maxpow,0,-1)],len(pfs)):
        ps.append(list(a))
    ranks=[]
    ps=ps[::-1]
    ranks=sorted([(i,myprod(ps[i],pfs)) for i in range(len(ps))],key=op.itemgetter(1))
    rps=[]
    for i in range(len(ps)):
        rps.append(ps[ranks[i][0]])
    return rps

def divisibility(powers):
    """
    returns the number of divisors of a natural number, given a list of the
    exponents of its prime factors
    """
    d=1
    for x in powers:
        d*=(2*x+1)
    return d

def myprod(primes,powers):
    p=1
    for i in range(len(primes)):
        if powers[i]==0:
            break
        p*=int(int(primes[i])**int(powers[i]))
    return p

def erat2a():
    """primes generator"""
    D = {}
    yield 2
    for q in it.islice(it.count(3), 0, None, 2):
        p = D.pop(q, None)
        if p is None:
            D[q * q] = 2 * q # use here 2 * q
            yield q
        else:
            x = p + q
            while x in D:
                x += p
            D[x] = p

dr(1000)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

