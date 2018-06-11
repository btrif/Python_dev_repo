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
                if square_free_nr(n//i ) and square_free_nr( i )  :
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

@2018-05-15 - Error here : n = 100      aF =  [[10, 10], [4, 5, 5], [2, 5, 10], [2, 2, 5, 5]]   len = 4 ;  Shouldn't appear [ 4, 5, 5 ]
@2018-05-27 - I think it can be done with an O(sqrt(n)) algorithm
IDEA: take 2: => 2x2 = 4, 2x3 = 6, 2x2x2 = 8, 2x5=10; 2x2x3=12, 2x6 = 12, 2x7 = 14, 2x2x2x2 = 16 ;
2x3x3 = 18, 6x3 = 18, 2x2x5 = 20, 2x10 = 20
3x5 = 15, 3x7 = 21 ... and so on ...
Try to find a formula based on Combinations !


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

