#!/usr/bin/python
# Solved by Bogdan Trif @
#The  Euler Project  https://projecteuler.net
'''
Digital Signature   -       Problem 290

How many integers 0 ≤ n < 10**18 have the property that  the sum of the digits of n equals the sum of digits of 137*n?

'''
import time
from itertools import count

print('\n--------------------------TESTS------------------------------')





print('\n================  My FIRST SOLUTION,   ===============\n')
t1  = time.time()

s = '9'*3

counter = 0
for k in count(int(s), -1 ):
# for i in range(0,18):
#     k = int('9'+'0'*i)
    S = sum([int(i) for i in list(str(k))])
    # print([int(i) for i in list(str(137*k))])
    T = sum([int(i) for i in list(str(137*k))])
    if S == T : #== 18:
        counter+=1
        print(str(counter)+'.       n = ',k,'         Sn=' ,S, '  ' ,T,'              137n =' ,137*k)
    if k % 10**9 == 0 :
        print(k, counter)
    if k==0 : break

print('\nAnswer :  ', counter)

# 2016-12-01

# 9*18 => 162
# 9*17 ==> 153 144  135
#  9*16 => 126 117
#  9*15 => 108
# 9*14 => 99
# 9 *13 => 90 , 81
# 9 *11 => 81 , 72. 63
# 9 *9 => 54, 45
# 9 *6,7 => 36, 27
# 9 *1,2,34,5 => 18, 9

# SUMS :        @ 2016-12-01
# sum = 27 ==> there are : 207692 numbers until '9'*8
# sum = 18 ==> there are :  3502 numbers until '9'*7            ==> Q: 4932 = 18*2*137 ?   19728 = 18 * 2 * 2**2 * 137 ?,  9864 = 18 * 2**2 * 137
# sum = 9 ==> there are :  18 numbers until '9'*18  --------- AL OF THEM

# @ 2017-03-23, 18:36 - Only digits with the total sum = multiple of 9 are feasable
# I must find what particularity have the numbers with multiple digits of 9 have:
# Example :  n =  846          Sn= 18    18               137n = 115902  ON
# But 864 IS NOT on on the LIST    OFFF
#
# Instead : n =  882          Sn= 18    18               137n = 120834 and there is also
#               n =  828          Sn= 18    18               137n = 113436   ON
#
#  n =  891          Sn= 18    18               137n = 122067  ON
#  n = 819            IS NOT on LIST                                  OFF
#
# n =  873          Sn= 18    18               137n = 119601   ON
# n =  837                                                                     OFF


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
