#!/usr/bin/python                   o(^_^)o         ( ͡° ͜ʖ ͡°)
# © Solved by Bogdan Trif @
#The  Euler Project  https://projecteuler.net
'''
Rounded Square Roots        -       Problem 255

We define the rounded-square-root of a positive integer n as the square root of n rounded to the nearest integer.

The following procedure (essentially Heron's method adapted to integer arithmetic) finds the rounded-square-root of n:

Let d be the number of digits of the number n.
If d is odd, set x_0 = 2×10**(d-1)⁄2.
If d is even, set x_0 = 7×10**(d-2)⁄2.
Repeat:

x_(k+1) = floor( ( x_k + ceil( n/x_k ))  /2 )

until x_(k+1) = x_k.

As an example, let us find the rounded-square-root of n = 4321.
n has 4 digits, so x0 = 7×10(4-2)⁄2 = 70.

x_1 = floor( ( 70 + ceil( 4321/70 )) /2  ) =66
x_2  = floor( ( 66 + ceil( 4321/66 ))  /2 ) =66

Since x2 = x1, we stop here.
So, after just two iterations, we have found that the rounded-square-root of 4321 is 66 (the actual square root is 65.7343137…).

The number of iterations required when using this method is surprisingly low.
For example, we can find the rounded-square-root of a 5-digit integer (10,000 ≤ n ≤ 99,999)
with an average of 3.2102888889 iterations (the average value was rounded to 10 decimal places).

Using the procedure described above, what is the average number of iterations required to find
the rounded-square-root of a 14-digit number (10**13 ≤ n < 10**14)?

Give your answer rounded to 10 decimal places.

Note: The symbols ⌊x⌋ and ⌈x⌉ represent the floor function and ceiling function respectively.

'''
import time
from math import ceil, floor, sqrt



def Heron_integer_arithmetic(n):
    d = len(str(n))
    if d%2 == 1 :
        x = 2*10**( (d-1)/2 )
    if d%2 ==0 :
        x = 7*10**((d-2)/2 )
    i1, i2 = x, -16
    cnt=0
    while i1 != i2 :
        cnt+=1
        i1 = x
        x = floor( ( x+ceil((n/x )) )/2 )
        i2 = x
        # print('i1, i2 = ', i1, i2, '        x=',x)

    return x, cnt

print('\nHeron_integer_arithmetic : \t', Heron_integer_arithmetic(4321))


print('\n--------------------------TESTS------------------------------')
t1  = time.time()

# down, up = 10**13+8*10**11+7*10**10+6*10**9+8*10**8+8*10**7+6*10**6+4*10**5 , 10**14
down, up = 10**4 , 10**5
L = up - down
S=0
cnt = 0
for n in range(down, up) :
    cnt+=1
    a = Heron_integer_arithmetic(n)
    S+=a[1]
    print(str(n)+'.    ' , a, '        ' ,  sqrt(n) , '        ' ,  S/cnt )

print('\nAnswer : \t', round(S/L, 10 ) , '                ',  S/L )

# OBS : 2017-02-21 --> Must Do Reverse Engineering on that function
# There are values of 6,5,4
        ####  Boundary
    # 46440.     (215, 3)          215.49941995281566
    # 46441.     (216, 2)          215.5017401321855

# We can see the boundary between < 15.5 and >15.5

# It seems that there are 2 types of changes : 1. based on boundaries as above

# 2. Anomalies which I must investigate !!! as :
#             47400.     (218, 2)          217.7154105707724
#             47401.     (218, 3)          217.71770713472068
#
#             46600.     (216, 2)          215.87033144922904
#         46601.     (216, 3)          215.87264764207623
# 45800.     (214, 2)          214.00934559032697          2.938632999078238
# 45801.     (214, 3)          214.0116819241417          2.938634713144517
# 45399.     (213, 2)          213.0704108974308          2.9441242937853107
# 45400.     (213, 2)          213.07275752662517          2.944097624360894

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
# print('\n--------------------------SOLUTION 2,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
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
