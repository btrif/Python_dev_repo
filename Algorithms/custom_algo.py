#  Created by Bogdan Trif on 09-11-2019 , 10:57 AM.

# The formula is  ==> Perm(total_elem_nr) / [ Perm(elem_1) *Perm(elem_2) * ...* Perm(elem_n) ]
import gmpy2


def multiple_permutations(*args ) :
    ''' **©** Made by Bogdan Trif @ 2017-09-03, 12:15.
        Uses the formula Perm(total_elem_nr) / [ Perm(elem_1) *Perm(elem_2) * ...* Perm(elem_n) ]
    :param args:  the first arg is always the total number of elements, e.g. : for  the list [1, 1, 1, 1, 2, 2, 2 ,3, 3] = 9 elem ;
        The next elements will be in descending order the separate no of elem : 4 elem of '1' s , 3 elem of '2's , 2 elem of '3's
        will be called as follows : multiple_permutations(9, 4, 3, 2) = 1260
    :Explicit formula:      p = gmpy2.fac(9) // ( gmpy2.fac(4)*gmpy2.fac(3)*gmpy2.fac(2) )
    :return: int, Perm(total) / (Perm(elem_1) *Perm(elem_2) * ...* Perm(elem_n) )
    '''
    den = 1
    S=0          # the sum of all elements
    for i, j in enumerate(args) :
        # print(i,'    ', j,'     ' )
        if i == 0 :
            num = gmpy2.fac(j)
            N = j
        else :
            den *= gmpy2.fac(j)
            S += j
    # assert (N == S ) , "Total number of elements condition is not met !"
    if (N != S) :  raise ValueError ("Total number of elements condition is not met !")

    return (num // den)



# This will yield permutations of a total objects  = 9 , with 4 objects of A, 3 objects of B & 2 objects of C
print('multiple_permutations ( 9, 4, 3, 2 ) = ' , multiple_permutations( 9, 4, 3, 2 ) )
print('multiple_permutations ( 3, 1, 1, 1 ) = ' , multiple_permutations(3, 1, 1, 1 ) )

print('\n------------       Chinese Remainder Theorem   -----------------')

from functools import reduce

def chinese_remainder( N, A ):
    ''' :SOURCE: https://rosettacode.org/wiki/Chinese_remainder_theorem#Python_3.6
    :param N: all the modules : (n1, n2,..., nk)
    :param A:  all the arguments : (a1, a2, ..., ak)
    :return: the remainder of the product of modules n1*n2*...*nk

    :Example: we have that x = 2 (mod 7) x = 3 (mod 13).
     Here we have a1, a2 = 4, 9 and n1, n2 = 7, 13
    By applying Chine Remainder theorem we have that by applying both expressions we will get :
        the main relation :             **a1*m1*y1 + a2*m2*y2 ( mod M)**   where :
            1.    M=n1*n2 = 7*13 = 91
            2.    m_i = M/n_i => in our case : m1 = 91/7=13 and m2 = 91/13=7
            3.    m_i*y_i = 1 (mod n_i)  =>

    So we start to solve separately both equations and we find that :
        y1 = 6 (mod 7)  and y2 = 2 (mod 13),   replacing y1, y2 in the main relation =>
            and after simplifications :  x = 16 (mod 91). And this is our result
    '''

    sum = 0
    prod = reduce(lambda a, b: a*b, N)
    for n_i, a_i in zip(N, A):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

