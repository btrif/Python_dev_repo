#!/usr/bin/python                   ( ͡° ͜ʖ ͡°)
# Solved by Bogdan Trif @
#The  Euler Project  https://projecteuler.net
'''
        Investigating numbers with few repeated digits      -       Problem 172

How many 18-digit numbers n (without leading zeros) are there
such that no digit occurs more than three (3) times in n?

'''
import time, gmpy2
from itertools import combinations, permutations
import numpy as np

def multiple_permutations(*args ) :
    ''' **©** Made by Bogdan Trif @ 2017-09-03, 12:15.
        Uses the formula Perm(total_elem_nr) / [ Perm(elem_1) *Perm(elem_2) * ...* Perm(elem_n) ]
    :param args:  the first arg is always the total number of elements, e.g. : for  the list [1, 1, 1, 1, 2, 2, 2 ,3, 3] = 9 elem ;
        The next elements will be in descending order the separate no of elem : 4 elem of '1' s , 3 elem of '2's , 2 elem of '3's
    :Explicit formula:      p = gmpy2.fac(9) // ( gmpy2.fac(4)*gmpy2.fac(3)*gmpy2.fac(2) )
    :return: int, Perm(total) / (Perm(elem_1) *Perm(elem_2) * ...* Perm(elem_n) )
    '''
    den = 1
    S=0          # the sum of all elements
    for i, j in enumerate(args) :
        # print(i,'    ', j,'     ' )
        if i == 0 :
            num = gmpy2.fac(j)
            N = j
        else :
            den *= gmpy2.fac(j)
            S += j
    # assert (N == S ) , "Total number of elements condition is not met !"
    if (N != S) :  raise ValueError ("Total number of elements condition is not met !")

    return (num // den)


def comb_L( k ) :
    S = 0
    for i in range(2, k+1):
        c = gmpy2.comb(k, i)
        # print(c, S)
        S+=c * 2**(k - i)
    return S

def comb_A(n) :
    k  = n-2
    return k * 3**(k-1) - (k-1)*3**(k-2)

# print('\ncomb_L : \t', comb_L(7))
# print('\ncomb_A : \t', comb_A(7))

#
#
# @ 2017-01-31, 00:40         -       Problema de combinatorica
# It is not enough to search only for a digit L , you must be sure that not a single digit
# repeats more than 3 times ! you can not cross results from every digit
#
#
# 18 digit :
# 123456789012345678
# Remark in a 30 digit : 123456789012345678901234567890    every digit repeats 3 times
# => You cannot have a 31 digit number which has not at least 1 repeated digit
#
#
# @2017-09-02 --> We start with the small cases and we generalize :
#    So we can have number like : 111.222.333.444.555.666 + 7, 8, 9



print('\n-------------------------- MANUAL TESTS------------------------------')
t1  = time.time()

print('multiple_permutations : \t' , multiple_permutations(18, 3, 3, 3, 3, 3, 3 ) )

# To use as verification for the MAIN  ALGORITHM !!

# === 4 digits ===
# there were found :   333     repeating digits numbers => Number of non-repeating nrs is : 	 8667

# === 5 digits ===
# there were found :   7704     repeating digits numbers => Number of non-repeating nrs is : 	 82296

# === 6 digits ===
# tthere were found :   142650     repeating digits numbers => Number of non-repeating nrs is : 	 757350


def manual_test_repeating_digits( nr_of_digits ) :
    d = nr_of_digits
    low_range = 10**(d-1)
    high_range = 10**(d)
    cnt = 0
    for i in range(low_range, high_range) :
        Nr = [int(j) for j in str(i) ]
        for k in range( 9, 10 ) :
            if Nr.count(k) == 3 :
                cnt += 1
                print(i,'        ',Nr ,'       ' , Nr.count(k))
    print('\nthere were found :  ' , cnt,'   repeating digits numbers')
    return print('Number of non-repeating nrs is : \t', 10**(d)-10**(d-1) - cnt   )


# manual_test_repeating_digits(5)


t2  = time.time()
print('\nCompleted in :', round((t2-t1),4), 's\n\n')


print('\n================  My FIRST SOLUTION,   ===============\n')
t1  = time.time()
# The formula is  ==> Perm(total_elem_nr) / [ Perm(elem_1) *Perm(elem_2) * ...* Perm(elem_n) ]

Main approach :
We must first find partitions of 18 and limit to something like (1...3) -->
18 = [3, 3, 3, 3, 2, 2, 1, 1] or [3, 3, 3 ,3, 2, 2, 2 ]or [3, 3, 3 ,3, 1, 1 , 1,  1, 1, 1 ] --> with maximum 10 elements
we use the partition function , which we already have it !

The zero part must be substracted becase we cannot have 0 infront => so we must test on smaller cases exactly how we do it !
we can test with 5,6 digits numbers and each block of 1 number to represent 3 digits ofr example :
111.222.333.444.555.666 + 7, 8, 9 + (0) will be translated into [6, 1, 1, 1, 1, 1, 1 ] BUT ONLY as principle


##### ## The repeating digits for the 4-digits numbers                              # 333
C = ( (( gmpy2.fac(4) // gmpy2.fac(3) ) * 9 ) * 9 ) + 9 # ( +9 is coming from 0)
# Expl :
print('4-digits at least 3 repeating digits  : \t', C )

###### The repeating digits for the 5-digits numbers                            #       7704
C4 = ( (( gmpy2.fac(5) // gmpy2.fac(4) )*9 -1 )*9 +9 )
C5 =  ( (( gmpy2.fac(5) // gmpy2.fac(3)  ) ) )
print('\n5-digits at least 4 repeating digits  : \t', C4 )
print('5-digits at least 3 repeating digits  : \t', C5 )



P = multiple_permutations(9,4,3,2)
print('\nMultiple permutations   ', P   )




t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


# print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
# print('\n--------------------------SOLUTION 1,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
# print('\n--------------------------SOLUTION 2,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
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
