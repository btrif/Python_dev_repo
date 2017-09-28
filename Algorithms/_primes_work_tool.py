#!/usr/bin/python
import time, functools, itertools
from math import  gcd, sqrt, log
# The Most basic

# Prime numbers GENERATOR
print('---'*20,'PRIME NUMBERS GENERATOR - METHOD 1','---'*20)
t1  = time.time()

i = 2                              #Set the starting Prime, First Prime in the list, MAIN VARIABLE
END = 100                               #Set the END Prime, First Prime in the list, MAIN VARIABLE
while(i < END):                 # Set the last Prime Number - the Upper Limit
    j = 2
    while(j <= (i/j)):              # This condition checks in the lower list
        if not(i%j): break          # IF  it's TRUE it stops, if FALSE it continues    # VERY IMPORTANT This line checks if the number is PRIME
        j = j + 1                       #Returns FALSE and continues if is i%j = 0 ; Returns TRUE and stops if i%j = 1,2,....
    if (j > i/j) : print( i, " is prime", end= ';   ')           # If j > i/j means that the number is not already in the list, therefore must be another prime
    i = i + 1
print ("Good bye!")
print('------'*25)

t2  = time.time()
print('\n',END ,' primes generated in :', round((t2-t1)*1000,4), 'ms\n')


print('---'*20,'PRIME NUMBERS GENERATOR - FAST & ELEGANT WAY','---'*20)
t1  = time.time()

def primes(n):
    from math import sqrt
    count = 3
    while count < n:
        isprime = True

        for x in range(2, int(sqrt(count) + 1)):
            if count % x == 0:
                isprime = False
                break
        if isprime:
            print (count, end=' ')
        count += 1

primes(1000)

t2  = time.time()
print('\n' ,' primes generated in :', round((t2-t1)*1000,4), 'ms\n')


print('---'*20,'SIEVE of ERATOSTHENES :  Efficient PRIME GENERATOR algorithms','---'*20)
t1  = time.time()



import numpy
def prime_sieve_numpy(n):                       ### o(^_^)o  FASTEST  o(^_^)o  ###  Highly Efficient !!!
    """ Input n>=6, Returns a array of primes, 2 <= p < n
    http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n/3035188#3035188 """
    sieve = numpy.ones(n//3 + (n%6==2), dtype=numpy.bool)
    for i in range(1,int(n**0.5)//3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[       k*k//3     ::2*k] = False
            sieve[k*(k-2*(i&1)+4)//3::2*k] = False
    return numpy.r_[2,3,((3*numpy.nonzero(sieve)[0][1:]+1)|1)]


def primesfrom3to(n):               ### o(^_^)o  FASTEST  o(^_^)o  ###  Highly Efficient !!!
    """ Returns a array of primes, 3 <= p < n
    http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n/3035188#3035188
      SIEVE of ERATOSTHENES                       """
    sieve = numpy.ones(n//2, dtype=numpy.bool)
    for i in range(3, int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = False
    return 2*numpy.nonzero(sieve)[0][1::]+1

def prime_sieve_numpy_2(n):          ### THIRD
    import numpy as np
    """return array of primes 2<=p<=n"""
    sieve=np.ones( n+1, dtype=bool )
    for i in range( 2, int((n+1)**0.5+1) ) :
        if sieve[i] :
            sieve[2*i :: i] = False
    return np.nonzero(sieve)[0][2:]


print('-----To generate 10 to some power of primes use the bellow formula, log is in 10 base :-------')
lim = 10**5
primes = prime_sieve_numpy(int( lim * log(lim)*1.2 ) )
print(len(primes), primes[:50] ,'\n\n' )


def prime_sieve(n):       # FOURTH      o(^_^)o
    sieve = [True] * n
    for i in range(3, int(n**0.5)+1, 2):
        if sieve[i]:
            sieve[ i*i :: 2*i ] = [False] * ( (n-i*i-1) // (2*i) +1 )
    return [2] + [i for i in range(3, n , 2) if sieve[i] ]

def prime_sieve_generator(lower, upper):      #FIFTH FASTEST
    """  Sieve of Eratosthenes
    Create a candidate list within which non-primes will be marked as None.         """
    cand = [i for i in range(3, upper + 1, 2)]
    end = int(upper ** 0.5) // 2

    # Loop over candidates (cand), marking out each multiple.
    for i in range(end):
        if cand[i]:
            cand[cand[i] + i::cand[i]] = [None] * ( (upper // cand[i]) - (upper // (2 * cand[i])) - 1 )

    # Filter out non-primes and return the list.
    return [2] + [ i for i in cand if i and i > lower ]




def sieve_2(lower, upper_bound):          # SIXTH
    ''':Description:        SIEVE OF ERATOSTHENES ALGORITHM  , SECOND FASTEST
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

print(sieve_2(11900, 12000))


def primes_up_to(n):            #### SEVENTH
    ''' SIEVE of ERATOSTHENES :  PRIME GENERATOR algorithms
        # http://code.activestate.com/recipes/576640/ '''
    import math
    nroot = int(math.sqrt(n))
    sieve = [True] * (n + 1)# range(n + 1)
    sieve[0] = False
    sieve[1] = False

    for i in range(2, nroot+1):
        if sieve[i]:
            m = n / i - i
            # print(i,'   ', m )
            sieve[i * i: n + 1: i] = [False] * (int(m) + 1)

    return [i for i in range(n+1) if sieve[i]]


def gen_primes(limit):                                  # EIGHTH
    ''' SIEVE of ERATOSTHENES :  Efficient PRIME GENERATOR algorithms
    Code by David Eppstein, UC Irvine, 28 Feb 2002,     http://code.activestate.com/recipes/117119/ '''
    D = {}
    i = 2
    while i <= limit:
        if i not in D:
            yield i
            D[i * i] = [i]
        else:
            for p in D[i]:
                D.setdefault(p + i, []).append(p)
            del D[i]
        i += 1

p = gen_primes(1000)
primus = [i for i in p]
print (primus)


t2  = time.time()
print('\n' ,' primes generated in :', round((t2-t1)*1000,4), 'ms\n')

t1  = time.time()

from itertools import filterfalse
def Eratosthène_sieve(N) :              ### @2017-03-21 - Not yet tested but IS SLOW !!!
    ## -- Crible d'Eratosthène jusqu'à N ------------------
    vPrime = list(range(N + 1))
    vPrime[1] = 0

    d = 2
    while d**2 <= N:
        vPrime[d*2::d] = [0]*(N//d - 1)
        d += 1
        while not vPrime[d]:
            d += 1
    vPrime = list(filter(lambda i : i!=0 in vPrime  , vPrime ))
    return vPrime

t2  = time.time()
print('\n' ,' primes generated in :', round((t2-t1)*1000,4), 'ms\n')

###################################

print('\n---------------------------------DETECT PRIME --------------------------------')

print('\n---------------------- Fastest Method to check for a prime is gmpy2 Module --------------')
import gmpy2
# print('gmpy2 is prime Test ',gmpy2.is_prime( 18014398241046527))
print('gmpy2 is prime Test - THE FASTEST tested :  ',gmpy2.is_prime( 10000079 ) )


def Miller_Rabin(p, k = 50):  # Miller-Rabin primality test
    import random
    if p == 2: return True
    if p < 2 or p & 1 == 0: return False

    d = (p - 1) >> 1
    while d & 1 == 0:
        d >>= 1

    for i in range(k):
        a = random.randint(1, p - 1)
        t = d
        y = pow(a, t, p)
        while t != p - 1 and y != 1 and y != p - 1:
            y = pow(y, 2, p)
            t <<= 1
        if y != p - 1 and t & 1 == 0:
            return False
    return True

print('Miller_Rabin Primality Algorithm Test: \t' , Miller_Rabin(151681868531) )

def isprime(n):
    ''' SLOWER METHOD. But Does not depend on a pre-generated sieve or on other module !'''
    if n == 1:
        return False
    for i in range(2, int((n**0.5)+1)):
        if not n % i:
            return False
    return True


# print(isprime(100000980001501))
print('isprime  Function Test:    ',isprime(10000079))


# primes = sieve_2(2,10000079)     # MUST BE Generated outside of the function for EFFICIENCY !
primes = sieve_2(2,1000)     # MUST BE Generated outside of the function for EFFICIENCY !
def is_prime(num):
    ''' Second Fastest DETECT PRIME BUT Dependent on the pre-generated sieve(lower, upper_bound).
        Is efficient ONLY if uses a list of pre-generated primes outside the function.
    :Usage:     If you work with BIG primes, ASSURE that you have build a list up to the square root of that prime,
                    otherwise will generate errors !
    :Example:   If you work with : 100000980001501 = [10000019, 10000079] assure you have the UP Sieve > 10000079 '''
    root = int((num)**0.5 + 1)
    for i in primes:
        if i > root:
            break
        if num % i == 0:
            return False
    return True

# print('is_prime function test :  ',is_prime(100000980001501))

#X = 19791979197911             # Type the  number you want to check
X = 1979
# X = 6597326399323993

if is_prime(X) == 1 : print(X ,' IS a Prime !')
else : print('is_prime Function test  :   ',X,' NOT a Prime ')

'''
def detect_prime(n):                # Function which checks if a number is prime
    # Function which checks if a number is prime
    i = n
    while(i <= n):
        j = 2
        while(j <= (i/j)):
            if not(i%j):
                return False
                break
            j = j + 1
        if (j > i/j) : return True
        i = i + 1

if detect_prime(X) == True : print(X ,' IS a Prime !')
else : print(X,' NOT a Prime ')
'''


t1  = time.time()



t2  = time.time()
print('\n','Completed in : ', round((t2-t1)*1000,4), 'ms')
######################################################

print('------'*20)
print('---'*20,'PRIME NUMBERS GENERATOR - using FOR LOOP, THE MOST BASIC - SLOW','---'*20)

for n in range(2, 16):
     for x in range(2, n):
         if n % x == 0:
             print(n, 'equals', x, '*', n // x, end = ';  ')
             break
     else:
         print(n, 'is a prime number', end = ';  ')

print('-----'*20,'\n')

#############################################

# Prime numbers GENERATOR Function
def primes_gen(i=81, END=100 ):
    '''  Prime numbers GENERATOR Function
    i - Sets the starting Prime, First Prime in the list, MAIN VARIABLE
    END - Sets the END Prime, First Prime in the list, MAIN VARIABLE
    '''
    while(i < END):                 # Set the last Prime Number - the Upper Limit
        j = 2
        while(j <= (i/j)):              # This condition checks in the lower list
            if not(i%j): break          # IF  it's TRUE it stops, if FALSE it continues    # VERY IMPORTANT This line checks if the number is PRIME
            j = j + 1                       #Returns FALSE and continues if is i%j = 0 ; Returns TRUE and stops if i%j = 1,2,....
        if (j > i/j) : print( i, end=' ')           # If j > i/j means that the number is not already in the list, therefore must be another prime
        i = i + 1
primes_gen(100,250)

##################################################################
print('\n\n','=='*20,'    PERFORMANCE TESTS    ','=='*20)
import time

CHECK_NR = 1000               # Here you put the test number for both for and while cases

print('--------FOR LOOP TEST---------')
t1  = time.time()
tmp1=[]
for n in range(2, CHECK_NR):
     for x in range(2, n):
         if n % x == 0:
             #print(n, 'equals', x, '*', n // x)
             break
     else:
            tmp1.append(n)
            #print(n, end=' ')

t2  = time.time()
print('\n',len(tmp1) ,' primes generated in :', round((t2-t1)*1000,4), 'ms')            #9592  primes generated in : 166006.495 ms

###################################################

print('\n','-----'*20)
print('\n--------WHILE LOOP TEST, FAR MORE EFFICIENT THAN FOR---------')
t1  = time.time()
tmp2=[]

i=2
while(i < CHECK_NR):                 # Set the last Prime Number - the Upper Limit
    j = 2
    while(j <= (i/j)):              # This condition checks in the lower list
        if not(i%j): break          # IF  it's TRUE it stops, if FALSE it continues    # VERY IMPORTANT This line checks if the number is PRIME
        j = j + 1                       #Returns FALSE and continues if is i%j = 0 ; Returns TRUE and stops if i%j = 1,2,....
    if (j > i/j) :  tmp2.append(i)  #   print( i, end= ' ')        # If j > i/j means that the number is not already in the list, therefore must be another prime
    i = i + 1

t2  = time.time()
print('\n',len(tmp2) ,' primes generated in :', round((t2-t1)*1000,4), 'ms')    #9592  primes generated in : 2366.1354 ms

######################################

print('\n\n=============  FACTOR DECOMPOSITION  ===================')

def factors(a):
    '''Outputs a list of the unique prime factors of its input; The Second Fastest Algorithm
    This Function is splitting a number in its factors, and detects also if the number is a prime. '''
    b = 2
    d = []
    f = a
    while f > 1:
        while f % b != 0:
            b = b + 1
        d = d + [b]
        f = f / b
    if len(d) >1:
        print('The factors of  ',a,':   ',d)
    else: print(a,' is prime')

factors(int(''.join(('1', '8', '9', '9', '3', '4', '3'))))          # The factors of  999997 are :  [757, 1321], The factors of  428571 are :  [3, 3, 3, 3, 11, 13, 37]


print('-------------- Using module pyprimes , FASTEST FACTOR DECOMPOSITION ---------------------------')

def get_factors(n):       ### o(^_^)o  FASTEST  o(^_^)o  ###
    ''' Decompose a factor in its prime factors. This function uses the pyprimes module. THE FASTEST  '''
    from pyprimes import factorise
    return [val for sublist in [[i[0]]*i[1] for i in factorise(n)] for val in sublist]

print(get_factors(1979197919791979))
#print(list(i[0] for i in list(factorise(3932273))))


def prime_factors(n):       # From mhb038, England, Euler Forum
    """returns the prime factors of n"""
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


def factor(n):
    '''  Factor as a dictionary. Must test the speed ...'''
    Factors = {}
    if n%2 ==0:
        Factors[2]=1
        n = n//2
        while n%2==0:
            Factors[2]+=1
            n = n//2
    p=3
    while n>1:
        if n%p==0:
            Factors[p]=1
            n=n//p
            while n%p==0:
                Factors[p]+=1
                n=n//p
        else:
            p+=2
    return Factors
factor(32)




#####################################################

#   CMMDC - Cel Mai Mare Divizor Comun - The Greatest Common Divisor - GCD
print('\n------------   CMMDC - Cel Mai Mare Divizor Comun - The Greatest Common Divisor - GCD ------------------')

def cmmdc(a, b):        # GCD
    '''a, b: positive integers     , cmmdc, c.m.m.d.c., Cel Mai Mare Divizor Comun
    returns: a positive integer,  The Greatest Common Divisor of a & b.   '''
    testValue = min(a, b)
    # Keep looping until testValue divides both a & b evenly
    while a % testValue != 0 or b % testValue != 0:
        testValue -= 1
    return testValue

def cmmdc_rec(a, b):        #  GCD, CMMDC Recursive
    '''    a, b: positive integers     , cmmdc, c.m.m.d.c., Cel Mai Mare Divizor Comun
        returns: a positive integer,  The Greatest Common Divisor of a & b.    '''
    if b == 0:
       return a
    else:
       return cmmdc_rec(b, a % b)

def gcd(a, b):      # GCD
    """Return greatest common divisor using Euclid's Algorithm."""
    while b:
        a, b = b, a % b
    return a


print('Test for the GCD cmmdc Function :\t',cmmdc(1445468, 300173))
print('Test for the GCD cmmdc_rec Function :\t',cmmdc(1445468, 300173))
print('Test for the GCD math.gcd Function :\t',cmmdc(1445468, 300173))
print('Test for the GCD gcd Custom Function :\t',cmmdc(1445468, 300173))
print(cmmdc_rec(1445, 3005))
factors(197)


print('\n------------   CMMMC - Cel Mai Mic Multiplu  Comun - The Lowest Common Multiple LCM ------------------')

def lcm(a, b):
    """Return lowest common multiple."""
    return a * b // gcd(a, b)

print('LCM, Cel Mai Mic Multiplu  Comun Test :  \t',lcm(120, 121))

print('\n--------------------------------CIRCULAR PRIMES -----------------------------------')
############################################################################
# Function CIRCULAR PRIMES, Check if the CIRCULAR permutations of a number are primes

def circulate_number(A):
      tmp=[]
      for v in range(len(str(A))):
            a , i , s =  str(A), len(str(A)), ''
            for c in range(i):
                  #print(a[(v+c) % j] ,end='  ')
                  s += str(a[(v+c) % i])
            #return s
            tmp.append(int(s))
            #print(s)
            v+= 1
      return tmp #print(tmp)


def circular_primes(n):
    '''Function which checks if the permutations of a number are primes
    Depends on the Function detect_prime & circulate_number'''
    counter=0
    for x in circulate_number(n):
            if (is_prime(x) == 1 ):
                counter+=1
                print(x, end=' ')
    if (len(str(n)) == counter): return True    #   print('YES, all permutations are prime !')
    else:  return False                                 #print('NO, only',counter,' are primes')

print(circulate_number(1234))
print(circular_primes(197))
###################################################

print('\n---------------------------- DIVISORS --------------------------------')

class PrimeTable():    #  ( ͡° ͜ʖ ͡°)  ### !! FIRST FASTEST
    def __init__(self, bound):
        self.bound = bound
        self.primes = []
        self._sieve()

    def _sieve(self):
        visited = [False] * (self.bound + 1)
        visited[0] = visited[1] = True
        for i in range(2, self.bound + 1):
            if not visited[i]:
                self.primes.append(i)
            for j in range(i + i, self.bound + 1, i):
                visited[j] = True
        print('Prime count:', len(self.primes))

class Factorization():

    ''' Based on a prebuilt prime sieve, and we must pay attention that the prime up range is not
    to low, so that we don't miss a prime when we first factor . As default the value is set to 10.000   '''
    def __init__(self):
        self.prime_table = PrimeTable(10**4)

    def get_divisors(self, n):
        d = n
        f = {}
        for p in self.prime_table.primes:
            if d == 1 or p > d:
                break
            e = 0
            while d % p == 0:
                d = d // p
                e += 1
            if e > 0:
                f[p] = e
        if d > 1:
            f[d] = 1
            #raise Exception('prime factor should be small', d)
        unpacking = [[p**e for e in range(f[p] + 1)] for p in f]
        return sorted([self._product(divisor) for divisor in itertools.product(*unpacking)])

    def _product(self, list):
        result = 1
        for number in list:
            result *= number
        return result


F  = Factorization()
print( F.get_divisors(180180) )


def get_divisors(n):      ### ( ͡° ͜ʖ ͡°)  SECOND FASTEST ,  MUST BE IMPROVED !! It is a sqrt(n) Algorithm
    from math import sqrt
    factors = set()
    for x in range(1, int(sqrt(n)) + 1):
        if n % x == 0:
            factors.add(x)
            factors.add(n//x)
    return sorted(factors)

for i in (72, 90, 210): print( "%i: factors: %s" % (i, get_divisors(i)) )



def  calculate_divisors(nr):
    '''**©** Made by Bogdan Trif @ 2016-12-08, 16:30.
        :Description: Functions which computes the number of divisors of a number.
                It uses the Numbers of Divisors Theorem :which says : if N=a**x*b**y*c**z => divisors_nr=(x+1)(y+1)(z+1)
            Example: N = 216 = 2**3 * 3**3 => divisors_nr = (3+1)(3+1) = 16
    :param nr: int, nr
    :return: int, divisors_number                   '''
    import functools, operator
    from pyprimes import factorise
    def factors(nr):
        ''' Decompose a factor in its prime factors. This function uses the pyprimes module. THE FASTEST  '''
        return [i for i in factorise(nr)]
    N = factors(nr)
    return  functools.reduce( operator.mul , [ (i[1]+1) for i in N ])




def get_divisors_2(n):       ### o(^_^)o  #  More powerfull for numbers > 10**10
    ''' first it decomposes the number in prime factors , then makes combinations of all the factors
    to get all the divisors '''
    from pyprimes import factorise
    from itertools import combinations
    from functools import reduce
    from operator import mul
    L = [val for sublist in [[i[0]]*i[1] for i in factorise(n)] for val in sublist]
    D={1}
    for i in range(1, len(L)+1):
        # print( list(combinations(L,i)) )
        for j in list(combinations(L, i) ) :
            D.add ( reduce(mul, j)   )
    return list(sorted(D))


def divisors(n):     # SECOND FASTEST, Very close to the First
    return set(functools.reduce(list.__add__,([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

for i in (72, 90, 210): print( "%i: factors: %s" % (i, divisors(i)) )

class GET_DIVISORS(object):     ### THIRD PLACE, LOW PERFORMANCE
    '''**©** Made by Bogdan Trif @ 2016-11-15, based on itertools.combinations module
    and with a little help on list(functools.reduce(operator.mul, i) for i in comb)

    :param nr:  int
    :return: a list with the factors ( method factorise) or divisors (method divisors)
    :Usage:  >>> GET_DIVISORS().divisors(90)    # to obtain the divisors
                                                                                                              '''
#     def __init__(self, nr):   # We don't want to initialize the class with a number
#     self.nr = nr

    def factorise(self, nr):
        ''' Decompose a factor in its prime factors. This function uses the pyprimes module. THE FASTEST  '''
        from pyprimes import factorise
        return [val for sublist in [[i[0]]*i[1] for i in factorise(nr)] for val in sublist]

    def divisors(self, nr):
        ''':Description: Use the itertools, functools, operator, gmpy2 modules.
        In the case of multiple calls take the module imports outside the class and load only once => improved speed. '''
        from itertools import combinations
        import functools, operator, gmpy2
        if gmpy2.is_prime(nr) == True or nr == 1 :
            return [1]    # Must be adjusted to [1] if you change on list
        else :
            all_factors =  self.factorise(nr)
            # set_factors=list(set(all_factors))
            comb= set()
            # print(all_factors)
            for i in range(1, len(all_factors)):
                c = set(combinations(all_factors, i) )
                comb.update(c)
                comb_prod = list(functools.reduce(operator.mul, i) for i in comb)
                comb_prod.sort()
        return  comb_prod[::-1]   # sum([1]+ comb_prod)   !!! Remember to change on  return [1]  for isprime case !

print('Here we test the GET_DIVISORS CLASS :  ',GET_DIVISORS().divisors(90))




print('\n----------- PAIR FACTORING OF A NUMBER -------------------')

def pair_Factors(n):        # VERY EFFICIENT !!!! SUPER INTELLIGENT ALGORITHM
    '''Pair Factoring, VERY EFFICIENT !
    :param n:
    :return:     '''
    todo, combis = [(n, 2, [])], []
    while todo:
        n, i, combi = todo.pop()
        while i * i <= n:
            if n % i == 0:
                combis += combi + [i, n//i],
                todo += (n//i, i, combi+[i]),       # If needed only PAIRS (a,b) comment this line !!!
            i += 1
    return combis

def pair_Factors_rec(n):        # Recursive Pair Factoring, Just a little bit more slow
    def factor(n, i, combi, combis):
        while i * i <= n:
            if n % i == 0:
                combis += combi + [i, n//i],
                factor(n//i, i, combi+[i], combis)
            i += 1
        return combis
    return factor(n, 2, [], [])


print('pair_Factors : \t', pair_Factors(90))
print('pair_Factors_rec : \t', pair_Factors(90))

print('\n------------------  Digital Root of a number --------------------  ')

def dr(n) :   # Digital Root of a number
    '''':Description: Returns the Digital Root of a number
    https://en.wikipedia.org/wiki/Digital_root#Congruence_formula    '''

    if n == 0 : return 0
    elif n%9 == 0 : return 9
    else : return n%9

print('\nDigital Root of a number : \t 467 \t =\t' ,dr(467) )

print('\n------------------  EULER Phi,  Φ (n) of a number, EULER TOTIENT -------------------- ')

def euler_totient(n):           # Remark : For large array better use Sieve approach
    """ **©** Made by Bogdan Trif @ 2017-02-08 .
    returns Euler totient (phi) of n = Φ (n)
        Uses the formula of the Totient  : Φ (n) =  Π {p | n}  n *(1 - 1/p) ;
        where p are each prime factors and n is the number  for which we compute
        In number theory, Euler's totient function counts the positive integers up to a given integer n
        that are relatively prime to n. It is written using the Greek letter phi as φ(n) or ϕ(n),
        and may also be called Euler's phi function.
        Example : Φ (12) = 4 =   [1,5,7,11]
        https://en.wikipedia.org/wiki/Euler's_totient_function
        http://marcharper.codes/2015-08-07/totients.html            """
    from pyprimes import factorise
    phi = n
    pfs = list(factorise(n))
    print(pfs)
    for pf in pfs:
        phi*=(1-1/pf[0])
    return int(phi)

print('euler_totient : \t', euler_totient(600))
print('euler_totient : \t', euler_totient(90))

def Euler_Totient_Sieve(n):
    ''' Constructs a SIEVE of totients up to n
    :param n: up range number
    :return: list, totients     '''
    phi = list(range(n+1))
    for i in range(2,n+1):
        if phi[i]==i:
            for x in range(i,n+1,i):
                phi[x]-=phi[x]//i
    return phi[1:][:100]            # Take care to remove the [:100], it is only for printing

print('Euler Totient Sieve : \t', Euler_Totient_Sieve(600))



print('\n------------------  Divisor Square Sum  - sigma_2 -------------------- ')

def divisor_square_sum_sigma_2(n):              #σ2(n)
    '''     **Π  = [((p_1**(a_1+1)*2)-1) / (p_1**2 -1)]*...*[ ((p_k**(a_k+1)*2)-1) / (p_k**2 -1) ]**

        condensed form:  = **Π  {p_k - prime, a_k - the exponential of the prime } ((p_k**(a_k+1)*2)-1) / (p_k**2 -1)**
    :where: p_1, p_2,...p_k are the prime factors of the number , together with their
    corresponding coefficients exponentials a_1, a_2,...,a_k
        :param n: int, number
        :return: int, sigma2 representing the Sum of the *Squares* of its divisors !              '''
    # http://math.stackexchange.com/questions/166501/delta-2n-the-sum-of-the-squares-of-the-positive-divisors-of-n
    from pyprimes import factorise
    import functools, operator
    D = list(factorise (n ))
    P = [( i[0]**((i[1]+1)*2)-1 ) //(i[0]**2-1) for i in D ]
    # print(D)
    return functools.reduce(operator.mul, P)

print('Divisor Square Sum Sigma : \t ', divisor_square_sum_sigma_2(429606) )


print('\n------------------  Divisor Sum  - sigma -------------------- ')

def divisor_sum_sigma(n):           #   σ(n)
    '''    **Π  = [(p_1**(a_1+1)-1) / (p_1 -1)]*...*[ (p_k**(a_k+1)-1) / (p_k -1) ]**
     condensed :  = **Π  {p_k - prime, a_k - the exp of the prime } =  ((p_k**(a_k+1)-1) / (p_k -1)**
    :where: p_1, p_2,...p_k are the prime factors of the number , together with their
    corresponding coefficients exponentials a_1, a_2,...,a_k
        :param n: int, number
        :return: int, sigma representing the Sum of its divisors !              '''
    # https://en.wikipedia.org/w/index.php?title=Divisor_function&action=edit&section=4
    from pyprimes import factorise
    import functools, operator
    D = list(factorise (n ))
    P = [( i[0]**(i[1]+1)-1 ) //(i[0]-1) for i in D ]
    # print(D)
    return functools.reduce(operator.mul, P)

test_nr = 429606
print(' divisor_sum_sigma : \t' ,divisor_sum_sigma(test_nr) )

divisors = get_divisors(test_nr)
print('Divisor Sum Term by term Verification Check: ', sum(divisors) ,'\n' ,divisors)


print('\n-------------------- is CUBE ,  is SQUARE   ----------------------')
is_cube = lambda x: int (x**(1/3)+0.5)**3 == x
print('is cube : \t', is_cube(1000)  )
is_square = lambda x :  int(sqrt(x))**2 == x
print('is Square : \t', is_square(1000)  )






