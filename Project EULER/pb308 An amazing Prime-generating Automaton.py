#  Created by Bogdan Trif on 14-10-2017 , 6:26 PM.
# © o(^_^)o  Solved by Bogdan Trif  @
#The  Euler Project  https://projecteuler.net
'''
An amazing Prime-generating Automaton           -           Problem 308
A program written in the programming language Fractran consists of a list of fractions.

The internal state of the Fractran Virtual Machine is a positive integer, which is initially set to a seed value.
Each iteration of a Fractran program multiplies the state integer by the first fraction in the list which will leave it an integer.

For example, one of the Fractran programs that John Horton Conway
wrote for prime-generation consists of the following 14 fractions:

17/91 , 78/85 , 19/51 , 23/38 , 29/33 , 77/29 , 95/23 , 77/19 , 1/17 , 11/13 , 13/11 , 15/2 , 1/7 , 55/1 .

Starting with the seed integer 2, successive iterations of the program produce the sequence:
15, 825, 725, 1925, 2275, 425, ..., 68, 4, 30, ..., 136, 8, 60, ..., 544, 32, 240, ...

The powers of 2 that appear in this sequence are 2^2, 2^3, 2^5, ...
It can be shown that all the powers of 2 in this sequence have prime exponents and that all
the primes appear as exponents of powers of 2, in proper order!

If someone uses the above Fractran program to solve Project Euler Problem 7 (find the 10001st prime),
how many iterations would be needed until the program produces 2^10001-st prime ?

'''
import time, zzz
from gmpy2 import mpq

import numpy
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

primes = prime_sieve_numpy(10**5+10**4)
print( '10001-st prime is : \t',primes[10**4])

Fractran = [  mpq (17, 91), mpq(78,85 ), mpq(19,51) , mpq(23,38) , mpq(29,33) , mpq(77,29) ,
             mpq(95,23) , mpq(77,19) , mpq(1,17) , mpq(11,13) , mpq(13,11) , mpq(15,2) , mpq(1,7) , mpq(55,1) ]
# print(Fractran)



print(2*Fractran[0])

print('\n--------------------------TESTS------------------------------')
t1  = time.time()

def brute_force_conceptualization() :
    seed = 2
    for i in range(10**2) :
        for j in Fractran :
            m = seed *j
            if m%1 == 0 :
                seed = m
                print('iter = ', i , '     j= ', j,'         new seed = ', m)
                if numpy.math.log2(m) %1 == 0 :
                    print('iter = ', i , '         new seed = ', m ,'-------- 2-power = ',   int(numpy.math.log2(m)) )


                break

brute_force_conceptualization()


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




