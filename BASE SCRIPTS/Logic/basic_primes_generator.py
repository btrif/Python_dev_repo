#!/usr/bin/python3
# comments.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    for n in primes():      #generate a list of prime numbers
        if n > 100: break
        print(n, end=' ')

def isprime(n):
    if n == 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
    else:
        return True

def primes(n=1):
   while(True):
       if isprime(n): yield n
       n += 1 

print(isprime(31) == True)

#############################################
# from MITx.6.00.1x Course
# A Different Version :

def genPrimes():
    primes = []   # primes generated so far
    last = 1      # last number tried
    while True:
        last += 1
        for p in primes:
            if last % p == 0:
                break
        else:
            primes.append(last)
            yield last


if __name__ == "__main__": main()
