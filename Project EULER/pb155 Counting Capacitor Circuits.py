#!/usr/bin/python
# Solved by Bogdan Trif @
#The  Euler Project  https://projecteuler.net
'''
                            Counting Capacitor Circuits         -       Problem 155
An electric circuit uses exclusively identical capacitors of the same value C.
The capacitors can be connected in series or in parallel to form sub-units, which can then be connected in series or in parallel
with other capacitors or other sub-units to form larger sub-units, and so on up to a final circuit.

Using this simple procedure and up to n identical capacitors, we can make circuits having a range of different total capacitances.
For example, using up to n=3 capacitors of 60 F each, we can obtain the following 7 distinct total capacitance values:

If we denote by D(n) the number of distinct total capacitance values we can obtain when using up to n equal-valued capacitors
and the simple procedure described above, we have: D(1)=1, D(2)=3, D(3)=7 ...

Find D(18).

Reminder : When connecting capacitors C1, C2 etc in parallel, the total capacitance is C_T = C1 + C2 +...,
whereas when connecting them in series, the overall capacitance is given by: 1/ C_T = 1/C1 + 1/ C2
'''
import time
from fractions import Fraction
from decimal import *
getcontext().prec = 25
from itertools import chain
import gmpy2

def add_capac_paralel(c1, c2):
    # return  c1+c2
    # return  Decimal(c1) + Decimal(c2)
    return  sum((Fraction(c1) , Fraction(c2)))

def add_capac_serie(c1 , c2):
    # return 1/(1/c1+1/c2)
    # return 1/(1/Decimal(c1)+1/Decimal(c2))
    return 1/sum((1/Fraction(c1),1/Fraction(c2)))

def gen_left_part(n):
    ''':Description:    Function which returns the number of partitions left to be considered.
        It is used on the Euler Problem 155
    :param:     n - integer, number of capacitors to be considered
    :Example:    >>> gen_left_part(7) will yield :         [(1, 6), (2, 5), (3, 4)]
        These represents the configurations which are new for this number of capacitors.
        All the others like (1,1,5), (1,2,4)...and so on, have been already calculated on the
        previous numbers of capacitors and are actually included in the results of (1,6) .
        Counting them again will be redundant  '''
    part=[]
    m=n//2
    for i in range(1, m+1):
        part.append((i, n-i))
        # print(i, n-i, end='  ' )
    return part

print('--------------------------TESTS------------------------------')

print('\nTest for the gen_left_part function : ' , gen_left_part(8))
print('Test Add Capacitors in Serie:  ', add_capac_serie(36,15))
a= add_capac_serie(36,15)
print('Test Add Capacitors in Paralel:  ', add_capac_paralel(a,45))
b= add_capac_paralel(a,45)
c = add_capac_serie(b,a)
print('Test Add Capacitors in Serie:  ', c)

print('\n------------------')

C={1 : [60] }
print('Initial Capacitance in dict: ', C)
print('Test Dictionary C with capacitors : ',C[1][0])

print('\n------------------')
print(1/(1/37+1/59+1/17+1/73))      # 8.583813362230122
print(1/Decimal(3))
print(Decimal(17)+Decimal(29))

#
# for i in range(len(C)) :
#     # print(add_capac_paralel(C[i]))
#     # print(add_capac_serie(C[i]))
#     C.append(add_capac_paralel(C[i]))
#     C.append(add_capac_serie(C[i]))
# print(C)
#
# for i in range(len(C)) :
#     C.append(add_capac_paralel(C[i]))
#     C.append(add_capac_serie(C[i]))
# print(list(set(C)))

############################
#
# def Condensators(n):
#     C = [60]
#     for k in range(1, n):
#         D=[]
#         for i in range(len(C)) :
#             D.append(add_capac_paralel(C[i]))
#             D.append(add_capac_serie(C[i]))
#         C = C+D
#         C = sorted(list(set(C)))
#     return C

# print('\n',len(Condensators( 4 )), Condensators( 4 ) )
# print('\nResult: ',len(Condensators( 5 )), Condensators( 5)[0:1000] )

# 1 piece: 1 [60]
# 2 pieces : 2 [30, 120]
# 3 pieces : 7 [40.0, 180, 20.0, 120, 90.0, 60, 30.0]
# 4 pieces : 15 [15.0, 20.0, 24.0, 30.0, 36.0, 40.0, 45.0, 60, 80.0, 90.0, 100.0, 120, 150.0, 180, 240]
# 5 pieces :  31 [12.0, 15.0, 17.142857, 20.0, 22.5, 24.0, 25.714286, 30.0, 34.285714, 36.0, 37.5, 40.0, 42.857143, 45.0, 48.0, 60, 75.0, 80.0, 84.0, 90.0, 96.0, 100.0, 105.0, 120, 140.0, 150.0, 160.0, 180, 210.0, 240, 300]

# I need the partition of numbers :   5     =    4+1,    3+2,      3+1+1,     2+2+1,     2+1+1+1,   1+1+1+1+1
# Must solve other problems first, Must do analysis on what combinations have been already performed on
#   previous other numbers, 4,3,2
# Combinations must also be done serie & paralel
# We must eliminate the partitions already computed at the lower numbers. Done

# Answers : Tried : 262143 = 2**18-1, 4836060

# for i in partitions(7):    print(i)

print('\n================  My FIRST SOLUTION, VERY SLOW  ===============\n')
# I must renounce to the fraction module
def pb155(n):
    for x in range(2, n+1):
        G=gen_left_part(x)
        print('Part.   ',G,'            #### ',x,' ####              ', round(( time.time() - t1),6), 's')
        C[x] = []
        # print('dictionary entry is created : ' , C)
        for i in range(len(G)):
            # print(G[i][0], G[i][1])
            D1, D2 = G[i][0], G[i][1]
            # print('------------------')
            for j in range(len( C[ D1] )) :
                for k in range(len( C[D2] )) :
                    # print(C[D1][j], C[D2][k] ,'      ' ,C[D1], C[D2])
                    s =  str(add_capac_serie(  C[D1][j]  ,C[D2][k] ))
                    p =  str( add_capac_paralel(  C[D1][j]  ,C[D2][k] ) )
                    # print('Serie & Parallel add   : ' ,s, p )
                    C[x].extend([s , p])
                    # print('dictionary evolution:    ' ,C[x])
        C[x] = list(set(C[x]))
        # C[x].sort()
        # print('===========')
    # E = sorted({x for v in C.values() for x in v})
    E = sorted(set(chain.from_iterable(C.values())))
    print('\n', len(E) ,  E[0:1000])                 # Flatten the dictionary
    # print('\nResult:   ',C)
    return print('\nResult : ',len(E))


# Now I have problems with the rounding !!          Every rounding gives a different result !!!!!!!!!!!! @2016-11-13, 13:34 Idea ?
# work with frac module

if __name__ == "__main__":
    t1  = time.time()

    # C={1 : [60] }
    C={1 : ['60'] }

    # pb155(12)

    t2  = time.time()
    print('\nCompleted in :', round((t2-t1),6), 's\n\n')

# To speed up thing I need to use mpq from gmpy2 module


a = gmpy2.mpq(3,11)/7 + gmpy2.mpq(11,8)/29
print(' = = gmpy2.mpq :' ,a ,'      ' , a.numerator, '      ' ,a.denominator)   # IMplement on problem 155 to speed up









print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')

print('\n--------------------------SOLUTION 1,  VERY VERY GOOD --------------------------')
t1  = time.time()
# The Python library's Fraction class and sets made this easy to do, although it does take 1:27 in pypy.  Here is my code:

import datetime, time
import fractions
from math import gcd

class capfrac:
    def __init__(self, num, dem):
        gcd1 = gcd(num, dem)
        self.num = num // gcd1
        self.dem = dem // gcd1
    def __add__(self, c1):
        return capfrac(self.num*c1.dem + c1.num*self.dem, self.dem*c1.dem)
    def add_inv(self, c1):
        return capfrac(self.num*c1.num, self.dem*c1.num + c1.dem*self.num)
    def __eq__(self, c1):
        return self.num*c1.dem == c1.num*self.dem
    def __hash__(self):
        return self.num * 10000 + self.dem

C_val = capfrac(1,1)

def par(c1, c2):
    return c1+c2

def ser(c1, c2):
    return c1.add_inv(c2)

def add_circuit(circuits, found_circuits, new_circuit, count):
    if new_circuit in found_circuits:
        return
    circuits[count].append(new_circuit)
    found_circuits.add(new_circuit)

def generate_circuits(circuits, found_circuits, total_count):
    for count1 in range(1, int(total_count/2)+1):
        count2 = total_count - count1
        for c1 in circuits[count1]:
            for c2 in circuits[count2]:
                add_circuit(circuits, found_circuits, ser(c1, c2), total_count)
                add_circuit(circuits, found_circuits, par(c1, c2), total_count)

def main():
    limit = 12
    circuits = [[] for i in range(0, limit+1)]
    found_circuits = set()
    found_circuits.add(C_val)
    circuits[1].append(C_val)
    tm=[]; tm.append(time.time())
    for c in range(2, limit+1):
        generate_circuits(circuits, found_circuits, c)
        tm.append(time.time()  )
        print('%s %s %s %s' % (c, len(found_circuits), datetime.datetime.now(), round(tm[-1]-tm[-2], 4) ))

# main()

t2  = time.time()
print('\nCompleted in :', round((t2-t1),6), 's\n\n')





print('\n--------------------------SOLUTION 2,  VERY INTERESTING SOLUTION, hacatu, USA --------------------------')
t1  = time.time()
# The Python library's Fraction class and sets made this easy to do, although it does take 1:27 in pypy.  Here is my code:

from fractions import Fraction as Q

MAX = 12
capss = [set(), {Q(1,1)}]

for n in range(2, MAX + 1):
    caps = set()
    for a in range(1, n//2 + 1):
        for c1 in capss[a]:
            for c2 in capss[n - a]:
                caps.add(c1 + c2)
                caps.add(1/(1/c1 + 1/c2))
    # print(caps)
    capss.append(caps)
print(len(set.union(*capss)))

t2  = time.time()
print('\nCompleted in :', round((t2-t1),6), 's\n\n')




print('\n--------------------------SOLUTION 3,  QUITE FAST  --------------------------')
t1  = time.time()
# Dynamic programming approach - any set of n capacitors can be broken down into a set of 'a' capacitors and
# a set of 'b' capacitors, combined either in parallel or in series, where a,b<n   and a+b=n .
# Thought about porting to Java for the necessary speed improvement to go under a minute, but was too lazy

nr = 12
def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)

def red(t):
    g = gcd(t[0], t[1])
    return (t[0] / g, t[1] / g)

d = [ set(), set( [ (1, 1) ] ) ]
for x in range(2, nr+1):
    s = set()
    for y in range(1, x):
        d1 = d[y]
        d2 = d[-y]

        for elem1 in d1:
            for elem2 in d2:
                f1 = (elem1[0] * elem2[0], elem1[1] * elem2[0] + elem1[0] * elem2[1])
                f2 = (elem1[0] * elem2[1] + elem1[1] * elem2[0], elem1[1] * elem2[1])
                s.add(red(f1))
                s.add(red(f2))

    d.append(s)

s = set()
for x in range(len(d)):
    s.update(d[x])

print (len(s))


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 3, Bo , USA  --------------------------')
t1  = time.time()

# I re-visited this problem after some time and found OldCigarette's method on page 4 to be quite good.
# Here's an adaptation of that code using gmpy2's mpq type for fractions.


def problem_155(n):
  from collections import defaultdict
  from itertools import product
  from gmpy2 import mpq

  # D[n] holds a list of capacitance values that can be made with n capacitors
  D = defaultdict(list)
  # answer is the set of all capacitance values found
  answer = set()
  D[1].append(mpq(1, 1))
  answer.add(mpq(1, 1))
  for n in range(2, n + 1):
    for n_1 in range(1, n // 2 + 1):
      for c_1, c_2 in product(D[n_1], D[n - n_1]):
        parallel = c_1 + c_2
        if parallel not in answer:
          D[n].append(parallel)
          answer.add(parallel)
        series = mpq(1, mpq(1, c_1) + mpq(1, c_2))
        if series not in answer:
          D[n].append(series)
          answer.add(series)

  return len(answer)

print(problem_155(18))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')      # Completed in87083.981037 ms

print('\n--------------------------SOLUTION 4, mercurium, Taiwan   --------------------------')
t1  = time.time()

# I wrote this in python using the idea that you can put two sets of capacitors in parallel any time you want.
# Denoting A[n] as the number of ways you can combine capacitors with exactly n capacitors to get a value
# that you can't with n-1 or less capacitors, I found the interesting fact that:
#
# All capacitor values for A[n] can be found by combining A[i] and A[n-i] capacitors in parallel.
#
# Runtime was slower because I made my own unoptimized fraction operation, but still
#
#
# def gcd(a,b):
#   if a==0: return b
#   return gcd(b%a,a)
#
# def combine(a,b):
#   x = a[0]*b[1] + a[1]*b[0]
#   y = a[1]*b[1]
#   return (x/gcd(x,y),y/gcd(x,y))
#
#
# A = [[(0,0)],[(1,1)]]
# A_set = set([(1,1)])
# A[1] = [(1,1)]
# count = 1
#
# for n in range(2,19):
#   cap_lst = []
#   for i in range(1,n):
#     j = n-i
#
#     for a in A[i]:
#       for b in A[j]:
#         item = combine(a,b)
#         if item not in A_set:
#           A_set.add(item) #C1
#           A_set.add((item[1],item[0]))
#           cap_lst.append(item) #C1
#           cap_lst.append((item[1],item[0]))
#
#   A.append(cap_lst)
#   count+= len(cap_lst)

print(count)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')      # Completed in : 134.853 s

print('\n--------------------------SOLUTION 5,  BRUTE FORCE, wakkadojo, USA  --------------------------')
t1  = time.time()
# After solving many problems, I am running out of problems I can brute force.
# I used to be ashamed of brute forcing, but these days I cherish the few remaining such problems.

def gcd (a, b):
    return b if a == 0 else gcd (b % a, a)

class frac:
    def __init__ (self, n, d):
        self.n, self.d = n, d
    def inv (self):
        return frac (self.d, self.n)
    def __add__ (self, other):
        a, b = self.n*other.d + self.d*other.n, self.d*other.d
        g = gcd (a, b)
        return frac (a//g, b//g)
    def __hash__ (self):
        return hash ((self.n, self.d))
    def __eq__ (self, other):
        return self.n == other.n and self.d == other.d
    def __repr__ (self):
        return str (self.n) + '/' + str (self.d)

k = 18+1
d = [ set () for _ in range (k) ]
d[1].add (frac (1, 1))
for i in range (1, len (d)-1):
    for j in range (1, (i+1)//2+1):
        for y in d[j]:
            for x in d[i+1-j]:
                d[i+1].add (x + y)
                d[i+1].add ((x.inv () + y.inv ()).inv ())
print (len (set (x for y in d for x in y))) # get rid of doubles

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 6,   --------------------------')
t1  = time.time()

def gcd (a, b):
    return b if a == 0 else gcd (b % a, a)

class frac:
    def __init__ (self, n, d):
        self.n, self.d = n, d
    def inv (self):
        return frac (self.d, self.n)
    def __add__ (self, other):
        a, b = self.n*other.d + self.d*other.n, self.d*other.d
        g = gcd (a, b)
        return frac (a//g, b//g)
    def __hash__ (self):
        return hash ((self.n, self.d))
    def __eq__ (self, other):
        return self.n == other.n and self.d == other.d
    def __repr__ (self):
        return str (self.n) + '/' + str (self.d)

k = 18+1
d = [ set () for _ in range (k) ]
d[1].add (frac (1, 1))
for i in range (1, len (d)-1):
    for j in range (1, (i+1)//2+1):
        for y in d[j]:
            for x in d[i+1-j]:
                d[i+1].add (x + y)
                d[i+1].add ((x.inv () + y.inv ()).inv ())
print (len (set (x for y in d for x in y))) # get rid of doubles

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

'''

print('\n--------------------------SOLUTION 7, OldCigarette, USA  --------------------------')
t1  = time.time()

# This one took me a while, my first solutions where really slow but I slowly got better ideas.
# My final solution is similar to ones already posted.
# The basic idea is that any circuit can be constructed out of two sub-circuits that are either in parallel or series.
# We don't actually care how these sub-circuits are constructed only their total capacitance and the number of capacitors
# required to make them. We can prune sub-optimal (circuits that take more capacitors then required to achieve a certain value).
# So this gives us a simple dynamic programming solution.
# I also added a custom fraction class to speed things up a bit with some tricks I saw on here.

import datetime
import fractions

class capfrac:
    def __init__(self, num, dem):
        gcd = fractions.gcd(num, dem)
        self.num = num // gcd
        self.dem = dem // gcd
    def __add__(self, c1):
        return capfrac(self.num*c1.dem + c1.num*self.dem, self.dem*c1.dem)
    def add_inv(self, c1):
        return capfrac(self.num*c1.num, self.dem*c1.num + c1.dem*self.num)
    def __eq__(self, c1):
        return self.num*c1.dem == c1.num*self.dem
    def __hash__(self):
        return self.num * 10000 + self.dem

C_val = capfrac(1,1)

def par(c1, c2):
    return c1+c2

def ser(c1, c2):
    return c1.add_inv(c2)

def add_circuit(circuits, found_circuits, new_circuit, count):
    if new_circuit in found_circuits:
        return
    circuits[count].append(new_circuit)
    found_circuits.add(new_circuit)

def generate_circuits(circuits, found_circuits, total_count):
    for count1 in range(1, total_count//2+1):
        count2 = total_count - count1
        for c1 in circuits[count1]:
            for c2 in circuits[count2]:
                add_circuit(circuits, found_circuits, ser(c1, c2), total_count)
                add_circuit(circuits, found_circuits, par(c1, c2), total_count)

def main():
    limit = 18
    circuits = [[] for i in range(0, limit+1)]
    found_circuits = set()
    found_circuits.add(C_val)
    circuits[1].append(C_val)
    for c in range(2, limit+1):
        generate_circuits(circuits, found_circuits, c)
        print('%s %s %s' % (c, len(found_circuits), datetime.datetime.now()))

main()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


