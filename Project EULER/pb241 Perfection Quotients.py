#!/usr/bin/python                   o(^_^)o         ( ͡° ͜ʖ ͡°)
# © Solved by Bogdan Trif @
#The  Euler Project  https://projecteuler.net
'''
            Perfection Quotients        -       Problem 241

For a positive integer n, let σ(n) be the sum of all divisors of n, so e.g. σ(6) = 1 + 2 + 3 + 6 = 12.

A perfect number, as you probably know, is a number with σ(n) = 2n.

Let us define the perfection quotient of a positive integer as	p(n)	= 	σ(n) / n .

Find the sum of all positive integers n ≤ 10**18 for which p(n) has the form k + 1⁄2, where k is an integer.


'''
import time, zzz, sys
from gmpy2 import is_prime, mpq
from math import log
from operator import mul
from functools import  reduce
from itertools import combinations, combinations_with_replacement

def count_elem(lst):        # Nice function, made by Bogdan Trif @ 2017-04-09, 13:30
    X = []
    for i in set(lst):
        # print(i, lst.count(i), end='; ')
        X.append((i, lst.count(i) ))
    return X

def divisor_sum_sigma(n):       #   σ(n)
    '''    **Π  = [(p_1**(a_1+1)-1) / (p_1 -1)]*...*[ (p_k**(a_k+1)-1) / (p_k -1) ]**
     condensed :  = **Π  {p_k - prime, a_k - the exp of the prime } =  ((p_k**(a_k+1)-1) / (p_k -1)**
    :where: p_1, p_2,...p_k are the prime factors of the number , together with their
    corresponding coefficients exponentials a_1, a_2,...,a_k
        :param n: int, number
        :return: int, sigma representing the Sum of its divisors !              '''
    # https://en.wikipedia.org/w/index.php?title=Divisor_function&action=edit&section=4
    from pyprimes import factorise
    import functools, operator
    D = list(factorise (n ))
    P = [( i[0]**(i[1]+1)-1 ) //(i[0]-1) for i in D ]
    # print(D)
    return functools.reduce(operator.mul, P)


def get_factors(n):       ### o(^_^)o  FASTEST  o(^_^)o  ###
    ''' Decompose a factor in its prime factors. This function uses the pyprimes module. THE FASTEST  '''
    from pyprimes import factorise
    return [val for sublist in [[i[0]]*i[1] for i in factorise(n)] for val in sublist]

def prime_sieve_generator(lower, upper):      #FIFTH FASTEST
    """  Sieve of Eratosthenes
    Create a candidate list within which non-primes will be marked as None.         """
    cand = [i for i in range(3, upper + 1, 2)]
    end = int(upper ** 0.5) // 2

    # Loop over candidates (cand), marking out each multiple.
    for i in range(end):
        if cand[i]:
            cand[cand[i] + i::cand[i]] = [None] * ( (upper // cand[i]) - (upper // (2 * cand[i])) - 1 )

    # Filter out non-primes and return the list.
    return  [ i for i in cand if i and i > lower ]

print('\n--------------------------TESTS------------------------------')
t1  = time.time()

print('Maximum number of 2_s  : \t'  ,log(10**18, 2) ,'\n'  )

def brute_force(start ,up_lim, mod ) :
    start = start - ( start%mod )
    h=1
    for n in range( start, up_lim, mod ) :
        p = mpq( divisor_sum_sigma(n) , n )
        # print(n)
        if p.denominator == 2 :
            print(str(n)+'.      σ=', divisor_sum_sigma(n)  ,'         p=',p ,'       ', get_factors(n) )

        if n*100 //up_lim  > h-1 :        # Progress Bar #
            h += 1
            sys.stdout.write('\r' + str(h)+' % ['+'#'*h+str(' ')*(220-22*h//10) +']' )   # Font Segoe UI Semibold




# brute_force(10**13 , 10**15, 4193280 )

#       131040


# ======    OBSERVATIONS !!! @ 2017-03-26, 19:00   =====
# 1.  All the numbers are multiples of 24 = [2,2,2, 3]

# 3. the approach to solve this problem is to make lists of twos with other prime numbers and see
# if they solve aour condition ! Here we have an advantage as we now that we have ODD two's  !!
# 4. On forum say that are at least 21 numbers. I estimate there are no more than 25
# 5. There are at least 2 three's except the number 24. Therefore we can add always two threes. ' \
#         All the higher numers, > 1000 are  % 72


# 2      σ= 3          p= 3/2         [2]                               --> 1   two's
# 24      σ= 60          p= 5/2         [2, 2, 2, 3]                            --> 3
# 4680      σ= 16380          p= 7/2         [2, 2, 2, 3, 3, 5, 13]            --> 3
# 4320      σ= 15120          p= 7/2         [2, 2, 2, 2, 2, 3, 3, 3, 5]       --> 5
# 26208      σ= 91728          p= 7/2         [2, 2, 2, 2, 2, 3, 3, 7, 13]         --> 5
# 17428320      σ= 78427440          p= 9/2         [2, 2, 2, 2, 2, 3, 3, 5, 7, 7, 13, 19]             --> 5
# 8910720      σ= 40098240          p= 9/2         [2, 2, 2, 2, 2, 2, 2, 3, 3, 5, 7, 13, 17]           --> 7
# 91963648     σ= 229909120       p2(n)= 5/2           [2, 2, 2, 2, 2, 2, 2, 2, 7, 19, 37, 73]              --> 8
# 197064960     σ= 689727360       p2(n)= 7/2           [2, 2, 2, 2, 2, 2, 2, 2, 3, 5, 19, 37, 73]          --> 8
# 20427264      σ= 71495424          p= 7/2         [2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 11, 13, 31]          --> 9
# 8583644160      σ= 38626398720          p= 9/2         [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 5, 7, 13, 23, 89]            --> 10
# 57629644800     σ= 259333401600       p2(n)= 9/2           [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 5, 5, 7, 7, 13, 19, 31]           --> 11
# 206166804480      σ= 927750620160          p= 9/2         [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 5, 7, 13, 13, 31, 61]          --> 11
# 17116004505600      σ= 94138024780800          p= 11/2         [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 5, 5, 7, 7, 11, 13, 19, 31]     --> 11
# 57575890944      σ= 201515618304          p= 7/2         [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 11, 13, 43, 127]          --> 13
# 10200236032     σ= 25500590080       p2(n)= 5/2           [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 7, 19, 31, 151]              --> 14
# 21857648640     σ= 76501770240       p2(n)= 7/2           [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 5, 19, 31, 151]           --> 14
# 1416963251404800     σ= 6376334631321600       p2(n)= 9/2           [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 5, 5, 11, 17, 31, 43, 257]      --> 15
# 15338300494970880     σ= 69022352227368960       p2(n)= 9/2           [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 5, 7, 19, 19, 37, 73, 127]  --> 17

t2  = time.time()
print('\nCompleted in :', round((t2-t1)/60,6), 'min\n\n')

print('\n================  My FIRST SOLUTION,   ===============\n')
t1  = time.time()



# P20_100 = prime_sieve_generator(20, 100)
# P20_300 = prime_sieve_generator(2, 100)
# P20_1000 = prime_sieve_generator(20, 300)
# print(len(P20_100), P20_100,'\n' )
# print(len(P20_300), P20_300,'\n' )
# print(len(P20_1000), P20_1000,'\n' )

P10 = [ 5, 7 ]
P20 = [ 11, 13, 17, 19 ]

P300 =  prime_sieve_generator(20, 300)
print(len(P300), P300,'\n')

P1000 =  prime_sieve_generator(100, 1000)
print(len(P1000), P1000,'\n')


def main_function() :
    SET = {17116004505600, 57629644800, 206166804480, 8583644160, 20427264, 197064960, 91963648, 8910720,
           4680, 17428320, 2, 4320, 1416963251404800, 15338300494970880, 26208, 10200236032, 21857648640, 24, 57575890944}
    scnt = 0
    cnt, S = 0, 0
    for a in range(13, 25) :             # 2
        print(  '-------    ',a,'   -----------'  )
        if a <= 10 :
            b_rng = 4
            d_rng = 3
        if a > 10 :
            b_rng = 5
            d_rng = 4
        if a <= 12 :
            e_rng = 3
        if a > 12 :
            e_rng = 5

        for b in range(0, b_rng) :          # 3
            N = [ (2, a), (3, b) ]

            for c in range(0, 5):           #   P10  = [ 5, 7 ]
                for i1 in combinations_with_replacement( P10 , c) :
                    I1 =  count_elem(i1)
                    N1 = N[:]
                    if c > 0 :  N1 = N + I1
                    # print(I1,'              ', N1)
                    D1 = [( i[0]**(i[1]+1)-1 ) //(i[0]-1) for i in N1 ]
                    dss = reduce(mul, D1)
                    n = reduce (mul,  [i[0]**i[1] for i in N1 ] )
                    p = mpq( dss , n )
                    scnt += 1
                    if scnt %10**7 == 0 : print('__', scnt // 10**7,   '     set=' , len(SET), '     ' ,sum(SET),'    ',SET  )
                    if p.denominator == 2 and n <= 10**18 :
                        cnt+=1
                        SET.add(n)
                        print(str(cnt)+'.        n= ', n, '    σ=', dss,'      p(n)=',p ,'         ', get_factors(n)  )

                    for d in range(0, d_rng) :          # 20    --->  P20 = [ 11, 13, 17, 19 ]
                        for i2 in combinations_with_replacement(P20 , d) :
                            I2 =  count_elem(i2)
                            N2 = N1[:]
                            # print(I2,'              ', N2)
                            if d > 0 :  N2 = N1 + I2
                            D2 = [( i[0]**(i[1]+1)-1 ) //(i[0]-1) for i in N2 ]
                            dss2 = reduce(mul, D2)
                            n2 = reduce (mul,  [i[0]**i[1] for i in N2 ] )
                            p2 = mpq( dss2 , n2 )
                            scnt += 1
                            if scnt %10**7 == 0 : print('__', scnt // 10**7,   '     set=' , len(SET), '     ' ,sum(SET),'    ',SET  )
                            if p2.denominator == 2 and n2 <= 10**18 :
                                cnt+=1
                                SET.add(n2)
                                print(str(cnt)+'.        n2= ', n2, '    σ=', dss2,'      p2(n)=',p2  , '         ', get_factors(n2)  )

                            for e in range(0, e_rng) :      # 300
                                for i3 in combinations_with_replacement(P300 , e) :
                                    I3 =  count_elem(i3)
                                    N3 = N2[:]
                                    if e >0  :  N3 =  N2 + I3
                                    # print(I3,'              ', N3)
                                    D3 = [( i[0]**(i[1]+1)-1 ) //(i[0]-1) for i in N3 ]
                                    dss3 = reduce(mul, D3)
                                    n3 = reduce (mul,  [j[0]**j[1] for j in N3 ] )
                                    p3 = mpq( dss3 , n3 )
                                    scnt += 1
                                    if scnt %10**7 == 0 : print('__', scnt // 10**7,   '     set=' , len(SET), '     ' ,sum(SET),'    ',SET  )
                                    if p3.denominator == 2 and n3 <= 10**18 :
                                        cnt+=1
                                        SET.add(n3)
                                        print(str(cnt)+'.        n3= ', n3, '    σ=', dss3,'      p3(n)=',p3  , '         ', get_factors(n3)  )

                                    # if a > 10 :
                                    #     for f in P1000 :
                                    #         I4 =  (f, 1)
                                    #         N4 = N3 + [ I4 ]
                                    #         D4 = [( i[0]**(i[1]+1)-1 ) //(i[0]-1) for i in N4 ]
                                    #         dss4 = reduce(mul, D4)
                                    #         n4 = reduce (mul,  [i[0]**i[1] for i in N4 ] )
                                    #         p4 = mpq( dss4 , n4 )
                                    #         scnt += 1
                                    #         if scnt %10**7 == 0 : print('__', scnt // 10**7,   '     set=' , len(SET), '     ' ,sum(SET),'    ',SET  )
                                    #         if p4.denominator == 2 and n4 <= 10**18 :
                                    #             cnt+=1
                                    #             SET.add(n4)
                                    #             print(str(cnt)+'.        n4= ', n4, '    σ=', dss4,'      p4(n)=',p4  , '         ', get_factors(n4)  )
                                    #
                                    #
                                    #         N5 = N2 + [ I4 ]
                                    #         D5 = [( i[0]**(i[1]+1)-1 ) //(i[0]-1) for i in N5 ]
                                    #         dss5 = reduce(mul, D5)
                                    #         n5 = reduce (mul,  [i[0]**i[1] for i in N5 ] )
                                    #         p5 = mpq( dss5 , n5 )
                                    #         scnt += 1
                                    #         if scnt %10**7 == 0 : print('__', scnt // 10**7,   '     set=' , len(SET), '     ' ,sum(SET),'    ',SET  )
                                    #         if p4.denominator == 2 and n4 <= 10**18 :
                                    #             cnt+=1
                                    #             SET.add(n5)
                                    #             print(str(cnt)+'.        n5= ', n5, '    σ=', dss5,'      p5(n)=',p5  , '         ', get_factors(n5)  )



                                    #
                                    #             if a >10 :
                                    #                 for g in range(1, 3) :
                                    #                     for i5 in combinations_with_replacement(P300 , g) :
                                    #                         I5 =  count_elem(i5)
                                    #                         N5 = N4 + I5
                                    #                         D5 = [( i[0]**(i[1]+1)-1 ) //(i[0]-1) for i in N5 ]
                                    #                         dss5 = reduce(mul, D5)
                                    #                         n5 = reduce (mul,  [i[0]**i[1] for i in N5 ] )
                                    #                         p5 = mpq( dss5 , n5 )
                                    #                         scnt += 1
                                    #                         if scnt %10**7 == 0 : print('__',scnt // 10**7, '     set=', sum(SET),'    ',SET  )
                                    #                         if p5.denominator == 2 and n5 <= 10**18 :
                                    #                             cnt+=1
                                    #                             SET.add(n5)
                                    #                             print(str(cnt)+'.        n5= ', n5, '    σ=', dss5,'      p5(n)=',p5  , '         ', get_factors(n5)  )

        # for b in range(0, 7) :              # 3
        #     for c in range(0, 4) :              # 5
        #         for d in range(0, 3) :            # 7
        #             for e in range(0, 2) :           # 11
        #                 for f in range(0, 3) :           # 13
        #                     for g in range(0, 3) :           # 17
        #                         for h in range(0, 3) :           # 19
        #                             N = [ (2, a), (3, b), (5, c), (7, d), (11, e), (13, f), (17,g), (19, h)  ]
        #                             D = [( i[0]**(i[1]+1)-1 ) //(i[0]-1) for i in N ]
        #                             dss = reduce(mul, D)
        #                             n = reduce (mul,  [i[0]**i[1] for i in N ] )
        #                             p = mpq( dss , n )
        #                             if p.denominator == 2 and n <= 10**18 :
        #                                 cnt+=1
        #                                 SET.add(n)
        #                                 print(str(cnt)+'.        n= ', n, '    σ=', dss,'      p(n)=',p ,'         ', get_factors(n)  )
        #                             if a >= 8 :
        #                                 for i in range( len(P20_100)) :           #  23- 100
        #                                     scnt += 1
        #                                     N2 = N + [ (P20_100[i], 1) ]
        #                                     D2 = [( i[0]**(i[1]+1)-1 ) //(i[0]-1) for i in N2 ]
        #                                     dss2 = reduce(mul, D2)
        #                                     n2 = reduce (mul,  [i[0]**i[1] for i in N2 ] )
        #                                     p2 = mpq( dss2 , n2 )
        #                                     if p2.denominator == 2 and n2 <= 10**18 :
        #                                         cnt+=1
        #                                         SET.add(n2)
        #                                         print(str(cnt)+'.        n2= ', n2, '    σ=', dss2,'      p2(n)=',p2  , '         ', get_factors(n2)  )
        #                                     for j in range(i , len(P20_300)) :           #  23- 100
        #                                         scnt += 1
        #                                         N3 = N2 + [ (P20_300[j], 1) ]
        #                                         D3 = [( i[0]**(i[1]+1)-1 ) //(i[0]-1) for i in N3 ]
        #                                         dss3 = reduce(mul, D3)
        #                                         n3 = reduce (mul,  [i[0]**i[1] for i in N3 ] )
        #                                         p3 = mpq( dss3 , n3 )
        #                                         if p3.denominator == 2 and n3 <= 10**18 :
        #                                             cnt+=1
        #                                             SET.add(n3)
        #                                             print(str(cnt)+'.        n3= ', n3, '    σ=', dss3,'      p3(n)=',p3  , '         ', get_factors(n3)  )
        #                                         for k in range(j, len(P20_1000)) :           #  23- 300
        #                                             scnt += 1
        #                                             N4 = N3 + [ (P20_1000[k], 1) ]
        #                                             D4 = [( i[0]**(i[1]+1)-1 ) //(i[0]-1) for i in N4 ]
        #                                             dss4 = reduce(mul, D4)
        #                                             n4 = reduce (mul,  [i[0]**i[1] for i in N4 ] )
        #                                             p4 = mpq( dss4 , n4 )
        #                                             if p4.denominator == 2 and n4 <= 10**18 :
        #                                                 cnt+=1
        #                                                 SET.add(n4)
        #                                                 print(str(cnt)+'.        n4= ', n4, '    σ=', dss4,'      p2(n)=',p4  , '         ', get_factors(n4)  )
        #
        #                                             if scnt %10**7 == 0 : print('__',scnt // 10**7, '        set=', sum(SET),'    ',SET  )
        #
        #
        #                                             for l in range(k, len(P20_300)) :           #  23- 300
        #                                                 scnt += 1
        #                                                 N7 = N4 + [ (P20_300[l], 1) ]
        #                                                 D7 = [( i[0]**(i[1]+1)-1 ) //(i[0]-1) for i in N7 ]
        #                                                 dss7 = reduce(mul, D7)
        #                                                 n7 = reduce (mul,  [i[0]**i[1] for i in N7 ] )
        #                                                 p7 = mpq( dss7 , n7 )
        #                                                 if p7.denominator == 2 and n7 <= 10**18 :
        #                                                     cnt+=1
        #                                                     SET.add(n7)
        #                                                     print(str(cnt)+'.        n7= ', n7, '    σ=', dss7,'      p2(n)=',p7  , '         ', get_factors(n7)  )
        #
        #                                                 if scnt %10**7 == 0 : print('__',scnt // 10**7, '        set=', sum(SET),'    ',SET  )
        #
        #                                             if P20_1000[k] > 100 :
        #                                                 scnt += 1
        #                                                 N5 = N + [ (P20_1000[k], 1) ]
        #                                                 D5 = [( i[0]**(i[1]+1)-1 ) //(i[0]-1) for i in N5 ]
        #                                                 dss5 = reduce(mul, D5)
        #                                                 n5 = reduce (mul,  [i[0]**i[1] for i in N5 ] )
        #                                                 p5 = mpq( dss5 , n5 )
        #                                                 if p5.denominator == 2 and n5 <= 10**18 :
        #                                                     cnt+=1
        #                                                     SET.add(n5)
        #                                                     print(str(cnt)+'.        n5= ', n5, '    σ=', dss5,'      p2(n)=',p5  , '         ', get_factors(n5)  )
        #
        #                                                 if scnt %10**7 == 0 : print('__',scnt // 10**7, '     set=', sum(SET),'    ',SET  )
        #
        #                                                 scnt += 1
        #                                                 N6 = N2+ [ (P20_1000[k], 1) ]
        #                                                 D6 = [( i[0]**(i[1]+1)-1 ) //(i[0]-1) for i in N6 ]
        #                                                 dss6 = reduce(mul, D6)
        #                                                 n6 = reduce (mul,  [i[0]**i[1] for i in N6 ] )
        #                                                 p6 = mpq( dss6 , n6 )
        #                                                 if p6.denominator == 2 and n6 <= 10**18 :
        #                                                     cnt+=1
        #                                                     SET.add(n6)
        #                                                     print(str(cnt)+'.        n6= ', n6, '    σ=', dss6,'      p2(n)=',p6  , '         ', get_factors(n6)  )
        #
        #                                                 if scnt %10**7 == 0 : print('__',scnt // 10**7, '        set=', sum(SET),'    ',SET  )


    return print('\nAnswer : \t',  sum(SET), '\n', SET )

main_function()

# FAILED :
#  1553738503452802
# 16772742100580482


t2  = time.time()
print('\nCompleted in :', round((t2-t1)/3600,6), 'hours\n\n')


# print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
# print('\n--------------------------SOLUTION 1,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 2,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 3,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
#
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

