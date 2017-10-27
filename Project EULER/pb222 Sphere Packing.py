#!/usr/bin/python
# Solved by Bogdan Trif @       Completed on Sun, 8 Oct 2017, 10:50
#The  Euler Project  https://projecteuler.net
'''
                    Sphere Packing      -       Problem 222

What is the length of the shortest pipe, of internal radius 50mm,
that can fully contain 21 balls of radii 30mm, 31mm, ..., 50mm?

[30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50] mm

Give your answer in micrometres (10**-6 m) rounded to the nearest integer.                                                  '''


import random
import time, itertools
from math import sqrt
import gmpy2

R = list(range(30, 51))
print(R,'\n')

y = lambda r1, r2 :  sqrt( (r1+r2)**2 - (100-r1-r2)**2  )

h = lambda r1, r2 : y(r1,r2) + r1 + r2


print('\n--------------------------TESTS------------------------------')
t1  = time.time()

# http://math.stackexchange.com/questions/610621/a-geometric-problem-in-placing-two-spheres-in-a-pipe

### Three balls ####  h1 - comb of r1, r2   ;  h2 comb of r2,r3   and H = total height of the three balls
r1, r2, r3 = 48, 49, 50
h1 = h(r1, r2)
h2 = h( r2, r3)
H = round(( r1 + y(r1, r2 ) + y(r2, r3) + r3) *1000)

print( 'height test  h1, h2 : ', h1 , h2 ,  ' The height of three balls of 48, 49, 50 radii : \t' ,  H   )

print('\n','----'*23)


def permutations_configuration_tests(  arr  ) :
    Z = list(itertools.permutations(arr)   )
    cnt = 0
    v_min = 10**8
    for T in Z :
        cnt +=1
        # print(str(cnt) +'.    '  ,   T )
        H = 0
        for j in range(1, len(T)) :
            r1, r2 = T[j-1], T[j]
            # print( r1, r2 )
            H += y(r1, r2)
        if H < v_min :
            v_min = H
            H = round((  H +  T[0]+T[-1] ) *1000 )
            print(str(cnt) + '.     Height =  ' , H ,'    Array : ' , T )

arr = list(range(44, 50+1))
permutations_configuration_tests( arr )

# The test shows that the minimum length is achieved when the larger radii are at the
# beginning & end , and the smaller radii are in the middle :
# 192.     Height =   656116     Array :  (50, 48, 46, 44, 45, 47, 49)
#  or
# 309721.     Height =   823496     Array :  (49, 47, 45, 43, 42, 44, 46, 48, 50)
# THEREFORE The array should look as :  ( Not  completely my contribution  )
# [50, 48, 46, 44, 42, 40, 38, 36, 34, 32, 30, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]

t2  = time.time()
print('\nCompleted in :', round((t2-t1), 4 ), 's\n\n')

print('\n================  My FIRST SOLUTION,   ===============\n')
t1  = time.time()

S, T =set(R), []
T1, T2 = [] , []
while  len(set(T)) < 21  :

    if max(S) % 2 == 0 :
        T1.append ( max (S) )
        S.remove( max(S) )
    elif len(S) > 0 :
        if max(S) % 2 != 0 :
            T2.append ( max (S) )
            S.remove( max(S) )

    T = T1 + sorted(T2, reverse=False)

print('Optimal array : ',T)

def compute_height_of_array( T ) :
    H = 0
    for j in range(1, len(T)) :
        r1, r2 = T[j-1], T[j]
        # print( r1, r2 )
        H += y(r1, r2)
    H = round((  H +  T[0]+T[-1] ) *1000 )

    return print('\nFinal Height =  ' , H ,'    Array : ' , T )

compute_height_of_array(T)

# Final Height =   1590933     Array :  [50, 48, 46, 44, 42, 40, 38, 36, 34, 32, 30, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1,   --------------------------')
t1  = time.time()


from itertools import permutations
from math import sqrt
import sys

class Problem():
    def solve(self):
        #self.benchmark()
        ball_arrangement = [49, 47, 45, 43, 41, 39, 37, 35, 33, 31, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]
        print(self.get(ball_arrangement))

    def benchmark(self):
        best_arrangement_so_far = None
        shortest_so_far = 30000
        all_balls = [_ for _ in range(40, 51)]
        for ball_arrangement in permutations(all_balls):
            total_distance = self.get(ball_arrangement)
            if total_distance < shortest_so_far:
                shortest_so_far = total_distance
                best_arrangement_so_far = ball_arrangement
                print(best_arrangement_so_far, shortest_so_far)

        print(best_arrangement_so_far, shortest_so_far)

    def get(self, ball_arrangement):
        distance = ball_arrangement[0] + ball_arrangement[-1]
        ball_count = len(ball_arrangement)
        for i in range(0, ball_count - 1):
            distance += self.get_distance(ball_arrangement[i], ball_arrangement[i+1])
        return distance

    def get_distance(self, a, b):
        return sqrt(200 * (a + b - 50))


problem = Problem()
problem.solve()




t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 2,   --------------------------')
t1  = time.time()



t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

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
