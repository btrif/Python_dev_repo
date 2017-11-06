#!/usr/bin/python                   ( ͡° ͜ʖ ͡°)
# Solved by Bogdan Trif @   Completed on Sat, 4 Mar 2017, 20:56
#The  Euler Project  https://projecteuler.net
'''
                Exploring Pascal's pyramid      -       Problem 154

A triangular pyramid is constructed using spherical balls so that each ball rests on exactly three balls of the next lower level.


Then, we calculate the number of paths leading from the apex to each position:

A path starts at the apex and progresses downwards to any of the three spheres directly below the current position.

Consequently, the number of paths to reach a certain position is the sum of the numbers
immediately above it (depending on the position, there are up to three numbers above it).

The result is Pascal's pyramid and the numbers at each level n are the coefficients of the trinomial expansion (x + y + z)**n.

How many coefficients in the expansion of (x + y + z)**200000 are multiples of 10**12?


'''
import time, math
import sympy
from gmpy2 import fac


from sympy import symbols, expand_mul, exp, log, sin, expand

x, y, z = symbols('x,y,z', positive=True)
print(sympy.expand( (x+y+z)**2 ) ,'\n\n')


print( sympy.binomial_coefficients_list(10) )

def fact_ending_zeros(n):
    p,e = 5,1
    pe = p**e
    cnt=0
    while pe <= n :
        cnt += n//pe
        e+=1
        pe = p**e
    return cnt

print('fact_ending_zeros : \t' ,fact_ending_zeros(100) )

def give_me_2_5_fact_digit_factors(n):
    '''return the number of factors of 2 & 5 found in a factorial
    :param n:  factorial
    :return: tuple, factors of 2 and 5    '''
    arr = []
    for p in [2,5] :
        e , cnt = 1, 0
        pe = p**e
        while pe <= n :
            cnt += n // pe
    #         print(str(e)+'.   ', pe,  n/pe, '   ', n//pe)
            e+=1
            pe = p**e
        arr.append(cnt)
    return arr
give_me_2_5_fact_digit_factors(10)

def calculate_trinomial_coefficient(n, m, k) :
    '''Description: (x+y+z)**n . The coefficients of (x+y+z)**4 are :
        1, 4, 4, 6, 12, 6, 4, 12, 12, 4, 1, 4, 6, 4, 1
                       1
                    4     4
                 6     12     6
              4    12    12    4
           1     4     6     4     1
    :param n: the power of the expansion
    :param m: is the row of the triangle
    :param k: is the column of the triangle
    :return: int, the coefficient of the trinomial expansion
    :Observations : n >= m, n>=k, m >=k
    :Formula: :   C{n,m} *C{m,k} = n! / [ (n-m)! * (m-k)! * k! ]
    '''
    from gmpy2 import fac
    # return ( math.factorial(n) // ( math.factorial(n-m)*math.factorial(m-k)* math.factorial(k) ))%10**16
    return ( fac(n) // ( fac(n-m)*fac(m-k)* fac(k) ))%10**16

print('calculate_trinomial_coefficient :\t', calculate_trinomial_coefficient(6, 0, 0 ))
print('calculate_trinomial_coefficient :\t', calculate_trinomial_coefficient(6, 1, 0 ))
print('calculate_trinomial_coefficient :\t', calculate_trinomial_coefficient(6, 2, 0 ))
print('calculate_trinomial_coefficient :\t', calculate_trinomial_coefficient(20, 7, 0 ))
print('calculate_trinomial_coefficient :\t', calculate_trinomial_coefficient(200000, 1, 1 ))

def trailing_zeros(longint):
    '''Function to calculare trailing zeros of a function '''
    manipulandum = str(longint)
    return len(manipulandum)-len(manipulandum.rstrip('0'))



def fact_digit_factors(n, p=2):
    '''Returns how many factors of a digit there are in a factorial    
    :param n:  the factorial
    :param p: digit, should be prime 2,3,5,7
    :return: the number of factors
    '''
    e = 1
    pe = p**e
    cnt=0
    while pe <= n :
        cnt += n // pe
#         print(str(e)+'.   ', pe,  n/pe, '   ', n//pe)
        e+=1
        pe = p**e
    return cnt

fact_digit_factors(6)

def calculate_trinomial_zeros(n,m,k):
    ''' :Observation: Depends on the function fact_ending_zeros
        :param n:  power
        :param m: row
        :param k:  column
        :return: int, number of zeros                              '''
    N = fact_ending_zeros(n)
    N_m = fact_ending_zeros(n-m)
    M_k = fact_ending_zeros(m-k)
    K = fact_ending_zeros(k)
    den = N_m + M_k + K

    t_N = fact_digit_factors(n)
    t_den = fact_digit_factors(n-m) + fact_digit_factors(m-k) + fact_digit_factors(k)
    diff =  t_N - t_den

    # print('\nTOWs    :  diff : ', diff, '    ', )
    # print('FIVEs   :   n= ',n , '     n-m = ',n-m,  '      m-k =',m-k ,'      k=',k ,   '   5"s =   ', N, N_m, M_k, K )
    if diff == 0 : return diff
    if    diff >= N-den > 0 : return N-den
    if    N-den > diff  > 0 : return diff

    return N-den


def get_trinomial_zeros(n,m,k):
    ''' :Observation: I must use the pre-built SIEVE although ! !!!!!                               '''

    N = give_me_2_5_fact_digit_factors(n)
    N_m = give_me_2_5_fact_digit_factors(n-m)
    M_k = give_me_2_5_fact_digit_factors(m-k)
    K = give_me_2_5_fact_digit_factors(k)

    # print(N, N_m, M_k, K)
    res = ( N[0] - N_m[0] - M_k[0] - K[0], N[1] - N_m[1] - M_k[1] - K[1] )
    # print(res)
    if res[0] <= res[1] : return res[0]
    if res[0] > res[1] : return res[1]


# def get_trinomial_zeros(n,m,k):
#     ''' :Observation:
#                                 '''
#     from gmpy2 import fac
#     N = fact_ending_zeros(n)
#     N_m = fact_ending_zeros(n-m)
#     M_k = fact_ending_zeros(m-k)
#     K = fact_ending_zeros(k)
#     den = N_m + M_k + K
#
#     t_N = fact_digit_factors(n)
#     t_den = fact_digit_factors(n-m) + fact_digit_factors(m-k) + fact_digit_factors(k)
#     diff =  t_N - t_den
#
#     # print('\nTOWs    :  diff : ', diff, '    ', )
#     # print('FIVEs   :   n= ',n , '     n-m = ',n-m,  '      m-k =',m-k ,'      k=',k ,   '   5"s =   ', N, N_m, M_k, K )
#     if diff == 0 : return diff
#     if    diff >= N-den > 0 : return N-den
#     if    N-den > diff  > 0 : return diff
#
#     return N-den

def build_precalculated_zeroes_sieve(n):
    D={}
    for i in range(n+1):
        D[i] = give_me_2_5_fact_digit_factors(i)
    return D

D = build_precalculated_zeroes_sieve(30)
print(D)

def zeros_trinomial(n,m,k, D):          #######
    ''' :Observation:      use a pre-build external Dictionary                          '''
    N = D[n]
    N_m = D[n-m]
    M_k = D[m-k]
    K = D[k]
    # print(N, N_m, M_k, K)
    res = ( N[0] - N_m[0] - M_k[0] - K[0], N[1] - N_m[1] - M_k[1] - K[1] )
    # print(res)
    if res[0] <= res[1] : return res[0]
    if res[0] > res[1] : return res[1]



print('\n--------CORRECTNESS CHECK --------')

n , m = 2000, 1999
for k in range(0, m+1 , 1):
    c = calculate_trinomial_coefficient( n, m, k  )%10**20
    # c2 = calculate_trinomial_zeros( n, m, k   )
    c2 = get_trinomial_zeros( n, m, k   )
    tz = trailing_zeros(c)
    if tz != c2  :          # Condition, if not correct it will print !!1
        print('',str(k)+'.     n=', n,'     m=',m , '        k=',  k ,'       correct value= ' ,c,'       ', c2 )



print('get_trinomial_zeros : \t' ,get_trinomial_zeros(6,6,3) )
print(' get_trinomial_zeros : \t' ,get_trinomial_zeros(2000, 1800, 8 ) )


print('\n--------------------------TESTS------------------------------')
t1  = time.time()


def trinominal_layer(dim, zeros ) :
    znct = 0
    maxv = 0

    for i in range( dim+1 ):
        cnt = 0
        tmp = []
        for j in range( 0, i+1 ) :
            # print(i, j)
            c = int(calculate_trinomial_coefficient( dim, i, j  )) %10**12
            if c > maxv : maxv = c
            if c % 10**3 == 0 : cnt+=1
            tmp.append(c )
        for h in tmp :
            f = trailing_zeros(h)
            if f >= zeros :
                znct+=1
                cnt +=1
        print(str(i)+'.     ',tmp,'           ',  cnt)


    return print('\nAnswer : \t', znct ,'    maxv : ', maxv)

trinominal_layer(20, 2)


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------BRUTE FORCE TEST------------------------------')
t1  = time.time()


def  brute_force_test(layer, zeros ):
    n = layer
    gen_cnt = 0

    # for m in range(n-2, -1,-1) :
    for m in range(43750, n-1 ) :
    # for m in range(0, n+1 ) :
    # for m in range(41709, -1,  -1 ) :
        row_cnt = 0
        for k in range( m+1  ):
            c = calculate_trinomial_zeros( n, m, k  )%10**20
            if c >= zeros :
                row_cnt += 1
                # print(str(row_cnt)+'.     n=', n,'     m=',m , '        k=',  k ,'       value= ' ,c,'        row_cnt=', row_cnt)

        gen_cnt += row_cnt

        print('++++++++ -------',m,'---------     gen_cnt : \t', gen_cnt,'       row_cnt :', row_cnt,'     +++++++++++' )
    return print('\nAnswer : \t', gen_cnt)

# brute_force_test(2*10**5, 12 )
# brute_force_test(20, 2 )


t2  = time.time()
print('\nCompleted in :', round((t2-t1),6), 's\n\n')

print('\n================  My FIRST SOLUTION,   ===============\n')
t1  = time.time()

# I must build a sieve with precomputed values of combinations of factorials
# since 200.000 is always up we just calculate it  not once
# Again, we must find the cross terms, no need to calculate them all.
# Besides that we use only half of each row . Here we gain a speed x2 times

# @ 2017-03-03, 22:22. I lef that I must build a sieve with precomputed values of C(200000, )
# which will be constructed for the function get_trinomial_zeros which will take the values from the sieve
# Only after that we can hope in a reasonable timed brute force 2-3 hours


def  smart_brute_force(layer, zeros ):
    n = layer
    gen_cnt = 0
    priv = False
    D = build_precalculated_zeroes_sieve(layer)

    # for m in range(n, -1,-1) :
    # for m in range(43750, n-1 ) :
    # for m in range(0, n-1 ) :
    # for m in range(0, n+1 ) :
    for m in range(41750, -1,  -1 ) :
        row_cnt, p_cnt = 0 , 0
        for k in range( m//2+1  ):
            c = zeros_trinomial( n, m, k ,D  )
            if c >= zeros :
                row_cnt += 1
                # print(str(row_cnt)+'.     n=', n,'     m=',m , '        k=',  k ,'       value= ' ,c,'        row_cnt=', row_cnt)
                if k == m/2 : priv = True

        if m % 2 == 1 :
            p_cnt += 2*row_cnt
        if m % 2 == 0 :
            if row_cnt > 0 :
                if priv == False :  p_cnt += 2*row_cnt
                if priv == True :  p_cnt += 2*row_cnt-1
        gen_cnt += p_cnt
        priv = False
        # print('++++++++ -------',m,'---------     gen_cnt : \t', gen_cnt,'       row_cnt :', p_cnt,'     +++++++++++' )
        print('row = ',m,'     row_cnt= ', row_cnt,'       gen_cnt :', gen_cnt )
    return print('\nAnswer : \t', gen_cnt)

smart_brute_force(2*10**5, 12 )         #   Answer : 	 479742450


# smart_brute_force(20, 2)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)/60, 6), 'min\n\n')

##### GOOOD IDEAS ###########
# Use Legendre's Theorem :        http://mathbmt.com/legendretheo

# ==== Fri, 18 Sep 2009, 06:11, Seth Troisi, USA
#coefficients of expansion of (x+y+z)^200000
#	there are 200001*200002/2 terms = 20000300001 terms
#the 200,000 row of pascals pyramid
#each term has coefficent of (a+b+c)!/(a!b!c!)x^a*y^b*z^c
#how do you make 200,000!/(a!b!c!) %= 10^12

#200000!/(a!b!c!) factors must have 2^12,5^12
#200000 factors to 2^199994 * 5^49998 ...
#we only care about factors of 2 and 5
#so check a!b!c! for factors of 2 \ 5
#	for all a,b,c that satify
#		a + b + c = 200,000
#		a >= b >= c
#		a >= 66,667


print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n-------------------- SOLUTION 1,  5 min, GREAT GREAT SOLUTION, Must study it  --------------------------')
t1  = time.time()


# ==== Sat, 25 Feb 2012, 08:18, ving, USA
# Brute force for c <= b <= a; a + b + c = N.
# C(a, b, c) = N! / (a! * b! * c!)
#
# I precomputed powers of 2 and 5 that divide factorials.  One important optimization:
# if d = power of 5 that divides N! - powers of 5 that divide a! + b! + c! < 12,
# I decrement b not by 1, but by b % p5 + 1, where
# p5 = 5^(12-d).
#
# Still almost 4 mins in very slow Python on my very slow machine.
#
# The most fun part was precomputing tables for powers of 2 and 5 that divide factorials using list comprehensions...


def solution_1():
    N = 200000

    facts5 = [0, 0, 0, 0, 0] # facts5[n] = the highest power of 5 that divides n!
    d = 1
    while len(facts5) < N:
        facts5 += [f+d for f in facts5] + [f+2*d for f in facts5] + \
                  [f+3*d for f in facts5] + [f+4*d for f in facts5]
        d = 5*d + 1

    facts2 = [0, 0] # facts2[n] = the highest power of 2 that divides n!
    d = 1
    while len(facts2) < N:
        facts2 += [f+d for f in facts2]
        d = 2*d + 1

    count = 0

    a = N//3 + 1
    while a <= N:
        if a % 10000 == 0:
            print(a, count)

        # Keep c <= b <= a; a + b + c = N

        b = min(a, N - a)
        c = N - a - b

        d0 = facts5[N] - facts5[a]

        while c <= b:
            d =  d0 - (facts5[b] + facts5[c])
            if d >= 12:
                d = facts2[N] - (facts2[a] + facts2[b] + facts2[c])
                if d >= 12:
                    if c < b < a:
                        count += 6
                    else:    # if c = b < a or c < b = a;
                        count += 3
                    # c = b = a never happens since N % 3 != 0;
                    #   if it did, would increment count by 1
                c += 1
                b -= 1
            else:
                p5 = 5**(12 - d)
                b -= (b % p5 + 1)
                c = N - a - b
        a += 1

    return print(count)  # Answer: 479742450 (at a = 70000 2764461)


t2  = time.time()
print('\nCompleted in :', round((t2-t1)/60, 6), 'min\n\n')

print('\n--------------------------SOLUTION 2,    --------------------------')
t1  = time.time()

# === Wed, 7 Jan 2009, 21:29, tolstopuz, Russia
# About 5'20" on E8400

def gen(n, p):
    f = (n + 1) * [0]
    for i in range(1, len(f)):
        j, c = i, 0
        while j % p == 0:
            j //= p
            c += 1
        f[i] = f[i-1] + c
    return f

n = 200000
n5 = [2,2,4,0,0,0,0,0]
t = 12
f2 = gen(n, 2)

def y(nn, p, k, l = 0, carry = 0, a = 0, b = 0, c = 0, cnt = 0):
    for c2 in range(max(0, k - 2 * max(len(nn) - l - 2, 0)), 1 if l == len(nn) - 1 else 3):
        d = carry * p + nn[l] - c2
        for aa in range(max(0, d - 2 * (p - 1)), min(p, d + 1)):
            for bb in range(max(0, d - aa - (p - 1)), min(p, d - aa + 1)):
                for cc in range(max(0, d - aa - bb), min(p, d - aa - bb + 1)):
                    an, bn, cn = a * p + aa, b * p + bb, c * p + cc
                    if an <= bn <= cn:
                        if l + 1 == len(nn):
                            if f2[n] - f2[an] - f2[bn] - f2[cn] >= t:
                                cnt += 1 if an == cn else 3 if an == bn or bn == cn else 6
                        else:
                            cnt = y(nn, p, k - c2, l + 1, c2, an, bn, cn, cnt)
    return cnt

print(y(n5, 5, t))

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
