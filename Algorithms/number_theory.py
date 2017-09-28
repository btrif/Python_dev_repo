
def egcd(a, b):         #Extended Euclidian Algorithm
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def extendedEuclid(a, b):
    if b == 0:
        return a, 1, 0
    k, q = a // b, a % b # a = kb + q
    g, xp, yp = extendedEuclid(b, a % b)
    # g = xp * b + yp * q
    #   = xp * b + yp * (a - kb)
    #   = (xp - k*yp) * b * yp * a
    return g, yp, xp - k * yp


def modinv(a, m):       # Modular Inverse
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

print('modinv Modular Inverse :\t', modinv(7, 31))
print('modinv Modular Inverse :\t', modinv(17, 43))

######################################


def Euler_totient(n):   # o(^_^)o  @2017-01-23, 10:30 by Bogdan Trif
    ''':Works without errors !
        https://en.wikipedia.org/w/index.php?title=Euler%27s_totient_function&action=edit&section=3
    :param n: int
    :return: int, Euler Phi, Euler Totient
    '''
    def get_factors(n):       ### o(^_^)o  FASTEST  o(^_^)o  ###
        ''' Decompose a factor in its prime factors. This function uses the pyprimes module. THE FASTEST  '''
        from pyprimes import factorise
        return [val for sublist in [[i[0]]*i[1] for i in factorise(n)] for val in sublist]
    F = set(get_factors(n))
    for i in F :
        n*=(1-1/i)
    return round(n)

N = 100001051
print('\nEuler_totient function : \t N=',N ,'\t' ,Euler_totient(N))


import math
import sys

class ChineseRemainderTheorem():
    """
    Solve
        x = a (mod m)
        x = b (mod n)
    where m and n are coprime.
    """
    def solve(self, a, m, b, n):
        q = m*n
        (x, y) = self._extended_gcd(m, n)
        root = a + (b - a) * x * m
        return ((root % q) + q) % q

    def _extended_gcd(self, a, b):
        (x, y) = (0, 1)
        (last_x, last_y) = (1, 0)
        while b != 0:
            (q, r) = divmod(a, b);
            (a, b) = (b, r)
            (x, last_x) = (last_x - q * x, x)
            (y, last_y) = (last_y - q * y, y)
        return (last_x, last_y)

class ModInverse():
    """
    Solve ax = 1 (mod m).
    """
    def get(self, a, m):
        g, x, y = self._extended_gcd(a, m)
        if g != 1:
            raise Exception('modular inverse does not exist')
        else:
            return x % m

    def _extended_gcd(self, a, b):
        if a == 0:
            return (b, 0, 1)
        else:
            g, y, x = self._extended_gcd(b % a, a)
            return (g, x - (b // a) * y, y)