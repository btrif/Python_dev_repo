#!/usr/bin/python
# Solved by Bogdan Trif @
#The  Euler Project  https://projecteuler.net
'''
Palindromic sums        -       Problem 125

The palindromic number 595 is interesting because it can be written as the sum of consecutive squares:

            595 = 6**2 + 7**2 + 8**2 + 9**2 + 10**2 + 11**2 + 12**2.

There are exactly eleven palindromes below one-thousand that can be written as consecutive square sums,
and the sum of these palindromes is 4164.
Note that 1 = 0**2 + 1**2 has not been included as this problem is concerned with the squares of positive integers.

Find the sum of all the numbers less than 10**8 that are both palindromic and can be written as the sum of consecutive squares.


'''
import time, math, sys, numpy

import numtheory

print(numtheory.is_palindromic(595) )

sys.setrecursionlimit(100000)

def palin_generator(up_range):
    palindromes = [1,2,3,4,5,6,7,8,9]
    """Generates palindromic numbers."""
    # if len(str(up_range)) % 2 == 1 :
    l = len(str(up_range))//2
    # elif len(str(up_range)) % 2 == 0 :
    #     l = int(len(str(up_range))/2)
    # print('for orientation: ', len(str(up_range)) , l   )

    for i in range(1, 10) :
        palindromes.append( int(str(i)+str(i)[::-1 ] )   )

    for i in range(10, 10**(l) ):
        s1 = int( str(i)+str(i)[:-1][::-1])
        s2 =  int(str(i)+str(i)[::-1 ] )
        if s1 < up_range : palindromes.append( s1   )
        if s2 < up_range : palindromes.append( s2   )

    return palindromes






print('\n--------------------------INITIAL TESTS------------------------------')

t1  = time.time()



def dec_squares_rec(a, p) :
    if a == 0 :      return False
    if a**2 == p : return False
    S = 0
    for j in range(a, 0, -1 ) :
        S+=j**2
        # S = ( (a*(a+1)*(2*a+1) )-((j*(j+1)*(2*j+1)) ) )/ 6
        if S == p :
            return (p , list(range(a, j-1 , -1)))
        if S > p :
            return dec_squares_rec(a-1, p)
    return False

def descending_squares(a , p):
    if a == 0 :      return False
    if a**2 == p : return False
    for i in range(a, 0, -1) :
        if a > (i*(i+1)*(2*i+1))/6 : break
        for j in range(i, -1, -1 ) :
            S = ( (i*(i+1)*(2*i+1) )-((j*(j+1)*(2*j+1)) ) )/ 6
            if S == p :
                return (p , list(range(i, j , -1)))
            if S > p :
                break
    return False



print(' Test dec_squares Function : \t'  ,dec_squares_rec(24, 595) )
print(' Test dec_squares Function : \t'  ,dec_squares_rec(11, 595) )
print(' Test dec_squares Function : \t'  ,dec_squares_rec(11, 55) )

print('\n---------- The New Function ---------------')
print(' Test descending_squares Function : \t'  ,descending_squares(24, 595) )
print(' Test descending_squares Function : \t'  ,descending_squares(11, 595) )
print(' Test descending_squares Function : \t'  ,descending_squares(11, 55) )




t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n========  My FIRST SOLUTION,  VERY SLOW, > 1 hour ===============\n')


t1  = time.time()



def palindromic_sums_first(up_range):
    cnt, S, h = 0, 0, 0
    Pal = palin_generator(up_range)
    # print(Pal)
    for p in Pal :
            a = int((p/2)**(1/2) )+1
            DS = descending_squares(a, p)
            if DS != False :
                cnt+=1
                S+=p
                print(str(cnt)+'.   ', DS )
        # if p*100 //len(Pal)  > h-1 :        # Progress Bar #
        #     h += 1
        #     sys.stdout.write('\r' + str(h)+' % ['+'#'*h+str(' ')*(220-22*h//10) +']' )   # Font Segoe UI Semibold
        #     # sys.stdout.write('\r' + str(h)+' % ['+'#'*h+str(' ')*(100-h) +']' )         #  Calibri, Adjust the numbers, for the font of your configuration
        #     # sys.stdout.flush()
    return print('\nTotal Sum of Palindromes : \t', S)

# palindromic_sums_first(10**8)         # Answer : Total Sum of Palindromes : 	 2906969179




# UP TO 10**6  --> Total Sum of Palindromes : 	 14893023       # Completed in : 9853.563547 ms
# 117.    (15822851, [539, 538, 537, 536, 535, 534, 533, 532, 531, 530, 529, 528, 527, 526, 525, 524, 523, 522, 521, 520, 519, 518, 517, 516, 515, 514, 513, 512, 511, 510, 509, 508, 507, 506, 505, 504, 503, 502, 501, 500, 499, 498, 497, 496, 495, 494, 493, 492, 491, 490, 489, 488, 487, 486, 485, 484, 483, 482, 481, 480, 479])

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')      # Completed in : 1 hour



print('\n========  My SECOND SOLUTION,  IMPROVED ===============\n')

t1  = time.time()



def palindromic_sums_II(up_range):
    cnt, Pal_S, h = 0, 0, 0
    Pal = set(palin_generator(up_range))            # REVOLUTION  !!! WITH SETS !! Much FASTER Than Lists  :
    for i in range(1, int(numpy.sqrt(up_range)) ) :         # Completed in : 0.910 s  with SETS   VERSUS   33.245  second !!!! with LISTS  !!!!
        # print('START HERE --- > ', i)
        sq_sum = i**2
        j = 1
        while sq_sum < up_range :
            sq_sum += (j+i)**2
            # print(sq_sum)
            if sq_sum in Pal :
                Pal_S += sq_sum
                Pal.remove(sq_sum)
                cnt+=1
            j+=1

        # if (cnt-1)*100 //cnt  > h-1 :        # Progress Bar #
        #     h += 1
        #     sys.stdout.write('\r' + str(h)+' % ['+'#'*h+str(' ')*(220-22*h//10) +']' )   # Font Segoe UI Semibold
        #     # sys.stdout.write('\r' + str(h)+' % ['+'#'*h+str(' ')*(100-h) +']' )         #  Calibri, Adjust the numbers, for the font of your configuration
        #     # sys.stdout.flush()
    return print('\nTotal Sum of Palindromes : \t', Pal_S)

palindromic_sums_II(10**8)         # Answer : Total Sum of Palindromes : 	 2906969179




# UP TO 10**6  --> Total Sum of Palindromes : 	 14893023       # Completed in : 9853.563547 ms
# 117.    (15822851, [539, 538, 537, 536, 535, 534, 533, 532, 531, 530, 529, 528, 527, 526, 525, 524, 523, 522, 521, 520, 519, 518, 517, 516, 515, 514, 513, 512, 511, 510, 509, 508, 507, 506, 505, 504, 503, 502, 501, 500, 499, 498, 497, 496, 495, 494, 493, 492, 491, 490, 489, 488, 487, 486, 485, 484, 483, 482, 481, 480, 479])

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')








print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
# === GENERAL IDEA ===== 2016-12-19 12:12
# Instead of checking for each and every palindrome if it has associated a consecutive set of squares,
# better go from 1 up and see what palindromes you can find , sum them. Then, go to 2 up and find
# all the palindromes from the list and sum them. Then from 3, 4 and so on. VERY NICE IDEA !!!!


print('\n--------------------------SOLUTION 1,  SUPERB IMPLMENTATION & IDEA --------------------------')
t1  = time.time()

# ===== Wed, 12 Oct 2016, 18:27, mbh038, England
# About 210 ms in Python. I used code translated from the overview for problem 36 to quickly generate a set of all the palindromes.
# After that it was straightforward. There are a couple that can be generated by more than one sequence of consecutive squares, it seems.

import numpy as np

#from p36 outline
def makePalindrome(n,base,oddlength):
    res = n
    if oddlength:
        n = n // base
    while n > 0:
         res = base*res + n % base
         n = n // base
    return res

def mbh038_pb125(limit):
    """find all palindrome numbers below limit that are sums of consecutive squares"""

    pals=set()
    for oddlength in [True,False]:
        i,p = 0,0
        while p < limit:
             p = makePalindrome(i, 10, oddlength)
             pals.add(p)
             i +=1
    palsum=0
    for x in range(1,int(np.sqrt(limit))):
        # print('START HERE --- > ',x)
        i=1
        sqsum=x**2
        while sqsum<limit:
            sqsum+=(x+i)**2
            # print(sqsum)
            if sqsum in pals:
                palsum+=sqsum
                pals.remove(sqsum)
            i+=1
    print( palsum )


mbh038_pb125(10**8)


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 2,   --------------------------')
t1  = time.time()

# ===== Wed, 2 Sep 2015, 11:55, hornemann55, Denmark
# Pretty straight forward. Code runs in 0.55 sec

s=0
used=set()
for b in range(1,10000):
   s2 = b*b
   for a in range(b-1,0,-1):
      s2 += a*a
      if s2 > 100000000:
         break
      st = str(s2)
      if st == st[::-1] and not s2 in used:
         s +=s2
         used.add(s2)
print(s)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 3,  SLOW --------------------------')
t1  = time.time()
# ===== Thu, 13 Oct 2016, 20:49, aolea , Spain

def aolea():
    aux = []
    sum = 0
    count = 0
    for i in range (0,10**4+1):
        for j in range(i+2,10**4+1):
            num_sum_sq = int((j*(j+1)*(2*j+1)-i*(i+1)*(2*i+1))/6)
            if num_sum_sq < 10**8:
                if str(num_sum_sq)[::-1] == str(num_sum_sq):
                    if num_sum_sq not in aux:
                        aux.append(num_sum_sq)
                        sum = sum + num_sum_sq
                        count = count + 1
                        print(i,j,num_sum_sq,sum)
    return  print(count,sum)

# aolea()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 4,  FAST  --------------------------')
t1  = time.time()

# ===== Sat, 5 Nov 2016, 09:27, intestine, Japan
# There are only two duplicates:554455,9343439


#Project Euler 125 : Palindromic sums
def psums():
    s = 0
    a = []
    for i in range(1,7500):
        x = i**2 + (i+1)**2
        j = i + 2
        while x < 100000000:
            if (x not in a) & (str(x) == str(x)[::-1]):
                s += x
                a.append(x)
            x += j**2
            j += 1
    return s
print (psums())

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 5,   --------------------------')
t1  = time.time()

# ==== Sun, 4 Oct 2015, 14:28, elvischen
# use sqrt(10^8/2) and n*(n+1)*(2*n+1)/6 to be the limit


from numtheory import  is_palindromic

list_2 = []
for i in range(22400):
    list_2.append(i*i)

Max_x = 10**8
x = []
for i in range(1,22360):
    sum_x = list_2[i]
    j = 1
    while (j < 700):
        sum_x += list_2[i+j]
        j += 1
        if sum_x > Max_x:
            break
        if is_palindromic(sum_x):
            x.append(sum_x)

print (sum(set(x)))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 6,   --------------------------')
t1  = time.time()

# ========  Mon, 18 Jan 2016, 20:49, kahawala , Sri Lanka
# How is this one?? works under 0.5 seconds!!!!!!!!!! :D :D :D :* <3

def palindromic(x):
    y=str(x)
    if y==y[::-1]:
        return True
A=set()
for x in range(1,5000):
    sum_of_square=0
    a=x
    count=0

    while  a**2<=100000000 and sum_of_square<=100000000:
       sum_of_square+= a**2
       count+=1
       if sum_of_square>=100000000:
           break
       if count==1 and palindromic(sum_of_square):1
       elif palindromic(sum_of_square):A.add(sum_of_square)
       a+=1
print (sum(A), "Hurrayy!!!!!!!!!!!")



t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 7,   --------------------------')
t1  = time.time()

#
# ===== Mon, 18 Apr 2016, 11:17, ikarnikamit, India
# python 2.6.6, RunTime: 0.302266836166 s
# -*- coding: utf-8 -*-
__author__ = "karnikamit"


def is_palindrome(n):
    n_str = str(n)
    return n_str == n_str[::-1]


def euler(limit):
    p_s = set()
    limit_to = int(limit ** 0.5)
    for i in range(1, limit_to):
        num = i ** 2
        while num < limit:
            i += 1
            num += i ** 2
            if is_palindrome(num) and num < limit:
                p_s.add(num)
    return sum(p_s)

if __name__ == '__main__':
    print (euler(10 ** 8))    # 2906969179

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 8,   --------------------------')
t1  = time.time()

# ==== Thu, 4 Sep 2014, 23:18, Skiracer, England
# quite simple once the plan is laid down
#deals with the consecutive squares
def conS(i,j):
	return (((i*(i+1)*(2*i+1))//6)-(j*(j+1)*(2*j+1))//6)

#checks if the number is a palindrome
def isPalindrome(x):
	x=str(x)
	if(x==x[::-1]):
		return True
	return False

#create a set of the numbers we want to check for uniqueness
conSecPal=[]
for i in range(0,10**4):
	for j in range(i-2,-1,-1):
		x=conS(i,j)
		if(x>10**8):
			break
		if(isPalindrome(x)):
			conSecPal.append(x)
nonRep=set(conSecPal)
print(sum(nonRep),len(nonRep))


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

