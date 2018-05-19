#  Created by Bogdan Trif on 07-10-2017 , 11:55 PM.
# © o(^_^)o  Solved by Bogdan Trif  @       Completed on Thu, 29 Mar 2018, 23:19
#The  Euler Project  https://projecteuler.net/problem=401
'''
                        Sum of squares of divisors      -       Problem 401


The divisors of 6 are 1,2,3 and 6.
The sum of the squares of these numbers is 1+4+9+36=50.

Let sigma2(n) represent the sum of the squares of the divisors of n. Thus sigma2(6)=50.

Let SIGMA2 represent the summatory function of sigma2,

that is SIGMA2(n) = ∑sigma2(i) for i=1 to n.

The first 6 values of SIGMA2 are: 1,6,16,37,63 and 113.

Find SIGMA2(10^15) modulo 10^9.


'''
import time, zzz
from math import sqrt, ceil, floor


# https://en.wikipedia.org/wiki/Square_pyramidal_number
def get_divisors(n):      ### ( ͡° ͜ʖ ͡°)  FASTEST  ( ͡° ͜ʖ ͡°)  ### !! FIRST FASTEST !! Must be improved !!

    factors = set()
    for x in range(1, int(sqrt(n)) + 1):
        if n % x == 0:
            factors.add(x)
            factors.add(n//x)
    return sorted(factors)


print('\n--------------------------TESTS------------------------------')
t1  = time.time()

# A way to check :
Appearences = dict()
def validation_test(lim) :
    SIGMA2 = 0
    for i in range(1, lim + 1) :
        gd = get_divisors(i)
        for x in gd :
            if x in Appearences :
                Appearences[x]+=1
            else :
                Appearences[x] = 1

        sigma2 = sum([ j*j for j in gd ])
        print(str(i) +'.    divisors : ', gd , '   sigma2 =  ', sigma2  )
        SIGMA2 += sigma2

    print('\n',Appearences)
    print('\nAppearences :\n ')
    for k in range(1, lim+1 ):
        if k in Appearences :
            print(' k= ', k ,'      appearence = ' , Appearences[k] )

    return print('\nSIGMA2 = ', SIGMA2)

# validation_test(10**3)

t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n')

print('\n================  My FIRST SOLUTION, Completed in : 2 min  ===============\n')
t1  = time.time()

### 2018-03-29, 22:40  - LOGIC -
# KEY OBSERVATION : find the EQUILIBRIUM POINT !!!!! Which is sqrt(lim)
###  PART II - We observe that lager terms appear scarcely as we go up : Like
# Appearences :
#  k=  1       appearence =  10
#  k=  2       appearence =  5
#  k=  3       appearence =  3
#  k=  4       appearence =  2
#  k=  5       appearence =  2
#  k=  6       appearence =  1
#  k=  7       appearence =  1
#  k=  8       appearence =  1
#  k=  9       appearence =  1
#  k=  10       appearence =  1
# This means we can use the Number of appearances i and compute what numbers appear once, in this case from 10 down to 6
# Then count how many numbers appear twice, here we have from 5 down to 4...and so on.
# We observe that int(sqrt(10)) = 3 appear only once and from down there all the numbers appear more often .
# So we go down until sqrt(10)
#
# ###     PART I :
# Starting from i=1 to sqrt(10) = 3 we count how many terms we have of 1, in this case there are 10/1 = 10 terms
# how many terms of 2, => 10/2 = 5 ...and so on. We stop at sqrt(3)

Square_sum = lambda n : n * (n+1) *(2*n+1) //6
# lim = 10

# print('Square_sum ('+ str(lim)+') = ' , Square_sum(lim) )

Custom_Square_Sum = lambda down, up : (up * (up+1) *(2*up+1) //6 ) - (down * (down+1) *(2*down+1) //6 )
# print('Custom_Square_Sum ( ) = ' , Custom_Square_Sum(2, 4),'\n' )



def my_first_solution(lim) :
    SIGMA2 = 0
    prnt = 10**6

    for i in range(1, floor(sqrt(lim)) +1 ) :

        ### Part II - i represents the Number of APPEARANCES, what range of numbers appear once, what range of numbers appear twice
        # and so on , We only go to sqrt(lim) as we see that is the equilibrium point
        up_lim = lim // i
        down_lim = lim // (i+1) +1
        CSS = Custom_Square_Sum(down_lim-1, up_lim)

        SIGMA2 += CSS * i
        if i % (prnt) == 0 :
            print('i=' , i , '      up_lim = ' , up_lim, '      down_lim = ' , down_lim  ,'        Custom_Square_Sum = ', CSS,'        ', CSS*i  )

        #### PART I - i represents the NUMBER ITSELF and we count how many times number 1 appear => lim/1
        # 2 appears => lim/2, ... and so on... The upper limit is sqrt(lim) which is the Equilibrium point
        nr_of_app = lim// i
        if i % (prnt) == 0 :
            print('i=' , i , '      nr_of_appearances = ' , nr_of_app ,'         ', i*i * nr_of_app)
        SIGMA2 += i*i * nr_of_app

    if floor(sqrt(lim)) == lim//(floor(sqrt(lim))) :
        SIGMA2 = SIGMA2 - ( (  floor(sqrt(lim)))**2 * ( lim//(floor(sqrt(lim))) ) )
        return print('\nSIGMA2 = ',  SIGMA2  , '\nSIGMA2 (  mod 10^9 )= ', SIGMA2%(10**9)  )
    else :
        return print('\nSIGMA2 = ',  SIGMA2   , '\nSIGMA2 (  mod 10^9 )= ', SIGMA2%(10**9) )

my_first_solution(10**15)           #     ANSWER :   SIGMA2 (  mod 10^9 )=  281632621

t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')            #Completed in : 122608.01 ms


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




