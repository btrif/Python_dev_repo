#!/usr/bin/python3
# Solved by Bogdan Trif @       Completed on Wed, 28 Sep 2016, 10:14
#The  Euler Project  https://projecteuler.net
'''
                                            Truncatable primes      -       Problem 37

The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right,
and remain prime at each stage: 3797, 797, 97, and 7.
Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
'''

import time
t1  = time.time()

def detect_prime(n):                # Function which checks i a number is prime
    '''  Function which checks if a number is prime
    '''
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

Pri=[]
Hunted=[]
i = 20                             #Set the starting Prime, First Prime in the list, MAIN VARIABLE
END = 1000000                               #Set the END Prime, First Prime in the list, MAIN VARIABLE
while(i < END):                 # Set the last Prime Number - the Upper Limit
    j = 2
    while(j <= (i/j)):              # This condition checks in the lower list
        if not(i%j): break          # IF  it's TRUE it stops, if FALSE it continues    # VERY IMPORTANT This line checks if the number is PRIME
        j = j + 1                       #Returns FALSE and continues if is i%j = 0 ; Returns TRUE and stops if i%j = 1,2,....
    if (j > i/j) :
        if ( '0' not in str(i) and '4' not in str(i)  and '6' not in str(i) and '8' not in str(i) and '1' not in str(i)[0]\
              and '1' not in str(i)[-1] and '9' not in str(i)[0] and '9' not in str(i)[-1] ):
            Pri.append(i)                     #  print( i, " is prime", end= ';   ')           # If j > i/j means that the number is not already in the list, therefore must be another prime
    i = i + 1

#print(len(Pri),Pri,'\n')

for z in Pri:
    tmp=[]
    for i in range(len(str(z))+1):
        a , b = str(z)[0:i] ,  str(z)[i-1::]            # str(z)[i-1::]
        #print(a,'    ' ,b)
        if (a != '' and b !='' ) :
            tmp.append(int(a))
            tmp.append(int(b))
            iter = 0
            for q in tmp:
                if detect_prime(q) == True:
                    iter+=1
                    #print(iter)
            #print(tmp)
    if iter == len(tmp) :
        Hunted.append(max(tmp))
        print(max(tmp),tmp)

print('\n','And their sum is:  ',  sum(Hunted),'   ' ,Hunted)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,4), 'ms')



'''
for z in Pri:
    tmp=[]
    for i in range(len(str(z))+1):
        a = str(z)[0:i]
        b = str(z)[i::]
        print(a,'   ;  ',b)


fae = 'abcdefghij'
print(fae[2::])
'''

'''
23 [2, 23, 23, 3]
37 [3, 37, 37, 7]
53 [5, 53, 53, 3]
73 [7, 73, 73, 3]
313 [3, 313, 31, 13, 313, 3]
317 [3, 317, 31, 17, 317, 7]
373 [3, 373, 37, 73, 373, 3]
797 [7, 797, 79, 97, 797, 7]
3137 [3, 3137, 31, 137, 313, 37, 3137, 7]
3797 [3, 3797, 37, 797, 379, 97, 3797, 7]
739397 [7, 739397, 73, 39397, 739, 9397, 7393, 397, 73939, 97, 739397, 7]

 And their sum is:   748317     [23, 37, 53, 73, 313, 317, 373, 797, 3137, 3797, 739397]

Completed in : 62379.5679 ms
'''