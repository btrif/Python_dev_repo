#!/usr/bin/python                   o(^_^)o         ( ͡° ͜ʖ ͡°)
# © Solved by Bogdan Trif @
#The  Euler Project  https://projecteuler.net
'''
                    Step Numbers        -       Problem 178

Consider the number 45656.
It can be seen that each pair of consecutive digits of 45656 has a difference of one.
A number for which every pair of consecutive digits has a difference of one is called a step number.
A pandigital number contains every decimal digit from 0 to 9 at least once.

How many pandigital step numbers less than 10^40 are there?

'''
import time

### LOGIC ###
We only have to start from 10**9 == 10-digit number up
Question : How many pandigital numbers are in 10-digit ?
A: Because it cannot start with 0 we will have 9*8*7*6*5*4*3*2*1*0 = 9*9!

Q2 : How many step-numbers are in a 10-digit number ?  NO DEGREE OF LIBERTY !
 A2 : Can't start with 0 but we can with 9 ==> 987.654.321.0
we can't have  897.654.321.0 or 123.456.789.0 because it is not step-number => 1 pand-step-number   !!!

Q3 : What about in a 11-digit number ? Again. Can't start with 0  => ONE DEGREE OF LIBERTY
A3 : Here we have +1 degree of liberty => but still can't start with lower numbers because :
        345.678.987.65 is not a valid step number =>
    We have : 987.654.321.01 , 898.465.321.01, 101.234.567.89,  => 3 pand-step-numbers   !!!

Q4 : 12-digits ?  2 DEGREES OF LIBERTY
A4 : We have :
987.654.321.012 ,
987.654.321.010 ,
987.654.321.210,
987.654.323.210,
987.654.543.210,
987.656.432.101,
987.676.543.210,
987.876.543.210,
898.765.432.101
789.876.543.210
101.234.567.898, 120.123.456.789 ,
210.123.456.789,            =>   14   pand-step-numbers

# 3 degrees of liberty : 13-digits :
9.898.765.432.101
8.989.876.543.210
7.898.765.432.101
9.876.543.210.132, 9.876.543.432.101, 9.876.545.432.101, 9.876.565.432.101






print('\n--------------------------TESTS------------------------------')
t1  = time.time()






t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n================  My FIRST SOLUTION,   ===============\n')
# t1  = time.time()







# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


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
