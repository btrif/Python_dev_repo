#!/usr/bin/python3
# Solved by Bogdan Trif @ 2016-09-14 1:53 PM
#The  Euler Project  https://projecteuler.net
'''
                Smallest multiple   -   Problem 5       c.m.m.m.c.
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''
z=20            # The number you need to modify

nrs = [j for j in range(1,z+1)]
multiples=[]
primes=[]
N=1     # In the beginning, everything =1 :) !!!!!!!!

# Generate the prime numbers we need for our range
i=1
while(i < z):                 # Set the last Prime Number - the Upper Limit
    j = 2
    while(j <= (i/j)):              # This condition checks in the lower list
        if not(i%j): break          # IF  it's TRUE it stops, if FALSE it continues    # VERY IMPORTANT This line checks if the number is PRIME
        j = j + 1                       #Returns FALSE and continues if is i%j = 0 ; Returns TRUE and stops if i%j = 1,2,....
    if (j > i/j) : primes.append(i)                # If j > i/j means that the number is not already in the list, therefore must be another prime
    i = i + 1

print('Primes in this range are :', primes)

def common_factor(a,b):         # this functions finds the common factors of two numbers,
    temp_a=[]
    factors=[]
    for i in [1,2,3,5,7,11]:                # here if you already have a prime array (list) you can replace it, here is : primes
        if a % i == 0:                      # it will not suffice this small list of primes when working with large numbers, >
            temp_a.append(i)
            #print(temp_a)
    for j in temp_a:
        if b%j == 0:
            factors.append(j); #print(j)

    return factors


# Here the primes are multiplied:
for w in primes:
    N *=w
print('Multiplication of the primes in range : ',N)

for s in nrs:
    temp_m=[]
    print(N , ' & ',s,'  ; Mod =' , N%s, ' ;     common factors: ',common_factor(s, N%s))
    if N%s != 0:
        q = common_factor(s, N%s)[-1]
        N *= q
        multiples.append(q)

print('\nMultiplied factor  list:   ',multiples)

print('--------------- TESTS -----------------')
print('Common factors :  ')
print(common_factor(2,4))
print('Last common factor :',common_factor(24,36)[-1])

for i in common_factor(24,72):
    print(i, end=' ')

print('\n\nAnd the CMMMC (Smallest multiple) number is : ',N,'       !!!!!!!!')          #cmmmc,  c.m.m.m.c. -  Cel Mai Mic Multiplu Comun
