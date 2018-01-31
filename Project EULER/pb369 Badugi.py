#  Created by Bogdan Trif on 07-12-2017 , 12:54 PM.
# © o(^_^)o  Solved by Bogdan Trif  @
#The  Euler Project  https://projecteuler.net
'''
                         Badugi          -           Problem 369

In a standard 52 card deck of playing cards, a set of 4 cards is a Badugi
if it contains 4 cards with no pairs and no two cards of the same suit.

Let f(n) be the number of ways to choose n cards with a 4 card subset that is a Badugi.

For example, there are 2598960 ways to choose five cards from a standard 52 card deck,
of which 514800 contain a 4 card subset that is a Badugi,

so f(5) = 514800.

Find ∑f(n) for 4 ≤ n ≤ 13.


'''
import time, zzz
from math import factorial
from itertools import combinations

def choose(n, k):
    return factorial(n) // (factorial(k) * factorial(n-k))

# ♠ Spades - S ,   ♥ Hearts - H   ,  ♦  Diamonds - D , ♣ Clubs - C

CA = { '2':2, '3':3 , '4':4 , '5':5, '6':6 , '7':7, '8': 8 , '9': 9, 'T':10, 'J':12, 'Q':13, 'K':14, 'A' :15 }
C = '23456789TJQKA'
# print(C)
print(choose(52, 4  ))
print(choose(52, 5  ))
print(choose(52, 13  ))


CARDS = []
for i in C :
    for j in 'SHDC' :
        # print(i, j)
        CARDS.append(str(i+j) )
print(CARDS)



print('\n--------------------------TESTS------------------------------')
t1  = time.time()

def brute_force_Acknowledgement( ) :
    comb = combinations(CARDS, 5)
    cnt = 0
    for I in comb :
        a =  [ o[0] for o in I ]
        b =  [ o[1] for o in I ]
        if len(set(a)) >= 4 and len(set(b)) == 4 :
            cnt+=1
            print(str(cnt)+ '.    ' ,I )

    print('\nUnique 4-Sets = ', cnt ,'         from  C(52, 4) = 270725  combinations ' )

brute_force_Acknowledgement()

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




