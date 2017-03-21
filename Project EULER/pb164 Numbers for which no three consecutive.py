#!/usr/bin/python
# Solved by Bogdan Trif @
#The  Euler Project  https://projecteuler.net
'''
Numbers for which no three consecutive digits have a sum greater than a given value     -       Problem 164

How many 20 digit numbers n (without any leading zero) exist such that
no three consecutive digits of n have a sum greater than 9?

'''
import time
from itertools import combinations_with_replacement, combinations, permutations


digits = list(range(0,10))
print(digits)
C = list(combinations_with_replacement(digits, 3))
# print(len(C) , C)

A=[]
for i in range(len(C)):
    if sum(C[i]) <=9 :
        A.append(C[i])
print('\n',len(A), A)

B=[]
for i in range(len(A)):
    g = list(permutations(A[i]))
    for j in range(len(g)):
        # if g[j][0] !=0 :
        B.append(g[j])

B = list(sorted(set(B)))
print('\n',len(B), B)

print('\n--------------------------TESTS------------------------------')

# 9000 xxxx xxxx xxxx xxxx
# 8000 xxxx xxxx xxxx xxxx
# 7000 xxxx xxxx xxxx xxxx
# 6000 xxxx xxxx xxxx xxxx
# 5000 xxxx xxxx xxxx xxxx
# 4000 xxxx xxxx xxxx xxxx
# 3000 xxxx xxxx xxxx xxxx
# 2000 xxxx xxxx xxxx xxxx
# 1000 xxxx xxxx xxxx xxxx
#
# x000 xxxx xxxx xxxx xxxx    = 10**16 * 9
# xx00 0xxx xxxx xxxx xxxx    = 10**15 * 99
#        ....    ....     ....    ....
# xxxx xxxx xxxx xxxx 000x    = 10**1 * 9999 9999 9999 9999
# xxxx xxxx xxxx xxxx x000    = 10**0 * 9999 9999 9999 9999 9


# x00x        10**1 * 9 = 90
# xx0x        10**1 *99 = 990
# x00xx       10**2 * 9 = 900
# xx00x       10**1 * 99 = 990

B=B[0:10]
print(B)
Z = int(str(9)*20)
N=[]

for i in range(0,1): #range(len(B)) :
    print( B[i])
    if B[i][0] == 0 :
        rng = 17
        for j in range(1, rng+1) :
            n = int(str(9)*j)*10**(rng-j)
            print('9' * j , B[i] ,10**(rng-j) , '    ', len ('9' * j )+len(B[i])+rng-j , rng-j ,'        case1' )
            N.append( n )

    elif B[i][0] != 0  :
        rng = 17
        print('',B[i],  10**(rng),'    ' , len(B[i])+rng, rng , '        case2')
        n = 10**(rng)
        N.append(n)
        for j in range(1, rng+1 ) :
            n = int(str(9)*j)*10**(rng-j)
            print('9' * j ,  B[i],  10**(rng-j),'    ' , len ('9' * j )+len(B[i])+rng-j, rng-j , '        case2')
            N.append( n )
    print('----------------------')

# print(N)

print('\n\nFinal Res : \t', Z - sum(N),'    ' ,len( str( Z - sum(N)) )   )


print('\n---------------- MORE TESTS ON THE CONCEPT ----------------')

itr=0
up_rng = 10**4

for i in range(up_rng//10 , up_rng):
    s = str(i)
    if s.find('0') != -1 :
        itr+=1
        print(str(itr)+'.   ',s)

print('\n 00 : \t\t', itr    )




print('\n================  My FIRST SOLUTION,   ===============\n')
t1  = time.time()











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
