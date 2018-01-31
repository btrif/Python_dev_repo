#  Created by Bogdan Trif on 20-11-2017 , 11:24 AM.
# © o(^_^)o  Solved by Bogdan Trif  @
#The  Euler Project  https://projecteuler.net
'''
                 Prime Mountain Range            -           Problem 569

A mountain range consists of a line of mountains with slopes of exactly 45°,
and heights governed by the prime numbers, pn.
The up-slope of the kth mountain is of height p_2k−1,
and the downslope is p_2k. The first few foot-hills of this range are illustrated below.

p569-prime-mountain-range.gif

Tenzing sets out to climb each one in turn, starting from the lowest.
At the top of each peak, he looks back and counts how many of the previous peaks he can see.

In the example above, the eye-line from the third mountain is drawn in red,
showing that he can only see the peak of the second mountain from this viewpoint.
Similarly, from the 9th mountain, he can see three peaks, those of the 5th, 7th and 8th mountain.

Let P(k) be the number of peaks that are visible looking back from the kth mountain.
Hence           P(3)=1   and   P(9)=3.

Also ∑{k=1, 100 } P(k)=227

Find ∑{ k=1, 2500000 } P(k)        .

'''
import time, zzz
from math import sin, cos, acos, asin, sqrt, pi



def prime_sieve(n):       # FOURTH      o(^_^)o
    sieve = [True] * n
    for i in range(3, int(n**0.5)+1, 2):
        if sieve[i]:
            sieve[ i*i :: 2*i ] = [False] * ( (n-i*i-1) // (2*i) +1 )
    return [2] + [i for i in range(3, n , 2) if sieve[i] ]


# y − y1 = m(x − x1)      # line equation , Line Equation




print('\n--------------------------TESTS------------------------------')
t1  = time.time()

lim = 10**4
primes = prime_sieve(lim)
print(primes)
# print( ' cos 45 : ',  2*cos(45*pi/180) ,  ' sin 45 : ',  2*sin(45*pi/180)    )



def Y(x1, y1, x0, y0 ,x ):
    '''    :Description: line equation (Line Equation) . Takes two points and forms the equation of a line.
        then it takes an x value and computes y (the heigth ) using the initial function

    :return: y(x)                                   '''

    m = ( (y1-y0)/(x1-x0) )

    def y( m, x0, y0, x ):
        return m*( x - x0 ) + y0

    return  y( m, x0, y0, x )


print(' Y line equation test :  ', Y(28, 8, 2, 2, 10 ) )

pos = (5, -1)
V = [ (2, 2) ]
A = [ (0,0), (2,2) ]
x0, y0 = 2, 2

cnt = 0
i=2
while i < 2 * 10 :
    p1, p2 = primes[i], primes[i+1]
    varf = (pos[0]+ p1, pos[1]+ p1   )
    vale = (varf[0]+p2 , varf[1]-p2 ,   )
    pos = vale

    V.append(varf)
    A.append(varf) ; A.append(vale)

    # print(   ( varf[1] - V[0][1] ) ,  ( varf[0] - V[0][0] )      )
    x1, y1 =    varf[0],  varf[1]                      # y = m * (y-y0) / ( x-x0)
    print(' V : ',V[-1] , V )
    print('SEEN = ', end='  ')
    for j in range( len(V)-2 , -1, -1  ) :
        height = Y( x1, y1, x0, y0 , V[j][0] )
        if  height < V[j][1] :
            cnt +=1
            print( V[j], ' h=', height , end ='  ;     ' )
    print()
    print(str(i//2+1)+ '.     p1= ', p1, '      p2= ', p2,  '     varf= ', varf ,  '     vale= ', vale , '     cnt=', cnt  )
    print(V)


    i+=2

print(V)
print('\nA : ',A)

print('\nAnswer : ', cnt)

# @2017-11-20             Mdaaa, trebuie sa trag linie la toate, Nu ajunge numai la una singura !!

t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')

print('\n================  My FIRST SOLUTION,   ===============\n')
# t1  = time.time()





# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')


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

