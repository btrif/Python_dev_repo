#  Created by Bogdan Trif on 16-10-2017 , 11:57 AM.
# © o(^_^)o  Solved by Bogdan Trif  @
#The  Euler Project  https://projecteuler.net
'''
                    Steady Squares          -           Problem 284

The 3-digit number 376 in the decimal numbering system is an example of numbers with the special property
that its square ends with the same digits: 376^2 = 141.376.
Let's call a number with this property a steady square.

Steady squares can also be observed in other numbering systems. In the base 14 numbering system,
the 3-digit number c37 is also a steady square: c37^2 = aa0c37,
and the sum of its digits is c+3+7 = 18 in the same numbering system.

The letters a, b, c and d are used for the 10, 11, 12 and 13 digits respectively,
in a manner similar to the hexadecimal numbering system.

For 1 ≤ n ≤ 9, the sum of the digits of all the n-digit steady squares in the base 14 numbering system is 2d8 (582 decimal).
Steady squares with leading 0's are not allowed.

Find the sum of the digits of all the n-digit steady squares in the base 14 numbering system for
1 ≤ n ≤ 10000 (decimal) and give your answer in the base 14 system using lower case letters where necessary.


'''
import time, zzz
import sys
sys.setrecursionlimit(10000000)

def toStr(n, base ):
   '''Very elegant. Works Fine. Has problems for huge numbers > 500 digits. Because of the
   sys.getrecursionlimit() . I tried o increase it to sys.setrecursionlimit(10000000) and
   when dealing with 2000 digit numbers fails again .

   :param n:
   :param base:
   :return:
   '''
   convertString = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefg"
   # print(len(convertString))
   if n < base:
      return convertString[n]
   else:
      return toStr(n//base,base) + convertString[n%base]

for i in range(1, 43) :
    print(toStr(i, 14 ), end='  ')

print('\n', int('c37', 14) )

print('Convert in base 14 : ' ,toStr(5764801, 14) )


def baseconvert(n, base):
    """convert positive decimal integer n to equivalent in another base (2-36)"""

    digits = "0123456789abcdefghijklmnopqrstuvwxyz"

    try:
        n = int(n)
        base = int(base)
    except:
        return ""

    if n <= 0 or base <= 2 or base >= 36:
        return ""

    s = ""
    while 1:
        r = n % base
        s = digits[r] + s
        n = n // base
        if n == 0:
            break

    return s


print('\n--------------------------TESTS------------------------------')
t1  = time.time()


for i in range(1, 10**5) :
    ii = i*i
    f = toStr(i, 14)
    fs = toStr(ii, 14)
    if f == fs[-len(f)::] :
        print( i , '     dec sq = ', ii,'          f_14  =  ', f  , '        f_sqare_14= ', fs )


t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')

print('\n================  My FIRST SOLUTION,   ===============\n')
t1  = time.time()

Super = '178'
s1 = '7'
s2 = '8'

# lim = 9
lim = 1000
stop = 1
while 1 :
    for i in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd' ] :
        # print( i + s1)
        u1, u2 = i + s1,  i + s2      # Build new number in base 14
        d1, d2 = int( u1 , 14) , int( u2 , 14)       # Transform to decimal
        d1_sq, d2_sq  = d1*d1 , d2*d2         # Square the decimal
        u1_sq, u2_sq  = baseconvert(d1_sq, 14), baseconvert(d2_sq, 14)      # Convert square decimal to base 14

        if u1 == u1_sq[-len(u1)::] :
            s1 = i + s1
            print(str(len(s1))+  '.       dec : ', str(d1)[-10::], '   ;        ',str(d1_sq)[-10::] ,'           base_14 :  ', u1[-200::] , '       ', s1[-200::])
            if not s1.startswith('0') and len(s1) <= lim :
                Super += s1


        if u2 == u2_sq[-len(u2)::] :
            s2 = i + s2
            print(str(len(s2))+  '.       dec : ', str(d2)[-10::], '   ;       ',str(d2_sq)[-10::] ,'           base_14 :  ', u2[-200::] , '       ', s2[-200::] )
            if not s2.startswith('0') and len(s2) <= lim :
                Super += s2


        if len(u1) > lim and len(u2) > lim  :
            stop = lim
            break
    if stop == lim : break

print('\nSuperString : ', Super[:1000])

Sum = 0
for i in Super :
    a = int( i , 14)
    Sum += a

print('Sum in dec = ', Sum )
print('\nResult = ' ,  baseconvert(Sum, 14)  )

# something with mod 14


t2  = time.time()
print('\n# Completed in :', round((t2-t1) , 2), 's\n\n')


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




