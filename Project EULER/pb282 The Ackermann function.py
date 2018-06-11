#!/usr/bin/python                   o(^_^)o         ( ͡° ͜ʖ ͡°)
# © Solved by Bogdan Trif @
#The  Euler Project  https://projecteuler.net
'''
The Ackermann function          -       Problem 282

For non-negative integers m, n, the Ackermann function A(m, n) is defined as follows:



For example A(1, 0) = 2, A(2, 2) = 7 and A(3, 4) = 125.

Find   Sum {n=0, 6} A(n, n) and give your answer mod 14**8.

'''
import time, zzz

M = {(1, 0) : 2 }
def A(m, n, M):
    print(M)
    if m==0 :
        if (m,n) in M : return M[(m,n)]
        else :
            M[m,n] = n+1
            return n+1

    if m>0 and n==0 :
        if (m,n) in M : return M[(m,n)]
        else :
            return A(m-1, 1, M)

    if m>0 and n>0 :
        if (m,n) in M : return M[(m,n)]
        else :
            return A( m-1,  A(m, n-1, M), M )


# print('\nAckermann function test : \t', A(3, 4, M ))

# @ 2017-03-10 --> Here without a SMART MEMOIZATION implementation, no chance to solve the problem !!!
# Must implement a smart memoization to the recursive function

def A_no_mem(m, n):
    if m==0 : return n+1
    if m>0 and n==0 :
        return A_no_mem(m-1, 1)

    if m>0 and n>0 :
        return A_no_mem( m-1,  A_no_mem(m, n-1) )


print('\nAckermann no memoization function test : \t', A_no_mem(4, 1 ))

https://www.saylor.org/site/wp-content/uploads/2011/06/Ackermann-Function.pdf
http://mathworld.wolfram.com/AckermannNumber.html       <--NOTATION


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

