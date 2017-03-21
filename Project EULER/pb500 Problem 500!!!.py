#!/usr/bin/python                   o(^_^)o         ( ͡° ͜ʖ ͡°)
# © Solved by Bogdan Trif @     Completed on Wed, 15 Mar 2017, 16:42
#The  Euler Project  https://projecteuler.net
'''
                        Problem 500!!!      -       Problem 500

The number of divisors of 120 is 16.
In fact 120 is the smallest number having 16 divisors.

Find the smallest number with 2**500500 divisors.
Give your answer modulo 500500507.


'''
import time, gmpy2
import functools, operator

def sieve(n):       # SECOND FASTEST
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]

from pyprimes import factorise
def factors(nr):
    ''' Decompose a factor in its prime factors. This function uses the pyprimes module. THE FASTEST  '''
    return [i for i in factorise(nr)]

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

n = 2**1 * 3**1 * 5**1 * 7**1 * 11**1
print('calculate_divisors : \t',n ,calculate_divisors(n ))
n = 2**3 * 3**3 * 5**1   #* 7 * 11
print('calculate_divisors : \t',n  ,calculate_divisors(n ))
n = 2**3 * 3**3 * 5**1
print('calculate_divisors : \t',n ,calculate_divisors(n ))
n = 2**7 * 3**3 * 5**1
print('calculate_divisors : \t',n ,calculate_divisors(n ))
n = 2**7 * 3**3 * 5**1 * 7**1
print('calculate_divisors : \t',n ,calculate_divisors(n ))
n = 2**15 * 3**3 * 5**1 * 7**1
print('calculate_divisors : \t',n ,calculate_divisors(n ))
n = 2**15 * 3**3 * 5**1 * 7**3
print('calculate_divisors : \t',n ,calculate_divisors(n ))
n = 2**15 * 3**7 * 5**1 * 7**3
print('calculate_divisors : \t',n ,calculate_divisors(n ))
n = 2**15 * 3**3 * 5**3 * 7**3
print('calculate_divisors : \t',n ,calculate_divisors(n ))
n = 2**7 * 3**3 * 5**3 * 7**1 * 11**1 * 13**1
print('calculate_divisors : \t',n ,calculate_divisors(n ))
n = 2**7 * 3**3 * 5**1 * 7**1 * 11**1 * 13**1 * 17**1
print('calculate_divisors : \t',n ,calculate_divisors(n ))

n =  2**3 * 3*1 * 5**1
print('\ncalculate_divisors : \t', n ,'    ',calculate_divisors(n))

# @2017-03-15 - Now I need to adjust the powers to be 2**(16-1), or powers like : (4-1), 2-1, 8-1, ...

print('\n--------------------------TESTS------------------------------')
t1  = time.time()

# primes = sieve(10**3)
# print(len(primes), primes[:100] )
#
# Prim=[]
# divisors = 10
#
# for p in primes[:divisors+1] :
#     Prim.append( [ p,1 ] )
#
# Prim.pop()
#
# print('\nThe initial list : \t', Prim)
#
# for i in range(len(Prim)-2, -1, -1) :
#     # print ( Prim[i] )
#     n , k = Prim[i][0], Prim[i][1]
#     if n**(k+1) < Prim[-1][0]** Prim[-1][1] :
#         j, e = 1, 1
#         print('init :   ',n,j)
#         print( 'check' ,n, j+2**(e+1)-1, j+2**(e+1) )
#         A = Prim[:]
#         last_index = len(Prim)-1
#         while n**(2**e ) < Prim[last_index][0]** Prim[last_index][1] :
#             print('comparison : ',n**(2**e ) ,  Prim[last_index][0]** Prim[last_index][1]  )
#         # while n**(j ) < Prim[-1][0]** Prim[-1][1] :
#
#             j+=2**e
#             e+=1
#             print(e, j, n,      '    test : ', n**j, '     target :',Prim[-1][0]** Prim[-1][1] )
#             # if n**j < Prim[-1][0]** Prim[-1][1] :
#             Prim[i].pop(1)
#             Prim[i].append(j)
#             Prim.pop(last_index)
#             last_index -= 1
#
# print('\n Modified list : \t ',Prim)
#
# P =  functools.reduce(operator.mul,  [i[0]**i[1] for i in Prim ] )      #   %500500507
# P2 =  functools.reduce(operator.mul,  [i[0]**i[1] for i in Prim ] ) %5001
# P3 =  functools.reduce(operator.mul,  [( i[0]**i[1]) %5001 for i in Prim ] ) %5001
# print('\nAnswer : \t', P )
# print('Modulo test :', P2, P3)

# @2017-02-22, 11:00 --> Need to fix the above algorithm !!!


# print('\nRedundant check :', P, calculate_divisors(P),'\n' )



print('\n------------------ BRUTE FORCE CHECK ----------------------')
target = 2**10
for i in range(0, 10**9, 30030) :
    u = calculate_divisors(i)
    if u == target :
        print(i,'    <--' , factors(i) )
        break

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n================  My FIRST SOLUTION,  SLOW, 10 min ===============\n')
t1  = time.time()



def get_lowest_exp(Tracker, P, prime) :
    minp, key = 10**20, 0
    i =  0
    while P[i]**2 < prime :
        if  P[i]** (Tracker[P[i]]) < minp :
            minp = P[i]** (Tracker[P[i]])
            key = P[i]
        i+=1
    return minp, key


def first_solution_pb500( div_nr ) :
    P = sieve(10**7)
    print('Primes : ', len(P) ,P[:100] )
    divisors = 0
    Tracker = {}

    for p in P :
        e, nr = get_lowest_exp(Tracker, P, p)
        if e < p :
            # print('case 1   e < p    nr=', nr , '    e =  ', e , '          p= ', p)
            Tracker[nr]  = Tracker[nr]*2
            divisors +=1
            if divisors == div_nr : break
            e, nr = get_lowest_exp(Tracker, P, p )

        if e > p :
            # print('case 2    e > p  nr=', nr , '    e =  ', e , '          p= ', p)
            Tracker[p] = 2
            divisors +=1
            if divisors == div_nr : break
        if divisors%(10**4) == 0 : print(divisors,'     ', len(Tracker))

    print('\nTracker : \t', len(Tracker) )#, Tracker)
    DIV = [ (k, v-1) for k, v in sorted(Tracker.items())  ]
    print('\nDivisors list : \t',DIV[:10], DIV[-10::])
    res = functools.reduce( operator.mul,  [ pow( k, v-1, 500500507 ) for k,v in Tracker.items()  ] ) %500500507


    return print('\nAnswer : \t', res )

# divisors_pb500(500500)                              # Answer : 	 35407281
first_solution_pb500(100)                              # Answer : 	 35407281



t2  = time.time()
print('\nCompleted in :', round((t2-t1),6), 's\n\n')            #   Completed in : 580.514204 s

print('\n================  My SECOND SOLUTION, VERY FAST , < 1 sec  ===============\n')
t1  = time.time()


def pb500() :
    P = sieve(7400050)[:500500]
    print(len(P), P[-10::])
    i=0
    while P[i] < (7376507)**(1/2) :
        p = P[i]
        while P[i]*p < P[-1] :
            P[i] *= P[i] * p
            P.pop(-1)
            # print(P)
        i+=1
    print(P[:100])

    Prod = 1
    for j in P :
        Prod = (Prod *j) % 500500507

    return print('\nAnswer : \t ', Prod % 500500507 )

pb500()

t2  = time.time()
print('\nCompleted in :', round((t2-t1),6), 's\n\n')            #   Completed in : 580.514204 s


print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1,  INCREDIBLE FAST,  1 sec --------------------------')
t1  = time.time()

def primes(n):
    sieve = [True] * n
    for i in range(3, int(n**0.5)+1, 2):
        if sieve[i]:
            sieve[i*i::2*i] = [False] * int((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in range(3, n, 2) if sieve[i]]

data = primes(7370050)
plus = []
ans = 1
for i in data:
    while True:
        i **= 2
        if i > 7370050: break
        plus.append(i)

data += plus
for i in data:
    ans *= i
    ans %= 500500507
print(ans)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 2,  10 sec --------------------------')
t1  = time.time()

# === Fri, 7 Aug 2015, 21:07, Nicolas Patrois, France
# I first searched the number of divisors until 200 on my pocket calculator:
# Then I used OEIS and especially this sequence. Then:
# http://oeis.org/A005179

def solution_2():
    from math import sqrt

    def prod(lis,m):
      p=1
      for i in lis:
        p*=i
        p%=m
      return p

    nb=500500*20
    crible=[True]*nb
    crible[0:2]=False,False

    n=2

    while n<=sqrt(nb):
      for i in range(2*n,nb,n):
        crible[i]=False
      n+=1
      while not crible[n]:
        n+=1

    premiers=[]

    for i in range(2,nb):
      if crible[i]:
        premiers.append(i)

    del crible

    liste=[]
    for p in premiers:
      e=0
      while True:
        n=p**(2**e)
        liste.append(n)
        e+=1
        if n>nb:
          break
    liste.sort()
    liste=liste[:500500]

    return print('\nSolution : \t',prod(liste,500500507))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

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
