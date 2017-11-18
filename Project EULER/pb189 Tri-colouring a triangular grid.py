#!/usr/bin/python                   ( ͡° ͜ʖ ͡°)
# Solved by Bogdan Trif @
#The  Euler Project  https://projecteuler.net
'''
Tri-colouring a triangular grid     -       Problem 189

Consider the following configuration of 64 triangles:


We wish to colour the interior of each triangle with one of three colours: red, green or blue,
so that no two neighbouring triangles have the same colour.
Such a colouring shall be called valid. Here, two triangles are said to be neighbouring if they share an edge.
Note: if they only share a vertex, then they are not neighbours.

For example, here is a valid colouring of the above grid:

A colouring C' which is obtained from a colouring C by rotation or reflection is considered distinct from C unless the two are identical.

How many distinct valid colourings are there for the above configuration?

'''
import time
from itertools import combinations, permutations, combinations_with_replacement


# 2017-01-31, 21:54
# Problema de combinatorica avansata.
# IDEE : Inlocuim culorile cu cifre : Red, Green Blue --> R, G ,B = 1, 2, 3
# 2. La inceput o sa obtinem toate posibilitatile, inclusiv cele prin reflectie sau rotatie, dar le vom elimina la sfarsit
# aici consta dificultatea problemei --> cere CONFIGURATII DISTINCTE !!! MARE ATENTIE !
# 3. Va fi foarte greu de eliminat combinatiile duplicat , virtual chiar ultimul tringhiulas poate schimba
# intreaga configuratie, deci e posibil ca numai -1 sa trebuiasca sa scadem la sfarsit !

U = [1, 2, 3]
r1 = list(combinations(U, 1))
print(len(r1), r1)
t2 = list(combinations_with_replacement(U, 3 ))
# print(len(t2), t2)
r2 = []
for i in t2:
    p = list(permutations(i))
    r2.extend(p)
r2=list(set(r2))
print(len(r2),r2)

t3 = list(combinations_with_replacement(U, 5 ))
r3 = []
for i in t3:
    p = list(permutations(i))
    r3.extend(p)
r3=list(set(r3))
print(len(r3),r3)

t4 = list(combinations_with_replacement(U, 7 ))
r4 = []
for i in t4:
    p = list(permutations(i))
    r4.extend(p)
r4=list(set(r4))
print(len(r4),r4)




def validate_triangle(T):
    for i in range(1, len(T)) :
        for j in range(1, len(T[i]), 2 ):
            if T[i][j] == T[i][j-1] or T[i][j] == T[i][j+1] :   # compare adjacent triangles, same row
                return False
            if T[i][j] == T[i-1][j-1] :
                return False

    return True





T=    [ (3,),
       (1, 2, 3),
    (1, 2, 3, 1, 2),
(2, 3, 1, 2, 1, 3, 2) ]

print('\nvalidate_triangle test : \t', validate_triangle(T))


print('\n--------------------------TESTS------------------------------')
t1  = time.time()

def brute_force():
    cnt=0
    T= []
    for i in r1 :
        for j in r2 :
            for k in r3 :
            #     for l in r4 :
                triang = []
                # triang.extend([ i, j ,k ,l ])
                triang.extend([ i, j, k ])
                if validate_triangle(triang) == True :
                    cnt+=1
                    print(str(cnt)+'.       ', triang )


brute_force()               #   31968.        [(3,), (2, 1, 3), (2, 3, 2, 1, 2), (3, 1, 2, 1, 3, 1, 2)]


# All of them including Reflexions & Rotations
# T1 = 3 ; T2 = 24 ;  T3 = 528


t2  = time.time()
print('\nCompleted in :', round((t2-t1) , 4), 's\n\n')


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
