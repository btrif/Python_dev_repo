#!/usr/bin/python                   o(^_^)o         ( ͡° ͜ʖ ͡°)
# © Solved by Bogdan Trif @     Completed on Sat, 23 Sep 2017, 19:27
#The  Euler Project  https://projecteuler.net
'''
            Nim         -           Problem 301

Nim is a game played with heaps of stones, where two players take it in turn to remove
any number of stones from any heap until no stones remain.

We'll consider the three-heap normal-play version of Nim, which works as follows:
- At the start of the game there are three heaps of stones.
- On his turn the player removes any positive number of stones from any single heap.
- The first player unable to move (because no stones remain) loses.

If (n1,n2,n3) indicates a Nim position consisting of heaps of size n1, n2 and n3 then there is a simple function
X(n1,n2,n3) — that you may look up or attempt to deduce for yourself — that returns:

zero if, with perfect strategy, the player about to move will eventually lose; or
non-zero if, with perfect strategy, the player about to move will eventually win.
For example X(1,2,3) = 0 because, no matter what the current player does,
his opponent can respond with a move that leaves two heaps of equal size,
at which point every move by the current player can be mirrored by his opponent
until no stones remain; so the current player loses. To illustrate:
- current player moves to (1,2,1)
- opponent moves to (1,0,1)
- current player moves to (0,0,1)
- opponent moves to (0,0,0), and so wins.

For how many positive integers n ≤ 230 does X(n,2n,3n) = 0 ?

'''
import time, zzz

# === LINKS
#
# http://www.archimedes-lab.org/How_to_Solve/Win_at_Nim.html
# https://stackoverflow.com/questions/1991380/what-does-the-operator-do-in-java
# https://plus.maths.org/content/play-win-nim

X = lambda i : (i)^(2*i)^(3*i)

print('\n--------------------------TESTS------------------------------')
t1  = time.time()

# JUST BRUTE FORCE - NO IMPROVEMENTS !
def Brute_Force_Nim(lim) :
    cnt = 0
    for i in range(1, 2**lim +1):
        if X(i) == 0 :
            cnt +=1
        print(str(i)+'.        ',  i , 2*i , 3*i   ,'      ' ,bin(i) , bin(2*i) , bin(3*i) , '          = ',X(i)   )
    return print('\n Loosing Configurations : \t',  cnt )

Brute_Force_Nim(10)         #   Loosing configurations : 2178309


t2  = time.time()
print('\nCompleted in :', round((t2-t1) , 2), 's\n\n')      #   Completed in : 599.736 s

print('\n================  My FIRST SOLUTION,   ===============\n')
t1  = time.time()

# OBSERVATION






t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


# === GENERAL IDEA

# After doing some research about Nim Game, it results that if (A XOR B) XOR C is zero, the first player will always lose.
#
# We know that B = 2A, and it has the same bits but shifted to left, and A XOR B must be equal to C.
# That is only possible if A doesn't contain two consecutive 1's in its binary representation.
#
# So basically we must find all numbers that doesn't contains two consecutive ones in its binary representation using 30 bits.
# This is a famous problem :)

# === Sun, 30 Oct 2016, 17:04, armul, Guernsey
# Like the fact that this problem can be BF'd by keen BFers, but with analysis simplifies right down to a cool sequence.
# That is what maths is all about - taking computable stuff and spotting the patterns.
#
# A couple of comments. Lots of lovely mathematical explanations and proofs,
# but wanted to add some simpler demonstrations for the more visual of us:
#
# No consecutive ones
# If there are blocks of 1s then we can actually see what happens if we write it out:
#
# Pair:
# n XOR 2n    = -0110- XOR 0110-- = -101--
# 3n = n + 2n = -0110- + 0110--   = -001--
# so n XOR 2n XOR 3n  = -100--
#
# Triple:
# -01110- XOR 01110-- = -1001--
# -01110- + 01110--   = -0101--
# so n XOR 2n XOR 3n  = -1100--
#
# Quad:
# -011110- XOR 011110-- = -10001--
# -011110- + 011110--   = -01101--
# so n XOR 2n XOR 3n    = -11100--
# etc - the pattern is clear
#
# So clearly to get an XOR(n,2n,3n) = 0 we can't have consecutive ones in n.
#
# Fibonacci
# Again, writing out makes it obvious.
#
# Solutions for different numbers of bits:
# 2-bits: 00, 01 & 10 (3)    (So for n<4 there are three losing n: 0, 1, 2)
# 3-bits: 000, 001, 010 & 100, 101 (5)
# 4-bits: 0000, 0001, 0010, 0100, 0101 & 1000, 1001, 1010 (8)
# 5-bits: 00000, 00001, 00010, 00100, 00101, 01000, 01001, 01010,
#         & 10000, 10001, 10010, 10100, 10101 (13)
#
# To find the solutions for 6-bits you just take all the 5-bit solutions and put a zero
# on the front, then take all the 4-bit solutions and put a 10 on the front.
# i.e. Number of solutions for 6-bits = sum of number of solutions for 4- and 5-bits
# Instant Fibonacci!


print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1,  INSTANT --------------------------')
t1  = time.time()

# === Sun, 24 Sep 2017, 15:22, haryseldon, China
# So basically we must find all numbers that doesn't contains two consecutive ones in its binary representation using 30 bits.
# This is a famous problem :)


from math import factorial

def bicoef(m,n):
    return factorial(m) // factorial(n) // factorial(m-n)

def run():
    total = 0
    for i in range(1, 16):
        total += bicoef(30 - i + 1, i)
    return print('\nLosing configurations : \t',total +1 ) #add 2^30


run()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 2,   --------------------------')
t1  = time.time()

# ====Thu, 15 Dec 2016, 10:10, mbh038
# I played for a while with bitwise operations in Python, then simply printed the sums of values for
# which  X(n,2n,3n)=0X(n,2n,3n)=0 for n≤2kn≤2k for kk from 1 to 20. Et voila!
# One sees that for n≤2nn≤2n, the answer is the n+2n+2th Fibonacci term.
# I don't yet have an explanation for that, but here is the code, using Dijkstra's algorithm
# for the Fibonacci numbers, from his 1978 note EWD654. About 50μs.

def X(n1,n2,n3):
    return n1^n2^n3==0

def p301look(n):
    safe=1
    print(0,1)
    for i in range(1,n+1):
        for j in range(2**(i-1)+1,2**i+1):
            safe+=X(j,2*j,3*j)
        print(i,safe)

def dijkFib(n,memo={}):
    """returns nth Fibonacci term"""
    if n==0 or n==1:
        return n
    try:
        return memo[n]
    except KeyError:
        if n%2:
            result = dijkFib((n-1)//2,memo)**2+dijkFib((n+1)//2,memo)**2
        if not n%2:
            result = (2*dijkFib((n-1)//2,memo)+dijkFib((n+1)//2,memo))*dijkFib((n+1)//2)
        memo[n]=result
        return result

def p301(n):
    t=time.clock()
    print (dijkFib(n+2))
    print(time.clock()-t)

p301(30)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 3,  RECURSION , ELEGANT & BEAUTIFUL --------------------------')
t1  = time.time()

# ==== Wed, 9 Nov 2016, 23:10, Kasub, USA
# The key insight is that X(n, 2n, 3n) = 0 if the binary string of n does not contain consecutive ones.
# So all we must do is determine the number of positive integers fulfilling that condition.
# We don't even need to generate the numbers!
# Runs in 0.15 ms.

def memoize(func):
	memo = {}
	def inner(*args):
		if args in memo:
			return memo[args]
		else:
			result = func(*args)
			memo[args] = result
			return result
	return inner

# Counts all bitstrings of length n. Note: is equal to fibonacci sequence
@memoize
def count_bitstrings(n):
	if n == 1: return 1
	if n == 2: return 1
	return count_bitstrings(i - 1) + count_bitstrings(i - 2)

if __name__ == '__main__':

	begin = time.time()
	count = 1 # To account for 2^30
	max_value = 30
	for i in range(1, max_value + 1):
		count += count_bitstrings(i)
	end = time.time()
	print("Time taken:", end - begin)
	print("Solution:", count)


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


# print('\n--------------------------SOLUTION 4,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
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
#
# print('\n--------------------------SOLUTION 7,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 8,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
#
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

