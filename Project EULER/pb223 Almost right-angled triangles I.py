#!/usr/bin/python                   o(^_^)o         ( ͡° ͜ʖ ͡°)
# © Solved by Bogdan Trif @
#The  Euler Project  https://projecteuler.net
'''
        Almost right-angled triangles I     -       Problem 223

Let us call an integer sided triangle with sides a ≤ b ≤ c barely acute if the sides satisfy
a**2 + b**2 = c**2 + 1.

How many barely acute triangles are there with perimeter ≤ 25,000,000  (2.5*10**7)  ?


'''
import time, gmpy2
from math import gcd, sqrt
from pyprimes import factorise

def get_factors(n):       ### o(^_^)o  FASTEST  o(^_^)o  ###
    ''' Decompose a factor in its prime factors. This function uses the pyprimes module. THE FASTEST  '''
    return [val for sublist in [[i[0]]*i[1] for i in factorise(n)] for val in sublist]


print('\n-----------------------  BRUTE FORCE TESTS  ------------------------------')
t1  = time.time()


def brute_force( u ,up_lim) :
    ba_max = 0
    cnt=0
    for b in range(1, u):
        for a in range(1, b):
            c_sq = a*a + b*b - 1
            if  gmpy2.is_square(c_sq) :
                c = int(sqrt(c_sq))
                if c > b :
                    if a+b+c <= up_lim :
                        cnt+=1
                        print(str(cnt)+'.      a = ', a, '    b=' ,  b, '     c=',c,'     ', a+b+c,'         ',b/a ,'   a**2-1=', a**2-1)
                        if b/a > ba_max :
                            ba_max = b/a

    return print('\nAnswer : \t', cnt,'        ', ba_max)

up_lim = 25*10**2
brute_force(up_lim//2, up_lim )

t2  = time.time()
print('\nCompleted in :', round((t2-t1),6), 's\n\n')

print('\n================  My FIRST SOLUTION,   ===============\n')
t1  = time.time()

# http://echochamber.me/viewtopic.php?t=45132

# up_lim = 25*10**3
#
# SQ = [i*i for i in range(up_lim//2)]
# SQD = {x*x: x for x in range(up_lim//2) }
# # SQD2 = dict(zip(SQD.values(),SQD.keys()))
# print( len(SQ) ,SQ[:200])
# print( len(SQD) , { k:v for k,v in SQD.items() if v<100 } ,'\n\n')
#
#
# cnt=0
# for a in range(2, len(SQ) ):
#     if a > up_lim //3 : break
#     for b in range(a+1, len(SQ)):
#         c_sq = SQ[a] + SQ[b] - 1
#         if c_sq in SQD :
#             c = SQD[c_sq]
#             if a+b+c > up_lim : break
#             if a+b+c <= up_lim :
#                 cnt+=1
#                 print(str(cnt)+'.      ', a, b, c,'     ', a+b+c  , '        ', get_factors(a),'    ' ,get_factors(b),'    ' ,get_factors(c)      )
#
# print('\nAnswer : \t',  cnt )

#
# for a in range(1, 1000) :
#     ccbb = a*a -1

@2017-03-28 - I left here, I must use the a**2 -1 decomposition

t2  = time.time()
print('\nCompleted in :', round((t2-t1),6), 's\n\n')


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
