#!/usr/bin/python3
# Solved by Bogdan Trif @     Wed, 28 Sep 2016, 22:35
#The  Euler Project  https://projecteuler.net
'''
                Double-base palindromes     -       Problem 36

The decimal number, 585 = 1001001001 b2 (binary), is palindromic in both bases.
Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
(Please note that the palindromic number, in either base, may not include leading zeros.)
'''

fff='12345'
print(fff, fff[::-1])

def base_Conv( n, base ) :
   convertString = "0123456789ABCDEF"
   if n < base:
      return convertString[n]
   else:
      return base_Conv(n//base,base) + convertString[n%base]

print(base_Conv(585,2))
S=0
counter=1
for i in range(1,1000000):
    bnr = base_Conv(i,2)
    if ( bnr == bnr[::-1] and str(i) == str(i)[::-1]):
        S += i
        print(str(counter)+'.   ' ,i ,' ',bnr)
        counter +=1

print('\nAnd the total Sum is :', S)



