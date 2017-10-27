#  Created by Bogdan Trif on 14-10-2017 , 1:26 PM.
# EULER 266 - Pseudo Square Root
import operator
import time
from itertools import combinations
import functools
from math import sqrt

def get_factors(n):       ### o(^_^)o  FASTEST  o(^_^)o  ###
    ''' Decompose a factor in its prime factors. This function uses the pyprimes module. THE FASTEST  '''
    from pyprimes import factorise
    return [val for sublist in [[i[0]]*i[1] for i in factorise(n)] for val in sublist]

print('\n========  My SECOND SOLUTION,  O(2^n)  After learning on Euler Forum, 12 sec ===============\n')
t1  = time.time()

def closest_product_subset_list_algorithm() :

    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181]
    print(primes)
    P1 = primes[:len(primes)//2]
    P2 = primes[len(primes)//2:]

    print(P1)
    print(P2)

    Q1, Q2 = [1], [1]
    for i in P1 :
        Q1 += [ i*j for j in Q1 ]

    for i in P2 :
        Q2 += [ i*j for j in Q2 ]


    Q1 = sorted(Q1, reverse=False)
    Q2 = sorted(Q2, reverse=True)
    print(Q1[:50])
    print(Q2[:50])

    # === Same result can be achieved with the following approach
    def all_factors_combinations(lst) :
        ''' Returns the combinations of all elements from a list, preferable a prime factor list'''
        L =[1]
        for i in range(1, len(lst)+1 ) :
            c = list(combinations(lst, i))
            for j in c :
                L.append( functools.reduce(operator.mul, j) )
                # print(L)
        print(L)
        return L
    # all_factors_combinations(P1)

    l1, l2, = len(Q1), len(Q2)
    print('---- Those two approaches are also equivalent ---- NICE !! ---')
    target = sqrt( functools.reduce(operator.mul, P1+P2) )
    target2 = sqrt( Q1[-1] * Q2[0] )
    print('target1 = ',target ,'      target2 = ', target2)

    ### Main solution
    i, j, best = 0, 0, 0
    while i< l1 and j < l2 :
        curr_prod = Q1[i]*Q2[j]
        # print(curr_prod)
        if curr_prod > target :
            j += 1
        elif curr_prod < target :
            if curr_prod > best :
                best = curr_prod
                print('best = ', best)
            i += 1

    print('\nResult : \t',best)

    R1 = get_factors(best)
    print('the primes of the first half list are : ', R1)

    R2 = (set(primes)).difference(set(R1))
    print('the primes of the second half list are : ', sorted(list(R2)))



    return print('\nthe last 16 digits are : ', best%(10**16))

closest_product_subset_list_algorithm()

t2  = time.time()
print('\nCompleted in :', round((t2-t1) ,4), 's\n\n')



