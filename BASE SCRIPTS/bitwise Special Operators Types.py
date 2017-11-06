print("\nx & y  Does a 'bitwise and'. Each bit of the output is 1 if the corresponding bit of x AND of y is 1, otherwise it's 0.")
for a in range(10):
    for b in range(10):
        print('a=',a , ', b=',b,' ;    a & b=', a & b)

print('\n-----------Python Bitwise Operators Examples ---------------------\n')
a = 60            # 60 = 0011 1100
b = 13            # 13 = 0000 1101
c = 0

print('----------------------- AND  &    ----------------------------------')
# Line 1 - Value of c is  12    Bitwise  AND   &  ================
a = 60             # 60 = 0011 1100
b = 13             # 13 = 0000 1101
c = a & b         # 12 = 0000 1100      # Returns 0 if  one of them is 0, returns 1 is both of them are 1
print ("AND - Value of c is ", c)

print('-----------------------  OR  |    ----------------------------------')
# Line 2 - Value of c is  61    Bitwise    OR  |    =================
a = 60            # 60 = 0011 1100
b = 13            # 13 = 0000 1101
c = a | b         # 61 = 0011 1101       # Returns 1 if  one of them is 1, returns 0 is both of them are 0, IT IS opposite of '&' !
print("\nOR - Value of c is ", c)

print('----------------------- XOR ^   ----------------------------------')
# Exclusive or or exclusive disjunction is a logical operation that
# outputs true only when inputs differ (one is true, the other is false).

print('XOR  truth  table')
print('Input    |	  Output  ')
print('-'*22)
print('A	 | B    |' )
print('0	 | 0	 |     0')
print('0	 | 1	 |     1')
print('1	 | 0	 |     1')
print('1	 | 1	 |     0')


# Line 3 - Value of c is  49        XOR
c = a ^ b        # 49 = 0011 0001      # Returns 1 if only one of them is 1, retuns 0 whenever both of them are either 0, either 1
print("XOR - Value of c is ", c)

# Line 4 - Value of c is  -61       NOT
c = ~a           # -61 = 1100 0011     # Returns the opposite bit of the number. 1111 will become 0000 ;  1010 becomes 0101
print("NOT - Value of c is ", c)


print('\n-------- Shifts the bits -  Useful to make divisions or multiplications by powers of 2 -------------')
#Line 5 - Value of c is  240        SHIFT         Shifts the bits
#### !!!!!! Useful to make divisionas or multiplications by powers of 2
a = 60            # 60 = 0011 1100
b = 13            # 13 = 0000 1101
c = 0

c = a << 2;       # 240 = 1111 0000         # Shifts the bits to the left with 2 units. E.g.: 0011 becomes 1100
print("SHIFT  - Value of c is ", c)
c = a << 1;       # 120 = 0111 1000
print("SHIFT  - Value of c is ", c)
c = a << 3;       # 480 = 1111 1000 0
print("SHIFT  - Value of c is ", c)

#Line 6 - Value of c is  15
c = a >> 2;       # 15 = 0000 1111             # Shifts the bits to the right with 2 units. E.g.: 0100 becomes 0001
print("SHIFT  - Value of c is ", c)

                    #  AND | 0 1     OR | 0 1     XOR | 0 1    NOT | 0 1
                    #  ----+-----    ---+----     - ---+----    ----+----
                    #   0  | 0 0         0 | 0 1        0 | 0 1        | 1 0
                    #  1  | 0 1         1 | 1 1        1 | 1 0

print('\n-----------------')
print('255 = ',bin(0xff),'    261 = ', bin(261), '   5 = ', bin(5))
print('261 & 0xFF      -->   ', 261 & 0xFF)
print('261 | 0xFF      -->   ', 261 | 0xFF)
print('261 ^ 0xFF      -->   ', 261 ^ 0xFF)


print('\n---------------Further Examples ---------------------')
print('\nHere we just raise to power...starting from 2**0 =1 just by shifting the bit 1 to the left :')
x=1
for i in range(16):  print( x<<i , end='  ')
print('\nWe can divide/multiply any number by 2 using SHIFT (only if integer) :')
y = 3
for i in range(10): print( y<<i , end='  ')
print()



print('\n---------------- Bin BINARY,  oct OctoDecimal, dec DECIMAL, hexa, HEXADECIMAL CONVERSIONS -------------')

print('Convert from Decimal to Binary :  ', bin(155))
print('Convert from Binary to Decimal :  ', int(0b10011011))

print('Convert from Decimal to Octadecimal :  ', oct(755))
print('Convert from Octadecimal to Decimal :  ', int(0o1363))

print('Convert from Decimal to Hexadeciamal :  ', hex(755))
print('Convert from Hexadeciamal to Decimal :  ', int(0x2f3))



print('\n=============================')

# Converting an Integer to a String in Any Base

def toStr(n,base):
   convertString = "0123456789ABCDEF"
   if n < base:
      return convertString[n]
   else:
      return toStr(n//base,base) + convertString[n%base]

print(toStr(1453,16))
print(toStr(123,6))



print('\n----------------- BENCHMARK TEST between normal multiplication and BITWISE multiplication -----------')
# import time
# t1=time.time()
# y = 3
# for i in range(1,1000):
#     # a =  y<<i
#     print(y<<i,  end='  ')
# print('\nCompleted in :', round((time.time()-t1)*1000,6), 'ms\n\n')
#
# t1=time.time()
# w=3
# for k in range(1,1000) :
#     w*=2
#     print( w  ,  end='  ')
#
# print('\nCompleted in :', round((time.time()-t1)*1000,6), 'ms\n\n')
#########################################

# One of the most common uses of bitwise operations is for parsing hexadecimal colours.
# For example, here's a Python function that accepts a String like #FF09BE and returns a tuple of its Red, Green and Blue values.
def hexToRgb(value):
    # Convert string to hexadecimal number (base 16)
    num = (int(value.lstrip("#"), 16))

    # Shift 16 bits to the right, and then binary AND to obtain 8 bits representing red
    r = ((num >> 16) & 0xFF)

    # Shift 8 bits to the right, and then binary AND to obtain 8 bits representing green
    g = ((num >> 8) & 0xFF)

    # Simply binary AND to obtain 8 bits representing blue
    b = (num & 0xFF)
    return (r, g, b)

print('\nTest for the hexToRgb Function : ', hexToRgb('#FF09BE'))



print('\n ------------------ Concept of Mask ---------------- ')

# Remark - Mask are built using the bitwise operator OR '|' which is :
#            a=  1000   =  8
#            b=  0001   = 1
# c = a | b = 1001   = 9

print(' c= ', 8 | 1  , '  binary version of c = ' , bin( 8 | 1 )  )

mask = 0

print('\nthis shifts the 1 to left and add four zeros ( 16)  --->  ', (1 << 4))
mask |= 1 << 8      #  which means that if we have powers of 2 , no bits will be the same so practically we add bits together :
# e.g. : 0001 | 1000 = 1001    then 1001 |  0100 = 1101 ... and so on.
print('| is the bit-wise operator and we with mask |= 1 << 8 we binary add  100000000=256     '  , mask)

mask |= 1 << 0          # here the 1 is not shifted => therefore the mask will be OR bitwised (binary added ) with 1
print( 'operation :  mask |= 1 << 0  : ' ,mask )
mask |= 1 << 1          # here the 1 is shifted with 1 = 2 = 10 in binary => mask will be binary added with 10 ( 2 decimal)
print( 'operation :  mask |= 1 << 1  : ' , mask)