#  Created by Bogdan Trif on 16-11-2017 , 12:10 PM.
# © o(^_^)o  Solved by Bogdan Trif  @
#The  Euler Project  https://projecteuler.net
'''
Polynomials with at least one integer root          -           Problem 269

A root or zero of a polynomial P(x) is a solution to the equation P(x) = 0.
Define P_n as the polynomial whose coefficients are the digits of n.

For example,            P_5703(x) = 5x^3 + 7x^2 + 3.

We can see that:

P_n(0) is the last digit of n,
P_n(1) is the sum of the digits of n,
P_n(10) is n itself.

Define Z(k) as the number of positive integers, n,
not exceeding k for which the polynomial P_n has at least one integer root.

It can be verified that                 Z(100 000) is 14696.

What is Z(10^16)?


'''
import time, zzz

# === UNDERSTANDING OF THE PROBLEM ===
# Smallest polynomial with integer root  is  k = 10 ==> P_10(x) = x,
# next is P_11(x) = x+1, third is P_12(x) = x+2 ...
#
# The largest polynomial is :  k =10^16 => P_10^16(x) = x^16
# the previous one was P_9...9 = 9*x^15+9*x^14 +... + 9x + 9

=== LINKS ====
http://www.sparknotes.com/math/algebra2/polynomials/section4.rhtml
https://brilliant.org/wiki/rational-root-theorem/
http://www.sosmath.com/algebra/factor/fac10/fac10.html
http://imomath.com/index.php?options=622&lmm=0
http://www.wolframalpha.com/input/?i=plot(x%5E4+%2B+2x%5E3+%E2%80%93+7x%5E2+%E2%80%93+8x+%2B+12)
http://www.purplemath.com/modules/rtnlroot.htm

## Is Pascal Triangle polynom with root = -1    and is  P_14641
http://www.wolframalpha.com/input/?i=plot(x%5E4+%2B+4x%5E3+%2B+6x%5E2+%2B+4x+%2B+1)

## Is Pascal Triangle polynom with root = -1    and is  P_1331
http://www.wolframalpha.com/input/?i=plot(x%5E3+%2B+3x%5E2+%2B+3x%5E1+%2B++1)

## root = -2
http://www.wolframalpha.com/input/?i=roots(5x%5E3+%2B+8x%5E2+%2B+8)

=== KEYWORDS
Rational Root Theorem
Rational Zeros of Polynomials


print('\n--------------------------TESTS------------------------------')
t1  = time.time()



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




