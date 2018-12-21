#!/usr/bin/python3
# Solved by Bogdan Trif @ 2016-09-04 00:35
#The  Euler Project  https://projecteuler.net
'''
                                            10001st prime           -           Problem 7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10.001-st prime number?

'''

import time
t1  = time.time()
# THIS  IS OPTIMIZED CODE
my_array=[]
counter=0
i = 2

while(counter <= 10001):
    j = 2
    while(j <= (i/j)):
        if not(i%j): break
        j = j + 1
    if (j > i/j) :
        # my_array.append(i)
        counter += 1
        if counter == 10001:
            res=i
    i = i + 1


print ("Last element of the array is: ", res, '... which is also the 10001-th prime')          # 104743


t2  = time.time()
print('\nCompleted in :', round((t2-t1),2), 's')