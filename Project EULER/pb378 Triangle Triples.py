#  Created by Bogdan Trif on 08-07-2018 , 2:32 PM.
# © o(^_^)o  Solved by Bogdan Trif  @
#The  Euler Project  https://projecteuler.net
'''
                        Triangle Triples            -               Problem 378

Let T(n) be the nth triangle number, so T(n) = n (n+1) /2

Let dT(n) be the number of divisors of T(n).

E.g.: T(7) = 28 and dT(7) = 6.

Let Tr(n) be the number of triples (i, j, k) such that 1 ≤ i < j < k ≤ n and dT(i) > dT(j) > dT(k).

Tr(20) = 14,
Tr(100) = 5772 and
Tr(1000) = 11174776.

Find Tr(60 000 000).   6*10**7
Give the last 18 digits of your answer.             (%10^18)


'''
import time, zzz

from numpy import sqrt



def get_divisors(n):      ### ( ͡° ͜ʖ ͡°)  FASTEST  ( ͡° ͜ʖ ͡°)  ### !! FIRST FASTEST
    factors = set()
    for x in range(1, int(sqrt(n)) + 1):
        if n % x == 0:
            factors.add(x)
            factors.add(n//x)
    return sorted(factors)

T = lambda n : (n*n+n) //2

def brute_force(lim) :      # Algorithm solution  O( n^3 + n*log n)

    sieve=[0]*(lim+1)
    for i in range(1, lim+1):
        t = T(i)
        dt = get_divisors(t)
        dT=  len(dt)
        sieve[i] = dT

        # print('i =', i ,'     T= ',  t,'            dT= ',  dT ,'            div= ',  dt )

    print('sieve :' , sieve,'\n' )
    cnt=0
    for i in range(0, len(sieve) ) :
        for j in range(i+1, len(sieve) ) :
            for k in range(j+1, len(sieve) ) :
                if sieve[i] > sieve[j] > sieve[k]  :
                    cnt+=1
                    print(str(cnt)+'.    ',  i, j, k ,' T     :', T(i), T(j), T(k) ,'        ', sieve[i], sieve[j], sieve[k] )

    return print('\nAnswer  Brute Force O(n^3) : ' ,  cnt )



print('\n--------------------------TESTS------------------------------')
t1  = time.time()

brute_force(100)


t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')

print('\n================  My FIRST SOLUTION,   ===============\n')
# t1  = time.time()





# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')


# print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
# print('\n--------------------------SOLUTION 1,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 2,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 3,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 4,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 5,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 6,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 7,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 8,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
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

