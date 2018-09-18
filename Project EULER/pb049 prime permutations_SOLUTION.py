#!/usr/bin/python
# Solved by Bogdan Trif @ 15 Sep 16 (10:30)
#The  Euler Project  https://projecteuler.net
'''
                                        Prime permutations          -           Problem 49

The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways:
(i) each of the three terms are prime, and,
(ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property,
but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
'''
import itertools
import time
###################    START FUNCTIONS #########################
def unique_digit(X):
    #print(str(set(X)))
    if len(X) == len(set(X)):
        return True
        #print (X)
    else: return False #continue #print ('NOT unique !')

def detect_prime(n):
    i = n
    while(i <= n):
        j = 2
        while(j <= (i/j)):
            if not(i%j):
                return False
                break
            j = j + 1
        if (j > i/j) : return True
        i = i + 1


def string_to_list(strng):
   if (type(strng) == str):
      lst = list(strng)
      #print(lst)
      #print('The type of   ',lst, 'is :  ',type(lst))
      return lst
   #else: print('Not a string type !')

def list_to_string(lst):
   if ( type(lst) == list ):
      strng = ''.join(lst)
      #print(strng)
      #print('Type of  ',strng,' is:  ',type(strng))
      return strng
   #else: print('Not a list (array) type !')

def unique_digit_prime(n):          # Function built using two functions: detect_prime and unique_digit
    if (detect_prime(n) is True and unique_digit(str(n)) == True) :
        return True
    else:
        return False

def check_permutation(A , B):
   if ( type(A), type(B) == int ) :
      A, B = str(A), str(B)
      if ( type(A), type(B) == str ) :
         if ( sorted(A) == sorted(B) ) :
            #print(A,' is a permutation of ', B)
            return True
         else:
            #print(A,' is NOT a permutation of ', B)
            return False
      else: print('Not a string type !')

###################    END FUNCTIONS #########################
# Lists Deffinitions:
t1  = time.time()

print('----'*10,'  INITIAL PRIMES NUMBERS LIST ','----'*10)

ten_thousand_primes=[]
counter=1
i = 1000          #Set the starting Prime, First Prime in the list, 1000

while(i <= 9999):         # Set the last Prime Number Up, 9999
    j = 2
    while(j <= (i/j)):
        if not(i % j): break        # IF  it's TRUE it stops, if NOT TRUE it continues
        j = j + 1                       #Returns False and continues if is i%j = 0 ; Returns TRUE and stops if i%j = 1,2,....
    if (j > i/j) :
        ten_thousand_primes.append(i)
    i = i + 1


print ('Prime numbers between 1000 and 9999 are : ',ten_thousand_primes)
print ("First element of the array is: ", ten_thousand_primes[0], "    &     Last element of the array is: ", ten_thousand_primes[-1])
print ("There are   : ", len(ten_thousand_primes),'  prime numbers')

#prime_list = [ i for i in ten_thousand_primes  if i >1000]

print('----'*10,'  TESTS   ','----'*10)

print('test unique digit for 1026 :  ',unique_digit(str(1026)))
print('test unique digit for 1031 :  ',unique_digit(str(1031)) == True)

#for i in unique_digit_list:
  #  counter += 1
    #if counter < 5:
      #  print(i, type(i))

#k,a=1879,5487
#print(check_permutation(k,a) == True); print('\n'*2)

print('\n','---'*20,'  THE REQUESTED NUMBERS ','----'*10)

for k in ten_thousand_primes:
    #for L in [c for c in range(100,5000,2)]:                  #  with 100 lower limit:  Completed in :  47187.69884 ms
    for L in [3330]:                # If you supose that you know the difference number to be = 3330 , then it is Completed in : 127.007 ms
        a = k+L         # L is the difference between first prime and the 2nd prime
        if ( (detect_prime(a) == True) and (check_permutation(k,a) == True) and ( 1000 < a < 10000 )):
            #print(k, a)             # a is the new prime, the 2nd prime
            b = a + L
            if ( (detect_prime(b) == True) and (check_permutation(k,b) == True) and ( 1000 < b < 10000 )):
                print(k, a, b)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,2), 'ms')               #My solution was Completed in : 47013.80 ms

#print([c for c in range(100,500,2)])

print('\n','-----'*24,'\n')

##################################################

print('='*25 , 'OTHER SOLUTIONS FROM THE FORUM :','='*25)

t1  = time.time()

from sympy import sieve
li = list(sieve.primerange(1000,10000)) # List of 4 digit primes.

info = []
for i in range(len(li)):
    for j in range(i):
        info.append([li[i],li[j],li[i] - li[j]])
# List of lists containing [big prime, small prime, difference between the two]
# for all combinations of primes. This is kind of lazy, and takes 1.024 seconds.

filtered_info = [subset for subset in info if sorted(str(subset[0])) == sorted(str(subset[1]))]
# Filter out the sublists where both primes are permutations of each other.
# Takes 2.554 seconds because the list contains 562'330 sublists.
# Sorted is marginally faster than
# if all(str(subset[0]).count(char) == str(subset[1]).count(char) for char in str(subset[0]))
# which I used first, and took 2.934 seconds.

for i in range(len(filtered_info)):
    for j in range(i):
        if filtered_info[i][2] == filtered_info[j][2]:
# Find pairs of sublists where the difference between the primes are the same.
            if filtered_info[i][1] == filtered_info[j][0]:
# The small prime of the first sublist must equal the big prime of the second.
                print(filtered_info[i], filtered_info[j])
# Output:
# [8147, 4817, 3330] [4817, 1487, 3330]
# [9629, 6299, 3330] [6299, 2969, 3330]
# Takes 4.535 seconds total.

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,2), 'ms')

print('\n','-----'*25,'\n')



t1  = time.time()

print('nothing here ... ')

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,2), 'ms')
