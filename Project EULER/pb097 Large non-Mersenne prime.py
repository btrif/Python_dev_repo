#!/usr/bin/python
# Solved by Bogdan Trif @   Completed on Wed, 19 Oct 2016, 22:34
#The  Euler Project  https://projecteuler.net
'''
                            Large non-Mersenne prime        -       Problem 97
The first known prime found to exceed one million digits was discovered in 1999, and is a Mersenne prime
of the form 2**6972593−1;
it contains exactly 2,098,960 digits.
Subsequently other Mersenne primes,
of the form 2**p−1, have been found which contain more digits.

However, in 2004 there was found a massive non-Mersenne prime which contains 2,357,207 digits: 28433 × (2**7830457) +1.
Find the last ten digits of this prime number.
'''
# Answer :  27580.8739992577
import time

print('-----------------------MY SOLUTION , Very very Weak --------------------------------')
t1  = time.time()


print('7830457 % 62500     :',7830457 % 62500)
print('7830457 % 312500     :',7830457 % 312500)
print('7830457 % 1562500     :',7830457 % 1562500,'\n')


# IMPORTANT  ! : I need 12500 powers difference for the last 6 digits of the number

for i in range(1,20000):              #1152512   ; 12 --> 20   512 --> 100 , 2512 -->  500 , 52512 --> 2500 , 152512 --> 12500 , 1152512  --> 62500
      #print(i, 2**i ,str(2**i)[-2::] )
      #if str(2**i)[-7::] == '1152512' :
    if  i % 17957 == 0 :
         print(i,'     last digits :         ' ,str(2**i)[-10::]  )
         print( (int(str(2**i)[-10::]))* 28433+1  )
         last_ten = str(((int(str(2**i)[-10::]))* 28433+1))[-10::]

print('\n Last Ten Digits : ', last_ten)

t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')

print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1 , No Comment  rtoscani, Netherlands--------------------------')

print ((28433 * 2**7830457 + 1) % 10**10)

print('\n--------------------------SOLUTION 2 , INSTANT  lalalison, USA--------------------------')
t1  = time.time()

print((28433*pow(2, 7830457, 10**10) +1) % 10**10)

t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')
print('\n--------------------------SOLUTION 3 ,   mbh038, England--------------------------')

#About 40 ms in Python.

# I find the binary of b: 7830457=11101110111101110111001 = 2**22+2**21+....+2**3 + 2**0 = 7830457
# then, starting with 1, I successively multiply by 2 raised to each of these powers of 2 and take mod 10**10
# of the result each time. In this way I only need go through a loop as many times as there are ones in the binary of b.

def P97(a=28433,b=7830457,M=10):
        """returns a*2^b + 1 mod M"""
        M=10**M
        x=1
        binb=[int(x) for x in bin(b)[2:][::-1]]
        binb=[2**i for i in range(len(binb)) if binb[i]==1]
        for i in binb:
            x=(x*2**i)%M
        print((a*x+1)%M)

P97()

# <hits head on desk!>  I didn't think to just try  print((28433*2**7830457+1)%10**10)

print('\n--------------------------SOLUTION 4 ,   markus.obi, Germany--------------------------')

#Don't forget to add padding zeros if using modulo. In this case the first digit is not 0 - but you never know.

digits = 10
prime = 28433 * 2**(7830457) + 1
print(str(prime % 10**digits).zfill(digits))