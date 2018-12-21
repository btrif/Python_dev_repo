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
            cand[cand[i] + i::cand[i]] = [None] * ((n // cand[i]) - (n // (2 * cand[i])) - 1)

    # Filter out non-primes and return the list.
    return [2] + [i for i in cand if i]

def gen_prime_list(nr):
    primes_list = prime_generator(int(nr**0.5)+1)
    return primes_list

# nr=1979197919791979
nr=5040*13*29*73
primes_list = gen_prime_list(nr)

def factorize(n):
    prime_multiples = []
    for item in primes_list:
        if item > n:
            break
        else:
            while n > 1:
                if n % item == 0:
                    n //= item
                    prime_multiples.append(item)
                else:
                    break
    return prime_multiples

t1  = time.time()


print('!!!!!!!     The NEW Function ',factorize(nr))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

###############################################

t1  = time.time()

# def factoriBe(a):
#     '''Outputs a list of the unique prime factors of its input; The Second Fastest Algorithm
#     This Function is splitting a number in its factors, and detects also if the number is a prime. '''
#     b = 2
#     d = []
#     f = a
#     while f > 1:
#         while f % b != 0:
#             b = b + 1
#         d = d + [b]
#         f = f / b
#     if len(d) >1:
#         return d
#     #else: print(a,' is prime')

def factor_pyprimes(n):
    ''' Decompose a factor in its prime factors. This function uses the pyprimes module. THE FASTEST  '''
    from pyprimes import factorise
    return [val for sublist in [[i[0]]*i[1] for i in factorise(n)] for val in sublist]


# print('My previous Function : ',factoriBe(nr))
print('My previous Function : ',factor_pyprimes(nr))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')



t1  = time.time()





t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')












# def main():

#
# if __name__ == "__main__": main()
