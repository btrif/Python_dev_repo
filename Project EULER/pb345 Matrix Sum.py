#!/usr/bin/python
# Solved by Bogdan Trif @   Completed on Fri, 15 Sep 2017, 23:12
#The  Euler Project  https://projecteuler.net
'''
                    Matrix Sum      -       Problem 345

We define the Matrix Sum of a matrix as the maximum sum of matrix elements with each element being the only one in his row and column.
For example, the Matrix Sum of the matrix below equals 3315 ( = 863 + 383 + 343 + 959 + 767):

                                                              7  53 183 439 863
                                                            497 383 563  79 973
                                                            287  63 343 169 583
                                                            627 343 773 959 943
                                                            767 473 103 699 303

Find the Matrix Sum of:

                              7  53 183 439 863 497 383 563  79 973 287  63 343 169 583
                            627 343 773 959 943 767 473 103 699 303 957 703 583 639 913
                            447 283 463  29  23 487 463 993 119 883 327 493 423 159 743
                            217 623   3 399 853 407 103 983  89 463 290 516 212 462 350
                            960 376 682 962 300 780 486 502 912 800 250 346 172 812 350
                            870 456 192 162 593 473 915  45 989 873 823 965 425 329 803
                            973 965 905 919 133 673 665 235 509 613 673 815 165 992 326
                            322 148 972 962 286 255 941 541 265 323 925 281 601  95 973
                            445 721  11 525 473  65 511 164 138 672  18 428 154 448 848
                            414 456 310 312 798 104 566 520 302 248 694 976 430 392 198
                            184 829 373 181 631 101 969 613 840 740 778 458 284 760 390
                            821 461 843 513  17 901 711 993 293 157 274  94 192 156 574
                             34 124   4 878 450 476 712 914 838 669 875 299 823 329 699
                            815 559 813 459 522 788 168 586 966 232 308 833 251 631 107
                            813 883 451 509 615  77 281 613 459 205 380 274 302  35 805

'''
import time, heapq, itertools
from copy import deepcopy
import numpy as np

filename = 'pb345_matrix.txt'

f = open(filename, 'r')
text = f.read()
f.close()
# Initialize and populate matrix
matrix = []
# print(text,'        ',type(text),'\n')

for row in text.split('\n'):
    matrix.append(list(map(int, row.split(' '))))         # This maps the strings into ints on the run, SMART TECHNIQUE

print('================ THE MAIN MATRIX =================\n')
M = np.array(matrix)
for i in M :
    print(i)
print('\n'+'=='*25)

# @2017-02-07
# find max on a column, then interesect with the row to confirm.
# if there as new maximum establish that maximum and go on next row.
#
# Also must keep track of already marked positions !!!




print('\n--------------------------TESTS------------------------------\n')
t1  = time.time()

# tmp = heapq.nlargest(8, M[0])
# print( 'First 8  Largest elements in the list : ',heapq.nlargest(8, M[0]) )
# print([ (j, M[0].index(j))   for j in  tmp ])

#
# https://www.youtube.com/watch?v=-JjA4BLQyqE
# https://github.com/nayuki/Project-Euler-solutions/blob/master/java/p345.java
#
# /*
# 	 * With memoization we achieve a run time of O(n^2 * 2^n), instead of brute-forcing all O(n!) permutations.
# 	 * This is the same idea as the Held-Karp algorithm for the travelling salesman problem.
# 	 */

M_test = np.array( [ [7,  53 ,183 ,439 ,863],
                            [497 ,383 ,563  ,79 ,973],
                           [ 287 , 63 ,343 ,169 ,583],
                            [627, 343 ,773 ,959, 943],
                            [767 ,473 ,103 ,699, 303 ]] )

def brute_force_check(M_test) :
    M = deepcopy(M_test)
    max_sum = 0
    for c in list( itertools.permutations([0, 1,2,3,4 ] ) ) :
        s =  sum ([ M[0][ c[0] ] ,M[1][ c[1] ] ,M[2][ c[2] ] , M[3][ c[3] ] , M[4][ c[4]  ] ] )
        # print( [ M[0][ c[0] ] ,M[1][ c[1] ] ,M[2][ c[2] ] , M[3][ c[3] ] , M[4][ c[4]  ] ] )
        if s > max_sum :
            max_sum = s
            print('s = ', s ,'       ', M[0][ c[0]  ] ,M[1][ c[1]  ] ,M[2][ c[2]  ] , M[3][ c[3]  ] , M[4][ c[4]  ] )
    # print( len(  list( itertools.permutations([1,2,3,4,5] ) )))
    return print('\nSmallest sum=  ', max_sum )

# brute_force_check(M_test)






t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 's\n\n')

print('\n================  My FIRST SOLUTION,   ===============\n')

def mukrane(M) :
    L = deepcopy(M)
    # STEP 1. For each row, find the lowest element and substract it from each element in that row.
    rmins = [ min(L[i]) for i in range(len(L)) ]
    print(rmins)
    for i in range(len(L)) :
        for j in range(len(L[i])) :
            L[i][j] -= rmins[i]

    print(' ------    Row Reduction : M\n', L)
    # STEP 2.
    # For each column, find the lowest element and substract it from each element in that column.
    # If the lowest value is 0, don't change that column
    cmins = [ min(L.transpose()[i]) for i in range(len(L)) ]
    print(cmins)
    for i in range(len(cmins)) :
        if cmins[i] != 0 :
            for j in range(len(L[i]) ) :
                L[j][i] -= cmins[i]
    print(' ------    Column Reduction : M\n', L)
    # STEP 3. Cross out the o's using the minimum number of horizontal and vertical lines
    #     If the number of lines < n, then we must reduce the matrix again

    min_nr_of_crosses(L, 1 )
    print('\n', L )

    return L


def min_nr_of_crosses(M, iteration) :      # RECURSION !!! YEEEEEEEES !  @ 2017-09-14, 20:00
    print('\n ------ New iteration starts here -------   ', iteration ,'\n')

    ###########CASE 1  ROW PRECEDENCE FIRST   ###############
    print('\n ######## CASE  1  #############')
    N = deepcopy(M)
    rcount1 = [  len(M[i]) - np.count_nonzero(N[i])  for i in range(len(N)) ]
    ccount1 = [  len(N.transpose()[i]) - np.count_nonzero(N.transpose()[i])  for i in range(len(N.transpose())) ]
    cnt1 = 0
    col1, row1 = [], []
    print('initial  rcount1 & rcount1 :  ', rcount1 , '    ', ccount1 )

    while ( sum(rcount1)+sum(ccount1)) > 0 :
        if max(rcount1) >= max(ccount1):
            xm = np.argmax(rcount1)
            print('CASE 1  row 1 xm= ',xm)
            N = np.delete(N, xm , axis=0 )
            N = np.insert(N, xm, values=[2222]*len(M)  ,axis=0)
            row1.append(xm)
            print('row1 = ', row1)
            cnt1+=1
        else :
            xm = np.argmax(ccount1)
            N = np.delete(N, xm , axis=1 )
            N = np.insert(N, xm, values=[2222]*len(M)  ,axis=1)
            print('CASE 1  col 1  : \t', xm)
            col1.append(xm)
            print('col1 = ', col1 )
            cnt1 += 1
        print('\n',N,'\n')
        rcount1 = [  len(N[i]) - np.count_nonzero(N[i])  for i in range(len(N)) ]
        ccount1 = [  len(N.transpose()[i]) - np.count_nonzero(N.transpose()[i])  for i in range(len(N.transpose())) ]
        print('IN while loop  rcount1, rcount1 , cnt1 =  \t', cnt1, '      ' , rcount1, ccount1 ,'\n' , row1, col1 , '\n' )

        N1 = deepcopy(N)
    ###########CASE 2  COL PRECEDENCE FIRST   ###############
    print('\n ######## CASE  2  #############')
    N = deepcopy(M)
    rcount2 = [  len(M[i]) - np.count_nonzero(N[i])  for i in range(len(N)) ]
    ccount2 = [  len(N.transpose()[i]) - np.count_nonzero(N.transpose()[i])  for i in range(len(N.transpose())) ]
    cnt2 = 0
    col2, row2 = [], []
    print('initial  rcount2 & rcount2 :  ', rcount2 , '    ', ccount2 )

    while ( sum(rcount2)+sum(ccount2)) > 0 :
        if max(ccount2) >= max(rcount2):
            xm = np.argmax(ccount2)
            print(' CASE 2  col 1  : \t', xm)
            N = np.delete(N, xm , axis=1 )
            N = np.insert(N, xm, values=[2222]*len(M)  ,axis=1)
            col2.append(xm)
            print('col2 = ', col2 )
            cnt2 += 1
        else :
            xm = np.argmax(rcount2)
            print('CASE 2 row 2 xm= ',xm)
            N = np.delete(N, xm , axis=0 )
            N = np.insert(N, xm, values=[2222]*len(M)  ,axis=0)
            row2.append(xm)
            print('row2 = ', row2)
            cnt2+=1

        print('\n',N,'\n')
        rcount2 = [  len(N[i]) - np.count_nonzero(N[i])  for i in range(len(N)) ]
        ccount2 = [  len(N.transpose()[i]) - np.count_nonzero(N.transpose()[i])  for i in range(len(N.transpose())) ]
        print('in while loop  rcount2, ccount2 , cnt2 =  : \t', cnt2,'       ' ,rcount2, ccount2   , '\n'  , row2, col2 ,'\n'  )

        N2 = deepcopy(N)
################# END ############




    print('how many crossing cnts : \t', ' cnt1 =' ,cnt1 , '      cnt2 =' ,cnt2 , ' min =  ', min(cnt1, cnt2) )
    if min(cnt1, cnt2) == len(M) :
        print(' \n%%%%%%%%%%%%%  just before it ends  %%%%%%%%%%%%%%%%%%: \n',M ,'\n')

        # if len( select_positions( N, POS =[] ) ) == len(M) :
        return M
        # else :
        #     return min_nr_of_crosses(M, iteration + 1 )




    if (cnt1 == len(M) or cnt2 == len(M) ) :
        if cnt1 <= cnt2 :
            row, col, cnt  = row1, col1, cnt1
            N = deepcopy(N1)

        else :
            row, col, cnt  = row2, col2, cnt2
            N = deepcopy(N2)

    if (cnt1 < len(M) and cnt2 < len(M) ) :
        if cnt1 >= cnt2 :
            row, col, cnt  = row1, col1, cnt1
            N = deepcopy(N1)

        else :
            row, col, cnt  = row2, col2, cnt2
            N = deepcopy(N2)




    crossings = [ ( i,j )  for i in row for j in col ]
    print('\n=== Crossings : \t', row, col ,'     ', crossings )
    nmin = N.min()
    print('Minimum of Matrix leftover nmin is : \t', nmin ,'\n')

    # We substract for the non-zero elements and we add for the crossings
    if cnt < len(M) :
        for i in range(len(M)) :
            for j in range(len(M[i])) :
                if i in row or j in col :
                    continue
                elif M[i][j] != 0 :
                    M[i][j] -= nmin
        for k in crossings : M[k[0]][k[1]] += nmin

    print(' M: \n',M)

    if cnt < len(M) :
        # if iteration < 10 :
        print('##########################################')
        return min_nr_of_crosses(M, iteration + 1 )



def select_positions(A , POS) :
    # Select positions :
    print('----------- SELECT POSITIONS ------------------')

    rcount =np.array( [  len(A[i]) - np.count_nonzero(A[i])  for i in range(len(A)) ] )
    ccount = np.array( [  len(A.transpose()[i]) - np.count_nonzero(A.transpose()[i])  for i in range(len(A.transpose())) ] )
    print('\n--- in solve rcount, ccount : ' , rcount, ccount)

    print('np.where  i = \t' , np.where( rcount == 1)  )
    i = np.where( rcount == 1)[0][0]
    j = np.where(A[i] == 0 )[0][0]
    # print( 'i, j : \t',i, j )
    for a in range(len(A[j]) ) :
        # print(A[a][j])
        if A[a][j] ==0 :
            if a == i : A[i][j] = -2
            else : A[a][j] = -1         # Greu co logica asta, am pierdut 15 minute aici
    POS. append((i,j))
    print('POS : \t', POS)
    print(A)
    rcount =np.array( [  len(A[i]) - np.count_nonzero(A[i])  for i in range(len(A)) ] )
    ccount = np.array( [  len(A.transpose()[i]) - np.count_nonzero(A.transpose()[i])  for i in range(len(A.transpose())) ] )
    print('POS in  rcount, ccount : ' , rcount, ccount)

    # print('np.where for rcount = 1 : \t' ,np.where(rcount == 1 )[0] , 'len : ', len(np.where(rcount == 1)[0] )  )
    if len(np.where(rcount == 1)[0] ) >0 :
        return select_positions(A, POS)

    return POS


def substract_matrix_maximum(M) :
    ''' this function is for the case when we want to Maximize the profit, or maximize
        the matrix sum as in the problem Euler 345 from projectEuler
    :Description:   We find the maximum value in the matrix and we substract max - M[i][j]
        for each value in the matrix
    :param M: int 2D array, matrix
    :return: return int 2D array matrix     '''
    N = deepcopy(M)
    vmax = max ( [  max(N[i]) for i in range( len(N )) ])

    # print('max value in the matrix : \t', vmax  )
    for i in range(len(N)) :
        for j in range(len(N[i])) :
            N[i][j] = vmax - N[i][j]
    # print('N: \n',N)
    return N

################## END  FUNCTIONS   ##################

print ('\n ---- My Failed solution because my Munkres algorithm does not work as it should on big matrices------------------'   )

def failed_solution_must_fix_my_mukrane_algo() :
        print('\noriginal M : \n',M)
        # M = deepcopy(M_test)

        # N = substract_matrix_maximum(M)
        O = deepcopy(M)
        N = deepcopy(O)

        # min_nr_of_crosses(N, iteration= 1)
        print('\n------------------------')

        Q = deepcopy( mukrane( O) )
        print('\nMukrane : \n', Q )
        POS = select_positions( Q, POS =[] )
        print('how many positions : \t' ,len(POS))

        print('M:\n',M )
        print('\nThe final position values are : ')
        S = 0
        for i,j in POS :
            print(i, j , '    ', M[i][j]  )
            S += M[i][j]

        print('\n SUM : \t', S)



    # test_POS = np.array( [[   0  ,  6 , 196 , 432 , 877,  515 , 290  ,637   , 0  ,847 , 279 ,   0 , 342 , 175  , 551],
    #                          [ 443,  119  ,609 , 775 , 780  ,608 , 203  ,  0 , 443  ,  0 , 772 , 463 , 405 , 468  , 704],
    #                          [ 418,  214 , 454  ,  0 ,  15 , 483 , 348, 1045 ,  18 , 735 , 297  ,408  ,400,  143   ,689],
    #                          [ 200 , 566 ,   6 , 382,  857 , 415 ,   0 ,1047  ,  0  ,327  ,272 , 443 , 201,  458  , 308],
    #                          [ 782 , 158 , 524 , 784  ,143 , 627 , 222,  405  ,662 , 503  , 71 , 112  ,  0 , 647 ,  147],
    #                          [ 744 , 290  , 86 ,  36 , 488 , 372 , 703 ,   0 , 791 , 628 , 696 , 783  ,305 , 216 ,  652],
    #                          [ 819 , 771  ,771,  765  ,  0 , 544  ,425 , 162 , 283 , 340 , 518 , 605 ,  17  ,851   ,147],
    #                          [ 214 ,   0 , 884 , 854  ,199 , 172  ,747 , 514 ,  85 ,  96 , 816,  117,  499  ,  0  , 840],
    #                          [ 428,  664 ,  14 , 508 , 477 ,  73  ,408  ,228 ,  49 , 536 ,   0  ,355  ,143  ,444  , 806],
    #                          [ 285 , 287 , 201 , 183  ,690 ,   0  ,351 , 472 , 101 ,   0 , 564 , 791 , 307  ,276 ,   44],
    #                          [  58 , 663  ,267 ,  55 , 526   , 0  ,757,  568  ,642 , 495  ,651 , 276  ,164 , 647  , 239],
    #                          [ 783,  383  ,825,  475 ,   0  ,888  ,587 ,1036 , 183,    0 , 235  ,  0  ,160 , 131  , 511],
    #                          [  10 ,  60  ,  0 , 854 , 447 , 477  ,602 , 971 , 742 , 526 , 850 , 219  ,805 , 318  , 650],
    #                          [ 733 , 437 , 751  ,377 , 461 , 731  ,  0  ,585 , 812 ,  31  ,225 , 695 , 175 , 562  ,   0],
    #                          [ 765 , 795  ,423 , 461,  588  , 54  ,147 , 646  ,339  , 38 , 331 , 170,  260 ,   0  , 732]] )
    #
    # POS = select_positions( test_POS, POS =[] )
    #
    # print('M:\n',M )
    # print('\nThe final position values are : ')
    # S = 0
    # for i,j in POS :
    #     print(i, j , '    ', test_POS[i][j]  )
    #     S += test_POS[i][j]
    #
    # print('\n SUM : \t', S)

    # solve()

print('\n======  MY GOOD SOLUTION, actually scipy does all the job with Hungarian algo behind =====')
t1  = time.time()

def solve_with_scipy(M) :

    # Normally scipy.optimize.linear_sum_assignment minimizes the cost of a matrix,
    # but if we substract from the maximum of the matrix each value we do a MAXIMIZATION of the matrix.
    # We must take care to take to take the values from the original matrix and not the modified one
    # We can also put as argument -M and thus we MAXIMIZE THE COST

    from scipy.optimize import linear_sum_assignment
    # cost = substract_matrix_maximum(M)
    # cost = deepcopy(M)

    # print(cost)
    #   The minus is there because by default it minimizes whereas we wanted to maximize.
    row_ind, col_ind = linear_sum_assignment(-M)
    S = 0
    for i in range(len(M)) :
        print('row = ' ,row_ind[i] ,'   ;  col = ' ,col_ind[i]  ,'       val = ', M[ row_ind[i] ][ col_ind[i] ]  )
        S += M[ row_ind[i] ][ col_ind[i] ]

    return print('\nResult : \t', S)


solve_with_scipy(M)

t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,6), 'ms\n\n')

# LINKS : GENERAL IDEAS

# - Can be done with Hungarian algorithm , Munkres algorithm
# - Can be done also with Traveling Salesman Problem Dynamic Programming Held-Karp algorithm
# https://www.youtube.com/watch?v=-JjA4BLQyqE
# https://stackoverflow.com/questions/4075669/hungarian-algorithm-in-python
# pip install munkres
# https://docs.scipy.org/doc/scipy-0.18.1/reference/generated/scipy.optimize.linear_sum_assignment.html


print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1,  Dynamic programming --------------------------')
t1  = time.time()

# ==== Sun, 18 Jun 2017, 15:29,  entibo, France
# Dynamic programming with bitwise keys containing row number and available columns:

import re

def solve(matrix):
	n = len(matrix)
	d = {}
	m = 1
	for i in range(n):
		b = ( ((~m) & ((1<<n)-1)) << 4 ) + n
		d[b] = matrix[-1][i]
		m <<= 1

	def f(b):
		if b in d:
			return d[b]
		best = 0
		m = 1 << (n+4-1)
		for i in range(n):
			if not (m&b):
				v = matrix[b&15][i] + f((b|m)+1)
				if v > best:
					best = v
			m >>= 1
		d[b] = best
		return best
	return f(0)

easy, hard = [
	[
		[
			int(num)
			for num in re.findall("\d+", line)
		]
		for line in open(fd).readlines()
	]
	for fd in [filename, filename]
]

# print(solve(easy))
print(solve(hard))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 2,  Dynamic Programming --------------------------')
t1  = time.time()

# ==== Sun, 23 Apr 2017, 10:47 , st_2605, Python

matrix=[[7,53,183,439,863,497,383,563,79,973,287,63,343,169,583],
[627,343,773,959,943,767,473,103,699,303,957,703,583,639,913],
[447,283,463,29,23,487,463,993,119,883,327,493,423,159,743],
[217,623,3,399,853,407,103,983,89,463,290,516,212,462,350],
[960,376,682,962,300,780,486,502,912,800,250,346,172,812,350],
[870,456,192,162,593,473,915,45,989,873,823,965,425,329,803],
[973,965,905,919,133,673,665,235,509,613,673,815,165,992,326],
[322,148,972,962,286,255,941,541,265,323,925,281,601,95,973],
[445,721,11,525,473,65,511,164,138,672,18,428,154,448,848],
[414,456,310,312,798,104,566,520,302,248,694,976,430,392,198],
[184,829,373,181,631,101,969,613,840,740,778,458,284,760,390],
[821,461,843,513,17,901,711,993,293,157,274,94,192,156,574],
[34,124,4,878,450,476,712,914,838,669,875,299,823,329,699],
[815,559,813,459,522,788,168,586,966,232,308,833,251,631,107],
[813,883,451,509,615,77,281,613,459,205,380,274,302,35,805]]

subset_sum={}

def solve( rows , col ):
    subset=[]
    st=''
    for i in rows:
        st += str(i)
    if st in subset_sum:
        return subset_sum[st]
    else:
        st=''
        for i in rows:
            rows1 = rows[:]
            rows1.remove(i)
            st += str(i)
            if col < 14:
                t = solve(rows1, col+1)
                subset.append( t+matrix[i][col] )
            elif col == 14:
                subset.append( matrix[i][col] )
        subset_sum[st] = max(subset)
    return max(subset)



rows=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
print (solve(rows,0))




t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 3,  Dynamic programming with memoization.  --------------------------')
t1  = time.time()

# === Sun, 5 Jun 2016, 04:22, azax1, USA

mat = [ [7, 53, 183, 439, 863, 497, 383, 563, 79, 973, 287, 63, 343, 169, 583],
        [627, 343, 773, 959, 943, 767, 473, 103, 699, 303, 957, 703, 583, 639, 913],
        [447, 283, 463,  29,  23, 487, 463, 993, 119, 883, 327, 493, 423, 159, 743],
        [217, 623,   3, 399, 853, 407, 103, 983,  89, 463, 290, 516, 212, 462, 350],
        [960, 376, 682, 962, 300, 780, 486, 502, 912, 800, 250, 346, 172, 812, 350],
        [870, 456, 192, 162, 593, 473, 915,  45, 989, 873, 823, 965, 425, 329, 803],
        [973, 965, 905, 919, 133, 673, 665, 235, 509, 613, 673, 815, 165, 992, 326],
        [322, 148, 972, 962, 286, 255, 941, 541, 265, 323, 925, 281, 601,  95, 973],
        [445, 721,  11, 525, 473,  65, 511, 164, 138, 672,  18, 428, 154, 448, 848],
        [414, 456, 310, 312, 798, 104, 566, 520, 302, 248, 694, 976, 430, 392, 198],
        [184, 829, 373, 181, 631, 101, 969, 613, 840, 740, 778, 458, 284, 760, 390],
        [821, 461, 843, 513,  17, 901, 711, 993, 293, 157, 274,  94, 192, 156, 574],
        [ 34, 124,   4, 878, 450, 476, 712, 914, 838, 669, 875, 299, 823, 329, 699],
        [815, 559, 813, 459, 522, 788, 168, 586, 966, 232, 308, 833, 251, 631, 107],
        [813, 883, 451, 509, 615,  77, 281, 613, 459, 205, 380, 274, 302,  35, 805] ]

def matrixSum(mat):
    dic = { () : 0 }
    n = len(mat)
    for i in range(n):
        newDic = { }
        for j in range(n):
            for key in dic.keys():
                if j in key:
                    continue
                arr = list(key)
                index = 0
                while index < len(arr) and arr[index] < j:
                    index += 1
                arr = tuple(arr[0:index] + [j] + arr[index:])
                val = mat[i][j] + dic[key]
                if arr in newDic:
                    if newDic[arr] < val:
                        newDic[arr] = val
                else:
                    newDic[arr] = val

        dic = newDic
#     print(dic)
    return dic.values()


print (matrixSum(mat))


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 4,  simulated annealing, VERY SLOW --------------------------')
t1  = time.time()

# Sat, 11 Jun 2016, 11:30, MazPino, Python , Germany
# I found the answer by "simulated annealing", which might not be the best algorithm to use.

from random import random
from math import exp
from copy import copy
from itertools import permutations

a = [[  7,  53, 183, 439, 863, 497, 383, 563,  79, 973, 287,  63, 343, 169, 583],
     [627, 343, 773, 959, 943, 767, 473, 103, 699, 303, 957, 703, 583, 639, 913],
     [447, 283, 463,  29,  23, 487, 463, 993, 119, 883, 327, 493, 423, 159, 743],
     [217, 623,   3, 399, 853, 407, 103, 983,  89, 463, 290, 516, 212, 462, 350],
     [960, 376, 682, 962, 300, 780, 486, 502, 912, 800, 250, 346, 172, 812, 350],
     [870, 456, 192, 162, 593, 473, 915,  45, 989, 873, 823, 965, 425, 329, 803],
     [973, 965, 905, 919, 133, 673, 665, 235, 509, 613, 673, 815, 165, 992, 326],
     [322, 148, 972, 962, 286, 255, 941, 541, 265, 323, 925, 281, 601,  95, 973],
     [445, 721,  11, 525, 473,  65, 511, 164, 138, 672,  18, 428, 154, 448, 848],
     [414, 456, 310, 312, 798, 104, 566, 520, 302, 248, 694, 976, 430, 392, 198],
     [184, 829, 373, 181, 631, 101, 969, 613, 840, 740, 778, 458, 284, 760, 390],
     [821, 461, 843, 513,  17, 901, 711, 993, 293, 157, 274,  94, 192, 156, 574],
     [ 34, 124,   4, 878, 450, 476, 712, 914, 838, 669, 875, 299, 823, 329, 699],
     [815, 559, 813, 459, 522, 788, 168, 586, 966, 232, 308, 833, 251, 631, 107],
     [813, 883, 451, 509, 615,  77, 281, 613, 459, 205, 380, 274, 302,  35, 805]]

def simulated_annealing() :
    max = 0
    list = [9,4,14,7,5,3,6,12,10,2,13,8,11,1,0] # Initial value
    n = 0
    ll = len(list)

    fitx = 0
    fity = 0
    ly = copy(list)
    t = 100.0 #Temperature
    lx = copy(ly)
    sx = 0
    sy = 0
    while True:
        n += 1
        sum = 0

        while True:
            aa = int(random()*ll)
            bb = int(random()*ll)
            if aa != bb:
                break
        ex = lx[aa]
        lx[aa] = lx[bb]
        lx[bb] = ex

        for i in range(15):
            sum += a[i][lx[i]]

    # Simulated annealing:

        fitx = -sum*0.1
        if fitx < fity:
            ly = copy(lx)
            fity = fitx
            sx += 1
        else:
            if exp(-(fitx-fity)/t)>random():
                ly = copy(lx)
                fity = fitx
                sy += 1
            else:
                lx = copy(ly) # reset

        if sum > max:
            max = sum
            lmax = copy(lx)
            print (n,lx,sum)
        if n % 1000000 == 0:
            print ("=====>")
            print (t,lx,fitx,sx)
            print (t,ly,fity,sy)
            print (n,max,lmax)
            t = t * 0.999
            sx = 0
            sy = 0


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 5,   --------------------------')
t1  = time.time()

# === Tue, 3 Jan 2017, 18:41, DaPhreak , Germany
# Is it considered cheating to use builtin optimization packages? With those, I only need 4 lines of Python:
# The minus is there because by default it minimizes whereas we wanted to maximize.
# Says 2.8ms execution time here (not sure how accurate the measurement is though).

from scipy import optimize
rowind, colind = optimize.linear_sum_assignment(-M)
print ( M[:,list(colind)].trace() )

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 6,   --------------------------')
t1  = time.time()

# ==== Tue, 20 Sep 2011, 09:28, snydej, USA

input = """  7  53 183 439 863 497 383 563  79 973 287  63 343 169 583
627 343 773 959 943 767 473 103 699 303 957 703 583 639 913
447 283 463  29  23 487 463 993 119 883 327 493 423 159 743
217 623   3 399 853 407 103 983  89 463 290 516 212 462 350
960 376 682 962 300 780 486 502 912 800 250 346 172 812 350
870 456 192 162 593 473 915  45 989 873 823 965 425 329 803
973 965 905 919 133 673 665 235 509 613 673 815 165 992 326
322 148 972 962 286 255 941 541 265 323 925 281 601  95 973
445 721  11 525 473  65 511 164 138 672  18 428 154 448 848
414 456 310 312 798 104 566 520 302 248 694 976 430 392 198
184 829 373 181 631 101 969 613 840 740 778 458 284 760 390
821 461 843 513  17 901 711 993 293 157 274  94 192 156 574
 34 124   4 878 450 476 712 914 838 669 875 299 823 329 699
815 559 813 459 522 788 168 586 966 232 308 833 251 631 107
813 883 451 509 615  77 281 613 459 205 380 274 302  35 805"""

matrix = [[int(n) for n in line.split(" ") if n] for line in input.strip().splitlines()]
N = len(matrix)

sums = [0] * (1 << N)
for i in range(1, len(sums)):
    cols = [c for c in range(N) if i & 1 << c]
    r = len(cols) - 1
    sums[i] = max([sums[i ^ 1 << c] + matrix[r][c] for c in cols])

print(sums[-1])

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

