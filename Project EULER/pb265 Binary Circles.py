#  Created by Bogdan Trif on 16-10-2017 , 9:57 PM.
# © o(^_^)o  Solved by Bogdan Trif  @   Completed on Sat, 11 Nov 2017, 13:21
#The  Euler Project  https://projecteuler.net
'''
                    Binary Circles          -           Problem 265

2N binary digits can be placed in a circle so that all the N-digit clockwise subsequences are distinct.

For N=3, two such circular arrangements are possible, ignoring rotations:

p265_BinaryCircles.gif

For the first arrangement, the 3-digit subsequences, in clockwise order, are:
000, 001, 010, 101, 011, 111, 110 and 100.

Each circular arrangement can be encoded as a number by concatenating the binary digits starting
with the subsequence of all zeros as the most significant bits and proceeding clockwise.
The two arrangements for N=3 are thus represented as 23 and 29:

00010111 2 = 23
00011101 2 = 29
Calling S(N) the sum of the unique numeric representations, we can see that S(3) = 23 + 29 = 52.

Find S(5).


'''
import time, zzz

import sys


def rotate(l, n):
    return l[-n:] + l[:-n]

def de_bruijn(k, n):
    """
    de Bruijn sequence for alphabet k
    and subsequences of length n.
    """
    try:
        # let's see if k can be cast to an integer;
        # if so, make our alphabet a list
        _ = int(k)
        alphabet = list(map(str, range(k)))

    except (ValueError, TypeError):
        alphabet = k
        k = len(k)

    a = [0] * k * n
    sequence = []

    def db(t, p):
        if t > n:
            if n % p == 0:
                sequence.extend(a[1:p + 1])
        else:
            a[t] = a[t - p]
            db(t + 1, p)
            for j in range(a[t - p] + 1, k):
                a[t] = j
                db(t + 1, t)
    db(1, 1)
    return "".join(alphabet[i] for i in sequence)

print(de_bruijn(2, 3))
print(de_bruijn("abcd", 2))


print('\n----------------  TESTS & BRUTE FORCE, 2 min using pypy------------------------------')
t1  = time.time()

# for i in range(32+1):
#     print(i,'             ', bin(i) )

def really_brute_force( n = 3) :
    S = 0
    for i in range(  2**(2**n - 6 ) + 2**(2**n - 10 ) ,  2**(2**n-5)) :
        if i % 10**6 ==0 :
            sys.stdout.write('\r' + str(i) +'              '+  str(round((time.time() - t1) , 2) ) +'  sec'   )   # Font Segoe UI Semibold
        N = str(bin(i))[2:].zfill(2**n)             # padding       n = '4'    ;     n.zfill(3) ;     '004'
        c =  N.count('1')
        # print(N)
        if  c == 16 :
            if  N[:n] == '0'*n   :
                C = set()
                for j in range(2**n) :
                    a = N[:n]
                    # print(a, type(a))
                    C.add( int( a, 2  ) )
                    N = rotate(N, -1 )
                # print(i,'        ', N, '        ' ,C)
                if len(C) == 2**n :
                    print(i,'     ones = ', c  ,'      N= ',N, '      ' , C )
                    S += i

    print('\nAnswer =  ', S )
    return S

# really_brute_force(5)               #   Answer =   209110240768             # Completed in :   109.67   sec



t2  = time.time()
print('\n# Completed in :', round((t2-t1) , 2), 's\n\n')

print('\n================  My FIRST SOLUTION,   ===============\n')
# t1  = time.time()





# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')



# ==== GENERAL IDEAS =====
# https://en.wikipedia.org/wiki/De_Bruijn_sequence

print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n------------------   SOLUTION 1,  BRUTE- FORCE - RECURSION, < 100 ms, MAGNIFIC --------------------------')
t1  = time.time()


# ==== Sat, 21 Nov 2009, 11:20, Peter de Rivaz, England
# Bruteforce recursive solution in Python.
# Under 1 second.  Could probably memoize based on the contents of S so far to go faster as
# it doesn't matter what order the items appear in the set.
# Function gets called 92636 times.
# Can anyone confirm that S(3)=71087247404272512 if done in base 3?

def e265_recurse( S , last , N ):
   if len(S) == N:
      return last
   last *= 2
   t = last & (N-1)
   s = 0
   if t not in S:
      S.add( t )
      s += e265_recurse( S, last, N )
      S.remove( t )
   t+=1
   if t not in S:
      S.add( t )
      s+=e265_recurse(S, last+1, N)
      S.remove( t )
   return s

def euler265(n):
   print ( e265_recurse( set( [0]) , 0 , 2**n )/ 2**(n-1) )

euler265(3)

t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')


print('\n--------------------------SOLUTION 2, De Bruijn Sequence  --------------------------')
t1  = time.time()

# ==== Sat, 21 Nov 2009, 12:08, Israel
# Wow, you guys are fast!
# Used De Bruijn Sequence

def solution_De_Bruijn_Sequence():

    def c(a):
        yield ''.join(a[1:]) + '0'
        yield ''.join(a[1:]) + '1'

    n = 5
    tot = 0
    stack = [('0'*n, frozenset(['0'*n]), ['0b'])]
    while stack:
        a, v, i = stack.pop()
        if len(v) == 2 ** n:
            tot += int(''.join(i),2) // (2 ** (n - 1))
        else:
            for x in c(a):
                if x not in v:
                    stack += [(x, v | frozenset([x]), i + [x[-1]])]

    return print(tot)

solution_De_Bruijn_Sequence()

t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')


print('\n--------------------------SOLUTION 3, RECURSION  --------------------------')
t1  = time.time()

# ==== Sat, 21 Nov 2009, 14:03, gianchub, England

N = 3
mask = 2**N - 1
m = 1 << (N-1)
p = 2 ** N - 1
sol = []

def rec(l, t, c):
    if c == 2**N:
        sol.append( l )
        return None
    t1, t2 = ( t<<1 ) & mask, ( (t<<1) + 1) & mask
    if not t1 in l:
        rec( l+[t1], t1, c+1 )
    if not t2 in l:
        rec( l+[t2], t2, c+1 )


def p265():
    rec( [0], 0, 1 )
    res = [ sum(2**(p-i) if (b&m) else 0 for (i, b) in enumerate(s)) for s in sol ]
    print ('Solution: %d' % (sum(res)))

p265()

t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')


print('\n--------------------------SOLUTION 4,  SMART & Beautiful RECURSION  --------------------------')
t1  = time.time()

# ==== Sat, 21 Nov 2009, 20:29, Taifu, Italy
# Generic solution in python:

tot = 0
def p265(base, d, others):
    global tot
    if len(others) == d:
        tot += int("".join(str(x[0]) for x in others), base)
    else:
        last = others[-1]
        for n in range(base):
            if last[1:] + (n,) not in others:
                p265(base, d, others + [last[1:] + (n,)])
base = 2
n = 3
p265(base, base**n, [(0,)*n])
print( tot)

t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')


print('\n--------------------------SOLUTION 5,  RECURSION, HIGHLY EFFICIENT  --------------------------')
t1  = time.time()

# === Sun, 22 Nov 2009, 05:05, MrDrake, Australia
# 3 line recursive search (<1s)


def f(n, s):
    if len(s) == 2**n + n-1:
        return int( s[:2**n], 2 )

    return sum( [ f(n, s+d) for d in "01" if (s+d)[-n:] not in s ] )

print (f(3, "0"*3) )
print (f(5, "0"*5) )

t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')


print('\n--------------------------SOLUTION 6,  RECURSION  --------------------------')
t1  = time.time()

# ====Sun, 22 Nov 2009, 14:29, inamori, Japan

N = 3
M = 2 ** N

def gen_number(b0 = 0, k = 0, m0 = 0):
    if k == M - 1:
        if m0 == 1:
            yield 0
    elif k == 0:
        m = M // 2
        for n in gen_number(1 << m, 1, m):
            yield (n << 1) + 1
    else:
        for i in range(2):
            m = (m0 >> 1) + (i << (N - 1))
            if (b0 & (1 << m)) == 0:
                b = b0 | (1 << m)
                for n in gen_number(b, k + 1, m):
                    yield (n << 1) + i

print( sum(gen_number()))

t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')


print('\n--------------------------SOLUTION 7,  Interesting --------------------------')
t1  = time.time()

# =====Thu, 26 Nov 2009, 07:07, igor.chubin, Ukraine

n = 5
tot = 0
x = 2 ** (2 ** n + 1) - 1
h = 2 ** (2 ** n) + 1
k = 2 ** (n + 1) - (2 ** (n - 1) + 1)
stack = [(h, 0, 0)]
while stack:
    s, a, i = stack.pop()
    if s == x:
        tot += i >> (n - 1)
        continue
    b = 2 * (k & a)

    if s != (s | (1 << b)):
        stack += [(s | (1 << b), b, (i << 1) + (b & 1))]
    if s != (s | (1 << (b + 1))):
        stack += [(s | (1 << (b + 1)), b + 1, (i << 1) + ((b + 1) & 1))]


print(tot)


t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')


print('\n--------------------------SOLUTION 8,  Recursion  --------------------------')
t1  = time.time()

def bin2dec(a):
    s=0
    for x in a: s=s*2+x
    return s

def check(a,l,n):
    r=[]
    for i in range(l):
        r+=[bin2dec(a[i:i+n])]
    return len(r)==len(set(r))

def gen(a,n):
    if len(a)==2**n:
        if check(a+a,len(a),n):
            return bin2dec(a)
    else:
        if check(a,len(a)-n+1,n):
            return gen(a+[0],n)+gen(a+[1],n)
    return 0

print( gen([0]*5 , 5) )

t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')


print('\n--------------------------SOLUTION 9,  DEPTH FIRST SEARCH, DFS --------------------------')
t1  = time.time()

# ====Fri, 27 Nov 2009, 01:33, loreto, England
# I initially noticed some similarities with Gray Code but hadn't heard of De Bruijn's sequence.
# Still, using a depth-first search I got the answer in 1 second, in Python 3:

N = 5

total = 0
def score(ring):
    global total

    v = 0
    for a in ring: v = 2*v+a
    total += v

def search(seen, ring):
    if len(ring) == 2**N:
        for i in range(1, N):
            a = ring[-i:]+ring[:N-i]
            if tuple(a) in seen: return
            seen |= set([tuple(a)])

        score(ring)
        return

    a = ring[-(N-1):]+[0]
    b = ring[-(N-1):]+[1]

    if tuple(a) not in seen: search(seen|set([tuple(a)]), ring+[0])
    if tuple(b) not in seen: search(seen|set([tuple(b)]), ring+[1])


search(set([tuple([0]*N)]), [0]*N)
print(total)

t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')


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




