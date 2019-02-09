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

        .. math::
            \sum_{ k=0}^{n-1} ( a + kd ) = n / 2 * ( 2*a + (n-1)*d )

        :Example: : [ 2, 8, 14, 20, 26 ], Sum = 70. We see that first term a = 2
        difference d = 6, and there are 5 terms, n = 5

    :param a: int, first term
    :param d: int, difference between terms
    :param n: int, numbers of terms in sequence
    :return: sum                    '''

    return ( 2*a + (n-1)*d  ) * n //2


def custom_sum2( a, d, lim ) :
    ''' :Description: Makes the custom summation of the form :
        a + (a+d) + (a+2d) + (a+3d) + ...
        which is a constant increasing sequence up to the number  = lim

        .. math::
            \sum_{ k=0}^{n-1} ( a + kd ) = n / 2 * ( 2*a + (n-1)*d )

        :Example: : [ 3, 8, 13, ... , 93, 98 ],  start number a=3 , difference betweeen d = 5
        First calculates how many terms : terms = 20, then it calculates the overall sum
    :param a: int, first term
    :param d: int, difference between terms
    :param n: int, numbers of terms in sequence
    :return: sum                    '''
    n = (lim-a)//d  +1

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

    print(' ANSWER = ', sum (sieve) )
    return sieve

brute_force_check(10**2)


print('\n-----------------MANUAL CHECK -------------------')
'''

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


# @2017-11-20 - Simulation of the problem above works well. <-- ON THE RIGHT PATH !!
# I must do exclusion- inclusion principles  add combinations of 2, substract conbinations of 3 and so on ...
# However using itertools doesn't work as there are 11 primes in the combination 2,3,5,7,11,13,,17,23,29 < 10^12
# I must use something else as I don;t want to use 11 for loops. Must learn from problems like 248 and so on
#     where inclusion - exclusion is used

'''




t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')

print('\n----------------  My FIRST ATTEMPT,   -------------------------\n')
t1  = time.time()

# https://www.mathsisfun.com/algebra/sequences-sums-arithmetic.html
# We must use the formula  :      Sigma { k=0, n-1  } ( a + kd) =  n/2 * ( 2*a + (n-1)*d )



print('custom_sum test : ',  custom_sum(4, 6, 16) )
print('custom_sum test : ',  custom_sum(4, 3, 4) )
print(' Sum Check ' ,sum( list(range( 3, 100, 3 )) ) )


print()

def first_attempt():

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


print('\n=================  My SECOND SOLUTION,   =================\n')
t1  = time.time()

'''     @2019-01-06, 11:03 IDEA
1.  We need only primes up to sqrt(lim)
2.  We Sum = n*(n+1)//2  all nr's and then we substract 



def find_pattern(prime, up_lim):
    P = prime_sieve( up_lim  )
    index = P.index(prime)
    S = set(P[:index] )
    print('S : ', S )
    A = []
    n = prime
    while n < up_lim*up_lim :
        flag = False
        for i in S :
            if n%i == 0 :
                flag = True
                break
        if flag == False :
            # print(n, end = '  ')
            A.append(n)

        n +=prime
    print(A)
    print( [  A[i]-A[i-1] for i in range(1, len(A) )  ]   )

    return A

find_pattern(13, 100 )

THIS IDEA  doesn't work !!!!!  Look at the following pattern for 13 and try to find a pattern
for the primes up to 100 and numbers up to 10.000 !
It is not feasable !

[13, 169, 221, 247, 299, 377, 403, 481, 533, 559, 611, 689, 767, 793, 871, 923, 949, 1027, 1079, 1157, 1261, 
1313, 1339, 1391, 1417, 1469, 1651, 1703, 1781, 1807, 1937, 1963, 2041, 2119, 2171, 2197, 2249, 2327, 2353, 
2483, 2509, 2561, 2587, 2743, 2873, 2899, 2951, 2977, 3029, 3107, 3133, 3211, 3263, 3341, 3419, 3497, 3523, 
3601, 3653, 3679, 3757, 3809, 3887, 3991, 4043, 4069, 4121, 4199, 4303, 4381, 4511, 4537, 4589, 4667, 4693, 
4771, 4849, 4901, 4927, 4979, 5057, 5083, 5161, 5213, 5239, 5317, 5447, 5473, 5603, 5629, 5681, 5707, 5759, 
5837, 5941, 5993, 6019, 6071, 6227, 6253, 6331, 6383, 6409, 6487, 6539, 6617, 6773, 6799, 6851, 6877, 6929, 
7033, 7111, 7163, 7241, 7267, 7319, 7397, 7423, 7501, 7631, 7657, 7709, 7787, 7813, 7891, 7943, 7969, 8021, 
8047, 8177, 8203, 8333, 8359, 8411, 8489, 8567, 8593, 8671, 8749, 8801, 8879, 8957, 8983, 9061, 9113, 9139, 
9217, 9269, 9347, 9451, 9503, 9529, 9607, 9659, 9763, 9841, 9893, 9971, 9997]

[156, 52, 26, 52, 78, 26, 78, 52, 26, 52, 78, 78, 26, 78, 52, 26, 78, 52, 78, 104, 52, 26, 52, 26, 52, 182, 52, 78, 26, 
130, 26, 78, 78, 52, 26, 52, 78, 26, 130, 26, 52, 26, 156, 130, 26, 52, 26, 52, 78, 26, 78, 52, 78, 78, 78, 26, 78, 52, 
26, 78, 52, 78, 104, 52, 26, 52, 78, 104, 78, 130, 26, 52, 78, 26, 78, 78, 52, 26, 52, 78, 26, 78, 52, 26, 78, 130, 26, 
130, 26, 52, 26, 52, 78, 104, 52, 26, 52, 156, 26, 78, 52, 26, 78, 52, 78, 156, 26, 52, 26, 52, 104, 78, 52, 78, 26, 
52, 78, 26, 78, 130, 26, 52, 78, 26, 78, 52, 26, 52, 26, 130, 26, 130, 26, 52, 78, 78, 26, 78, 78, 52, 78, 78, 26, 78, 
52, 26, 78, 52, 78, 104, 52, 26, 78, 52, 104, 78, 52, 78, 26]


'''


lim = 10**2
P = prime_sieve( int( lim**(1/2)) )
print( len(P),P[:30] )

Sum = lim*(lim+1)//2
print('Sum = ', Sum )

for i in range(len(P)) :
    print( P[i] )


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




