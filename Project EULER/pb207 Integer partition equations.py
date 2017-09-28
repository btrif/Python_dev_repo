#!/usr/bin/python                   o(^_^)o         ( ͡° ͜ʖ ͡°)
# © Solved by Bogdan Trif @
#The  Euler Project  https://projecteuler.net
'''
Integer partition equations     -       Problem 207

For some positive integers k, there exists an integer partition of the form   4**t = 2**t + k,
where 4t, 2t, and k are all positive integers and t is a real number.

The first two such partitions are 4**1 = 2**1 + 2 and 4**1.5849625... = 2**1.5849625... + 6.

Partitions where t is also an integer are called perfect.
For any m ≥ 1 let P(m) be the proportion of such partitions that are perfect with k ≤ m.
Thus P(6) = 1/2.

In the following table are listed some values of P(m)

   P(5) = 1/1
   P(10) = 1/2
   P(15) = 2/3
   P(20) = 1/2
   P(25) = 1/2
   P(30) = 2/5
   ...
   P(180) = 1/4
   P(185) = 3/13

Find the smallest m for which P(m) < 1/12345

'''
import time, math, gmpy2




# print('\n--------------------------TESTS------------------------------')
# t1  = time.time()
#
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n================  My FIRST SOLUTION,  2 sec without print ===============\n')
t1  = time.time()


# OBSERVATION : m must be perfect square !
def integer_partitions_equations(frac_lim) :
    epsilon = 1e-8
    tcnt, cnt = 0, 0
    i = 2
    r = 10**10
    while r >= gmpy2.mpq(1, frac_lim ) :
        m = i*i
        t = math.log(m, 4)
        a, b = 4**t, 2**t
        k = a - b
        cnt +=1
        k = round(k)
        if  abs( round(t) -t ) < epsilon :
            tcnt +=1
        r = gmpy2.mpq(tcnt, cnt)
        # print(i ,'  m=',m, '   k=', k,'       a=', a,  ' ==    b=' , b , '  +     t=', t , '     t_int=', tcnt , '  cnt=', cnt , '   ;  ratio=' , r )
        i+=1

    return print('\nSmallest m for which P(m) < 1/12345 :\t ', k)

# integer_partitions_equations(12345)                #       Smallest m for which P(m) < 1/12345 :	  44043947822

# @2017-09-26 - Ceva nu iese . Nu imi dau seama, what the fuck !


t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,6), 'ms\n\n')              #Completed in : 11313.64727 ms


print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1,   --------------------------')
t1  = time.time()

# === Mon, 8 May 2017, 21:44, gk121
# Simple solution in python

s,n = 0,1
while True:
    if n & (n + 1) == 0: s += 1
    if s/n < 1/12345: break
    n += 1
print("m = " + str(n*(n+1)))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 2,   --------------------------')
t1  = time.time()

# ==== Sun, 20 Aug 2017, 15:58, VicTheTurtle, France
# Only 0.0005 sec in Python !
# This is not a great technique, just a little trick.
# First I find like several people here a closed form formula for P.
# Then, to have an idea of how big is the solution, I implemented Newton (not sure if it is allowed with
# all the verifications with f', f'' etc but dichotomia was unacceptable since I had no upper bound) to solve
# the equation "f-1/12345=0" where I removed "int" in f so that f is continue...
# So it was like x=4.8*10**10. Then I just decided to let m=0.9x and suppose that before m, P is greater than 1/12345
# Because of discontinuity of "int", dichotomia is still impossible
# So I added blocks of powers of 10, starting with 10**9 (since I had now the approximate solution)
# If P(m+10**i) < 1/12345, then i <- i-1, else m <- m+10**i
# Until i=-1. m is now the greatest integer before P goes under 1/12345 : the solution is then m+1
# The implementation here does not show the Newton thing, and starts at m=0, i=10 (block=10**10 since solution < 4.8*10**10)
# so that I have to calculate less than 50 values of P

from math import log,sqrt
m=0
i=10
n = lambda m: (1+sqrt(1+4*m))//2 - 1
P = lambda m: int(log(n(m)+1.5,2))/n(m)
while i>=0:
    block=10**i
    while P(m+block)>=1/12345:
        m+=block
    i-=1
print(m+1)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

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
