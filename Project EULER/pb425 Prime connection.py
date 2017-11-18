#  Created by Bogdan Trif on 16-10-2017 , 4:51 PM.
# © o(^_^)o  Solved by Bogdan Trif  @
#The  Euler Project  https://projecteuler.net
'''
                Prime connection        -       Problem 425

Two positive numbers A and B are said to be connected (denoted by "A ↔ B") if one of these conditions holds:
(1) A and B have the same length and differ in exactly one digit; for example, 123 ↔ 173.
(2) Adding one digit to the left of A (or B) makes B (or A); for example, 23 ↔ 223 and 123 ↔ 23.

We call a prime P a 2's relative if there exists a chain of connected primes between 2 and P and no prime in the chain exceeds P.

For example, 127 is a 2's relative. One of the possible chains is shown below:
2 ↔ 3 ↔ 13 ↔ 113 ↔ 103 ↔ 107 ↔ 127

However, 11 and 103 are not 2's relatives. !

=== CASE 103
Because 103 --> 101 --> 01     Wrong --> because we can't make primes of 3 digits larger than 103 the only possibility for
 a prime < 103 is 101. Also if we cut on left we remain with 03. Wrong
 === CASE 11
 Wrong ---> because we can't make primes of 2 digits > 11 and if we cut on left => 1 which is not a primes !

Let F(N) be the sum of the primes ≤ N which are not 2's relatives.
We can verify that F(10^3) = 431 and F(10^4) = 78728.

Find F(10^7).

'''
import time, zzz

import itertools
import numpy
# @2017-11-09 - We must start the other way around. From 127 to 2

def prime_sieve_numpy(n):                       ### o(^_^)o  FASTEST  o(^_^)o  ###  Highly Efficient !!!
    """ Input n>=6, Returns a array of primes, 2 <= p < n
    http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n/3035188#3035188 """
    sieve = numpy.ones(n//3 + (n%6==2), dtype=numpy.bool)
    for i in range(1,int(n**0.5)//3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[       k*k//3     ::2*k] = False
            sieve[k*(k-2*(i&1)+4)//3::2*k] = False
    return numpy.r_[2,3,((3*numpy.nonzero(sieve)[0][1:]+1)|1)]



print('\n--------------------------TESTS------------------------------')
t1  = time.time()

lim = 10**3
primes =  prime_sieve_numpy(lim)[4:]
P = set(primes)

print(primes[:1000],' \n')

# Enemy = [11, 17, ]
# for i in primes[4:] :
#     if str(i).find('2') != 0 :
#         s = str(i)
#         flag = 0
#         for j in range(0, len(s) ) :
#             for k in range(1,10) :
#                 new_s = s[0:j] + str(k) + s[j+1:]
#                 if int(new_s) in P :
#                     # print(s, new_s)
#                     flag +=1
#         if flag == 0 :
#             Enemy.append(i)
#             print(i)
#
# print(Enemy)



D = { 3, 5, 7 }
E = { 11, 101, 103 }
# D = { 3, 5, 7, 37, 131, 137 }
def is_two_relative(p, ref_prime ,D, E):

    if p in D and p < ref_prime :
        D.add(ref_prime)
        return True



    l = len(str(p))

    # print('max digit = ', max( [int(i) for i in list(str(p)) ] )  , [int(i) for i in list(str(p))]   )

    if  max([int(i) for i in list(str(p))]) <= 1 :
        lst = ['3', '7', '9']
        for j in lst :
            p2 = int(str(p)[ :len(str(p))-1]+j)
            print('new p2 =  ', p2 ,'       ref_prime = ', ref_prime)
            if  p2 < ref_prime :     # we form new prime , eg. from 11 we form 13, 17, 19
                if int(str(p2)[1:]) in D :
                    D.add(ref_prime)
                    return True
        # E.add(p)
        return False


    # We first try to remove the leftmost digit :
    if  str(p)[1] != '0' and  int( str(p)[1:]  ) in D :
        print('We first check if prime by removing leftmost digit :  ' ,str(p)[1:]  )
        D.add(ref_prime)
        # print(D)
        return True

    dig_index = l
    while dig_index >= 1:
        # print(dig_index)
        if p == ref_prime and dig_index == l :
            rng = int(str(p)[l-1])-1
        else : rng = 9

        for i in range(rng, -1, -1 ) :
            p1 = int(str(p)[ : dig_index-1]+ str(i) + str(p)[dig_index : ])
            print(i,'       ' ,p1)
            if p1 in D and p1 < ref_prime :   # check if is a connection
                D.add(ref_prime)
                return True
            # Do not put include E

            if p1 in primes and p1 < ref_prime :   # check only if is prime and < than original prime
                return is_two_relative(p1, ref_prime , D, E )

        dig_index -=1

    # E.add(ref_prime)
    return False

    # lst = [ i for i in lst if i < last_dig ]
    # print(lst)

    # if len(lst) > 0 :
    #     for i in lst :
    #         print('yes we pass by here !')
    #         rp = int( str(p)[:len(str(p))-1 ] + str(i) )
    #         if rp in P :        # is_prime check !
    #             new_p = int( str(rp)[1:]  )         # we cut the leftmost digit
    #             # print(rp, new_p)
    #             if new_p in D :
    #                 D.add(rp)
    #                 return True
    #
    #             for X in itertools.product(range(0, 9+1), repeat = l-2 ) :
    #                 print(X)
    #                 middle = ''.join(str(i) for i in X)
    #                 new_p = middle+str(i)
    #                 if new_p in D :
    #                     D.add(rp)
    #                     return True
    #

# @2017-11-09 - I left here. the function doesn't work for case 181 because I must substitute the inner digit and
# make checks and also because is a special case as it finishes with 1
# but I am on the good track !

    # LEFTMOST DIGIT  Case
    #     if last_dig == '9' : lst = [7, 3, 1]
    #     if last_dig == '7' : lst = [3, 1]
    #     if last_dig == '3' : lst = [1]
    #
    #     for i in lst :
    #         rp = int( str(p)[:len(str(p))-1 ] + str(i) )
    #         if rp in P :        # is_prime check !
    #             new_p = int( str(rp)[1:]  )
    #             # print(rp, new_p)
    #             if new_p in D :
    #                 D.add(rp)
    #                 return True

Motherfucker nu-mi iese recursia la cazul 107. Nu am nici o idee cum sa fixez si m-am
not saturat

print('is_two_relative : '  ,is_two_relative(107, 107 , D, E ) ,'\n ')
print('D : ', D)
print('E :  ',E)



# S = 0
# for p in primes :
#     check =  is_two_relative( p, p, D, E )
#     print('-------------------------\n','prime = ' , p )
#     print('D : ',D)
#     print('E : ',E)


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




