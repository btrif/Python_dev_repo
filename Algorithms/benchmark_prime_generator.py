import time

def prime_generator(n):
    """  Sieve of Eratosthenes
    Create a candidate list within which non-primes will be marked as None.
    """
    cand = [i for i in range(3, n + 1, 2)]
    end = int(n ** 0.5) // 2

    # Loop over candidates (cand), marking out each multiple.
    for i in range(end):
        if cand[i]:
            cand[cand[i] + i::cand[i]] = [None] * ( (n // cand[i]) - (n // (2 * cand[i])) - 1 )

    # Filter out non-primes and return the list.
    return [2] + [i for i in cand if i]


def sieve(lower, upper_bound):
    ''':Description:        SIEVE OF ERATOSTHENES ALGORITHM  ,
    :param:      :lower: = lower_integer including
                     :upper_bound: = upper integer excluding
    :returns:   a list containing all primes between lower and upper bound
    :Usage:             Example:    primes = sieve(2, 100)                    '''

    n = upper_bound + 1
    check = [True] * n
    check[0] = check[1] = False
    for i in range(2, int(upper_bound**0.5) + 1):
        if check[i]:
            for j in range(i**2, upper_bound + 1, i):
                check[j] = False
    primes = [i for i, flag in enumerate(check) if flag and i > lower ]
    return primes


#######################################



t1  = time.time()

primus = prime_generator(10**5)
print( len(primus) ,primus[0:10000])

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

###################

t1  = time.time()

primes= sieve(1 , 10**5)
print(len(primes) ,  primes[0:10000])

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
