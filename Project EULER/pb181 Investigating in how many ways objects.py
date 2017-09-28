#!/usr/bin/python                   o(^_^)o         ( ͡° ͜ʖ ͡°)
# © Solved by Bogdan Trif @
#The  Euler Project  https://projecteuler.net
'''
Investigating in how many ways objects of two different colours can be grouped      -       Problem 181

Having three black objects B and one white object W they can be grouped in 7 ways like this:

(BBBW)	    (B,BBW)	(B,B,BW)	(B,B,B,W)	(B,BB,W)	(BBB,W)	(BB,BW)
In how many ways can sixty black objects B and forty white objects W be thus grouped?
60 B, 40 W = ?
'''
import time, zzz

[1, 1, 1, 0]

4 -> (BBBW)
31 -> (B,BBW) , (BBB,W)
22 -> (BB,BW)
2 1 1 -> (B,B,BW) , (B,BB,W)
1 1 1 1 -> (B,B,B,W)
_________________________ = 6 ways


[1, 1, 1, 1, 0, 0]

6 -> ( BBBBWW )
51 -> (BBBBW, W) , (BBBWW, B)
42 -> (BBBB, WW) , (BBBW, BW), (BBBB, WW)
33 -> (BBB, BWW), (BBW, BBW), (BWW, BBB)
4 1 1 -> (BBBB, W, W), (BBBW, B, W), (BBWW, B, B)
3 2 1 -> (BBB, BW, W), (BBB, WW, B), (BBW, BW, B), (BBW, BB, W),  (BWW, BB, B)
2 2 2 -> (BB, BB, WW), (BB, BW, BW), (BB, BW, BW)
2 2 1 1 -> (BB, BB, W, W), (BB, BW, B, W), (BW, BW, B, B),
2 1 1 1 1 -> (BB, B, B, W, W), (BW, B, B, B, W), (WW, B, B, B, B),
1 1 1 1 1 1 -> (B, B, B, B, W, W)
___________________________ = 1 + 2+ 3 + 3+ 3 +5 +3+ 3 + 1 = 24 ways




Partitions

def partition(number):
    answer = set()
    answer.add((number, ))
    for x in range(1, number):
        for y in partition(number - x):
            answer.add(tuple(sorted((x, ) + y)))
            #print(answer)
    return answer

print(partition(4))




print('\n--------------------------TESTS------------------------------')
t1  = time.time()






t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')

print('\n================  My FIRST SOLUTION,   ===============\n')
# t1  = time.time()







# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')


# print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
# print('\n--------------------------SOLUTION 1,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 2,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 3,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 4,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 5,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 6,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 7,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 8,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 9,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 10,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 11,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 12,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')

