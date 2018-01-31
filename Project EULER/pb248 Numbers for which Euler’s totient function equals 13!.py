#  Created by Bogdan Trif on 27-09-2017 , 7:26 PM.
# © o(^_^)o  Solved by Bogdan Trif  @   Completed on Sat, 18 Nov 2017, 15:51
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
from pyprimes import factorise

def get_factors(n):       ### o(^_^)o  FASTEST  o(^_^)o  ###
    ''' Decompose a factor in its prime factors. This function uses the pyprimes module. THE FASTEST  '''
    return [val for sublist in [[i[0]]*i[1] for i in factorise(n)] for val in sublist]
from functools import reduce


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


def prime_sieve(n):       # FOURTH      o(^_^)o
    sieve = [True] * n
    for i in range(3, int(n**0.5)+1, 2):
        if sieve[i]:
            sieve[ i*i :: 2*i ] = [False] * ( (n-i*i-1) // (2*i) +1 )
    return [2] + [i for i in range(3, n , 2) if sieve[i] ]


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


print('\n--------------------------SOLUTION 2, INVERSE PHI , invphi , 15 sec, INCREDIBLE --------------------------')
t1  = time.time()



from gmpy2 import is_prime

# ==== Sun, 7 Jun 2009, 22:28, gianchub, England
# Google was my friend on this one. It turned up this paper:
# www.new.dli.ernet.in/rawdataupload/upload/insa/INSA_2/20005a81_22.pdf...
# That paper is really interesting:
# Within my library:

def invphi(m):
    ''' Returns the sorted list of numbers n such that phi(n) = m '''
    # some special cases
    if m <= 0:
        return [0]
    elif m == 1:
        return [1, 2]
    elif m > 1 and m%2 != 0:
        return []

    # phi(p^d) with p prime
    def phipd(p, d):
        return (p-1) * (p**(d-1))

    # returns a decreasing ordered list of all primes p such that p-1 | n
    def primesFromDivisors(n):
        divs = set()
        factors, exps =  zip(* (factorise(n) )   )
        for i in itertools.product(*(range(x+1) for x in exps)):
            pp = reduce(lambda x, y : x*y, (factors[j] ** i[j] for j in range(len(i))), 1) + 1
            if is_prime(pp):
                divs.add(pp)
        return sorted(divs, reverse = True)

    # prepares a small table of phis (phi^(-1) sets, to aid the calculation)
    def smallTable(mmax):
        M = 2**62
        primes = prime_sieve(mmax)
        nnum, nden, nmax = 1, 1, 0
        for p in primes:
            nnum, nden = nnum * p, nden * (p-1)
            if nnum > mmax:
                nnum, nden = nnum // p, nden // (p-1)
                nmax = (mmax * nnum) // nden
                break
        tmphi = list(range(nmax + 1))
        sf = [M] * (nmax + 1)
        for pr in primes:
            for p in range(pr, nmax + 1, pr):
                tmphi[p] = (tmphi[p] * (pr - 1)) // pr
                if pr < sf[p]:
                    sf[p] = pr
        for n, m in enumerate(tmphi):
            if m > mmax:
                continue
            if not m in phis:
                phis[m] = []
            phis[m].append([n, sf[n]])
        phis[1][0][1] = M

    # does the calculation (recursively if needed)
    def calc(m, M):
        divs = primesFromDivisors(m)
        if not m in phis:
            phis[m] = []
        for p in divs:
            d = 1
            ppd = phipd(p, d)
            while ppd <= m:
                if m % ppd == 0:
                    x = m // ppd
                    if x == 1 or x % 2 == 0:
                        if not x in phis:
                            calc(x, M)
                        for v in phis[x]:
                            t = (p**d) * v[0]
                            if v[1] > p:
                                phis[m].append([t, p])
                                if m == M:
                                    res.add(t)
                d += 1
                ppd = phipd(p, d)

    # inner vars
    # results set
    res = set()
    # invphi table
    phis = {}
    # invphi table dimension
    mmax = int(m**0.5) + 100
    smallTable( min(mmax, 5000) )
    calc(m, m)
    # return sorted results list
    return sorted(res)


def main2() :
    from math import factorial
    res = invphi( factorial(13) )
    print(res[150000-1] )

main2()

t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')


print('\n--------------------------SOLUTION 3,  BEAUTIFUL, SUBLIME, Must learn it --------------------------')
t1  = time.time()

# ==== Wed, 24 Jun 2009, 01:13, albert, Netherlands
# I did this one in Python, not Forth. It runs in 7 seconds.
# Like some people I made a list of primes that are
# possible candidates. At first I treated the small
# primes that can occur to a power differently, but
# after some tinkering an elegant recursive procedure
# with mere three parameters results, that treats all
# primes uniformly.


# $Id: euler248.py,v 1.7 2009/06/22 19:43:18 albert Exp $
# Copyright (2008): Albert van der Horst {by GNU Public License

# Euler problem

# What is the 100.000 number where phi(n) = 13!.
# Euler totient function.

# Analysis:
# 13! = 2^10 . 3^5 . 5^2 . 7 . 11 . 13
# Each number N we divide in factors p^n that are either prime or
# a prime power. Then phi(N) is the product of (p-1).p^(n-1).
# If p is larger than 13, the power n is just one.
# If N' is  a remaining product of phi(N) , then either N'+1
# must be prime, or it must be divisible by some p <= sqrt(13!).
# Then phi(N) must be divisible by (p-1).
# Smaller factors must satisfy that p^(n-1) divides 13!

# It has been noted that there are not too many of those numbers.
# So we make a list, then order that list and find the 100.000 number.

from math import sqrt

def fac(n):
    result = 1
    for i in range(n):
        result *= i+1
    return result


TTF = fac(13)

MAX_SIEVE = 1 + int(sqrt(TTF+1))
primes = []

solutions = []

def is_prime( p ):
    if p<4 :
        if p<2:
            return 0
        return 1
    if p%2 == 0 : return 0
    s = int(sqrt(p+1))
    for i in range(3,s+1,2):
        if p%i == 0: return 0
    return 1

# Fill the primes with candidates for factors of n.
# Note that we want at least one entry that is larger
# than MAX_SIEVE
def fill():
    i = 2
    while 1:
        if is_prime(i) and ( TTF % (i-1) == 0) :
            primes.append(i)
            if i>MAX_SIEVE: break
        i +=1

# Now we proceed from the smallest entries in the table to the largest,
# until the part of 13! not taken into account no longer allows for
# two factors. At each point the remaining factor is inspected,
# it may be a prime minus one and is accepted, or it must be split further.
# The criterion to stop is rest < (phi)^2 where phi is the smallest
# prime power totient that can be expected still.

# Investigate the already found part of n and the remainder of phi(n)
# with respect to primes larger than the prime with index ip.
# Successes are added to the list solutions.
def investigate( remn, remphi, ip):
    # Is remphi in itself a new prime factor?
    if is_prime( 1+ remphi ) and (1+remphi) >= primes[ip]:
        solutions.append( remn*(1+remphi) )

    p = primes[ip]
    # Subtle: small primes can have power >2.
    # And phi is a product of (p-1)'s
    while p <= 13 or remphi > (primes[ip]-1)**2 :
        pow = p
        phi = p-1
        while remphi%phi == 0 :
            investigate( remn*pow, remphi/phi, ip+1)
            pow *= p
            phi *= p
        ip += 1
        p = primes[ip]

def doit():
    fill()
    investigate( 1, TTF, 0 )
    solutions.sort()
    print( "And the 100,000th n with phi(n) = 13! (euler248) is:")
    print( solutions[100000-1]) # Count from 0!

doit()

t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')


print('\n--------------------------SOLUTION 4,   --------------------------')
t1  = time.time()

# === Sat, 6 Jun 2009, 04:09, BjornEdstrom, Sweden
# Fun problem! This problem was a breeze for me because I already had code for the inversed phi function. It is slow, but generic.

F = Factorization(10**3)

def inverse_phi(N, a=1):
    saved = []

    if N < 1:
        raise ValueError

    if N == 1:
        if a > 1:
            return [1]
        return [1, 2]

    divisors = F.get_divisors(N)


    for div in divisors :
        if (div < a) or (not Miller_Rabin(div + 1)):
            continue
        N_ = N / div
        div += 1
        P = div

        while True:
            saved += map(lambda x: x*P, inverse_phi(N_, div))
            if N_ % div:
                break
            P *= div
            N_ /= div

    return saved

print(  inverse_phi(240) )


def euler248():
    ret = inverse_phi( 1*2*3*4*5*6*7*8*9*10*11*12*13 )
    ret = list(ret)
    ret.sort()
    return ret[150000-1]

print( euler248()  )


t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')


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




