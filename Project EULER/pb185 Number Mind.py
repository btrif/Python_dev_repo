#!/usr/bin/python
# Solved by Bogdan Trif @
#The  Euler Project  https://projecteuler.net
'''
Number Mind     -   Problem 185

The game Number Mind is a variant of the well known game Master Mind.

Instead of coloured pegs, you have to guess a secret sequence of digits.
After each guess you're only told in how many places you've guessed the correct digit.
So, if the sequence was 1234 and you guessed 2036, you'd be told that you have one correct digit;
however, you would NOT be told that you also have another digit in the wrong place.

For instance, given the following guesses for a 5-digit secret sequence,

                                        90342 ;     2 correct
                                        70794 ;     0 correct
                                        39458 ;     2 correct
                                        34109 ;     1 correct
                                        51545 ;     2 correct
                                        12531 ;     1 correct

The correct sequence 39542 is unique.

Based on the following guesses,

                                5616185650518293 ;      2 correct
                                3847439647293047 ;      1 correct
                                5855462940810587 ;      3 correct
                                9742855507068353 ;      3 correct
                                4296849643607543 ;      3 correct
                                3174248439465858 ;      1 correct
                                4513559094146117 ;      2 correct
                                7890971548908067 ;      3 correct
                                8157356344118483 ;      1 correct
                                2615250744386899 ;      2 correct
                                8690095851526254 ;      3 correct
                                6375711915077050 ;      1 correct
                                6913859173121360 ;      1 correct
                                6442889055042768 ;      2 correct
                                2321386104303845 ;      0 correct
                                2326509471271448 ;      2 correct
                                5251583379644322 ;      2 correct
                                1748270476758276 ;      3 correct
                                4895722652190306 ;      1 correct
                                3041631117224635 ;      3 correct
                                1841236454324589 ;      3 correct
                                2659862637316867 ;      2 correct

Find the unique 16-digit secret sequence.

'''
import time
import numpy as np

# filePath = r'pb185 Number Mind.txt'
filePath = r'pb185 Number Mind_test.txt'

def build_matrices_M_and_Z(filepath):
    M, Z = np.array([], dtype=int),  np.array([], dtype=int )

    Q = [(line.rstrip('\n')).split(';') for line in open(filePath)]

    for i in range(len(Q)) :
        n1 = str(Q[i][0].strip())
        n2 = int(Q[i][1].split()[0])
        # print( n1  ,[int(i) for i in list(n1)] , n2 )       # [ int(i) for i in list(n1) ]
        # print(M)
        if i == 0 :
            M = np.column_stack( [int(i) for i in list(n1)])   #  append([int(i) for i in list(n1)])
            Z = np.append(Z, n2 )
        else :
            M = np.row_stack([M, [int(i) for i in list(n1)] ])
            Z = np.append(Z, n2  )
        # V[i+1] = [ [int(i) for i in list(n1)] , int(n2)  ]
    return M, Z

M, Z = build_matrices_M_and_Z(filePath)

print('\nM potential matrix : \n', M)
# for m in range(len(M)):  print(M[m])
print('\nZ Check Matrix : \t', Z)



print('\n--------------------------TESTS------------------------------')
# 2017-08-25, 17:00
# Testing the DOT PRODUCT - Matrix Multiplication ---> Attenstion A*B is not the DOT PRODUCT

test = None
if test == True :
    A = np.array([ [ 2,0],[0, 1]], int)
    B = np.array([2,1], int)

    print('Dot product I : \t' ,A.dot(B))
    print('Dot product II : \t' ,np.dot(A,B))
    print( 'Element : A1,0 : \t',A[1][0])


print('\n================  My FIRST SOLUTION,   ===============\n')
# t1  = time.time()

# Building the X initial matrix which is the correct mapping of the values :
# We use the following model to map the correct values in a matrix :
# a_10,1 + a_1,2 + a_4,3 + a_5,4 + a_3,5 = 2
# a_8,1 + a_1,2 + a_8,3 + a_10,4 + a_5,5 = 0
# a_4,1 + a_10,2 + a_5,3 + a_6,4 + a_9,5 = 2
# a_4,1 + a_5,2 + a_2,3 + a_1,4 + a_10,5 = 1
# a_6,1 + a_2,2 + a_6,3 + a_5,4 + a_6,5 = 2
# a_2,1 + a_3,2 + a_6,3 + a_4,4 + a_2,5 = 1

def build_initial_matrix_X(M) :
    X = np.zeros((5, 10), int)

    for i in range(len(M) ) :
        for j in range(len(M[i])) :
            # print(M[i][j])
            X [j] [M [i][j]]  = 1
    return X

X = build_initial_matrix_X(M)
# print('X MAIN Matrix obtained from the specified conditions : \n', X, '\n',X.transpose() )


# Now once we constructed the main X matrix we eliminate the elements which =0  from the above statement.
# In the case we study a_7,0 + a_0,1 + a_7,2 + a_9,3 + a_4,4 = 0 so we eliminate those elements !
print('\nEliminate the 0 elements to simplify the matrix : ,')

def clean_main_matrix_X_of_zero_elements( X, Z, M):
    ''':Description: If 0 elements appear in the Z Check Matrix, then the matrix X
    is cleaned from the elements which appear in the column corresponding to the Z entry.
    :param X: Main Matrix
    :param Z: Check Matrix
    :param M: potential Matrix
    :return: X matrix     '''
    for i in range(len(Z)) :
        # print(Z[i])
        if Z[i] == 0 :
            row = M[i]
            print('row = ' ,row )
            row_entire = M[i]
            # for j in range(len(M[i])) :
            C = M.transpose()
            # print(C , len(C))
            for k in range( len(C ) ) :
                # print(str(k) ,'.            ' ,C[k] )
                A = C[k]
                # print( ' check value = ', row[k], end='   ')
                for l in range(len(A) ) :
                    # print(' ===' ,l)
                    # print('<-',  A[l], end= '  ; '   )
                    if A[l] == row[k] :
                        # print('row = ', row[k],'    col = ', k )
                        X[k] [ row[k]] = 0

    return X

# X = clean_main_matrix_X_of_zero_elements(X, Z, M)
# print('\nX INITIAL main cleaned matrix : \n', X , '\n',X.transpose() ,'\n--------------------'  )

def clean_M_clean_Z(M, Z):
    for z in range(len(Z)) :
        if Z[z] == 0 :
            Ref = M[z][:]
            # print(Ref)
            for i in range(len(M)):
                for j in range(len(M[i])) :
                    if Ref[j] == M[i][j] :
                        M[i][j] = 10

    # print('M matrix : \n',M,'\n\nZ :', Z)
    print( M[: , 0] )
    return M, Z

print('--------- Clean M & Clean Z :---------- \nM Matrix :\n', clean_M_clean_Z(M, Z)[0],'\n\n Z: ', clean_M_clean_Z(M,Z)[1] )

def check_complete_M_Z(M, Z ):
    def count_10s_in_M(M):
        sizeM, S10 = M.shape, 0
        print('Size of M :\t ',sizeM)
        for i in range(len(M)):
            print(M[i], np.count_nonzero( M[i] == 10)  )
            S10 += np.count_nonzero( M[i] == 10)
        if S10 == (sizeM[0] * sizeM[1] ) - sizeM[1] :
            return True

    count_10s_in_M(M)

    if np.sum(Z) == 0 and count_10s_in_M(M) :
        return True

    return False

print('\ncheck_complete_main_matrix : \t',check_complete_M_Z(M, Z),'\n------------------------' )

# M1 = np.array([[1, 10, 10],[10,4,10],[10,10,10], [10, 10, 2]])
# Z1 = np.array([0, 0, 0, 0])
# print('\ncheck_complete_main_matrix : \t',check_complete_M_Z(M1, Z1),'\n------------------------' )

def clean_main_X_on_select_and_adjust_Z( X, Z, M, pos ):
    ''':Description:  When a position is chosen that element is removed from matrix X
    and also is decremented in matrix Z. Moreover if that elem appears multiple times
    the elements in matrix Z are deacreased accordingly.
    :param X: Main Matrix
    :param Z: Check Matrix
    :param M: potential Matrix
    :param pos:  position which is chosen in the MAIN Matrix X
    :return:  X & Z matrices     '''
    row, nr = pos
    zero = np.zeros([1,10])
    # print(X[ : , row])
    X = np.delete(X, row, axis=0)
    X = np.insert(X, row, values=zero, axis=0)
    print('before cleaning X : \n',X)
    X[row][nr] = 1
    # print('\n',X)
    # print('\n',M[ : , col ])
    # print(Z)
    for i in range(len( M[:,row] )) :
        if M[:, row ][i] == nr :
            Z[i] -= 1
    # print(Z)
    return X, Z

# X1, Z1 = clean_main_X_on_select_and_adjust_Z( X, Z, M, [ 0 , 3] )
# print(' Verification clean_main_X1_on_select_and_adjust_Z1 : \n', X1, ' \n\nZ1 : ', Z1 ,'\n--------------------------' )



# @ 2017-08-28
#
# I tried this
# https://mathproblems123.wordpress.com/2017/01/28/linear-programming-1-project-euler-185/
# https://www.mathworks.com/help/optim/ug/linprog.html#buus4rj-1
# with linprog but did not work
#
# I need to rewrite some functions :(
#
# # A good approach seems the following :
# https://codereview.stackexchange.com/questions/54138/improving-efficiency-of-project-euler-185-16-place-mastermind
#
# # Another variant is with SIMULATED ANEALING
# http://euler.stephan-brumme.com/185/
# Let's try to translate the C++ code found here :
#
# https://en.wikipedia.org/wiki/Simulated_annealing
# https://github.com/perrygeo/simanneal

# def find_empty_location(X, pos):        # FIND EMPTY LOCATION
#
#     for row in range(9):
#         for col in range(9):
#             if(X[row][col]==0):
#                 l[0]=row
#                 l[1]=col
#                 return True
#     return False

def find_next_avail_pos(X, cur_pos):
    # print ( ( X.shape[0]-1, X.shape[1]-1) )
    # print(X)
    X = X.transpose()
    if tuple(cur_pos) == ( X.shape[0]-1, X.shape[1]-1) :
        if X[cur_pos[0]][cur_pos[1]] == 1 :
            return True #return (row, col)

    else :
        row, col = cur_pos[0], cur_pos[1]
        while (row, col) < ( X.shape[0]-1, X.shape[1]-1) :
            # Advance one column :
            if col < X.shape[1]-1 :
                row, col = row, col+1
                if X[row, col] == 1 :
                    print('X , row, col : ', X[row][col],'\trow , col =  ' ,row, col )
                    return True #(row, col)
            # Advance one row :
            elif col == X.shape[1]-1 :
                row, col  = row+1 , 0
                if X[row, col] == 1 :
                    print('X , row, col : ', X[row][col] ,'\trow , col =  ', row, col)
                    return True #(row, col)
            # THE END of the matrix
            if (row, col) == ( X.shape[0]-1, X.shape[1]-1) :
                if X[row, col] == 1 :
                    print('\n FINAL  position and shape : \t',cur_pos, X.shape )
                    return True #(row, col)
            # print(' row, col = ',row, col)

    return False


# a, b = 1,2
# if (a ==b):  print(' equal')
# elif (a > b) : print('a is greater')
# else : print('b is greater')
# pos = [0, 0]
# print( '\nfind_avail_pos : \t' ,find_next_avail_pos(X, [0,0] ) )

############ Main solution ################

def solve_number_mind(X, Z, M):
    clean_main_matrix_X_of_zero_elements( X, Z, M)
    clean_main_matrix_X_of_zero_elements( X, Z, M)
    row = 0
    X_t = X.transpose()
    for i in range(len( X_t[row] )) :
        if X_t[row][i] == 1 :
            print('col =  ', str(i), X_t[row][i] )

    print('\n',X)

    # pos = [0, 0]
    # if not find_next_avail_pos(X, pos) :
    #     print('TRUE !!!!!!!!!!!')
    #     return True
    #
    #     # We assign list values to row and col that we got from find_next_empty_location function
    # row, col = pos[0], pos[1]
    # print('row, col = ', row, col )
    #
    # for row in range(len( X.transpose()[col] )) :
    #     if X[row][col] == 1 :
    #         num = col
    #         print('>>> ',X[row][col],'     ', num)


# solve_number_mind(X, Z, M)
# print(X)


# print('\n',np.sum(Z))










# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


# print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
# print('\n--------------------------SOLUTION 1,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
# print('\n--------------------------SOLUTION 2,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
# print('\n--------------------------SOLUTION 3,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
# print('\n--------------------------SOLUTION 4,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
# print('\n--------------------------SOLUTION 5,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 6,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
