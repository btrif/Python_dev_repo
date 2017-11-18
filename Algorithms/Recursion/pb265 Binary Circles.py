#  Created by Bogdan Trif on 11-11-2017 , 7:48 PM.
import time


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

########################

print('\n--------------------------SOLUTION 5,  RECURSION  --------------------------')
t1  = time.time()

# === Sun, 22 Nov 2009, 05:05, MrDrake, Australia
# 3 line recursive search (<1s)


def f(n, s):
    if len(s) == 2**n + n-1: return int(s[:2**n], 2)
    return sum([f(n, s+d) for d in "01" if (s+d)[-n:] not in s])

print (f(3, "0"*3) )
print (f(5, "0"*5) )



