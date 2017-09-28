#  Created by Bogdan Trif on 27-09-2017 , 2:32 PM.
# © o(^_^)o  Solved by Bogdan Trif  @
#The  Euler Project  https://projecteuler.net
'''
                Weak Queens     -       Problem 534


The classical eight queens puzzle is the well known problem of placing eight chess queens on a 8×8 chessboard
so that no two queens threaten each other.
Allowing configurations to reappear in rotated or mirrored form, a total of 92 distinct configurations can be found for eight queens.

The general case asks for the number of distinct ways of placing n queens on a n×n board, e.g.
you can find 2 distinct configurations for n=4.

Lets define a weak queen on a n×n board to be a piece which can move any number of squares if moved horizontally,
but a maximum of n−1−w squares if moved vertically or diagonally, 0≤w<n being the "weakness factor".

For example, a weak queen on a n×n board with a weakness factor of w=1 located in the bottom row
will not be able to threaten any square in the top row as the weak queen would need to move n−1 squares
vertically or diagonally to get there, but may only move n−2 squares in these directions.

In contrast, the weak queen is not handicapped horizontally, thus threatening every square in its own row,
independently from its current position in that row.

Let Q(n,w) be the number of ways n weak queens with weakness factor w can be placed on a n×n board
so that no two queens threaten each other.
It can be shown, for example, that Q(4,0)=2, Q(4,2)=16 and Q(4,3)=256.

Let S(n)=∑{w=0, n−1} Q(n,w) .

You are given that S(4)=276 and S(5)=3347.

Find S(14).


'''
import time, zzz





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




