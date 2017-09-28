#  Created by Bogdan Trif on 14-09-2017 , 4:11 PM.

# Mukres (Hungarian Algorithm )

'''

Following Matrix :

10 15  9
9  18  5
6  14  3

==== PROCEDURE ====
STEP 1. For each row, find the lowest element and substract it from each element in that row.

in row 1, min is 9 so we substract this value from each element on that row
in row 2, min is 5
in row 3, min is 3

Resulted matrix :

1  6  0
4  13 0
3  11 0

-------------------------
STEP 2.
For each column, find the lowest element and substract it from each element in that column.
If the lowest value is 0, don't change that column

col 1 --> lowest elem is 1, so we substract 1
col 2 --> lowest elem is 6, so we substract 1
col 3  --> we ignore the col3 as the lowest elem is 0

Resulted matrix :
0  0  0
3  7  0
2  5  0


-------------------------
STEP 3.
Cross out the o's using the minimum number of horizontal and vertical lines

2 lines in our case => 2 lines < 3  ==>  we need to reduce again


If the number of lines < n, then we must reduce the matrix again, if not go to STEP 5.

In our case we go to step 4 as we only have 2 lines.

-------------------------
STEP 4.
Find the smallest element that has not been crossed out and substract it from the rest

As we look to the matrix in step 2 we find the smallest element not crossed out as beeing 2.
So we cross it , and we substract that number from the not crossed elements.
If a number has been crossed twice , add the smallest element to it.

0  0  2
1  5  0
2  3  0

Now we can draw the lines again and we see that we can cross three lines and we can move up
to pairing workers with jobs : 3 == n


-------------------------
STEP. 5 Start pairing workers to jobs
Start with the row with 1 zero and work your way from there. When we assign a job we
eliminate that row and column.

it will result :
A = 2
B = 3
C = 1



-------------------------
FINDING THE MAXIMUM
The algorithm is the same for maximum cost, except that in the start
we find the largest number in the whole grid and substract every element
from that number

Example :
22  26  18
1   20  18
15  9   12

it wil result :

4   0   8
25  6   8
11  15  14

that you simply continue the algorithm as normal
'''

import numpy as np
from copy import deepcopy
import time

def mukrane(M) :
    L = deepcopy(M)
    # STEP 1. For each row, find the lowest element and substract it from each element in that row.
    rmins = [ min(L[i]) for i in range(len(L)) ]
    print(rmins)
    for i in range(len(L)) :
        for j in range(len(L[i])) :
            L[i][j] -= rmins[i]

    # print(' ------    Row Reduction : M\n', L)
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

    L = deepcopy( min_nr_of_crosses(L, 1 ) )
    print('\n', L )

    return L


def min_nr_of_crosses(M, iteration) :      # RECURSION !!! YEEEEEEEES !  @ 2017-09-14, 20:00
    print('\n ------ New iteration starts here -------   ', iteration ,'\n')

    ###########CASE 1  ROW PRECEDENCE FIRST   ###############
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
            N = np.insert(N, xm, values=[1111]*len(M)  ,axis=0)
            row1.append(xm)
            print('row1 = ', row1)
            cnt1+=1
        else :
            xm = np.argmax(ccount1)
            N = np.delete(N, xm , axis=1 )
            N = np.insert(N, xm, values=[1111]*len(M)  ,axis=1)
            print('CASE 1  col 1  : \t', xm)
            col1.append(xm)
            print('col1 = ', col1 )
            cnt1 += 1
        print(N)
        rcount1 = [  len(N[i]) - np.count_nonzero(N[i])  for i in range(len(N)) ]
        ccount1 = [  len(N.transpose()[i]) - np.count_nonzero(N.transpose()[i])  for i in range(len(N.transpose())) ]
        print('in while loop  rcount1, rcount1 : \t',  rcount1, ccount1  )

        N1 = deepcopy(N)
    ###########CASE 2  COL PRECEDENCE FIRST   ###############

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
            N = np.insert(N, xm, values=[1111]*len(M)  ,axis=1)
            col2.append(xm)
            print('col2 = ', col2 )
            cnt2 += 1
        else :
            xm = np.argmax(rcount2)
            print('CASE 2 row 2 xm= ',xm)
            N = np.delete(N, xm , axis=0 )
            N = np.insert(N, xm, values=[1111]*len(M)  ,axis=0)
            row2.append(xm)
            print('row2 = ', row2)
            cnt2+=1

        print(N)
        rcount2 = [  len(N[i]) - np.count_nonzero(N[i])  for i in range(len(N)) ]
        ccount2 = [  len(N.transpose()[i]) - np.count_nonzero(N.transpose()[i])  for i in range(len(N.transpose())) ]
        print('in while loop  rcount2, ccount2 : \t',  rcount2, ccount2  )

        N2 = deepcopy(N)
################# END ############

    print('how many crossing cnts : \t', ' cnt1 = ' ,cnt1 , '      cnt2 = ' ,cnt2 , ' min =  ', min(cnt1, cnt2) )
    if min(cnt1, cnt2) == len(M) :
        print(' just before it ends : \n',M)
        return M

    if cnt1 <= cnt2 :
        row, col, cnt  = row1, col1, cnt1
        N = deepcopy(N1)

    else :
        row, col, cnt  = row2, col2, cnt2
        N = deepcopy(N2)

    crossings = [ ( i,j )  for i in row for j in col ]
    print('\n=== Crossings : \t', row, col ,'     ', crossings )
    nmin = N.min()
    print('Minimum of Matrix leftover is : \t', nmin )

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
        return min_nr_of_crosses(M, iteration + 1 )



def select_positions(A , POS) :
    # Select positions :

    rcount =np.array( [  len(A[i]) - np.count_nonzero(A[i])  for i in range(len(A)) ] )
    ccount = np.array( [  len(A.transpose()[i]) - np.count_nonzero(A.transpose()[i])  for i in range(len(A.transpose())) ] )
    print(' POS  in solve rcount, ccount : ' , rcount, ccount)

    # print('np.where  i = \t' , np.where( rcount == 1)  )
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
    # print(' rcount, ccount : ' , rcount, ccount)

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

if __name__ == '__main__':
    # M = np.array([ [80, 40, 50, 46,], [40, 70, 20, 25], [30, 10 , 20, 30], [35, 20, 25, 30  ] ])
    # M = np.array([ [16, 8, 10, 9,], [8, 14, 4, 5], [4, 0 , 2, 4], [7, 4, 5, 6  ] ])

    # M = np.array([ [ 4, 12, 10, 11 ], [12, 6, 16, 15], [ 16, 20 , 18, 16 ], [13, 16, 15, 14  ] ])
    M = np.array( [ [7,  53 ,183 ,439 ,863], [497 ,383 ,563  ,79 ,973],[287 , 63 ,343 ,169 ,583], [627, 343 ,773 ,959, 943], [767 ,473 ,103 ,699, 303 ]] )
    # M_min_crosses_test =np.array(  [ [  0 , 46 ,176, 432, 656] , [418, 304, 484 ,  0, 694], [224 ,  0, 280, 106, 320], [284,   0, 430, 616, 400], [664 ,370 ,  0, 596,   0]] )
    # M = np.array([[627, 773, 959 , 957],  [960, 682, 962, 250],  [322, 972, 962, 925],  [815, 813, 459, 308]])
    print('original M : \n',M )

    N = substract_matrix_maximum(M)
    O = deepcopy(N)

    # min_nr_of_crosses(N, iteration= 1)

    print('\n------------------------')


    Q = deepcopy( mukrane( O) )
    print('\nMukrane : \n', Q )
    POS = select_positions( Q, POS =[] )

    print('M:\n',M )
    print('\nThe final position values are : ')
    S = 0
    for i,j in POS :
        print(i, j , '    ', M[i][j]  )
        S += M[i][j]

    print('\n SUM : \t', S)

    print('\n============== sci.py optimize ===============')
    t1  = time.time()

    from scipy.optimize import linear_sum_assignment
    cost = substract_matrix_maximum(M)
    # cost = deepcopy(M)

    # print(cost)

    row_ind, col_ind = linear_sum_assignment(cost)
    S = 0
    for i in range(len(M)) :
        print( row_ind[i] , col_ind[i]  ,'       ', M[ row_ind[i] ][ col_ind[i] ]  )
        S += M[ row_ind[i] ][ col_ind[i] ]

    print('\nResult : \t', S)

    # print('\n row_ind : \t' , row_ind, ' col_ind : \t' , col_ind )

    # print(  cost[row_ind, col_ind].sum() )


@2017-09-16 --> needs some fixing, It dows not work for large matrices like 15x15

    t2  = time.time()
    print('\n# Completed in :', round((t2-t1)*1000,6), 'ms\n\n')
