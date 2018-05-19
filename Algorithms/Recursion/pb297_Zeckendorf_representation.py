#  Created by Bogdan Trif on 23-04-2018 , 8:48 AM.
import time

t1  = time.time()

def memo(func):
    cache = {}
    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrap

@memo
def f(i):
    if i < 2:
        return 0
    a, b = 1, 2
    while b < i:
        a, b = b, a+b
    return f(a) + (i - a) + f(i - a)

print( f(10**17))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


#######################################


t1  = time.time()

# ==== Sun, 17 Jun 2012, 20:16, ving, USA
# Another rendition in Python, similar to the above but using tail recursion:

N = 10**6 - 1  # Answer = 7894453
N = 10**17 - 1  # Answer = 2252639041804718029
#N = 10**500 - 1

sumz, fibs = [1, 1], [1, 1]

while fibs[-1] < N:
    sumz.append(sumz[-2] + sumz[-1] + fibs[-2] - 1)
    fibs.append(fibs[-2] + fibs[-1])

def get_sum_z(n):
    i = 0
    while fibs[i+1] <= n:
        i += 1
    sz = sumz[i]
    n -= fibs[i]
    if n > 0:
        sz += n + get_sum_z(n)
    return sz

print(get_sum_z(N))


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


###########################

t1  = time.time()

# ====Sat, 15 Sep 2012, 03:03, JavaGAR, USA
# This Python solution uses recursive functions to compute z values and sums of z values.
# Since the sumZ function uses previous sumZ values recursively, it employs values stored in a list and a dictionary for efficiency.
# Execution time is less than a second.

fib = [] # List of Fibonacci numbers
fibZSums = {0: 0, 1: 1, 2: 2, 3: 3} # Dictionary of z(n) values of Fibonacci numbers

def buildFib(maxFib):
    # Build the list of Fibonacci numbers
    a = 0
    b = 1
    while b <= maxFib:
        a, b = b, a + b
        fib.append(a)

def buildFibZSums():
    # Build the list of sums of z values from 1 to each Fibonacci number
    for n in range(5, len(fib) - 1):
        if fib[n] not in fibZSums:
            fibZSums[fib[n]] = sumZ(fib[n])

def z(n):
    # Recursive z function
    if n in fib:
        return 1
    else:
        i = 0
        while n > fib[i]:
            i += 1
        return 1 + z(n - fib[i - 1])

def fIndex(n):
    # Return the index in fib of the largest Fibonacci number <= n
    i = 0
    while n >= fib[i]:
        i += 1
    return i - 1

def zeckendorf(n):
    # Recursive function to return the Zeckendorf representation of n as a list
    if n in fib:
        return [n]
    else:
        i = 0
        while n > fib[i]:
            i += 1
        f = fib[i - 1]
        l = [f]
        l.extend(zeckendorf(n - f))
        return l

def sumZ(n):
    # Recursive function to return the sum of z values from 1 to n
    if n in fibZSums:
        return fibZSums[n]
    else:
        fi = fIndex(n)
        return sumZ(fib[fi - 1]) + fib[fi - 2] + sumZ(fib[fi - 2]) - 1 + (n - fib[fi]) + sumZ(n - fib[fi])

def main():
    buildFib(10 ** 18)
    buildFibZSums()
    print(sumZ(10 ** 6 - 1))
    print(sumZ(10 ** 17 - 1))

main()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')



######################


# === Sat, 19 Jun 2010, 00:40, st1974, Germany
# Another simple recursion solution

def zsum(n):
    if n<=3: return n

    f0, f1 = s0, s1 = 1, 2
    while n-f1 >= f0:
        s0, s1 = s1, s1 + s0 + f0 -1
        f0, f1 = f1, f0+f1
    return s1 + zsum( n-f1) + (n-f1)

print(zsum(10**17-1))


###########################


# === Fri, 18 Jun 2010, 20:42, mastro, Italy
# This was easy, similar algorithm as others but very short code:

def get_sum_z(n, cache={1: 0}):
    if n not in cache:
        prev = fib = 1
        while fib < n:
            prev, fib = fib, prev + fib
        cache[n] = n - prev + get_sum_z(n - prev) + get_sum_z(prev)
    return cache[n]

print(get_sum_z(10 ** 17))
