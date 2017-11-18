#  Created by Bogdan Trif on 27-09-2017 , 7:26 PM.
# © o(^_^)o  Solved by Bogdan Trif  @
#The  Euler Project  https://projecteuler.net
'''

Numbers for which Euler’s totient function equals 13!       -       Problem 248


The first number n for which φ(n)=13!       is      6227180929.

Find the 150,000th such number.


'''
import operator, random
import time, zzz
# from gmpy2 import fac, is_prime
import functools, itertools, operator
# from pyprimes import factorise

# def get_factors(n):       ### o(^_^)o  FASTEST  o(^_^)o  ###
#     ''' Decompose a factor in its prime factors. This function uses the pyprimes module. THE FASTEST  '''
#     return [val for sublist in [[i[0]]*i[1] for i in factorise(n)] for val in sublist]

def _prod(L):
    s = 1
    for i in  L:
        s*= i
    return s

def _power_dict( D) :
    s = 1
    for k,v in D.items():
        s*= k**v
    # for k in D.items():
    #     s*= k[0]**k[1]
    return s


class PrimeTable():    #  ( ͡° ͜ʖ ͡°)  ### !! FIRST FASTEST
    def __init__(self, bound):
        self.bound = bound
        self.primes = []
        self._sieve()

    def _sieve(self):       # FOURTH      o(^_^)o
        sieve = [True] * self.bound
        for i in range(3, int(self.bound**0.5)+1, 2):
            if sieve[i]:
                sieve[ i*i :: 2*i ] = [False] * ( (self.bound-i*i-1) // (2*i) +1 )
        self.primes = [2] + [i for i in range(3, self.bound , 2) if sieve[i] ]
        # print('Prime count:', len(self.primes) ,'           ATTENTION , LARGEST PRIME Included = ', self.primes[-1] ,'       !!!!!!!!!!!! ' )

class Factorization():

    ''' Based on a prebuilt prime sieve, and we must pay attention that the prime up range is not
    to low, so that we don't miss a prime when we first factor . As default the value is set to 10.000
      So we need uprange /2         '''
    def __init__(self, bound):
        self.prime_table = PrimeTable(bound)

    def get_factors(self, n):
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
        return f


    def get_divisors(self, n) :
        f = self.get_factors(n)
        unpacking = [[p**e for e in range(f[p] + 1)] for p in f]
        return sorted([self._product(divisor) for divisor in itertools.product(*unpacking)])


    def _product(self, list):
        result = 1
        for number in list:
            result *= number
        return result


def Miller_Rabin(p, k = 50):  # Miller-Rabin primality test
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



F = Factorization(10**5)
zap = F.get_factors(2*3*4*5*6*7*8)
print( zap,  [ k**v for k,v in  zap.items()  ] , _prod([ k**v for k,v in  zap.items()  ]) )

def euler_totient( dict_list_int ):           # Remark : For large array better use Sieve approach
    """ **©** Made by Bogdan Trif @ 2017-02-08 .
    returns Euler totient (phi) of n = Φ (n)
        Uses the formula of the Totient  : Φ (n) =  Π {p | n}  n *(1 - 1/p) ;
        where p are each prime factors and n is the number  for which we compute
        In number theory, Euler's totient function counts the positive integers up to a given integer n
        that are relatively prime to n. It is written using the Greek letter phi as φ(n) or ϕ(n),
        and may also be called Euler's phi function.
        Example : Φ (12) = 4 =   [1,5,7,11]
        https://en.wikipedia.org/wiki/Euler's_totient_function
        http://marcharper.codes/2015-08-07/totients.html
        :D: is a dictionary of the form {p1:k1, p2:k2...}. E.g : for 90 = {2:2, 3:2, 5:1 }
        or it is a list of the form 180 = [2, 2, 3, 3, 5 ]
        or it is an INT number
        """
    if type(dict_list_int) == dict :
        pfs = [ i for i in dict_list_int ]
        phi = 1
        for a in  [ i**j for i,j in dict_list_int.items() ] :
            phi *= a
    if type(dict_list_int) == list :
        pfs = set(dict_list_int)
        phi = 1
        for a in dict_list_int :
            phi *= a


    if type(dict_list_int) == int :     # Variant with Factorization class
        pfs = [ i for i in F.get_factors(dict_list_int) ]
        phi = 1
        for a in  [ i**j for i,j in F.get_factors(dict_list_int).items()  ] :
            phi *= a

    # if type(dict_list_int) == int :     # Variant with pyprimes module class
    #     pfs = [ i[0] for i in factorise(dict_list_int)]
    #     phi = dict_list_int

    for pf in pfs:
        phi *= (1-1/pf)
    return int(phi)


print('euler_totient : \t', euler_totient(600))


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
# https://math.stackexchange.com/questions/1507449/number-theory-find-all-solutions-of-phin-16-and-phin-24
# https://math.stackexchange.com/questions/101566/using-eulers-totient-function-how-do-i-find-all-values-n-such-that-phin-12
# https://math.stackexchange.com/questions/366415/find-all-the-natural-numbers-where-%CF%95n-110-eulers-totient-function
# https://artofproblemsolving.com/community/c3t265f3h1332651s1_totient_equals_2016
# https://faculty.math.illinois.edu/~ford/wwwpapers/sierp.pdf

# ==========
# Q : For how many values of $n$ does $\phi(n)=2016 ?
#
# A1 :    First, we find all primes, $p$, such that $p-1|2016$.
#     These are ${2,3,5,7,13,17,19,29,37,43,73,97,113,127,337,673,1009,2017}$
#     You can use 2 up to 5 times; 3 up to 3 times; 7 up to 2 times; and all others up to 1 time.
#
# A2 :    You need to find the solutions to
# $$2016 = p_1^{a-1}(p_1-1)p_2^{b-1}(p_2-1)\cdots p_m^{x-1}(p_m-1)$$Where $n=p_1^ap_2^b \cdots p_m^x$
#
# The power matters too. Note that $2^4 \cdot 3^2 \cdot 7^2$ works, but $2^3 \cdot 5 \cdot 7^2 \cdot 43$ does not.


print('\n--------------------------TESTS------------------------------')
t1  = time.time()

def brute_force( tot ) :
    max_len = 0
    F = Factorization(10**5)
    ALL = set()
    cnt = 0
    for n in range( int(39916800*5.50) , 39916800*6   ) :
        t = euler_totient(n)
        if t == tot :
            cnt+=1
            ALL.add(n)
            f = F.get_factors(n)
            # f = get_factors(n)
            if len(f) > max_len : max_len = len(f)
            print(str(cnt)+'.       n=' , n, '         t=', t , '     n=', f,'      len = ', len(f) ,'      ', max_len ,'      n/t =  ', n/t )
    print('\nALL =',ALL)
    print('\nnumbers = ', cnt)
    return ALL


# BF = brute_force( 2*3*4*5*6*7*8*9*10*11 )
# BF = brute_force( 2016 )

##### FACTORIALS ratios of largest numbers for which tot = k! and totient !!
# k! = 13 ! = > n=                                n/t = 6

##### FACTORIALS ratios of largest numbers for which tot = k! and totient !!
# k! = 13 ! = > n=                                n/t = 6       IS FEASABLE

# k! = 11  =>  n= 219669450          t= 39916800      n/t =   5.50318287037037          n= {19: 1, 2: 1, 3: 1, 5: 2, 7: 2, 11: 2, 13: 1}       len =  7        7
# k! = 10  =>  n= 19969950          t= 3628800         n/t =   5.50318287037037		    n= [2, 3, 3, 3, 5, 7, 7, 11, 13]       len =  9        9
# k! = 9  =>       n= 1891890        t= 362880          n/t =   5.213541666666667
# k! = 8  =>       n= 210210        t= 40320            n/t =   5.213541666666667	        n= [2, 3, 5, 7, 7, 11, 13]       len =  7        10
# k! = 7  =>      n= 22050          t= 5040              n/t =   4.375
# k! = 6  =>      n=  3150          t= 720                  n/ t = 4.375
# k! = 5  =>      n= 462            t= 120                    n/t =   3.85
# k! = 4  =>       n= 90             t= 24                    n/t =   3.75
# k! = 3  =>       n= 18            t= 6                      n/t =   3.0       n= [2, 3, 3]       len =  3        3




print()
t2  = time.time()
print('\n# Completed in :', round((t2-t1) , 2), 's\n\n')


print('\n============  My SECOND SOLUTION,  SLOW & Non-ELEGANT ,  90 minutes  ===============\n')
t1  = time.time()

# comb of 6, max prime = 1171
# comb of 5, max prime = 24571
# comb of 4, max prime = 982801
# comb of 3, max prime = 13899601
# comb of 2, max prime = 389188801
# comb of 1, max prime = 389188801


def second() :
    tot = 2*3*4*5*6*7*8*9*10*11*12*13           # 6227020800
    # tot = 2*3*4*5*6*7*8
    # tot = 5040
    Fa  = Factorization(10**5)
    F = Fa.get_factors(tot )
    print('Number = ',tot, '\nF = ', F )             #   [k for k in F.keys()] , [v for v in F.values()]
    Div = Fa.get_divisors(tot)
    print(len(Div), Div)
    P = [ i+1 for i in Div if Miller_Rabin(i+1) ]
    print(len(P), P , P[len(P)//2 -1: len(P)//2 +1  ] )

    max_tot_prime = max( [i for i in F ] )
    P2 = P[ P.index(max_tot_prime)+1 : ]
    print(max_tot_prime, '    ',  P2, ' \n' )

    # print(P.index(1171) , len(P[:P.index(1171) +1 ]), P[:P.index(1171) +1 ] )

    T = set()
    cnt = 0
    K =  [ k for k in F.keys()]           #       the keys of the totient factorization , the primes
    for comb1 in itertools.product(*map(range, [ v+2 for v in F.values() ] )   ) :
        cnt +=1
        if sum(comb1) <= 19 :
            d1 = { K[v]: comb1[v] for v in range(len(comb1))  if comb1[v] > 0  }
            print('\n---------------- ' +str(cnt) ,comb1 , '       ' ,  d1 ,'    ', [i for i in d1.keys() ] , [i for i in d1.values() ]  , '-----------------\n'  )

            # CASE 1  Small primes like  [2, 2, 3, 3, 5, 7, 7]
            tot_d1 = euler_totient(d1)
            n1 = _power_dict(d1)
            if tot_d1 == tot :
                cnt +=1
                T.add(n1)

                print(str(cnt) +  '.             n1=  ', n1 ,'           d1 =  ', d1 ,'      tot_d1 = ', tot_d1)


            ### CASE 2 Only combinations of large primes like  [7, 13, 71]
            for i2 in range(len(P2)) :
                comb2 = [ P2[i2] ]
                n = _prod(comb2)
                if n1*n> tot*6 : break

                d = { j:1 for j in comb2 }

                if  tot == euler_totient(d) :
                    T.add(n)
                    print(comb2 , '          n = ', n , '            d =' ,d ,'             ' ,euler_totient(d) )

                d2 = dict(  list( d1.items() ) + list(d.items() )  )
                n2 = _power_dict(d2)
                if  tot == euler_totient(d2) :
                    T.add(n2)
                    print( comb2 , '          n2 = ', n2 , '            d2 =' , d2 ,'             ' ,euler_totient(d2) )


                for i3 in range(i2+1, len(P2)) :
                    comb3 = [ P2[i2], P2[i3]  ]
                    n = _prod(comb3)
                    if n1*n> tot*6 : break

                    d = { j:1 for j in comb3 }

                    if  tot == euler_totient(d) :
                        T.add(n)
                        print(comb3 , '          n = ', n , '            d =' ,d ,'             ',  euler_totient(d ) )

                    d3 = dict(  list( d1.items() ) + list(d.items() )  )
                    n3 = _power_dict(d3)
                    if  tot == euler_totient(d3) :
                        T.add(n3)
                        print( comb3 , '          n3 = ', n3 , '            d3 =' , d3 ,'             ' , euler_totient(d3) )


                    for i4 in range(i3+1, len(P2)) :
                        comb4 = [ P2[i2], P2[i3] , P2[i4]  ]
                        n = _prod(comb4)
                        if n1*n> tot*6 : break

                        d = { j:1 for j in comb4 }

                        if  tot == euler_totient(d) :
                            T.add(n)
                            print(comb4 , '          n = ', n , '            d =' ,d ,'             ' , euler_totient(d) )

                        d4 = dict(  list( d1.items() ) + list(d.items() )  )
                        n4 = _power_dict(d4)
                        if  tot == euler_totient(d4) :
                            T.add(n4)
                            print( comb4 , '          n4 = ', n4 , '            d4 =' , d4 ,'             ' , euler_totient(d4))


                        for i5 in range(i4+1, len(P2)) :
                            comb5 = [ P2[i2], P2[i3] , P2[i4] , P2[i5]  ]
                            n = _prod(comb5)
                            if n1*n> tot*6 : break
                            d = { j:1 for j in comb5 }

                            if  tot == euler_totient(d) :
                                T.add(n)
                                print(comb5 , '          n = ', n , '            d =' ,d ,'             ' , euler_totient(d)  )

                            d5 = dict(  list( d1.items() ) + list(d.items() )  )
                            n5 = _power_dict(d5)
                            if  tot == euler_totient(d5) :
                                T.add(n5)
                                print( comb5 , '          n5 = ', n5 , '            d5 =' , d5 ,'             ', euler_totient(d5) )


                            for i6 in range(i5+1, len(P2)) :
                                comb6 = [ P2[i2], P2[i3] , P2[i4] , P2[i5] , P2[i6]  ]
                                n = _prod(comb6)
                                if n1*n> tot*6 : break

                                d = { j:1 for j in comb6 }

                                if  tot == euler_totient(d) :
                                    T.add(n)
                                    print(comb6 , '          n = ', n , '            d =' ,d ,'             '  , euler_totient(d) )

                                d6 = dict(  list( d1.items() ) + list(d.items() )  )
                                n6 = _power_dict(d6)
                                if  tot == euler_totient(d6) :
                                    T.add(n6)
                                    print( comb6 , '          n6 = ', n6 , '            d6 =' , d6 ,'             ' , euler_totient(d6)  )


                                for i7 in range(i6+1, len(P2)) :
                                    comb7 = [ P2[i2], P2[i3] , P2[i4] , P2[i5] , P2[i6], P2[i7]  ]
                                    n = _prod(comb7)

                                    if n1*n> tot*6 : break

                                    d = { j:1 for j in comb7 }

                                    if  tot == euler_totient(d) :
                                        T.add(n)
                                        print(comb7 , '          n = ', n , '            d =' ,d ,'             '   , euler_totient(d)  )

                                    d7 = dict(  list( d1.items() ) + list(d.items() )  )
                                    n7 = _power_dict(d7)
                                    if  tot == euler_totient(d7) :
                                        T.add(n7)
                                        print( comb7 , '          n7 = ', n7 , '            d7 =' , d7 ,'             '    , euler_totient(d7) )


    print('\nNrs with totients : \t',len(T) )
    S = sorted(T)

    k_th = 150000

    print('Last element = ', S[-1],'       n/t =  ', S[-1]/tot )

    print('\nAnswer :  ', k_th , '-th  element  = ' , S[ k_th-1 ])
    return S[ k_th-1 ]

# second()        #       Answer :   150000 -th  element  =  23507044290                   Completed in : 5185.58  s
# Nrs with totients : 	 182752
# Last element =  37020293310        n/t =   5.94510513117284







t2  = time.time()
print('\n# Completed in :', round((t2-t1) , 2), ' s\n\n')


#
# print('\n================  My FIRST SOLUTION,   ===============\n')
# t1  = time.time()
#
# def solution1(tot) :
#     Z = pair_Factors(2*3*4*5*6*7)
#     print('\nlen(Z) = ',len(Z))
#     print(Z[:1000],'\n')
#     CNT= set()
#     for I in Z :
#         tmp = []
#         nr = functools.reduce(operator.mul, I  )
#         # print(I,'         ' , nr )
#         Primes, NonPrimes = set(), []
#         for x in I :
#             if is_prime(x+1) :  Primes.add(x+1)
#             else :   NonPrimes.append(x)
#         Primes = sorted(Primes)
#         print('\n  -------   I = ' , I , '         Primes= ', Primes , '              NonPrimes  = ', NonPrimes, ' ----')
#
#         if len(Primes) >= 2 :
#             y1 = functools.reduce(operator.mul , Primes)
#
#             ### CASE 1    -
#             if len(NonPrimes) == 0 :
#                 n = y1
#                 # print('case 1  ' , str(len(CNT))+'.    ',I , '       n = ', n , '        Prms=', sorted(Primes) ,'       NonP= ', NonPrimes)
#
#
#
#             ### CASE 2
#             if len(NonPrimes) > 0 :
#                 Fct = set()
#                 for c in NonPrimes :
#                     d = set(get_factors(c))
#                     Fct = Fct.union(d)
#                     # print(' Fct = ', Fct ,'         ', Fct.difference(Primes) )
#                 if len(Fct.difference(Primes)) == 0:
#                     y2 = functools.reduce(operator.mul , NonPrimes )
#                     n = y1*y2
#
#                         # CNT.add(n)
#                     # print('case 2  ' , str(len(CNT))+'.    ',I , '       n = ', n , '        Prms=', sorted(Primes) ,'       NonP= ', NonPrimes)
#
#             #### CASE 3 is when we have  I =  [1, 2, 2, 6, 210] but we need only
#             if n < tot :
#                 c = I.count(2)
#                 z = n * 2**c
#                 if z > tot :
#                     CNT.add( z )
#                     # print('case 3  ',str(len(CNT))+'.    ',I , '    count(2)= '   , I.count(2),'.    ' , '       n = ', n , '      '   , z  )
#
#             ### CASE 4 - strange case when  n = 12700 = [ 2, 2, 5, 5, 127],
#             # I = [2, 4, 5, 126], Primes=  [3, 5, 127] , NonPrimes  =  [5]
#             # if len(NonPrimes) >0 :  three = functools.reduce(operator.mul, NonPrimes  )
#             # else :three = 1
#             if len(NonPrimes) == 0 :
#                 if 3 in Primes  and ( 3 not in NonPrimes ) : # we must eliminate the 3, because this comes from a 2
#                     w = functools.reduce(operator.mul , list(Primes)+NonPrimes   ) *4 //3
#                     if euler_totient(w) == 5040 :
#                         print('CASE 4       I = ', I ,    '       n = ', n ,  '       w=  '   , w , '      ',get_factors(w) )
#                     if w > tot : CNT.add(w)
#
#
#             if n > tot :
#                 CNT.add(n)
#                 CNT.add(2*n)
#
#                 # print( str(len(CNT))+'.    ',I , '       n = ', n , '        Primes=', sorted(Primes) ,'       NonPrimes= ', NonPrimes)
#
#     print('\nTotal count = ', len(CNT) )
#     print(CNT)
#
#     print('\nBF.difference(CNT )length difference : ', len(BF.difference(CNT)))
#     print( BF.difference(CNT))
#
#     print('\nCNT.difference(BF )length difference : ', len(CNT.difference(BF)))
#     print( CNT.difference(BF))
#
#
# # @2017-10-15 - I must investigate the 3-rd case : n = 17724, 11956,  16764, etc...
# # solution1(  fac(7)  )
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')


print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1,  147 sec --------------------------')
t1  = time.time()

# === Wed, 14 Jan 2015, 09:43, ChopinPlover, Taiwan
# Reference: http://arxiv.org/pdf/math/0404116.pdf
#
# This problem is quite easy after I solved ProjectEuler #342.  Thanks to ProjectEuler team :)
#
# Runtime:
# real	1m44.366s
# user	1m44.158s
# sys	0m0.147s

import itertools
import sys

class PrimeTable():
    def __init__(self, bound):
        self.primes = self.__init_primes(bound)

    def __init_primes(self, bound):
        primes = []
        visited = [False] * (bound + 1)
        visited[0] = visited[1] = True
        for i in range(2, bound + 1):
            if not visited[i]:
                primes.append(i)
            for j in range(i + i, bound + 1, i):
                visited[j] = True
        print("Prime count:", len(primes))
        return primes

    def is_prime(self, n):
        for p in self.primes:
            if p**2 > n:
                return True
            if n % p == 0:
                return False
        assert(False)

class Factorization():
    def __init__(self, bound):
        self.prime_table = PrimeTable(13)

    def get(self, n):
        result = {}
        d = n
        for p in self.prime_table.primes:
            if p**2 > d:
                break
            if d % p == 0:
                e = 0
                while d % p == 0:
                    e += 1
                    d = d // p
                result[p] = e
        if d > 1:
            result[d] = 1
        return result

    def get_all_divisors(self, factorization):
        unpacking = [[p**e for e in range(factorization[p] + 1)] for p in factorization]
        return sorted([self.__product(divisor) for divisor in itertools.product(*unpacking)])

    def __product(self, list):
        result = 1
        for number in list:
            result *= number
        return result

class Problem():
    def __init__(self):
        self.factorization = Factorization(13)
        self.prime_table = PrimeTable(80000)

    def solve(self):
        n_factorization = self.__get_factorial(13)
        solution = []
        dfs_stack = [[(p, a, n_factorization)] for p, a in self.__invert_prime(n_factorization, 1)]
        while dfs_stack:
            top = dfs_stack[-1]
            dfs_stack.pop(-1)
            p, a, f = top[-1]
            next_factorization = self.__remove_phi_factor(f, p, a)
            if not next_factorization:
                x = self.__get_number(top)
                solution.append(x)
                if len(solution) % 1000 == 1:
                    print(len(solution), "=>", x)
            for next_p, next_a in self.__invert_prime(next_factorization, p):
                next_state = top + [(next_p, next_a, next_factorization)]
                dfs_stack.append(next_state)
        sorted_solution = sorted(solution)
        print("stat =>", sorted_solution[0], sorted_solution[-1], len(sorted_solution))
        print("answer =>", sorted_solution[150000 - 1])

    def __invert_prime(self, n_factorization, min_prime):
        pairs = []
        n_divisors = self.factorization.get_all_divisors(n_factorization)
        for divisor in n_divisors:
            p = divisor + 1
            if p <= min_prime:
                continue
            if not self.prime_table.is_prime(p):
                continue
            max_a = n_factorization[p] if p in n_factorization else 0
            for a in range(max_a + 1):
                pairs.append((p, a))
        return pairs

    def __get_factorial(self, n):
        result = {}
        for i in range(2, n + 1):
            i_factorization = self.factorization.get(i)
            print(i, i_factorization)
            for p in i_factorization:
                if p not in result:
                    result[p] = 0
                result[p] += i_factorization[p]
        return result

    def __remove_phi_factor(self, some_factorization, p, a):
        result = dict(some_factorization)
        if p in result:
            assert(result[p] >= a)
            result[p] -= a
        else:
            assert(a == 0)

        y = self.factorization.get(p - 1)
        for q in y:
            assert(q in result)
            assert(result[q] >= y[q])
            result[q] -= y[q]

        normalized_result = {}
        for p in result:
            if result[p] != 0:
                normalized_result[p] = result[p]
        return normalized_result

    def __get_number(self, some_state):
        result = 1
        for p, a, f in some_state:
            result *= p**(a + 1)
        return result

def main1():
    problem = Problem()
    problem.solve()

main1()                 #    Completed in : 147960.46 ms

t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')


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




