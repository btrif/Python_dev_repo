#  Created by Bogdan Trif on 24-09-2017 , 10:22 PM.


# © o(^_^)o  Solved by Bogdan Trif  @
#The  Euler Project  https://projecteuler.net
'''
                Cyclic numbers          -       Problem 358


A cyclic number with n digits has a very interesting property:
When it is multiplied by 1, 2, 3, 4, ... n, all the products have exactly the same digits, in the same order, but rotated in a circular fashion!

The smallest cyclic number is the 6-digit number 142857 :
142857 × 1 = 142857
142857 × 2 = 285714
142857 × 3 = 428571
142857 × 4 = 571428
142857 × 5 = 714285
142857 × 6 = 857142

The next cyclic number is 0588235294117647 with 16 digits :

0588235294117647 × 1 = 0588235294117647
0588235294117647 × 2 = 1176470588235294
0588235294117647 × 3 = 1764705882352941
...
0588235294117647 × 16 = 9411764705882352

Note that for cyclic numbers, leading zeros are important.

There is only one cyclic number for which, the eleven leftmost digits are 00000000137
and the five rightmost digits are 56789
(i.e., it has the form 00000000137...56789 with an unknown number of digits in the middle).
Find the sum of all its digits.


'''
import time, zzz
from gmpy2 import mpq, mpz, next_prime
from decimal import *
getcontext().prec = 5000


# Right now, in thinking about p 358 “Cyclic numbers", I am enjoying reading Conway and Guys fascinating Book of Numbers. " \
#   pp157-163, which end with a statement of Fermat’s Little Theorem, are good for this problem. I hope!
# https://brilliant.org/discussions/thread/cyclic-numbers/
# http://www.mathamazement.com/Lessons/Everyday-Math/05_Miscellaneous/05_03_Important-Numbers/cyclic-number.html
# http://oeis.org/A004042

http://math.tutorcircle.com/number-sense/cyclic-numbers.html

def find_decimal_period(d):
    for i in range(10, len(d)) :
        if d[:i] == d[i:2*i] :
#             print(d[:i])
            return d[:i]
    return None

print('\n--------------------------TESTS------------------------------')
t1  = time.time()

# p_inv = Decimal(1)/Decimal(p)
    # "{0:.2f}".format(a)
    # print(p, '     ', (1/p), '    %.24f ' %p_inv  )
    # print('%.100f ' %(1/23))
    # oo = str( Decimal(1)/Decimal(7246376600) )
    # print( oo)

p = int(next_prime (724642591))
cnt = 0
for steps in range(10**7) :
    D = dict()
    if cnt%(10**3) == 0 :
        print('Prime = ', p ,'     ;        Inverse :  ' ,     '%.24f ' %(1/p) ,'      cnt = ' , cnt  )
    p_inv =  Decimal(1)/ Decimal(p)
    s = str("{0:.5000f}".format(p_inv))[2:]
    # print(   s  )
    period = find_decimal_period( s )
    if period != None :
        print( ' ---------------  period  :', period )
        D[p] = period
        print('\n' , p, '   s= ' , s , '\nperiod : ', period ,'\nlenght_period = ', len(period) )
        if period[-5::] == 56789 :
            Y = [ int(i) for i in period ]
            print('\nThe sum of the digits = ' , sum(Y) )

            break
    p = int( next_prime(p) )
    cnt += 1

http://math.tutorcircle.com/number-sense/cyclic-numbers.html


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



