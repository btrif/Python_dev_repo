#  Created by Bogdan Trif on 19-11-2017 , 12:47 PM.

# © o(^_^)o  Solved by Bogdan Trif  @
#The  Euler Project  https://projecteuler.net
'''
Smallest prime factor           -           Problem 521

Let smpf(n) be the smallest prime factor of n.

smpf(91)=7 because 91=7×13 and
smpf(45)=3 because 45=3×3×5.

Let S(n) be the sum of smpf(i) for 2 ≤ i ≤ n.

E.g. S(100)=1257.

Find S(10^12) mod 10^9.


'''
import time, zzz

def prime_sieve(n):       # FOURTH      o(^_^)o
    sieve = [True] * n
    for i in range(3, int(n**0.5)+1, 2):
        if sieve[i]:
            sieve[ i*i :: 2*i ] = [False] * ( (n-i*i-1) // (2*i) +1 )
    return [2] + [i for i in range(3, n , 2) if sieve[i] ]


T = lambda n : n*(n+1)//2


def custom_sum( a, d, n) :
    ''' :Description: Makes the custom summation of the form :
        a + (a+d) + (a+2d) + (a+3d) + ...
        which is a constant increasing sequence :

            :**Sigma { k=0, n-1  } ( a + kd) =  n/2 * ( 2*a + (n-1)*d )**:

        :Example: : [ 2, 10, 16, 22, 28 ], Sum = 52. We see that first term a=4
        difference d = 6, and there are 5 terms, n = 5

    :param a: int, first term
    :param d: int, difference between terms
    :param n: int, numbers of terms in sequence
    :return: sum                    '''

    return ( 2*a + (n-1)*d  ) * n //2



print('\n--------------------------TESTS------------------------------')
t1  = time.time()

def brute_force_check(up) :
    primes = prime_sieve(up)[ ::-1 ]
    print(primes[:101])
    sieve = [0]*( up +1)

    for p in primes :
        sieve[p :: p ] = [p] * ( (up)//(p))
    print(sieve[ : 101])

    print('\nS('+str(up)+') =  ', sum(sieve[:31]))
    print(sieve[:31])
    return sieve

brute_force_check(10**2)


print('\n-----------------MANUAL CHECK -------------------')
lim = 30
siva = [i for i in range(lim+1)]
siva[1] =0
S = sum(siva)
print( S , siva)


print('\n###     2      #####')
two = ( lim//2 -1)*(lim//2)//2
print( 'twos = ',    two*2  )
print('confirmation : ', sum([ i-2 for i in range(4, lim+1, 2)   ])   )
for i in range(2, len(siva)+1 ) :
    if i%2 ==0 : siva[i] =2

S -= (( lim//2 -1)*(lim//2)//2 )*2
print('Remove two-s  :  S = ',   S )

print(' siva = ',sum(siva),  '      ', siva )

print('\n ###     3      #####')
k = 3
three = ( lim//k -1)*(lim//k)//2
print( 'threes = ',    three *k  )
print('confirmation : ', sum([ i-k for i in range(6, lim+1, k)   ])   )
S -= three*k

print('Remove three-s  :  S = ',   S )

for i in range(k, len(siva)+1 ) :
    if i%k ==0 : siva[i] =k
    # if i%6 ==0 : siva[i] =2

print(' siva = ',sum(siva),  '      ', siva )


print('\n ###   ADD  2 &  3      #####')
p1, p2 = 2, 3
d = p1*p2
n = lim// (d)
a = d - p2
add = custom_sum( a , d , n  )
print(' a =', a  ,'  d =', d , '  n= ', n,  list(range(a, lim+1, d  ))  )
print('add =  ', add )
S += add
print('S 2, 3 = ' , S )



print('\n ###     5      #####')
k = 5
five = ( lim//k -1)*(lim//k)//2
print( 'fives = ',    five *k  )
print('confirmation : ', sum([ i-k for i in range(10, lim+1, k)   ])   )
S -= five*k

print('Remove five-s  :  S = ',   S )

for i in range(k, len(siva)+1 ) :
    if i%k ==0 : siva[i] =k
    # if i%15 ==0 : siva[i] = 3
    # if i%10 ==0 : siva[i] =2

print(' siva = ',sum(siva),  '      ', siva )


print('\n ###   ADD  3 &  5      #####')
p1, p2 = 3, 5
d = p1*p2
n = lim// (d)
a = d - p2
print(' a =', a  ,'  d =', d , '  n= ', n,  list(range(a, lim+1, d  )) )
add = custom_sum( a , d , n  )
print('add =  ', add )
S += add
print('S 2, 5 = ' , S )


print('\n ###   ADD  2 &  5      #####')
p1, p2 = 2, 5
d = p1*p2
n = lim// (d)
a = d - p2
print(' a =', a  ,'  d =', d , '  n= ', n,  list(range(a, lim+1, d  )) )
add = custom_sum( a , d , n  )
print('add =  ', add )
S += add
print('S 2, 5 = ' , S )



print('\n ###   SUBSTRACT  2,  3 &  5      #####')
p1, p2, p3 = 2, 3, 5
p = p1*p2*p3
d = lim// (p)
sub = ( d*(d+1)//2 ) * p
sub = p-max(p1,p2,p3)
print('sub =  ', sub )
S -= sub

print('S 2, 3, 5 = ' , S )


# @2017-11-20 - Simulation of the problem above works well.
# I must do exclusion- inclusion principles  add combinations of 2, substract conbinations of 3 and so on ...
# However using itertools doesn't work as there are 11 primes in the combination 2,3,5,7,11,13,,17,23,29 < 10^12
# I must use something else as I don;t want to use 11 for loops. Must learn from problems like 248 and so on
#     where inclusion - exclusion is used



t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')

print('\n================  My FIRST SOLUTION,   ===============\n')
t1  = time.time()

# https://www.mathsisfun.com/algebra/sequences-sums-arithmetic.html
# We must use the formula  :      Sigma { k=0, n-1  } ( a + kd) =  n/2 * ( 2*a + (n-1)*d )



print('custom_sum test : ',  custom_sum(4, 6, 16) )
print('custom_sum test : ',  custom_sum(4, 3, 4) )
print(' Sum Check ' ,sum( list(range( 3, 100, 3 )) ) )


print()


lim = 10**2
P = prime_sieve( int( lim**(1/2)) )
print( len(P),P[:30] )

S = lim*(lim+1)//2
print(S)
for i in range(len(P)):
    k = lim// P[i]
    S -= T(k-1)* P[i]
    # S +=  ( T(k)-T(k-1) ) * P[i]
    print(P[i], '     how many p-s = ', k-1 ,  '          substr =  ', T(k-1)* P[i] ,'          S = ' , S  )
    for j in range( i+1, len(P) ) :
        d =  P[i] * P[j]        # m = p1*p2
        l = lim // d
        a = d- P[j]
        # add = T(l) * 6
        sub = P[i] * l
        # add = T(l)* d
        add = custom_sum(a , d, l )


        diff2 = P[j] - P[i]
        S +=  add
        print('p1 =  ' ,P[i],'        p2 = ' , P[j] , '          p1*p2 =  ', d , '       l =  ', l ,   '  add =  ' , custom_sum(a , d, l ) ,'        sub =  ' ,  sub    )

print('\n S = ', S)





t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')


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




