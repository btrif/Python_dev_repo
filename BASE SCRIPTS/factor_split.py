import time

def primes(nr_to_check):
    primes=[]
    n = nr_to_check
    i = 2
    while(i < n):
        j = 2
        while(j <= (i/j)):
            if not(i%j): break          # IF  it's TRUE it stops, if FALSE it continues    # VERY IMPORTANT This line checks if the number is PRIME
            j = j + 1                       #Returns FALSE and continues if is i%j = 0 ; Returns TRUE and stops if i%j = 1,2,....

        if (j > i/j) : print( i, end= ' ')     #   primes.append(i)  print( i, end= ' ')     # If j > i/j means that the number is not already in the list, therefore must be another prime
        i = i + 1


primes(90)
print('\n'*2)

#################################################
print('-------------------------   The VERY SLOW METHOD   ---------------------------')

t1  = time.time()

def factor_slow(nr_to_check):
    primes=[]
    n = nr_to_check
    i = 2
    while(i < n):
        j = 2
        while(j <= (i/j)):
            if not(i%j): break          # IF  it's TRUE it stops, if FALSE it continues    # VERY IMPORTANT This line checks if the number is PRIME
            j = j + 1                       #Returns FALSE and continues if is i%j = 0 ; Returns TRUE and stops if i%j = 1,2,....
        if (j > i/j) : primes.append(i)    #     print( i, end= ' ')     # If j > i/j means that the number is not already in the list, therefore must be another prime
        i = i + 1

    factors=[]
    for x in primes:
        while n % x == 0 :
            n = n / x
            factors.append(x)
    if len(factors) != 0:
        print('\nThe factors of ',nr_to_check ,'are : ' ,factors, end = '')  #return factors #
    else :
        print('    ',nr_to_check,' is prime   ')  #else : return False

factor_slow(11)

t2  = time.time()
print('\nCompleted in :', (t2-t1)*1000, 'ms')

#################################################
print('\n-------------------------   The EFFICIENT METHOD   ---------------------------')


t1  = time.time()

def factors(n):
    nr_to_check = n
    factors=[]
    i, j = 2, 2
    while ( i<=n ) :
        while ( j < i/j ):
            if not (i%j) : break
            j +=1
        if (j > i/j) :
            if n % i == 0 :
                n = n / i           # Update n
                factors.append(i)
        if n % i != 0 :
            i += 1
    if len(factors) > 1:
                print('The factors of ',nr_to_check ,'are : ' ,factors)
    else : print(nr_to_check,' is prime')

factors(1979)

t2  = time.time()
print('\nCompleted in :', (t2-t1)*1000, 'ms\n')

print('\n-------------------------   The MOST EFFICIENT METHOD   ---------------------------')

t1  = time.time()

def factorizer(a): ##outputs a list of the unique prime factors of its input
    b = 2
    d = []
    f = a
    while f > 1:
        while f % b != 0:
            b = b + 1
        d = d + [b]
        f = f / b
    if len(d) >1:
        print('Factors of',a,' are : ',d)
    else: print(a,' is prime')

factorizer(1499)

t2  = time.time()
print('\nCompleted in :', (t2-t1)*1000, 'ms\n')         #Completed in 995.0568675994873 ms

print('--------------------------------------------\n')
for i in range(1000000,1000005 ):     factors(i)
