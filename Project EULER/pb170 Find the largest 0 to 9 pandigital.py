#!/usr/bin/python                   o(^_^)o         ( ͡° ͜ʖ ͡°)
# © Solved by Bogdan Trif @     Completed on Sun, 29 Oct 2017, 12:31
#The  Euler Project  https://projecteuler.net
'''
Find the largest 0 to 9 pandigital that can be formed by concatenating products     -       Problem 170

Take the number 6 and multiply it by each of 1273 and 9854:

6 × 1273 = 7638
6 × 9854 = 59124

By concatenating these products we get the 1 to 9 pandigital 763859124.

We will call 763859124 the "concatenated product of 6 and ( 1273  , 9854 )   ".

Notice too, that the concatenation of the input numbers, 612739854, is also 1 to 9 pandigital.

The same can be done for 0 to 9 pandigital numbers.

What is the largest 0 to 9 pandigital 10-digit concatenated product of an integer
with two or more other integers, such that the concatenation of the input numbers
is also a 0 to 9 pandigital 10-digit number?

'''
import time
from itertools import permutations
from gmpy2 import fac

# from eulerlib import is_pandigital


def is_pandigital(n):
    if len(str(n)) == 10 :
        N = list([int(i) for i in str(n)])
#         print(N, len(set(N)))
        if len(set(N)) == 10 :
            return True

    return False



# IDEA @ 2017-03-04,  16:30
# We go down from 9.876.543.210 on an inverse pandigital generator
# and try to break the number into 2,3, 4  parts,  (!!!!!! with two or more other integers,)
# and we multiply it with the same unique number it may be 1, 2 digits


# O = [ 4 , 3, 2 , 1 , 0 ]

Total_perm = fac(10) - fac(9)           # 10!-0! = 3265920

# WRONG = 9108724356



print('\n--------------------------TESTS------------------------------')
t1  = time.time()






t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n================  My FIRST SOLUTION,   ===============\n')
t1  = time.time()


def solution_1():
    O = [ 9 , 8,  7 , 6 , 5,  4 , 3,  2 , 1 , 0 ]
    Perm = permutations( O )
    print(Perm)
    cnt = 0
    for perm in Perm :
        if perm[0] > 0:
            cnt+=1
            # nr =  int(''.join( [ str(a) for a in perm ] ))
            # if cnt%10000 == 0 :
            #     print(str(cnt)+'.    ',  perm  , '            ',  nr     )
            # if cnt == 5*10**5 : break

            for i in range(3, 8) :
                p1, p2 = perm[ :i ], perm[ i: ]
                if p2[0] != 0 :
                    n1, n2 = int(''.join( [ str(a) for a in p1 ] )), int(''.join( [ str(a) for a in p2 ] ))
                    # print( p1 ,  p2,'      ', n1, n2 )
                    for x in [2, 3, 4, 6, 7, 9, 18, 27, 45, 54, 63, 72, 81  ] :
                        # if len(str(x)) != len(set(str(x))) : continue
                        x1, x2 = n1/x, n2/x
                        if x1%1 ==0 and x2%1==0 :
                            x1, x2 = int(x1), int(x2)
                            conc1 = int(str(x)+str(x1)+str(x2))
                            if is_pandigital(conc1) :
                                print(' x = ',x,'     n1, n2 = ' ,n1, n2 ,'      x1, x2 = ' , x1, x2 ,'     conc1 =  ' , conc1 ,'     conc PROD =   ' , str(n1)+str(n2)  )
                                return print('\nAnswer :  ' ,str(n1)+str(n2) )
            # for j in ([ 3, 3 , 4 ], [ 3, 4, 3 ], [ 4, 3 ,3 ]  ) :
            #     p3, p4, p5 = perm[ :j[0] ] , perm[ j[0] : j[0]+j[1] ] ,perm[ j[0]+j[1]: ]
            #     if p4[0] !=0 and p5[0] !=0 :
            #         n3, n4, n5 = int(''.join( [ str(a) for a in p3 ] )), int(''.join( [ str(a) for a in p4 ] )), int(''.join( [ str(a) for a in p5 ] ))
            #         # print(j,'              ' ,   p3, p4, p5 ,'        ', n3, n4, n5 )
            #         for xa in range(2, 10 ) :
            #             x3, x4, x5 = n3/xa, n4/xa, n5/xa
            #             if x3%1 ==0 and x4%1==0 and x5%1==0 :
            #                 x3, x4, x5 = int(x3), int(x4), int(x5)
            #                 conc2 = int( str(xa)+str(x3)+str(x4)+str(x5) )
            #                 if is_pandigital(conc2) :
            #                     print(' xa = ',xa,'     ' , x3, x4, x5 ,'     CONCATANATED PRODUCT =  ' , conc2 )


solution_1()            #   Answer:         9857164023      Completed in : 1.4331 s






t2  = time.time()
print('\nCompleted in :', round((t2-t1) , 4), 's\n\n')


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

