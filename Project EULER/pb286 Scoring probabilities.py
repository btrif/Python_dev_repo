#!/usr/bin/python                   o(^_^)o         ( ͡° ͜ʖ ͡°)
# © Solved by Bogdan Trif @
#The  Euler Project  https://projecteuler.net
'''
                    Scoring probabilities       -           Problem 286

Barbara is a mathematician and a basketball player.
She has found that the probability of scoring a point when shooting from a distance x is exactly (1 - x/q),
where q is a real constant greater than 50.

During each practice run, she takes shots from distances x = 1, x = 2, ..., x = 50 and,
according to her records, she has precisely a 2 % chance to score a total of exactly 20 points.

Find q and give your answer rounded to 10 decimal places.


'''
import time, zzz
from itertools import combinations, permutations, combinations_with_replacement, product

def Probabilty_scoring( x , q ) :
    return 1-x/q

def total_score( q ) :
    S= 0
    for x in range(1, 50+1) :
        S += Probabilty_scoring(x, q)
        # print(x,'      ',  Probabilty_scoring(x, q) )
    return S

print('\ntotal_score : \t', total_score(50.0001))
print('\ntotal_score : \t', total_score(42.500))
print('\ntotal_score : \t', total_score(42.51))
print('\ntotal_score : \t', total_score(42))


def probability(q):
    scoring = [0.0] * 51
    scoring[0] = 1.0
    for x in range(1, 51):
        next_scoring = [0.0] * 51
        next_scoring[0] = scoring[0] * x/q
        for y in range(1, 51):
            next_scoring[y] = scoring[y-1] * (1 - x/q) + scoring[y] * x/q
        scoring = next_scoring
    return scoring[20]

print( probability(42.5) )


def binary_search() :


    target = 20
    q = 42
    # r = 1
    Score = total_score(q)
    d = 1
    while abs(Score - target) > 10**(-15) :

        if Score > target :
            q -= d
        if Score < target :
            q += d

        d /= 2

        Score = total_score(q)

        print(Score, '           d = ', d, '          diff = ', abs(Score - target) ,'     q= ', q  )
    return print('\nAnswer : \t', round(Score,12))

# binary_search()








print('\n------------------------ TESTS, understanding the concept ------------------------------')
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

