#!/usr/bin/python
# Solved by Bogdan Trif @       Completed on Mon, 20 Mar 2017, 21:02
#The  Euler Project  https://projecteuler.net
'''
                        Exploring Pascal's triangle     -       Problem 148

We can easily verify that none of the entries in the first seven rows of Pascal's triangle are divisible by 7:


                                                                1
                                                            1     1
                                                         1     2     1
                                                      1     3     3     1
                                                   1     4     6     4     1
                                                1     5    10   10    5     1
                                            1     6    15    20    15    6    1
                                         1     7   21    35    35    21   7     1


However, if we check the first one hundred rows, we will find that only 2361 of the 5050 entries are not divisible by 7.

Find the number of entries which are not divisible by 7 in the first one billion (10**9) rows of Pascal's triangle.


'''

import copy
import time
from math import sqrt, log, floor
from pyprimes import factorise
import functools, operator

def prime_generator(lower, upper):      ### o(^_^)o  FASTEST  o(^_^)o  ###  HIghly Efficient !!!
    """  Sieve of Eratosthenes              !!!!!!!!! THE FASTEST SIEVE. It won the battle with sieve
    Create a candidate list within which non-primes will be marked as None.         """
    cand = [i for i in range(3, upper + 1, 2)]
    end = int(upper ** 0.5) // 2

    # Loop over candidates (cand), marking out each multiple.
    for i in range(end):
        if cand[i]:
            cand[cand[i] + i::cand[i]] = [None] * ( (upper // cand[i]) - (upper // (2 * cand[i])) - 1 )

    # Filter out non-primes and return the list.
    return [2] + [ i for i in cand if i and i > lower ]


def get_factors(n):       ### o(^_^)o  FASTEST  o(^_^)o  ###
    ''' Decompose a factor in its prime factors. This function uses the pyprimes module. THE FASTEST  '''

    return [val for sublist in [[i[0]]*i[1] for i in factorise(n)] for val in sublist]

def generate_Pascal_Triangle(row_nr) :
    '''**©** Made by Bogdan Trif @ 2016-12-20, 21:20.

        :Description: Generates the Pascal Triangle , Binomial Coefficients
        :param row_nr: int, the row number, int
        :return: nested list, matrix in the form of Pascal's Triangle       '''
    blueprint = [1]*(row_nr+1)
    Pascal= [blueprint]
    for i in range(row_nr) :
        tmp=[]
        for j in range(0, row_nr-i) :
            tmp.append(sum(Pascal[-1][0:j+1]) )
        # print(tmp)
        Pascal.append(tmp)
    return Pascal


def non_sevens_mechanically(row_nr):
    ''':Description : counts the number of factors not divisible with 7 number within the Pascal Triangle.
    :Observation:  It depends on the function    generate_Pascal_Triangle
        VERY SLOW     but is sure              '''
    Pascal = generate_Pascal_Triangle(row_nr-1)
    cnt = 0
    L = [val for sublist in Pascal for val in sublist]
    for n in L:
        if n %7 != 0 :
            cnt+= 1
    return cnt

def non_sevens_1(rows) :        #  @2017-03-20, 21:00  Other idea which I did not finish --> I was close at that time, but left it
    from math import log, floor
    L = [28**i for i in range(0,8)]
    # print('The leveles of Pascal s Triangle :\n' ,L,'\n')
    S = 0
    l = floor(log(rows, 7))
    c_th = rows//7**(l)    # Complete nr of rows
    comp = c_th*(c_th+1)//2     # complete in triangular
    c = comp * L[l]
    i_th = rows - c_th* 7**(l)  # incomplete rows
    inc = (c_th+1)* i_th*(i_th+1)//2
    # print('l =',l  , ' c_th, comp=',c_th,comp,' c=',c ,'; i_th,incomp=',i_th,inc)
    S += c + inc

    return S

def non_sevens(rows):  # The Main Function and CORRECT solution to the problem 148
    '''**©** Made by Bogdan Trif @ 2017-03-20, 21:00.
        :Description: ALGORITHM to Count the number of factors NOT divisible by 7 in the Pascal Triangle.
    :param row_nr: int, the row number of the Pascal's Triangle
    :return: int, the number of factors NOT divisible with 7       '''

    from math import log, floor
    l = floor(log(rows, 7))
    L = [28**i for i in range(0, l+1) ]
    # print('The levels of Pascal s Triangle :\n' ,L)

    M = []
    for i in range(l, 0,-1):
        coeff = rows//7**i
        rows = rows - coeff*7**i
#         print(i,7**i,rows, coeff, end= ' ;  ')
        M.append(coeff)

    M = M+[rows]
#     print(M)
    m = len(M)
    c = 1
    S  = L[m-1] * M[0]*(M[0]+1)//2
    # print('len=',m,'; M=',M,'; S=',S,'; c=',c)
    for j in range(1,m):
        c *= M[j-1]+1
        t = M[j]*(M[j]+1)//2
        # print(L[m-j-1], M[j] , 'c=',c, L[m-j-1]*M[j],'t=',t, c*L[m-j-1]*t)
        S += c*L[m-j-1]*t

    return S


def non_sevens_rec(rows) :      # !!! @2017-03-20, 20:37 - NOT Finished !!! Recursion not implemented
    from math import log, floor
    L = [28**i for i in range(0,8)]
    print('The levels of Pascal s Triangle :\n' ,L,'\n')
    S = 0
    l = floor(log(rows, 7))
    if log(rows, 7) %1 ==0 : return L[l]

    c_th = rows//7**(l)    # Complete nr of main rows
    comp = c_th*(c_th+1)//2     # complete in triangular
    c = comp * L[l]

    i_th = rows - c_th* 7**(l)  # incomplete rows
    inc = (c_th+1)* i_th*(i_th+1)//2   #   8 * 9 = 72 !!!! for 57 --> correct result = 60
    print('l =',l  , ' c_th=',c_th, ', compl=',comp,' c=',c ,'; i_th=',i_th,', incompl=',inc)
#     S += c + inc
    return c + inc



print('\n--------------------------TESTS------------------------------')
t1  = time.time()

print( 'Math Log 7 Test : \t' , log(10**9, 7 ))
print( 'Math Modulo 343 Test : \t' , 1000%343   )
print('\n--------------------------TESTS------------------------------')

# t1  = time.time()
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1),6), 's')

#### MECHANICAL COUNT FUNCTION CONSTRUCTION
# row_nr =  1000
# Pasc = generate_Pascal_Triangle(row_nr-1)
#
# # for i in range(len(Pasc)) :
# #     print(Pasc[i] )
#
# Se7en = copy.deepcopy(Pasc)
#
# for i in range(len(Se7en)):
#     for j in range(len(Se7en[i])):
#         if (Se7en[i][j]) %7 == 0 :
#             Se7en[i][j] = 7
#         else : Se7en[i][j] = 0
#
#
# # filename = "pb150 blueprint.txt"
# # f = open(filename, "w")
# # for i in range(len(Se7en)) :
#     # f.write( str( Se7en[i])+'\n' )
#     # print(Se7en[i] )
#
# L = [val for sublist in Pasc for val in sublist]
# # print(L, sum(L),'\n')
#
# cnt = 0
# for n in L:
#     if n %7 != 0 :
#         cnt+= 1
#         # print(n, end=' ,  ' )
# print('\nNumber of NON-Sevens :\t',cnt)

# S=0
def get_non_sevens(row_nr) :
    m = log(row_nr, 7)
    i = floor(m)
    print(m, i, end='    ')
    if m <= 1 :
        return (row_nr*(row_nr+1))//2
    elif m > 1 :
        a = row_nr // (7**i)
        b = row_nr%(7**i)
        print('(a, b)=' , a, b)
        A = (a*(a+1)//2)* get_non_sevens(row_nr - 7)
        print(A)
        if (a/7) %1 ==0 or b!= 0 :
            B = (a+1) * get_non_sevens(b)
            A+=B
    return A

# print('\n MAIN TEST for the Function get_non_sevens :\t', get_non_sevens(row_nr))

# m = math.log(row_nr)
# i = math.floor(m)


def non_sevens_firs(rows ) :        # Not Finished !!!!
    L = [28**i for i in range(1,11)]
    print('The leveles of Pascal s Triangle :\n' ,L,'\n')

    Suma = 0
    F , J =[], []

    while rows > 7  :
        m = log(rows, 7)
        i = floor(m)
        full_units = rows//(7**i)
        inc_units = rows %(7**i)
        F.append(full_units)
        o = L[i-1]*(full_units*(full_units+1))/2
        Suma += o
        k = (inc_units+1)* (L[i-1]*(inc_units*(inc_units+1)/2)/L[i-1] )
        Suma += k
        print(str(i)+'.   ' , full_units ,'\t' , rows ,'\t'*2 ,inc_units ,'\t'*2  ,round(m,3),'\t'*2 , F ,'\t'*2 ,L[i-1],'    \tSuma=' ,Suma, '\tk=',k,'\to=' ,o)
        rows = rows % (7**i)

    return print('\nTotal Sum: ', int(Suma))


print('--------  Testing the manual and the automatic functions  --------\n')

def automated_test():
    cnt =0
    for i in range(1, 200):
        if non_sevens_mechanically(i) != non_sevens(i) :
            cnt+=1
            print(str(i)+ '.     mechanical =' , non_sevens_mechanically(i), non_sevens(i), '   <- function',  )
    if cnt == 0 :   print('CONGRATULATIONS ! Your function works fine !!! ')

# automated_test()

# rows = 7**3
# print('\nManual Test for   ' +str(rows)+ ' \t = \t'  , non_sevens_mechanically(rows) )
print('----------------\n')

# @ 2016-12-22, 11:48
# I am close to the solution, need to fix the coefficients :
# Full is always sum[i] : example : sum(2)=3, sum(4)=10
# Partial is always only the second term and is
# # 3*L2 + 63*L1 + 63*L0 + 63* 21   This is VERY CORRECT
# 3*28**3+63*(28**2+28+21)


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n================  My FIRST SOLUTION,    FASTEST Algorithm , 0 ms  ===============\n')
t1  = time.time()

# It seems that my algorithm is the fastest from the Euler site. I use only length of the number iterations

res = non_sevens(10**100)
print('\nAnswer : \t', res )            #   Answer : 	 2129970655314432


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*10**6, 6), 'μs\n\n')          #  Completed in : 0.0 ms


print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1,  SIERPINSKi  TRIANGLE  --------------------------')
t1  = time.time()

# === Fri, 23 Dec 2016, 09:10, mbh038, England
# Less than 0.1 ms in Python (and less than 0.2 ms for 10**451045 rows), without using recursion.
# I really enjoyed this. By using brute force Python code on small row numbers, and this function in Mathematica
# http://www.oftenpaper.net/sierpinski.htm
# (based on one I found here) to draw a Sierpinski triangle mod m, I pieced together the way this works.
# I write the row number in the base we are interested in, then take each digit, starting with the highest power,
# and work my way down the self-similar structure, taking into account the number of branch points
# as we descend to each new digit. The code works for any base up to the limit imposed by numpy.

import numpy as np
import time

def p148(n,base=7):
    t=time.clock()
    s=str(np.base_repr(n,base))
    m=sum([x for x in range(1,base+1)])
    bsum=0
    smult=1
    for i in range(len(s)):
        if i>0:
            smult*=(int(s[i-1])+1)
        bsum+=m**(len(s)-i-1)*smult*sum([x for x in range(int(s[i])+1)])
    print(bsum,time.clock()-t)

#for exploratory work - small row numbers only!
def p148bf(n,base=7):
    t=time.clock()
    sum7=0
    for i in range(n):
        sum7+=np.prod([int(x)+1 for x in str(np.base_repr(i,base))])
    print(n,sum7,time.clock()-t)
    return sum7

#returns number of odd numbers mod n in first m rows
#sum([sum([nCk(y,x)%n!=0 for x in range(y+1)]) for y in range(m)])

p148(10**9)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 2, VERY FAST , Interesting, must study it ! --------------------------')
t1  = time.time()

# === Wed, 14 Dec 2016, 03:43, sO3SrLCr4Rqb00Zr..., Japan
# Like others, I saw this was a Sierpenski triangle (or something very similar to that),
# and then wrote a recursion to solve that solves in O(log(n)).
#
# Solves for 10**45 in 62ms in pure python (of which I'm sure 99.99% of the time is just setting up the python environment).
# After that I start running into the recursion limit.  No matter how you look at it, it's fast

from functools import lru_cache
import itertools

modme = 7
N = 10**45


def main(N):
    div = solve_by_powers(N)
    cells = triangle(N)
    not_div = cells - div
    print(cells, "cells total")
    print(div, "divisible by", modme)
    print(not_div, "not divisible by", modme)


def triangle(width):
    # 1+2+3+4+5+6+...width
    return width*(width+1)//2


def cutoff_triangle(width, height):
    return triangle(width) - triangle(width-height)

@lru_cache(None)
def solve_by_powers(N):
    if N <= modme:
        return 0
    for modme_power in itertools.count(2):
        if N <= modme**modme_power:
            layer_break = modme**(modme_power-1)
            depth = (N-1) % layer_break + 1
            prev_layer = N - depth
            to_this_layer = solve_by_powers(prev_layer)
            side_triangles = (N-1) // layer_break + 1
            zero_triangles = (N-1) // layer_break
            side_triangles_zeros = side_triangles * solve_by_powers(depth)
            zero_tri_width = layer_break - 1
            zero_tri_height = depth
            zero_triangles_zeros = zero_triangles * cutoff_triangle(zero_tri_width, zero_tri_height)
            return to_this_layer + side_triangles_zeros + zero_triangles_zeros

main(10**9)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n-------------SOLUTION 3, THE RECURSION similar to what I wanted to implement in the first place, BRAVO Khalid !!!  ----------')
t1  = time.time()

# ==== Sat, 10 Dec 2016, 21:11, Khalid, Saudi Arabia
# This one gave me a hard time. I saw the pattern pretty easily,
# but writing a fast algorithm that takes care of the pattern proved illusive.
# Then I decided to write out a recursive algorithm that does the partial solution, and it worked!
# And the algorithm is quick, it runs in less than a millisecond.

from math import log

def get_triangle(p, power):
    return sum(range(p+1))**power

def calc_triangle_partial(p, rows, power = None):
    if power is None:
        power = int(log(rows, p)) + 1
    step = p**(power - 1)
    prev_triangle = get_triangle(p, power-1)
    sum = 0
    i = 1
    while step * i <= rows:
        sum += i * prev_triangle
        i += 1
    remaining = rows - (step * (i - 1))
    if remaining > 0:
        power -= 1
        return sum + (rows // p**power + 1) * calc_triangle_partial(p, remaining, power)
    return sum

print (calc_triangle_partial(7, 10**9))


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 4, Sierpinsky, Similar to mine  --------------------------')
t1  = time.time()

# ===== Mon, 3 Oct 2016, 05:35, Sandamnit, USA
# Noticed the Sierpinski Triangle pattern after drawing it out by hand for p=2,
# after which it was a matter of just writing out 10**9 in base-7 and getting to work.
# There's certainly a more elegant way of doing this (as pointed out with the carries method) ' \
#      'but this runs in about 44ms on my machine, so I'm fairly pleased with it.

N = 10**9
k, p = 0, 7
factor = p*(p+1)//2

pows = []
while True:
   value = p**k
   if value > N: break
   pows = [value] + pows
   k += 1

coeffs = []
for k in range(len(pows)):
   coeffs += [N//pows[k]]
   N -= pows[k]*coeffs[-1]

total = 0
mult = 1
for k in range(len(pows)):
   e = len(pows)-k-1
   total += mult * factor**e * coeffs[k]*(coeffs[k]+1)//2
   mult *= (coeffs[k]+1)

print(total)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 5, RECURSION  --------------------------')
t1  = time.time()

# ==== Tue, 12 Jan 2016, 10:35, spacewolf009, Australia
# Identified the pattern, used simple recursion for the result.

def pascals_triangle(rows, base=1, mod=7):
    counter = 0
    if rows <= mod:
        for y in range(rows):
            row = []
            for x in range(y + 1):
                n = (base if x == 0 or x == y else (prev[x-1] + prev[x])) % mod
                row.append(n)
                if n != 0:
                    counter += 1
            prev = row
    else:
        top = pascals_triangle(mod, 1, mod)
        i, r, size = 1, 0, mod
        while r + size < rows:
            counter += i * top
            r += size
            i += 1
            if i == mod + 1:
                i, top = 2, counter
                size *= mod
        counter += i * pascals_triangle(rows - r, 1, mod)
    return counter

print (pascals_triangle(10**9))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n------------------ SOLUTION 6, VERY Interest Approach , RECURSION  ----------------------')
t1  = time.time()

# ====Sun, 22 May 2016, 04:19, azax1, USA
# Think about the rows of Pascal's triangle modulo 7. The first 7 rows are as given in the problem '
# (or at least, after you take them mod 7 they are); the 7th row collapses into 1,0,0,0,0,0,0,1.
# The original 11 in the n=0n=0 row seeded a tree of numbers 7∗82/28=28 large not divisible by 7,
# so each of the ones on either end of this new row is also the root of a new tree.
# ....

def f(n):
    if len(n) == 1:
        return (int(n) + 1) * (int(n) + 2) / 2
    v = int(n[0])
    return ((v * (v + 1)) / 2) * 28**(len(n) - 1) + (v + 1) * f(n[1:])

count = f("33531600615")            # 10^9 - 1 in base 7

print (count)


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 7,  Nice RECURSION  --------------------------')
t1  = time.time()

# ===Mon, 20 Jun 2016, 21:57, poposon
# Awesome problem. Found pattern by printing the first ~70 rows.
# Next was writing a recurrence relation to solve it in a divide-and-conquer fashion.

from math import log

def S(n):
    """ Sum of natural numbers up to and including n. """
    return n*(n+1)//2

def V(z, p):
    """
    Calculates number of non-divisible numbers in the triangle up to and
    including row z*7**p.

    Input:
        p: an exponent of 7
        z: coefficient, 1 < z < 7

    From pattern inspection we know,
        V(1)  = S(1) = 1
        V(7)  = S(7) = 28
        V(49) = 28*V(7) = 28**2
    So we can induce:
        V(7**n) = 28 * V(7**(n-1))
                = 28**n

    Furthermore we know that for any integer constant 1 < z < 7, the expression
        V(z * 7**n) = S(z) * V(7**n)
    is true (can be induced from pattern).
    """
    return S(z)*28**p


def solve(n):
    """
    Strategy

    With V, one can calculate the number non-divisible numbers in the
    triangle easily, for powers of 7 multiplied by a coefficient. Let's call
    such a number c.

    Find the largest c that fits within the questioned size, add V(c) to the
    result, and recurse for the remaining part r = n - c.

    If we hit the bottom and there are no whole triangles left, calculate
    partial values, which are simply S(n).
    """

    # calculate largest 7**p that fits in n.
    p = int(log(n, 7))

    # calculate largest coefficient z such that z*7**p < n
    z = n//7**p
    c = z*7**p

    r = n - c  # the remaining part

    # we don't have whole triangles left, only partial ones.
    if p <= 0:
        return S(n)

    ans = V(z, p)
    ans += solve(r) * (z+1) # The remaining part has one extra triangle.

    return ans


t = 1000000000
print (solve(t))


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 8,   --------------------------')
t1  = time.time()

# === Tue, 10 Jun 2014, 02:28, muffoosta
# I first though I had a nice solution by simply multiplying the digits (+1) of the row number in base 7.
# But luckily the upper bound of the problem forced me to make a better solution, runs instantly.

t, m, b, l = 0, 1, 7, 10 ** 100
for d in range(int(log(l) / log(b)), -1, -1):
    i = l // (b ** d)
    t += ((b * (b + 1) // 2) ** d) * i * (i + 1) // 2 * m
    l -= i * (b ** d)
    m *= i + 1
print(t)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 9,  very short --------------------------')
t1  = time.time()


n, c, r = 10 ** 9, 0, 0
while n:
  d = n % 7
  r = ((d * (d + 1)) >> 1) * 28 ** c + (d + 1) * r
  c += 1
  n //= 7
print (r)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 10,   --------------------------')
t1  = time.time()

# ==== Mon, 1 Jul 2013, 08:11, rendon, Mexico
# I've formulated a recursive function from the observed pattern in the first 1000 rows.

def notdiv7(rows):
  if rows <= 6:
    return rows * (rows + 1) / 2
  power = 1
  while power * 7 <= rows:
    power *= 7
  n = 1
  while (power * (n + 1)) <= rows:
    n += 1
  tr = n * (n + 1) // 2
  ans = tr * notdiv7(power - 1) + tr * power
  ans += (n + 1) * notdiv7(rows - power * n)
  return ans

print (notdiv7(10**9))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 11,  Interesting --------------------------')
t1  = time.time()

def change_base(n, p=7):
    """ Returns a list with the coeficients of 'n' in base 'p' """
    l = []
    while n != 0:
        l.append(n % p)
        n //= p
    l.reverse()
    return l

def G(l, p=7):
    """ Calculates the number of elements in the Pascal
        Triangle not multiple to 'p' until the 'l' line. """
    k = len(l)
    if k == 0:
        return 0
    k -= 1
    a = l[0]
    return (p*(p+1)//2)**k * a*(a + 1) // 2 + (a + 1) * G(l[1:], p)

print(G(change_base(10**9)))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 12, RECURSION  --------------------------')
t1  = time.time()

def triangle(n):
    if n < 7:
        return n*(n + 1)//2
    if n//7 < 7:
        return 14*(n//7)*(n//7 + 1)
    else:
        return 28*triangle(n//7)


def main(rows):
    non_divisible = 0
    numtriangles = 1
    remaining = rows
    k = 7
    while k <= rows:
        k *= 7
    while remaining > 0:
        non_divisible += numtriangles * triangle(remaining)
        while k > remaining:
            k = k // 7
        numtriangles *= (1 + remaining // k)
        remaining -= k * (remaining // k)
    return non_divisible

print(main(10**9))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 13, RECURSION  --------------------------')
t1  = time.time()

# === Mon, 6 May 2013, 08:56, jbum, USA
# I visualized it first in Processing, and saw the Sierpinski triangle.  Then produced this code to fill it.

from math import ceil,log

def countTri(rows):
  p = int(ceil(log(rows)/log(7)))
  # print( " >",p,rows)
  tot = 0
  if p == 1:
    return 28 if rows > 28 else rows*(rows+1)//2
  else:
    lo = 0
    p7 = 7**(p-1)
    for n in range(1,8):
      if rows > p7*n:
        tot += n*28**(p-1)
        lo = p7*n
      else:
        tot += n*countTri(rows-lo)
        break
  return tot

print (countTri(10**9))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


