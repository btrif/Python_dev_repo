#  Created by Bogdan Trif on 06-11-2017 , 12:30 PM.
# © o(^_^)o  Solved by Bogdan Trif  @       Completed on Tue, 7 Nov 2017, 13:14
#The  Euler Project  https://projecteuler.net
'''
                                Laserbeam           -           Problem 202

Three mirrors are arranged in the shape of an equilateral triangle, with their reflective surfaces pointing inwards.
There is an infinitesimal gap at each vertex of the triangle through which a laser beam may pass.

Label the vertices A, B and C. There are 2 ways in which a laser beam may enter vertex C, bounce off 11 surfaces,
then exit through the same vertex: one way is shown below; the other is the reverse of that.


There are 80840 ways in which a laser beam may enter vertex C,
bounce off 1000001 surfaces, then exit through the same vertex.

In how many ways can a laser beam enter at vertex C,
bounce off 12017639147 surfaces, then exit through the same vertex?


'''
import time, zzz

import sys


def gcd(a, b):      # GCD
    """Return greatest common divisor using Euclid's Algorithm."""
    while b:
        a, b = b, a % b
    return a

print('\n--------------------------TESTS------------------------------')
t1  = time.time()

# ===== MY IDEA, @2017-11-07
#models
# CAB   -   3, 9,  15, 21...            --> mod 6 +3        %6 =3
# ABC   -   5, 11, 17, 23, ...          --> mod 6 +5        %6 = 5
# BCA   -   1, 7, 13, 19, ...           --> mod 6  + 1       %6 = 1

#### STUDY CASE :
# reflections = 15        # 8+2 = 10 vertices = > no center => CABCABCABC -->0 1 2 3 4 5 6 7 8 9 indices (10 indices)
# indices for C = 0 ,3, 6, 9
# potential reflections 3, 6 =>
# to obtain rombs you do : 10-3-1 = 6 => (6, 3) but gcd (6,3) != 1 =>  UNvalid reflection


# ===== LINKS
# http://incompetech.com/graphpaper/triangle/


t2  = time.time()
print('\n# Completed in :', round((t2-t1) , 4 ), 's\n\n')

print('\n============  My FIRST SOLUTION, O(n/3),  SLOW,  20 min using pypy  ===============\n')
t1  = time.time()

def count_valid_reflections(reflections) :
    counter = 0
    vertices = (reflections+1) //2 +2
    #type
    Types = {1: 'BCA', 3 : 'CAB' , 5: 'ABC'  }
    type = Types[reflections%6]
    C_0 = type.find('C')
    Validate_Exit = lambda index, vertices : gcd(vertices-index-1, index)
    print('vertices= ', vertices,'      type: ', type, '    C_0 index = ', C_0 )
    if C_0 == 0 : index = 3
    else : index = C_0
    while index < vertices//2 :
        gcd_exit = Validate_Exit(index, vertices)
        print(str(index) +'          gcd_exit =  ' , gcd_exit ,'        Romb= ' ,( vertices-index-1, index ) )
        if gcd_exit == 1 :
            counter +=1

        if index %10**6 == 0 : sys.stdout.write('\r' + str(index) +'              '+  str(round((time.time() - t1),2)) +'  sec'   )   # Font Segoe UI Semibold

        index +=3

    print('\nValid reflections vertex C = ', counter*2)
    return counter*2


# count_valid_reflections(12017639147)          #Valid reflections vertex C = ', 1209002624
# count_valid_reflections(1000001)      #     Valid reflections vertex C =  80840
count_valid_reflections(1000003)



t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')


print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1,  INSTANT --------------------------')
t1  = time.time()

# ==== Fri, 5 Sep 2008, 22:27, soffer801, USA
# Beautiful! The grid was my first thought. I have done a lot of number theory,
# so the ideas were, though not obvious, easy to come by.
# It basically boiled down to factoring (N+3)/2, where N is the number of bounces.
# If you have seen the Euler Phi function, or Mobius Mu, knowledge of those help
# (though neither are directly used in my implementation).

import math

def getFactors(n,s):
    i=2
    while i<=n:
        if n%i==0:
            if i in s:
                s[i]+=1
            else:
                s[i]=1
            getFactors(n/i,s)
            break
        i+=1
    return s

def modInv3(n):
    if n%3==1:
        return (2*n+1)/3
    return (n+1)/3


def sign(n):
    if n==0:
        return 0
    return n/abs(n)

def cartesianCross(x,y):
    t=[]
    for xx in x:
        for yy in y:
            t+=[xx*yy]
    return t

x=(12017639147+3)/2
a=getFactors(x,{})

allFacts=[1]
for b in a:
    c=[1,-b]
    allFacts=cartesianCross(allFacts,c)
tot=0
for a in allFacts:
    tmp=((x-1)/3-modInv3(abs(a)))/abs(a)+1
    tmp*=sign(a)
    tot+=tmp
print (tot)

t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')


print('\n--------------------------SOLUTION 2,   --------------------------')
t1  = time.time()

# ==== Mon, 22 Sep 2008, 16:43, MrDrake, Australia
# Here's my code, runs in less than a second!

from math import sqrt

# limit = 12017639147
limit = 1000003

n = (limit + 3) / 2

factors = []

s = sqrt(n)
if int(s) == s: factors.append(s)

for i in range(1, int(s)):
    if n % i == 0:
        factors.append(i)
        factors.append(n / i)

factors.sort()

answers = {}

for f in factors:
	q = (f // 3) + (f % 3) - 1
	for g in factors:
		if g >= f: break
		if f % g == 0: q -= answers[g]
	answers[f] = q

print( answers[factors[-1]])

t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')


print('\n--------------------------SOLUTION 3,   Instant--------------------------')
t1  = time.time()


# ==== Sun, 18 Jan 2009, 21:31, tolstopuz, Russia
import itertools, functools, operator

n = (12017639147 + 3) // 2
f = [2, 5, 11, 17, 23, 29, 41, 47]

print(2 * sum((-1) ** sum(z) * ((n - 1) // 3 // functools.reduce(
    operator.mul, ((f[i] ** x) for i, x in enumerate(z)), 1))
              for z in itertools.product(range(0, 2), repeat = len(f))))

t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')


print('\n--------------------------SOLUTION 4, INSTANT, inclusion-exclusion Principle  --------------------------')
t1  = time.time()


# ==== Sat, 25 May 2013, 03:17, Hariram, India
# This was way more fun than the other laser and mirror problem(#144). Here is how I did it.
# To solve this problem, I created a 2D space with axis along CA and CB.
# This creates the whole reflected universe if we were inside this kaleidoscope.
# If (x, y) is a point on this plane, then C will correspond to all the points with (x-y) = 0 (mod 3).
# Suppose our beam starts from origin,
# then we need to find no of such positive (x, y) such that the line joining (0, 0) and (x, y) has the said number
# (let us refer to it as M). The line will pass through x-1 mirrors parallel to y-axis,
# y-1 mirrors parallel to x-axis and x+y-1 mirrors that are diagonal. So 2*(x+y)-3 = M. So x+y = (M-3)/2.
#
# We have (M-3)/2 = 6008819575 (let us call this c)
# But if x and y are not co-prime, this line would pass through another vertex (x/g, y/g)
# (here g is a common factor) before reaching (x, y).
# So gcd(x,y) = 1.
# This can be stated as gcd(x, c) = 1
#
# In simplified terms we need to find
# #{x| 1<x<c; gcd(x, c) == 1; [x - (c-x)] = 0 (mod 3)}
# The 3rd condition can be restated as x = 2c (mod 3)
#
# c has factors 5, 11, 17, 23, 29, 41, 47. (All are 3k+2 form. chosen to make the problem tricky)
# I first calculated the number x in the given range that are 2c (mod 3).
# By inclusion exclusion principle, I subtracted those x that are multiples of one of the factors of c.
# Then added no. of those x which are a multiple of 2 factors of c and so on.
#
# Here is the code in Python


c = 6008819575
f = [5,11,17,23,29,41,47]

t = f[:]
od=f[:]
ev=[1]

for i in range(6):
    t = [j*k for j in t for k in f if j%k != 0]
    if i%2 == 0:
        ev.extend(t)
    else:
        od.extend(t)
ev = set(ev)
od = set(od)
r = 3 - c%3
def nof(c, f, r):
    """ Returns no. of values of x s.t.
    0<x<f
    f|x
    x%3 = r%3
    """
    r = (r-1)%3 + 1
    if f%3 == 0:
        if r%3 == 0: return (c-1)//f
        else: return 0
    if f%3 == 2: r = 3 - r%3
    return (c-f*r-1)//(3*f)+1

s = 0
for i in ev:
    s += nof(c, i, r)
for i in od:
    s -= nof(c, i, r)

print (s)


t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')


print('\n--------------------------SOLUTION 5,   --------------------------')
t1  = time.time()

# === Tue, 11 Mar 2014, 10:55, ChopinPlover, Taiwan
# Find pattern and count in smart way (as Problem 1):
# (1) 2a + 2b - 3 = n
# (2) gcd(a, b) = 1
# (3) a = b (mod 3)
#
# It is my first time using vim to write my program :p

import itertools
import sys

class Problem():
    def __init__(self):
        self.primes = []
        self._init_primes()

    def solve(self):
        print(self.get_way_count(11))
        print(self.get_way_count(1000001))
        print(self.get_way_count(12017639147))

    def get_way_count(self, surface_count):
        assert(surface_count % 2 == 1)
        n = (surface_count + 3) // 2
        assert(n % 3 == 1)
        factors = self._get_prime_factors(n)

        count = (n - 2) // 3 + 1
        for multiply in self._get_factor_multiplies(factors):
            if multiply[1]:
                count -= self._get_multiply_count(n, multiply[0])
            else:
                count += self._get_multiply_count(n, multiply[0])
        return count

    def _get_factor_multiplies(self, factors):
        rv = []
        n = len(factors)
        for i in range(1, n + 1):
            for factor_subset in itertools.combinations(factors, i):
                x = 1
                for j in factor_subset:
                    x *= j
                rv.append([x, len(factor_subset) % 2 == 1])
        return rv

    def _get_multiply_count(self, n, multiply):
        first_k = None
        if multiply % 3 == 1:
            first_k = (multiply * 2 - 2) // 3
        elif multiply % 3 == 2:
            first_k = (multiply - 2) // 3
        last_k = (n - 2) // 3
        last_k = first_k + ((last_k - first_k) // multiply) * multiply
        return (last_k - first_k) // multiply + 1

    def _init_primes(self):
        SIEVE_RANGE = 80000
        sieve_visited = [False] * SIEVE_RANGE
        sieve_visited[0] = sieve_visited[1] = True
        for i in range(2, SIEVE_RANGE):
            if sieve_visited[i] is False:
                self.primes.append(i)
                for j in range(i + i, SIEVE_RANGE, i):
                    sieve_visited[j] = True

    def _get_prime_factors(self, n):
        factors = []
        d = n
        for i in range(len(self.primes)):
            if d == 1:
                break
            p = self.primes[i]
            if d < p**2:
                break
            if d % p == 0:
                while d % p == 0:
                    d = d // p
                factors.append(p)
        if d > 1:
            factors.append(d)
        return factors

def main4():
    problem = Problem()
    problem.solve()

main4()

t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')


print('\n--------------------------SOLUTION 6,  Vizualization program --------------------------')
t1  = time.time()

# ==== Thu, 24 Aug 2017, 17:30, martin_b, Czeck Republique
# I wrote a small visualisation program in python that shows the beam path.
# It was not of much use after all but at least got me started.


import matplotlib.pyplot as plt
import math
import numpy as np

epsilon, side = 1e-8, 1 / math.tan(math.radians(60))
# start x, start y, end x, slope, offset, angle
walls = (
    # top wall
    (-side, 1, side, 0, 1, math.radians(180)),
    # left wall
    (-side, 1, 0, math.tan(math.radians(300)), 0, math.radians(300)),
    # right wall
    (0, 0, side, math.tan(math.radians(60)), 0, math.radians(60))
)

def reflect(ray):
    for wi, w in enumerate(walls):
        m = math.tan(math.radians(90) - ray[0])
        n = ray[2] - m * ray[1]
        if wi != ray[3]:
            d = m - w[3]
            if abs(d) > epsilon:
                x = (w[4] - n) / d
                if x > w[0] and x < w[2]:
                    na = (w[5] - ray[0]) % (2 * math.pi)
                    return (na, x, m * x + n, wi)

def raycast(inputs, max_reflections=20):
    # paint triangle and axes
    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.plot((-side, 0, side, -side), (1, 0, 1, 1),
             color="black", linewidth=1.0)
    for index, input in enumerate(inputs):
        if isinstance(input, tuple):
            angle = 90 - math.degrees(math.atan(input[0] / (input[1] * side)))
        else:
            angle = input
        # ray angle, x, y, wall
        ray = (math.radians(angle), 0, 0, 1)
        for i in range(max_reflections):
            nr = reflect(ray)
            if nr:
                plt.plot((ray[1], nr[1]), (ray[2], nr[2]),
                         color=plt.cm.RdYlBu(index / len(inputs)), linewidth=1.0)
                ray = nr
            else:
                print(angle, "No intersection",)
                break
            if abs(ray[1]) < epsilon and abs(ray[2]) < epsilon:
                print(angle, "Got out", i)
                break
        else:
            print(angle, "Still inside")
    plt.show()

# if __name__ == '__main__':
    # input either tuple of height,offset or angle in degrees
    # raycast([(11, 3), (11, 6), 10], 100)

t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')




print('\n--------------------------SOLUTION 7,   --------------------------')
t1  = time.time()


t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')


print('\n--------------------------SOLUTION 8,   Instant,  inclusion-exclusion  --------------------------')
t1  = time.time()

# ==== Thu, 2 Apr 2009, 12:03, Whatang, Wales
# All,my first post on here :)
#
# My solution proceeds similar to what most have said.
# I calculated the number of possible beams,
# then used inclusion-exclusion to count those which shared some prime factor with (R+3)/2


import math

def multiplesInSequence(start,end,factor,step):
    # Return the number of elements of the arithmetic sequence start +
    # step * i which are <=end and which are divisible by factor
    x=start//factor
    x*=factor
    if x < start: x+=factor
    while (x-start) % step != 0 and x<end: x+=factor
    if x> end: return 0
    if x == end: return 1
    y=x+factor
    i=1
    while (y-x) % step != 0 and y<=end:
        y+=factor
        i+=1
    if y>end:
        return i-1
    return 1 + (end-x)//(factor*i)

def permuteItems(iterable):
    l=list(iterable)
    current=[]
    perms=[]
    recPerm(current,l,perms)
    return perms

def recPerm(current,items,perms):
    if len(items)==1:
        current.append(items[0])
        perms.append(list(current))
        current.pop()
        perms.append(list(current))
    else:
        current.append(items[0])
        recPerm(current,items[1:],perms)
        current.pop()
        recPerm(current,items[1:],perms)

def findSmallPrimeDivisors(t):
    primes=set()
    if t & 1 == 0:
        primes.add(2)
        t//=2
    top=1+int(math.sqrt(t))
    for n in range(3,top,2):
        if t % n == 0:
            residues=set((n % p for p in primes))
            if 0 not in residues: primes.add(n)
    return primes

def findPrimeDivisors(t):
    if t==1: return set()
    primes=findSmallPrimeDivisors(t)
    if len(primes)==0:
        primes.add(t)
    else:
        x=t
        for p in primes:
            while x % p ==0: x//=p
        primes=primes.union(findPrimeDivisors(x))
    return primes

def countPaths(R):
    if R&1==0: return 0
    end=(R+3)//2
    start=(R+3)//4
    sum=end
    m3=end % 3
    if m3==1: end-=2
    elif m3==2: end-=1
    else: return 0
    if sum & 1 == 0:
        step=6
        if end & 1 ==0: end -=3
    else:
        step=3
    numsteps=1+(end-start)//step
    primes=findPrimeDivisors(sum)
    if 2 in primes: primes.remove(2)
    primes=list(primes)
    primes.sort()
    # Begin with the number of steps in the sequence start + step * i
    # which are <= end
    count=numsteps
    # Now use inclusion-exclusion to count the number of elements of
    # the sequence which are divisible by some factor of sum
    for primeSet in permuteItems(primes):
        m=1
        for p in primeSet: m*=p
        if m==1: continue
        n=multiplesInSequence(start,end,m,step)
        if len(primeSet) & 1 == 0: count +=n
        else: count-=n
    return 2 * count



print(countPaths(11))
print(countPaths(1000001))
print(countPaths(12017639147))

t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')



# print('\n--------------------------SOLUTION 9,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 10,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 11,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 12,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')




