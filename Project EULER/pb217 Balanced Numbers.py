#  Created by Bogdan Trif on 16-10-2017 , 11:53 AM.
# © o(^_^)o  Solved by Bogdan Trif  @
#The  Euler Project  https://projecteuler.net
'''
        Balanced Numbers            -           Problem 217

A positive integer with k (decimal) digits is called balanced if its first ⌈k/2⌉ digits sum to the same value
as its last ⌈k/2⌉ digits, where ⌈x⌉, pronounced ceiling of x, is the smallest integer ≥ x,
thus ⌈π⌉ = 4 and ⌈5⌉ = 5.

So, for example, all palindromes are balanced, as is 13722.

Let T(n) be the sum of all balanced numbers less than 10^n .
Thus: T(1) = 45, T(2) = 540 and T(5) = 334795890.

Find T(47) mod 3^15


'''
import time, zzz

# 2018-03-30 - generate recursively the numbers and ...
### KEY OBSERVATION :
#     We only iterate EVEN numbers and then we put in the midle the numbers (0,1...9) to obtain
# an ODD number. So... our work is reduced to HALF !!
# max length = 47 ==> 23 digits on left, 23 digits on right
#
# 2.  We observe that 7539, 7548, 7557, 7566  have a difference of 9 as in the case of :
# 81209, 81218, 81227, 81236, 81245, 81254, 81263, 81272, 81281, 81290,  - so we can group them



def is_balanced(n) :
    l = len(str(n))
    m = l // 2
    if l %2 ==0 :
        s1, s2 = str(n)[ :m], str(n)[m:]
    if l %2 ==1 :
        s1, s0, s2 = str(n)[ :m], str(n)[m] , str(n)[m+1:]
        # print( s1 ,'     ' , s0 , '     ' , s2    )
    S1, S2 = sum([ int(i) for i in s1 ]), sum([ int(i) for i in s2 ])
    # print([ int(i) for i in s1 ] ,   ' ; S1= ' , S1 ,'     ', [ int(i) for i in s2 ], ' ; S2= ',S2 )
    return S1 == S2


# print('is_balanced : ' ,is_balanced(22822) )
print('is_balanced : ' ,is_balanced(99) )

print('\n--------------------------TESTS------------------------------')
t1  = time.time()

lim = 10**5
Sigma = 0
for n in range(1, lim+1) :
    if is_balanced(n) :
        Sigma += n
        print(n,'        ',  is_balanced(n) )

print('\nSigma = ', Sigma )

t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')

print('\n================  My FIRST SOLUTION,   ===============\n')
# t1  = time.time()





# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')


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




