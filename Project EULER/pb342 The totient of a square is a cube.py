#!/usr/bin/python                   o(^_^)o         ( ͡° ͜ʖ ͡°)
# © Solved by Bogdan Trif @
#The  Euler Project  https://projecteuler.net
'''
The totient of a square is a cube           -           Problem 342

Consider the number 50.
50**2 = 2500 = 2**2 × 5**4, so φ(2500) = 2 × 4 × 53 = 8 × 53 = 23 × 53. 1
So 2500 is a square and φ(2500) is a cube.

Find the sum of all numbers n, 1 &lt n < 1010 such that φ(n**2) is a cube.

1 φ denotes Euler's totient function.


'''
import time, zzz, gmpy2

def get_factors(n):       ### o(^_^)o  FASTEST  o(^_^)o  ###
    ''' Decompose a factor in its prime factors. This function uses the pyprimes module. THE FASTEST  '''
    from pyprimes import factorise
    return [val for sublist in [[i[0]]*i[1] for i in factorise(n)] for val in sublist]

def euler_totient(n):           # Remark : For large array better use Sieve approach
    """returns Euler totient (phi) of n = Φ (n)
        Uses the formula of the Totient  : Φ (n) =  Π {p | n}  n *(1 - 1/p) ;
        where p are each prime factors and n is the number  for which we compute
        In number theory, Euler's totient function counts the positive integers up to a given integer n
        that are relatively prime to n. It is written using the Greek letter phi as φ(n) or ϕ(n),
        and may also be called Euler's phi function.
        Example : Φ (12) = 4 =   [1,5,7,11]
        https://en.wikipedia.org/wiki/Euler's_totient_function
        http://marcharper.codes/2015-08-07/totients.html            """
    phi=n
    pfs=set(get_factors(n))
    for pf in pfs:
        phi*=(1-1/pf)
    return int(phi)

is_cube = lambda x: int (x**(1/3)+0.5)**3 == x

print('\n--------------------------TESTS------------------------------')
t1  = time.time()


def brute_force_test(up) :
    for n in range(1, up) :
        if gmpy2.is_prime(n) == False :
            to = euler_totient(n**2)
            if is_cube(to) :
                print(str(n)+'.       ', to,'     ',  int (to**(1/3)+0.5) ,'     ' ,get_factors(n), get_factors(to) )


brute_force_test(10**5)

@ 2017-03-24 - I only started it !

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n================  My FIRST SOLUTION,   ===============\n')
# t1  = time.time()







# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


# print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
# print('\n--------------------------SOLUTION 1,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 2,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 3,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 4,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
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
#
# print('\n--------------------------SOLUTION 7,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 8,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 9,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 10,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 11,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 12,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

