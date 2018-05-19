#  Created by Bogdan Trif on 18-05-2018 , 11:15 PM.
# © o(^_^)o  Solved by Bogdan Trif  @
#The  Euler Project  https://projecteuler.net
'''
                Strong Achilles Numbers         -           Problem 302

A positive integer n is powerful if p^2 is a divisor of n for every prime factor p in n.

A positive integer n is a perfect power if n can be expressed as a power of another positive integer.

A positive integer n is an Achilles number if n is powerful but not a perfect power.

For example, 864 and 1800 are Achilles numbers: 864 = 2^5·3^3 and 1800 = 2^3·3^2·5^2.

We shall call a positive integer S a Strong Achilles number if both S and φ(S) are Achilles numbers. (1)

For example, 864 is a Strong Achilles number: φ(864) = 288 = 2^5·3^2. However,

1800 isn't a Strong Achilles number because: φ(1800) = 480 = 2^5·3^1·5^1.

There are  :
7 Strong Achilles numbers below 10^4       and
656     below 10^8.

How many Strong Achilles numbers are there below 10^18?

(1) φ denotes Euler's totient function.


'''
import time, zzz
from pyprimes import factorise
from gmpy2 import is_square
from math import gcd

def get_factors(n):       ### o(^_^)o  FASTEST  o(^_^)o  ###
    ''' Decompose a factor in its prime factors. This function uses the pyprimes module. THE FASTEST  '''

    # return [val for sublist in [[i[0]]*i[1] for i in factorise(n)] for val in sublist]
    return list(factorise(n))

def euler_totient( dict_list_int ):           # Remark : For large array better use Sieve approach
    """ **©** Made by Bogdan Trif @ 2017-02-08 .
    returns Euler totient (phi) of n = Φ (n)
        Uses the formula of the Totient  : Φ (n) =  Π {p | n}  n *(1 - 1/p) ;
        where p are each prime factors and n is the number  for which we compute
        In number theory, Euler's totient function counts the positive integers up to a given integer n
        that are relatively prime to n. It is written using the Greek letter phi as φ(n) or ϕ(n),
        and may also be called Euler's phi function.
        Example : Φ (12) = 4 =   [1,5,7,11]
        https://en.wikipedia.org/wiki/Euler's_totient_function
        http://marcharper.codes/2015-08-07/totients.html
        :D: is a dictionary of the form {p1:k1, p2:k2...}. E.g : for 90 = {2:2, 3:2, 5:1 }
        or it is a list of the form 180 = [2, 2, 3, 3, 5 ]
        or it is an INT number
        """
    if type(dict_list_int) == dict :
        pfs = [ i for i in dict_list_int ]
        phi = 1
        for a in  [ i**j for i,j in dict_list_int.items() ] :
            phi *= a
    if type(dict_list_int) == list :
        pfs = set(dict_list_int)
        phi = 1
        for a in dict_list_int :
            phi *= a
    if type(dict_list_int) == int :
        pfs = [ i[0] for i in factorise(dict_list_int)]
        phi = dict_list_int

    for pf in pfs:
        phi *= (1-1/pf)
    return int(phi)






print('\n--------------------------TESTS------------------------------')
t1  = time.time()

def is_Strong_Achilles(n) :     # Very bad function !!! Shame on you !!
    Fn = get_factors(n)
    n_tot = euler_totient(n)
    if is_square(n_tot) or is_square(n) :
        return False

    Ftot = get_factors(n_tot)

    # gcd1 = [ gcd( Fn[i][1], Fn[i+1][1] ) for i in range(len(Fn) -1 )  ]
    # gcd2 = [ gcd( Ftot[i][1], Ftot[i+1][1] ) for i in range(len(Ftot) -1 )  ]
    #
    #
    # # print('gcd1 = ', gcd1, '     gcd2 = ', gcd2  )
    #
    # if set( gcd1  ) == {1} and set(gcd2) == {1} :
    #     return True

    power_n = [ i[1] for i in Fn ]
    power_n_tot = [ i[1] for i in Ftot ]
    # print('power_n = ', power_n, set(power_n) ,'    power_n_tot = ', power_n_tot, set(power_n_tot)  )

    if len(set(power_n)) ==1 or len(set(power_n_tot)) ==1 :
        return False

    test_n = [ 1 for i in power_n if i ==1 ]
    test_n_tot = [ 1 for i in power_n_tot if i ==1 ]

    # print('Fn =' ,Fn, '     Ftot = ', Ftot )

    if (1 in test_n ) or (1 in test_n_tot)  :
        return False

    for k in range( len(power_n)-1 ) :
        if gcd( power_n[k], power_n[k+1] ) !=1 :
            return False

    for l in range( len(power_n_tot)-1 ) :
        if gcd( power_n_tot[l], power_n_tot[l+1] ) !=1 :
            return False

    pow_n = [ i[1]%2 for i in Fn ]
    pow_n_tot = [ i[1]%2 for i in Ftot ]
    # print( '    test_n= ', test_n  , '    test_n_tot= ', test_n_tot  , '    pow_n= ', pow_n  , '    pow_n_tot= ', pow_n_tot )
    if sum(pow_n) > 0 and sum(pow_n_tot) > 0 :
        return True

    return False

n = 5832
n_tot = euler_totient(n)
print('n= ', n ,' = ' , get_factors(n)   ,'\t\teuler_totient = ', n_tot ,'=\t' , get_factors(n_tot)   )

print('\nis_Achilles :  ', is_Strong_Achilles(n)  )

print('\n---------------- Naive Brute Force check ---------------')

def naive_brute_force_check( lim ) :
    S =set()
    cnt = 0
    i = 2
    while i*i < lim :
        j = 2
        while i*i*j < lim :
            n = i*i*j
            if is_Strong_Achilles(n)  :
                if n not in S :
                    S.add(n)
                    cnt+=1
                    n_tot = euler_totient(n)
                    print(str(cnt)+'.      n=', n, '   ', get_factors(n), '     n_tot = ', n_tot,'    ', get_factors(n_tot)   )
            j+=1
        i+=1

naive_brute_force_check(10**6)      # Algorithms works ok for limit 10**4 , 7 numbers !



# IDEA : @2018-05-18, 23:30
# Must start from the totient and form numbers. Decompose the totient and form valid numbers
# Here must be some clever tricks to reduce the search span.
# Must be also an algorithm < O( n^(1/2) )  maybe an algo like O( log(n) )  or something wouyld be ideal
# @2018-05-19, 1:15 --> I'm on the good track

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

