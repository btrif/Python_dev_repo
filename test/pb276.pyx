from cpython cimport array
import array

import time
from pyprimes import factorise
import functools, operator, itertools
import numpy as np

cpdef int gcd(int a, int b):      # GCD
    """Return greatest common divisor using Euclid's Algorithm."""
    while b:
        a, b = b, a % b
    return a

cpdef int gcd3(int a, int b, int c):
    return gcd(gcd(a, b), c)


cpdef list_to_set(list huge_list):
    cdef list ids
    cdef set final_ids = set()
    for ids in huge_list:
        final_ids.update(set(ids))
    return final_ids

cpdef list get_factors( int n):       # From mhb038, England, Euler Forum
    """returns the prime factors of n"""

    cdef int i = 2
    cdef set factors = set()

    while i * i <= n:
        if n % i:
            i += 1
        else :
            n //= i
            factors.add(i)   # = np.insert(factors, [i])
    if n > 1  :
        factors.add(n)  # = np.insert(factors, [n])

    cdef list factors1 = list(factors)
    return factors1


cpdef list Ccombinations(n, list lst, list combos=[]):
    # initialize combos during the first pass through
    if combos is None:
        combos = []
    cdef int cmb = combos.count(lst)
    cdef int length = len(lst)
    cdef list refined_list
    if length == n:
        # when list has been dwindeled down to size n
        # check to see if the combo has already been found
        # if not, add it to our list

        if cmb == 0 :
            combos.append(lst)
            combos.sort()
        return combos
    else:
        # for each item in our list, make a recursive
        # call to find all possible combos of it and
        # the remaining items
        for i in range(len(lst)):
            refined_list = list(lst[:i]) + list(lst[i+1:])
            combos = Ccombinations(n, refined_list, combos)
        return combos


# list(combinations_by_subset([1,2,3,4,5], 3)   )


print('\n--------------------------TESTS------------------------------')
t1  = time.time()


cpdef double Primitive_integer_sided_triangles(int perim) :
    cdef double cnt = 0
    cdef int p = perim
    cdef int a
    cdef int b
    cdef int i
    cdef int k
    cdef int g
    cdef int f
    cdef list C
    cdef set F
    cdef tuple J



    for a in range(1, p//3+1) :
        print("size = " , a )# , "      cnt=", cnt)
        for b in range(a, (p-a)//2 + 1 ) :

                    # CASE 1
            if gcd(a,b)  == 1 :
                cnt += p-a-2*b+1
                if ( a+b <= p/2 )  :      # we substract the cases like a,b,c = 1,1,2 to a,b,c = 25,25,50
                    cnt -= 1

                    # CASE 2
            if ( gcd(a,b) != 1   ) :
                cnt +=  p - a- 2*b+1
                g = gcd(a,b)
                F =  set(get_factors(g))
                for i in range(1, len(F)+1) :
                    C = list( itertools.combinations( F, i ) )
                    for J in C :
                        f = functools.reduce( operator.mul , J)
                    # C = Ccombinations( i ,F  )
                    # for J in C :
                    #     f = 1
                    #     for k in J :
                    #         f *= k

                        if i%2 == 1 :
                            cnt -= ((p-a-2*b)//f) +1
                        if i%2 == 0 :
                            cnt +=  ((p-a-2*b)//f) +1

    return cnt

# Primitive_integer_sided_triangles(1000)
