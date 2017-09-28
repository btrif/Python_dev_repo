
### Modular multiplicative inverse function in Python

def egcd(a, b):
    '''     Extended Euclidian Algorithm    '''
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    '''Modular multiplicative inverse function   '''
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

print(modinv(11, 15))



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
print('eulerphi function  : \t N=', N, '\t', eulerphi(N))

