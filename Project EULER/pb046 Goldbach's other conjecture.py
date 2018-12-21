#!/usr/bin/python
# Solved by Bogdan Trif @   Completed on Wed, 30 Nov 2016, 23:46
#The  Euler Project  https://projecteuler.net
'''
                        Goldbach's other conjecture     -       Problem 46
It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.
9 = 7 + 2×12
15 = 7 + 2×22
21 = 3 + 2×32
25 = 7 + 2×32
27 = 19 + 2×22
33 = 31 + 2×12
It turns out that the conjecture was false.
What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
'''
import time
import gmpy2


def prime_generator(n):         # HIghly Efficient !!!!         THE FASTEST, The BEST , The ONE
    """  Sieve of Eratosthenes              !!!!!!!!! THE FASTEST SIEVE. It won the battle with sieve
    Create a candidate list within which non-primes will be marked as None.
    """
    cand = [i for i in range(3, n + 1, 2)]
    end = int(n ** 0.5) // 2

    # Loop over candidates (cand), marking out each multiple.
    for i in range(end):
        if cand[i]:
            cand[cand[i] + i::cand[i]] = [None] * ( (n // cand[i]) - (n // (2 * cand[i])) - 1 )

    # Filter out non-primes and return the list.
    return [2] + [i for i in cand if i]

def factorise( n):
        ''' Decompose a factor in its prime factors. This function uses the pyprimes module. THE FASTEST  '''
        from pyprimes import factorise
        return [val for sublist in [[i[0]]*i[1] for i in factorise(n)] for val in sublist]

primes = prime_generator(10**4)

def detect_Goldbach(n):
    j=0
    while primes[j] < n :
        i = primes[j]
        a = (n - i)/2
        # print(a,  i)
        if a % 1 == 0 :
            a = int(a)
            if gmpy2.is_square( a ) == True:
                return True
        j+=1
    return False

print('\n--------------------------TESTS------------------------------')

print('\nTest Function factorise : ', factorise(14))
print('\nTest Function detect_Goldbach : ', detect_Goldbach(24))


print('\n================  My FIRST SOLUTION,   ===============\n')
t1  = time.time()

def solve():
    for i in range(27,10**7, 2):
        if gmpy2.is_prime(i) == False :
            if detect_Goldbach(i) == False:
                return print('\nAnswer : ',i)

solve()                      #  Answer :  5777

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')          # Completed in : 230.013132 ms


print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1,  aolea, Spain --------------------------')
t1  = time.time()

from math import sqrt

def primos (num):
    iRoot = int(sqrt(num))
    primos = [2,3]
    for j in range(5,num,2):
        if j > num :
            break
        primos.append(j)
    for k in primos[1:]:
        if k > iRoot:
            break
        for l in primos[k+1:]:
            if l > k:
                if l % k == 0:
                    # print(k,l)
                    primos.remove(l)
    return primos

n = 10000
listPrimes = primos(n)

for i in range(101,n,2):
    flag = False
    for j in listPrimes :
        if j > i :
            break
        if int(sqrt((i-j)/2)) == sqrt((i-j)/2):
            flag = True
            # print (i,j,sqrt((i-j)/2))
            break
    if flag == False :
        result = i
        break
print(result)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')



print('\n--------------------------SOLUTION 2, shwetalm, USA  --------------------------')
t1  = time.time()

odd_nums = []
for i in range(1,10**4,2):
    odd_nums.append(i)

prime_nums = []
for i in odd_nums:
    for j in range(3,int(i**0.5)+1,2):
        if i%j == 0:
            break
    else:
        prime_nums.append(i)


odd_nums = set(odd_nums) ^ set(prime_nums)

sq_dub = []
for i in range(1,500):
    sq_dub.append(2*i**2)


for i in odd_nums:
    for j in sq_dub:
        if (i - j) in prime_nums:
            break
        elif j > i:
            print(i)
            break
    else:
        print(i)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 3, svamja, India, VERY NICE  --------------------------')
t1  = time.time()

# Another nice problem to play with!!
# maintain an array of double of squares and odd primes.
# Walk though odd numbers. You can collect primes by checking existing primes,
# or if it is a composite, then check if its difference with double of squares is a prime.

square_doubles = []
odd_primes = [ 3, 5, 7 ]

for i in range(1, 100):
    square_doubles.append(2*i*i)

sqroot_index = 0
sqroot = 3

for num in range(9, 100001, 2):
    is_prime = True

    # check if prime / composite

    for odd_prime in odd_primes:
        if odd_prime > sqroot: break
        if num % odd_prime == 0:
            is_prime = False
            break

    # prime found, save it safely

    if is_prime:
        odd_primes.append(num)
        if odd_primes[sqroot_index+1]*odd_primes[sqroot_index+1] < num:
            sqroot_index += 1
            sqroot = odd_primes[sqroot_index+1]
        continue

    # composite number -> check conjecture
    match_found = False
    for square_double in square_doubles:
        num_diff = num - square_double
        if num_diff in odd_primes:
            match_found = True
            break

    if not match_found:
        print ("invalid conjecture for ", num)
        break

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
