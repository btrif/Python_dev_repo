#  Created by Bogdan Trif on 03-11-2017 , 11:46 PM.
# © o(^_^)o  Solved by Bogdan Trif  @
#The  Euler Project  https://projecteuler.net
'''
                    Circular Logic              -           Problem 209

A k-input binary truth table is a map from k input bits (binary digits, 0 [false] or 1 [true]) to 1 output bit.
For example, the 2-input binary truth tables for the logical AND and XOR functions are:

                                        x	y	x AND y
                                        0	0	0
                                        0	1	0
                                        1	0	0
                                        1	1	1

                                        x	y	x XOR y
                                        0	0	0
                                        0	1	1
                                        1	0	1
                                        1	1	0

How many 6-input binary truth tables, τ, satisfy the formula

τ(a, b, c, d, e, f) AND τ(b, c, d, e, f, a XOR (b AND c)) = 0

for all 6-bit inputs (a, b, c, d, e, f)?
'''

import time, zzz
import itertools


'''
 CLARIFICATIONS 
I'm pretty sure I don't understand this problem. A truth table T(a, b, c, d, e, f) has 2^6 = 64 rows. 
To do T1 AND T2 (where T1 and T2 are 6 bit tables), do I compare T1.row1 to T2.row1, T1.row2 to T2.row2, etc? 
And get an answer < 64?

If this isn't right, can you give a smaller example? Or point me at a good link?

A six-input binary truth table has indeed 2^6=64 rows.
However, there are 2^64 different six-input truth tables.

As an example, consider 2-input binary truth tables: 
each one of them has 4 rows, but there are 2^4=16 such truth-tables, as shown below:
.
x y : A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P
---   -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
0 0 : 0  0  0  0  0  0  0  0  1  1  1  1  1  1  1  1
0 1 : 0  0  0  0  1  1  1  1  0  0  0  0  1  1  1  1
1 0 : 0  0  1  1  0  0  1  1  0  0  1  1  0  0  1  1
1 1 : 0  1  0  1  0  1  0  1  0  1  0  1  0  1  0  1
Each of the columns A-P above, represents a distinct 2-input binary truth table. 
A few of them are well known and have specific names e.g. column B is usually called "AND", 
column H is usually called "OR" etc. But most of them are not particularly useful, so they do not have distinct names.

Now, if you were asked to find how many of the 16 truth tables presented above have a special property e.g. 
T(a, b) AND T(b, a XOR b) = 0 for all 2-bit inputs (a,b), what would you do?

One possible approach might be to write down all the possible 2-bit inputs (a, b). 
For each input (a,b), write down (b, a XOR b), then list which of the truth-tables presented above satisfy the given condition:
.
(a, b)  (b,a XOR b)  Tables for which T(a, b) AND T(b, a XOR b) = 0
------  -----------  ----------------------------------------------
(0, 0)  (0, 0)       A B C D E F G H
(0, 1)  (1, 1)       A B C D E G I J K L M O
(1, 0)  (0, 1)       A B C D E F I J K L M N
(1, 1)  (1, 0)       A B C E F G I J K M N O
Observe that the required property is true for all 2-bit inputs, only for the truth-tables A, B, C and E: so the answer is 4. 

Problem 209 (View Problem) is asking you to find how many of the 2^64 six-input truth-tables 
have a certain property for all 6-bit inputs. 
Caution: The special property I used as an example, is NOT the same as the one used in problem 


'''







print('\n--------------------------TESTS------------------------------')
t1  = time.time()

for x in [0, 1]:
    for y in [0, 1]:
        print('x, y = ', x, y , '     AND   x & y = ', x&y , '  ;     XOR   x ^ y = ', x^y ,  )

print()

for a, b, c, d, e, f in itertools.product(range(0, 2), repeat=6):
    print(a, b, c, d, e ,  f,  end='   ')










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




