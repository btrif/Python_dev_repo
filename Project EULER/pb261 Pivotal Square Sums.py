#  Created by Bogdan Trif on 04-11-2017 , 11:59 PM.
# © o(^_^)o  Solved by Bogdan Trif  @
#The  Euler Project  https://projecteuler.net
'''
            Pivotal Square Sums             -           Problem 261

Let us call a positive integer k a square-pivot, if there is a pair of integers m > 0 and n ≥ k,
such that the sum of the (m+1) consecutive squares up to k equals
the sum of the m consecutive squares from (n+1) on:

(k-m)^2 + ... + k^2  = (n+1)^2 + ... + (n+m)^2.

Some small square-pivots are :

4:          3^2 + 4^2 = 5^2
21:         20^2 + 21^2 = 29^2
24:         21^2 + 22^2 + 23^2 + 24^2 = 25^2 + 26^2 + 27^2
110:       108^2 + 109^2 + 110^2 = 133^2 + 134^2

Find the sum of all distinct square-pivots ≤ 10^10.


'''
import time, zzz

# https://brilliant.org/wiki/sum-of-n-n2-or-n3/
# OBSERVATION : nr of right terms are = nr of left terms - 1              !!!!!
#
# BINARY SEARCH ! for the RHS terms
#

def get_factors(n):       ### o(^_^)o  FASTEST  o(^_^)o  ###
    ''' Decompose a factor in its prime factors. This function uses the pyprimes module. THE FASTEST  '''
    from pyprimes import factorise
    return [val for sublist in [[i[0]]*i[1] for i in factorise(n)] for val in sublist]

# Sum{k=1, n} ( k**2) = n*(n+1)*(2*n+1) / 6     So it starts with 1
Sum_squared_basic = lambda n :  n*(n+1)*(2*n+1) // 6

# print('Sum_squared_basic = ', Sum_squared_basic( 4 ))

def Sum_squared(k, n) :
    ''':Description: returns Sum{k, n} (k^2)
        :Example: Sum{4, 7} (k^2) = Sum{1, 7} (k^2) - Sum{1, 3} (k^2)
    :param k:  int, the starting k number
    :param n: int, ending number
    :return: int, Sum{k, n} (k^2)           '''
    Sum_squared_basic = lambda n :  n*(n+1)*(2*n+1) // 6
    S1 = Sum_squared_basic(k-1)
    S2 = Sum_squared_basic(n)
    return S2 -  S1

def pivot_square_sum(k, dn) :
    Sum_squared_basic = lambda n :  n*(n+1)*(2*n+1) // 6
    S1 = Sum_squared_basic(k-dn-1)
    S2 = Sum_squared_basic(k)
    # print(k, k-dn, S1, S2)
    return S2 -  S1



print('Sum_squared = ' , Sum_squared( 4 , 7 ) )
print('Verification : ' , sum(  [i*i for i in range(1,7+1)]) - sum( [i*i for i in range(1,3+1) ])    )

print('pivot_square_sum = ' , pivot_square_sum( 24 , 3 ) )
print('Verification : ' , sum(  [i*i for i in range(1,24+1)]) - sum( [i*i for i in range(1,21+1) ])    )

print('Sum_squared = ' , pivot_square_sum( 4 , 2 ) )

print('\nData problem verif : ', Sum_squared(21, 21+3) , Sum_squared(25, 25+2)   )

print('\n--------------------------TESTS------------------------------')
t1  = time.time()




def brute_force(pivot_lim):
    cnt, SUM = 0, 0
    for pivot in range(2, pivot_lim ) :
        # print('---------  pivot = ', pivot ,'--------------- ')
        for dn in range(1, 26) :
            SL = pivot_square_sum(pivot, dn)
            # print(' dn= ' , dn , SL)
            for j in range( pivot+1, pivot+500 ) :
            # j = pivot +1
                SR = Sum_squared ( j, j+dn-1 )
                # print( 'j = ', j , '    dn=' , dn ,  '    SL= ' , SL, '         SR = ' ,SR)
                if SL == SR :
                    cnt +=1
                    SUM += pivot
                    LHS, RHS =  list(range(pivot-dn, pivot+1 )),  list(range(j, j+dn ))
                    print(str(cnt) + '.          pivot =' , pivot  ,'          LHS =  ', LHS , '        RHS =  ', RHS  ,'      diff= ' , RHS[0] - LHS[-1] ,'     pivot= ', get_factors(pivot) )

    print('\nAnswer : \t', SUM)

brute_force( 10**4 )



# --------------------------TESTS------------------------------
# 1.          pivot = 21           LHS =   [20, 21]         RHS =   [29]       diff=  8      pivot=  [3, 7]
# 2.          pivot = 110           LHS =   [108, 109, 110]         RHS =   [133, 134]       diff=  23      pivot=  [2, 5, 11]
# 3.          pivot = 120           LHS =   [119, 120]         RHS =   [169]       diff=  49      pivot=  [2, 2, 2, 3, 5]
# 4.          pivot = 315           LHS =   [312, 313, 314, 315]         RHS =   [361, 362, 363]       diff=  46      pivot=  [3, 3, 5, 7]
# 5.          pivot = 684           LHS =   [680, 681, 682, 683, 684]         RHS =   [761, 762, 763, 764]       diff=  77      pivot=  [2, 2, 3, 3, 19]
# 6.          pivot = 697           LHS =   [696, 697]         RHS =   [985]       diff=  288      pivot=  [17, 41]
# 7.          pivot = 820           LHS =   [812, 813, 814, 815, 816, 817, 818, 819, 820]         RHS =   [862, 863, 864, 865, 866, 867, 868, 869]       diff=  42      pivot=  [2, 2, 5, 41]
# 8.          pivot = 1080           LHS =   [1078, 1079, 1080]         RHS =   [1321, 1322]       diff=  241      pivot=  [2, 2, 2, 3, 3, 3, 5]
# 9.          pivot = 1265           LHS =   [1260, 1261, 1262, 1263, 1264, 1265]         RHS =   [1381, 1382, 1383, 1384, 1385]       diff=  116      pivot=  [5, 11, 23]
# 10.          pivot = 2106           LHS =   [2100, 2101, 2102, 2103, 2104, 2105, 2106]         RHS =   [2269, 2270, 2271, 2272, 2273, 2274]       diff=  163      pivot=  [2, 3, 3, 3, 3, 13]
# 11.          pivot = 3255           LHS =   [3248, 3249, 3250, 3251, 3252, 3253, 3254, 3255]         RHS =   [3473, 3474, 3475, 3476, 3477, 3478, 3479]       diff=  218      pivot=  [3, 5, 7, 31]
# 12.          pivot = 4760           LHS =   [4752, 4753, 4754, 4755, 4756, 4757, 4758, 4759, 4760]         RHS =   [5041, 5042, 5043, 5044, 5045, 5046, 5047, 5048]       diff=  281      pivot=  [2, 2, 2, 5, 7, 17]
# 13.          pivot = 6669           LHS =   [6660, 6661, 6662, 6663, 6664, 6665, 6666, 6667, 6668, 6669]         RHS =   [7021, 7022, 7023, 7024, 7025, 7026, 7027, 7028, 7029]       diff=  352      pivot=  [3, 3, 3, 13, 19]
# 14.          pivot = 9030           LHS =   [9020, 9021, 9022, 9023, 9024, 9025, 9026, 9027, 9028, 9029, 9030]         RHS =   [9461, 9462, 9463, 9464, 9465, 9466, 9467, 9468, 9469, 9470]       diff=  431      pivot=  [2, 3, 5, 7, 43]



# @2017-12-11 - The regular pivots  are following the pattern 4, 12, 20, 32, .... => +4, +8, +12, +16 ,...
# The task now is to find the abnormal ones of the type :
# pivot = 110           LHS =   [108, 109, 110]         RHS =   [133, 134]
# pivot = 315           LHS =   [312, 313, 314, 315]         RHS =   [361, 362, 363]



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




