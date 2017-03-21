#!/usr/bin/python                   ( ͡° ͜ʖ ͡°)
# Solved by Bogdan Trif @       Completed on Sun, 26 Feb 2017, 22:50
#The  Euler Project  https://projecteuler.net
'''
An Arithmetic Geometric sequence        -       Problem 235

Given is the arithmetic-geometric sequence u(k) = (900-3k)r**k-1.

            Let s(n) = Σ {k=1...n} u(k).

Find the value of r for which s(5000) = -600,000,000,000.

Give your answer rounded to 12 places behind the decimal point.


'''
import time

# from decimal import *
# getcontext().prec = 20
import gmpy2




# def u1(k, r):
#     return Decimal((900-3*k) * r**(k-1))

# u = lambda k, r : (900-3*k) * r**(k-1)
u = lambda k, r : (900-3*k) * r**(k-1)

print('test u : ',u(2 , 2/33),'\n')

def s( r ):
    S=0
    for i in range(1, 5001):
        # S += Decimal(u1(i , Decimal(r)))
        # S += u(i , Decimal(r))
        S += u(i , r )
    return S






# 1001.   1.001         s = 	  -1647175481.404537
# 1002.   1.002         s = 	  -137389011510.7948

# 1320.   1.0023203189999998         s = 	  -595079742096.9348
# 1321.   1.0023213199999998         s = 	  -597826775555.0255
# 1322.   1.0023223209999998         s = 	  -600586575026.495
# 424.   1.0023221086328761852968227685778401792049407958984375         s = 	  -600000000000.1172755139854

print('\n--------------------------TESTS------------------------------')
t1  = time.time()

target =  -6*10**11


Scale = 10**18
cnt = 0
# R = gmpy2.mpq (1.002322108631888 ) #5962
R = gmpy2.mpq (1002322108632.88/(10**12)  )
# R = gmpy2.mpq (1002322108631.888/(10**12)  )
print(len(str(R)), str(R),'\n' )
for i in range( int(R* Scale), 2* Scale, 1) :
    cnt+=1
    # r =  Decimal (i   / Scale )
    r =   (i   / Scale )
    # S = Decimal (s(r) )
    S = s(r)
    print( str(cnt)+'.   r=',  r ,'        s = \t ', S    )
    if S < target :
        print( '\nAnswer : \t' ,round(r, 12))
        break




t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n================  My FIRST SOLUTION, ELEGANT  ===============\n')
t1  = time.time()

def binary_search() :       # Elegant solution Using binary Search  !!!!

    u = lambda k, r : (900-3*k) * r**(k-1)
    up= 5000
    target = -6*10**11
    r = 1
    d = 0.1
    Sn = 0
    while abs(Sn - target) > 1 :
        Sn = sum( [ u(k, r) for k in range(1, up+1 )  ] )
        if Sn > target :
            r += d
        if Sn < target :
            r -= d
            d /= 2

        print(Sn, '           r = ', r, '          diff = ', abs(Sn - target), '     ', round(r,12) )
    return print('\nAnswer : \t', round(r,12))

binary_search()


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1,   --------------------------')
t1  = time.time()

# ====Sat, 19 Nov 2016, 23:38, mbh038, England
# About 60 ms in Python, in 33 iterations using a bisection search starting with low and high bounds
# for r of 1.0 and 1.1 respectively. 36 iterations are required if the initial bounds for r are 1.0<r<1.2,
# and 40 iterations and 67 ms if I start with bounds 0<r<1.5.
# In truth, I first found the answer manually by the same means.

import time
def pe235(n=5000,target=-600000000000,low=0,high=1.5):
    t=time.clock()
    epsilon=1e-12
    ans=(low+high)/2.
    val=s(ans,n)
    lastans=high
    while abs(lastans-ans)>epsilon:
        lastans=ans
        if val>target:
            low=ans
        else:
            high=ans
        ans=(high+low)/2.0
        val=s(ans,n)
    print (round(ans,12),time.clock()-t)

def s(r,n):
    s=0
    for k in range(1,n+1):
        s+=(900-3*k)*r**(k-1)
    return s

pe235()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 2,   --------------------------')
t1  = time.time()

# Thu, 23 Oct 2014, 12:15, grauerwolf, Germany
# simple bisection in python 3



def u(k,r):
    return (900-3*k)*r**(k-1);

def s(n,r):
    return sum(u(k,r) for k in range(1,n+1));

if __name__ == '__main__':
    target = -600000000000
    epsilon = 1e-15
    r_lower = 1.0
    r_upper = 1.05
    s_lower = s(5000,r_lower)-target
    s_upper = s(5000,r_upper)-target
    while (r_upper-r_lower > epsilon):
        r_between = (r_lower+r_upper)/2
        s_between = s(5000,r_between)-target
        if (s_between*s_lower > 0):
            r_lower = r_between
            s_lower = s_between
        else:
            r_upper = r_between
            s_upper = s_between
    print(round(r_between,12))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 3,   --------------------------')
t1  = time.time()

# ==== Sat, 3 Jan 2015, 11:41, eidanch, Israel
# Newton's method made this pretty easy...


def u(k,r):
    return (900-3*k)*pow(r,k-1)

def s(n,r):
    return sum(u(k,r) for k in range(1,n+1))

def du_dr(k,r):
    return (900-3*k)*(k-1)*pow(r,k-2)

def ds_dr(n,r):
    return sum(du_dr(k,r) for k in range(1,n+1))

def newton_raphson(y,dy,x0,N):
    x = x0
    for i in range(N):
        x = x - y(x)/dy(x)
    return x

def e235(n=5000, y0=-600000000000):
    y = lambda x: s(n,x) - y0
    dy = lambda x: ds_dr(n,x)
    x0 = 1.001
    return newton_raphson(y,dy,x0,N=500)

if __name__ == '__main__':
    r = e235()
    print ("%.12lf" % r, s(5000,r))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 4,   --------------------------')
t1  = time.time()

# ==== Tue, 16 Jun 2015, 02:52, mmaximus, Portugal
# python decimal module. 100 digits accuracy. bisector method. No prisoners taken.
# Only real work I did was to find a closed form expression for the sum.

import decimal
from decimal import Decimal

decimal.getcontext().prec = 100

def s(n,r):
    return 900*(1-r**n)/(1-r) - 3*(r**n*(n*r-n-1)+1)/((1-r)**2)

def p(r):
    return s(5000,r)+6*10**11

left = Decimal(1002322)/Decimal(1000000)
right = Decimal(1002325)/Decimal(1000000)
error_tolerance = Decimal(1)/Decimal(10000000000000)
zero = Decimal(0)

while True:
    new_guess = Decimal((left+right)/2)
    P = p(new_guess)
    print(new_guess)
    if abs(P) < error_tolerance:
        break

    elif P < zero:
        right = new_guess

    else:
        left = new_guess

print(round(new_guess,12))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

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
