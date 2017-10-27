#  Created by Bogdan Trif on 26-10-2017 , 3:53 PM.
# Write a program to print all permutations of a given string
# 3.5
# A permutation, also called an “arrangement number” or “order,” is a rearrangement
# of the elements of an ordered list S into a one-to-one correspondence with S itself.
# A string of length n has n! permutation.
# Source: Mathword(http://mathworld.wolfram.com/Permutation.html)
#
# Below are the permutations of string ABC.
# ABC ACB BAC BCA CBA CAB
import time
from itertools import permutations, product

L = [1, 2, 3, 4, 5, 6, 7, 8, 9 ]

t1  = time.time()

P =[]
def permute( L , r,  l   ) :
    if r == l :
        # print(L)
        P.append(L[:])

    else :
        for i in range( r, l ):
            L[i], L[r] = L[r], L[i]

            permute(L, r+1,  l  )

            # Backtrack , this triggers backtracking
            L[i], L[r] = L[r], L[i]




permute(L, 0, len(L))
print(P[:200])



# print( list(permutations1(L))[:200])

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')




M = [9, 8, 7, 6, 5, 4, 3,2,1]

t1  = time.time()


print(list(permutations(M) )[:200]  )



t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')



