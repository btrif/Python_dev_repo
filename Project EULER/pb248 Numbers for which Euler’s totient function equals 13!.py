#  Created by Bogdan Trif on 27-09-2017 , 7:26 PM.
# © o(^_^)o  Solved by Bogdan Trif  @
#The  Euler Project  https://projecteuler.net
'''
Numbers for which Euler’s totient function equals 13!       -       Problem 248


The first number n for which φ(n)=13! is 6227180929.

Find the 150,000th such number.


'''
import operator
import time, zzz
from gmpy2 import fac, is_prime

import functools
from pyprimes import factorise

def get_factors(n):       ### o(^_^)o  FASTEST  o(^_^)o  ###
    ''' Decompose a factor in its prime factors. This function uses the pyprimes module. THE FASTEST  '''
    return [val for sublist in [[i[0]]*i[1] for i in factorise(n)] for val in sublist]

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

    phi = n
    pfs = list(factorise(n))
    for pf in pfs:
        phi*=(1-1/pf[0])
    return int(phi)

print('euler_totient : \t', euler_totient(600))
print('euler_totient : \t', euler_totient(90))

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



# @2017-09-27 --> Take smaller cases !!

print('\n--------------------------TESTS------------------------------')
t1  = time.time()

def brute_force( tot ) :
    ALL = set()
    cnt = 0
    for n in range(1, 10**5) :
        t = euler_totient(n)
        if t == tot :
            cnt+=1
            ALL.add(n)
            print(str(cnt)+'.      n=' , n, '      t=', t , '     n=', get_factors(n) )
    print('\nALL =',ALL)
    print('\nnumbers = ', cnt)
    return ALL

BF = brute_force( 2*3*4*5*6*7 )



print()
t2  = time.time()
print('\n# Completed in :', round((t2-t1) , 2), 's\n\n')

print('\n================  My FIRST SOLUTION,   ===============\n')
t1  = time.time()

tot = 5040
Z = pair_Factors(2*3*4*5*6*7)
print('\nlen(Z) = ',len(Z))
print(Z[:1000])
CNT= set()
for I in Z :
    tmp = []
    nr = functools.reduce(operator.mul, I  )
    # print(I,'         ' , nr )
    Prms, NonP = set(), []
    for x in I :
        if is_prime(x+1) :  Prms.add(x+1)
        else :   NonP.append(x)
    print('I = ' , I , '      Prms= ', Prms , '            NonP  = ', NonP)

    if len(Prms) >= 2 :
        y1 = functools.reduce(operator.mul , Prms)

        # CASE 1
        if len(NonP) == 0 :
            n = y1


        # CASE 2
        if len(NonP) > 0 :
            Fct = set()
            for c in NonP :
                d = set(get_factors(c))
                Fct = Fct.union(d)
            if len(Fct.difference(Prms)) == 0:
                y2 = functools.reduce(operator.mul , NonP )
                n = y1*y2
                # if n > 5040 :
                #     CNT.add(n)
                #     print('case 2  ' , str(len(CNT))+'.    ',I , '       n = ', n , '        Prms=', sorted(Prms) ,'       NonP= ', NonP)

        if n > tot :
            CNT.add(n)
            CNT.add(2*n)
            print( str(len(CNT))+'.    ',I , '       n = ', n , '        Prms=', sorted(Prms) ,'       NonP= ', NonP)

print('\nTotal count = ', len(CNT) )
print(CNT)

print('\nBF.difference(CNT )length difference : ', len(BF.difference(CNT)))
print( BF.difference(CNT))

print('\nCNT.difference(BF )length difference : ', len(CNT.difference(BF)))
print( CNT.difference(BF))

# @2017-10-15 - I must investigate the 3-rd case : n = 17724, 11956,  16764, etc...


t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')


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




