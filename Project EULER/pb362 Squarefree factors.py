#  Created by Bogdan Trif on 15-05-2018 , 10:06 AM.
# © o(^_^)o  Solved by Bogdan Trif  @
#The  Euler Project  https://projecteuler.net
'''
            Squarefree factors      -           Problem 362

Consider the number 54.
54 can be factored in 7 distinct ways into one or more factors larger than 1:
54, 2×27, 3×18, 6×9, 3×3×6, 2×3×9 and 2×3×3×3.
If we require that the factors are all squarefree only two ways remain: 3×3×6 and 2×3×3×3.

Let's call Fsf(n) the number of ways n can be factored into one or more squarefree factors larger than 1, so Fsf(54)=2.

Let S(n) be ∑Fsf(k) for k=2 to n.

S(100)=193.

Find S(10 000 000 000).

'''
import time, zzz
from gmpy2 import is_prime, is_square

def prime_generator(lower, upper):      ### o(^_^)o  FASTEST  o(^_^)o  ###  HIghly Efficient !!!
    """  Sieve of Eratosthenes              !!!!!!!!! THE FASTEST SIEVE. It won the battle with sieve
    Create a candidate list within which non-primes will be marked as None.         """
    cand = [i for i in range(3, upper + 1, 2)]
    end = int(upper ** 0.5) // 2

    # Loop over candidates (cand), marking out each multiple.
    for i in range(end):
        if cand[i]:
            cand[cand[i] + i::cand[i]] = [None] * ( (upper // cand[i]) - (upper // (2 * cand[i])) - 1 )

    # Filter out non-primes and return the list.
    return [2] + [ i for i in cand if i and i > lower ]

def get_factors(n):       ### o(^_^)o  FASTEST  o(^_^)o  ###
    ''' Decompose a factor in its prime factors. This function uses the pyprimes module. THE FASTEST  '''
    from pyprimes import factorise
    return [val for sublist in [[i[0]]*i[1] for i in factorise(n)] for val in sublist]

P = prime_generator(2, 10**2)

def square_free_nr(n):
    for i in P :
        if (n / i**2) % 1 == 0 :
            return False
    return True

def all_Factorizations(n):        # VERY EFFICIENT !!!! SUPER INTELLIGENT ALGORITHM
    '''Pair Factoring, VERY EFFICIENT !
    :param n:
    :return:     '''
    todo, combis = [ (n, 2, []) ], []
    if square_free_nr(n) : combis.append([n])
    while todo:
        n, i, combi = todo.pop()
        while i * i <= n : #and is_square(i) == False  :
            if n % i == 0 :
                if square_free_nr(n//i ) and square_free_nr( i )    :
                    combis += combi + [i, n//i],

                todo += (n//i, i, combi+[i]),       # If needed only PAIRS (a,b) comment this line !!!
            i += 1

    return combis



print('\n--------------------------TESTS------------------------------')
t1  = time.time()

print(all_Factorizations(100))
# print(get_factors(54))

def brute_force_test(lim):
    cnt = 0
    for n in range(2, lim+1) :
        if is_prime(n) :
            cnt += 1
        else :
            aF = all_Factorizations(n)
            print('n =', n, '     aF = ', aF,'         len =', len(aF) )
            cnt += len(aF)

    return print('\nBF Count = ', cnt)

brute_force_test(10**2)

'''
@2018-05-15 - Error here : n = 100      aF =  [[10, 10], [4, 5, 5], [2, 5, 10], [2, 2, 5, 5]]   len = 4 ;  Shouldn't appear [ 4, 5, 5 ]
@2018-05-27 - I think it can be done with an O(sqrt(n)) algorithm
IDEA: take 2: => 2x2 = 4, 2x3 = 6, 2x2x2 = 8, 2x5=10; 2x2x3=12, 2x6 = 12, 2x7 = 14, 2x2x2x2 = 16 ;
2x3x3 = 18, 6x3 = 18, 2x2x5 = 20, 2x10 = 20
3x5 = 15, 3x7 = 21 ... and so on ...
Try to find a formula based on Combinations !
@2019-01-05 -   IMPORTANT REMARK - WE must count number of ways

n = 42      aF =  [[42], [2, 21], [3, 14], [6, 7], [2, 3, 7]]          len = 5
n = 48      aF =  [[2, 2, 2, 6], [2, 2, 2, 2, 3]]          len = 2
n = 60      aF =  [[2, 30], [6, 10], [2, 2, 15], [2, 3, 10], [2, 5, 6], [2, 2, 3, 5]]          len = 6
n = 78      aF =  [[78], [2, 39], [3, 26], [6, 13], [2, 3, 13]]          len = 5
n = 84      aF =  [[2, 42], [6, 14], [2, 2, 21], [2, 3, 14], [2, 6, 7], [2, 2, 3, 7]]          len = 6
n = 90      aF =  [[3, 30], [6, 15], [3, 3, 10], [3, 5, 6], [2, 3, 15], [2, 3, 3, 5]]          len = 6

http://mathworld.wolfram.com/SquarefreeFactorization.html
https://en.wikipedia.org/wiki/Square-free_polynomial

@2019-01-31 --> IDEA TO Solve :
1.  Generate the primes up to 10**8
2.  Generate all the SQUARE FREE FACTORS which will generate all numbers of the form :
2, 3, 5, 6, 7, 10, 11, 13, 14, 15, 17, 19, 21, 22, 23, 26, 29, 30, 31, 33, 34 ...
which are all square free and have the form :  p1, p1*p2,  p1*p2*p3, ...etc
3.  Make a counter function which will generate and go like this , Small example up to 10**2 :
--------    2 factors   -------------
[2], [3], ... [last_prime < 10**2]
[2, 2], [2, 3], [2, 5], [2, 6], ... [2, 47] 
[3, 5], [3, 6], [3, 7], [3, 10], ... [3, 33]
 ...
 [10, 10]
-------------- 3 factors    -------
[2, 2, 2], [2, 2, 3], ... [2, 2, 23]
[2, 3, 3], [2, 3, 5], ... [2, 3, 15]
...   up to 10**2**(1/3)  = 4.63 = 3
[3, 3, 3], [3, 3, 5], [3, 3, 6], [3, 3, 7], [3, 3, 10]

----------- 4 factors -------------
[2, 2, 2, 2], [2, 2, 2, 3], [2, 2, 2, 5], [2, 2, 2, 6], [2, 2, 2, 7], [2, 2, 2, 10], [2, 2, 2, 11] 
...
[3, 3, 3, 3]
----------- 5 factors -------------
[2 2 2 2 2], [2 2 2 2 3], [2 2 2 2 5], [2 2 2 2 6]  
----------- 6 factors -------------
[2 2 2 2 2 2], [2 2 2 2 2 3]

4.   SECOND PART of the problem : 
take all the combinations of factors up to 10**2 and :
------  1 factor --------
[2]   in combination with nr of primes between 10**8 and 10**10/2
[3]   in combination with nr of primes between 10**8 and 10**10/3
[5]   in combination with nr of primes between 10**8 and 10**10/5
...

[97]  in combination with nr of primes between 10**8 and 10**10/97
------  2 factors --------
[2, 2]  in combination with nr of primes between 10**8 and 10**10 / 4
...
[10, 10]  in combination with nr of primes between 10**8 and 10**10 / 100
...
...
------  6 factors --------
[2 2 2 2 2 2] in combination with nr of primes between 10**8 and 10**10 / 64
[2 2 2 2 2 3] in combination with nr of primes between 10**8 and 10**10 / 96





'''

https://stackoverflow.com/questions/19070911/feasible-implementation-of-a-prime-counting-function
https://en.wikipedia.org/wiki/Prime-counting_function
https://github.com/kimwalisch/primecount/tree/master/src
http://mathworld.wolfram.com/PrimeCountingFunction.html


WATCH ALGO from problem 193 - Squarefree Numbers


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

