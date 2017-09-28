#  Created by Bogdan Trif on 10-09-2017 , 9:43 AM.
#!/usr/bin/python                   o(^_^)o         ( ͡° ͜ʖ ͡°)
# © Solved by Bogdan Trif @
#The  Euler Project  https://projecteuler.net
'''
                Flea Circus     -       Problem 213

A 30×30 grid of squares contains 900 fleas, initially one flea per square.
When a bell is rung, each flea jumps to an adjacent square at random
(usually 4 possibilities, except for fleas on the edge of the grid or at the corners).

What is the expected number of unoccupied squares after 50 rings of the bell? Give your answer rounded to six decimal places.


'''
import time, zzz
import numpy as np
import random
from copy import deepcopy

G = np.ones(( 4, 4) , dtype=int)
print(G)


choiceUL = random.choice( [( 0, 1) ,( 1, 0)  ] )
choiceUR = random.choice( [( 0, -1) ,( 1, 0)  ] )
choiceBL = random.choice( [( 0, 1) ,( -1, 0)  ] )
choiceBR = random.choice( [( -1, 0) ,( 0, -1)  ] )

choiceUProw = random.choice( [( 0, -1) ,( 0, 1) ,( 1, 0)  ] )
choiceDOWNrow = random.choice( [( 0, -1) ,( 0, 1) ,( -1, 0)  ] )
choiceLEFTcol = random.choice( [( 0, 1) ,( 1, 0) ,( -1, 0)  ] )
choiceRIGHTcol = random.choice( [( 0, -1) ,( 1, 0) ,( -1, 0)  ] )

choice_gen = random.choice( [( -1, 0) ,( 1, 0) ,( 0, 1) ,( 0, -1)  ] )

def one_jump(G) :
    l = len(G)
    H = deepcopy(G)     # copy the initial matrix

    for row in range(len(G)) :
        for col in range(len(G[row])) :
            CNT = G[row][col]           # The case when there are more than 1 fleas in a square , we use a for loop !
            if CNT > 0 :
                for i in range(CNT) :
                    # ROW 0
                    if row == 0  :
                        # choiceUL
                        if col ==0 :
                            dx, dy = random.choice( [( 0, 1) ,( 1, 0)  ] )
                            H[row+dx][col+dy] +=1
                            H[row][col] -=1
                        # choiceUR
                        elif col == l-1 :
                            dx, dy = random.choice( [( 0, -1) ,( 1, 0)  ] )
                            H[row+dx][col+dy] +=1
                            H[row][col] -=1
                        # choiceUProw
                        else :
                            dx, dy = random.choice( [( 0, -1) ,( 0, 1) ,( 1, 0)  ] )
                            # print('dx, dy = ', dx, dy,  '     row, col = ' , row, col)
                            H[row+dx][col+dy] +=1
                            H[row][col] -=1
                    # ROW n
                    if row == l-1 :
                        # choiceBL
                        if col ==0 :
                            dx, dy = random.choice( [( 0, 1) ,( -1, 0)  ] )
                            H[row+dx][col+dy] +=1
                            H[row][col] -=1
                        # choiceBR
                        elif col == l-1 :
                            dx, dy = random.choice( [( -1, 0) ,( 0, -1)  ] )
                            H[row+dx][col+dy] +=1
                            H[row][col] -=1
                        # choiceDOWNrow
                        else :
                            dx, dy = random.choice( [( 0, -1) ,( 0, 1) ,( -1, 0)  ] )
                            # print('dx, dy = ', dx, dy,  '     row, col = ' , row, col)
                            H[row+dx][col+dy] +=1
                            H[row][col] -=1
                    # COL 0 - choiceLEFTcol
                    if col == 0 and  0 < row < l-1  :
                        dx, dy = random.choice( [( 0, 1) ,( 1, 0) ,( -1, 0)  ] )
                        H[row+dx][col+dy] +=1
                        H[row][col] -=1

                    # COL n - choiceRIGHTcol
                    if col == l-1 and  0 < row < l-1  :
                        dx, dy = random.choice( [( 0, -1) ,( 1, 0) ,( -1, 0)  ] )
                        H[row+dx][col+dy] +=1
                        H[row][col] -=1

                    # choice_gen
                    elif  0< row < l-1 and 0 < col < l -1 :
                        dx, dy = random.choice( [( -1, 0) ,( 1, 0) ,( 0, 1) ,( 0, -1)  ] )
                        # print('dx, dy = ', dx, dy,  '     row, col = ' , row, col)
                        H[row+dx][col+dy] +=1
                        H[row][col] -=1
    # print('H : \n',H)
    return H

print('\n--------------------------TESTS------------------------------')
t1  = time.time()


def Monte_Carlo_custom_nr_of_jump(matrix_size , nr_of_jumps , runs ) :
    G = np.ones(( matrix_size, matrix_size) , dtype=int)
    x = len(G)
    S_zeros = 0

    for i in range(1, runs+1) :
        for j in range(nr_of_jumps) :
            Q = deepcopy(G)
            Q = one_jump(Q)
            G = deepcopy(Q)

        zero =  x*x - np.count_nonzero(Q)
        # print('zeros =  ', zero ,'    Q : \n',Q)
        S_zeros += zero
        if i % 10000 == 0 : print(i)

        K = S_zeros / runs

    print(G)
    return print('\nExpected number of free squares after  ' +str(nr_of_jumps) +  ' jumps : \t', K ,'    and ' ,runs , ' simulations' , ' for a' , 'matrix_size =' ,matrix_size )

# Monte_Carlo_custom_nr_of_jump( matrix_size=30 , nr_of_jumps = 50 , runs = 10**1 )

# https://en.wikipedia.org/wiki/Expected_value
# http://www.statisticshowto.com/probability-and-statistics/expected-value/
# https://math.stackexchange.com/questions/587959/what-is-the-expected-number-of-times-a-6-appears-when-a-fair-die-is-rolled-10-ti
# https://projecteuler.chat/viewtopic.php?f=50&t=2813&hilit=213
# https://stats.stackexchange.com/questions/2427/how-should-one-approch-project-euler-problem-213-flea-circus

#####   4 x 4 MATRIX SIMULATION   ######
# Expected number of free squares  after 1 jump : 	 4.77703   for 100.000 repetitions which is correct for 4x4 square in 20 s
# Expected number of free squares  after 2 jumps  :  5.68276
# Expected number of free squares after  3 jumps : 	 5.6749
# Expected number of free squares after  4 jumps : 	 5.67731
# Expected number of free squares after  5 jumps : 	 5.6766
# Expected number of free squares after  6 jumps : 	 5.67599            Completed in : 117.98 s

#####   30 x 30 MATRIX SIMULATION   ######
# Expected number of free squares after  50 jumps : 	 332.11      and 100 simulations  for a matrix_size = 30
# Expected number of free squares after  50 jumps : 	 332.485     and  1000  simulations  for a matrix_size = 30
# Expected number of free squares after  50 jumps : 	 332.2105     and  10000  simulations  for a matrix_size = 30

t2  = time.time()
print('\n#Completed in :', round((t2-t1), 2), 's\n\n')

print('\n================  My FIRST SOLUTION,   ===============\n')
t1  = time.time()
#
# G = np.ones((4, 4) , dtype=int)
# # print(G)
#
# def fleas_50_jumps(G):
#     x = len(G)
#     for jump in range(1, 51):
#         one_jump(G)
#         # print('\njump = ', jump, '\n',G)
#     # sum_check =  sum( [ sum(i) for i in G ] )
#     zero =  x*x - np.count_nonzero(G)
#     # print('\n',G)
#     # print('\nExpected number of unoccupied squares  = ' , zero )
#     return zero
#
# def Monte_Carlo_Simulation( nr_of_times) :
#     NR = 0
#     for i in range(nr_of_times) :
#         NR += fleas_50_jumps(G)
#     print('last frog arrangement : \n', G)
#
#     return print('\nExpected number of unoccupied squares  = ' , round(NR/nr_of_times, 6) )

# Monte_Carlo_Simulation(10**3)


# @2019-09-10 - Too slow in Python, about 80 hours : Implement in Java


def build_tranzition_matrix(matrix_size,  runs) :
    F = np.ones((matrix_size,matrix_size), dtype=float)
    G = deepcopy(F)

    for run in range( runs ) :
        F = deepcopy(G)
        for i in range(len(G)) :
            for j in range(len(G[i])) :
                if i == 0 :
                    if j==0  :  G[i][j] = F[i][j+1]*(1/3) +F[i+1][j]*(1/3)
                    if j== len(G)-1 :  G[i][j] = F[i][j-1]*(1/3) +F[i+1][j]*(1/3)
                    if j==1 :  G[i][j] = F[i][j-1]*(1/2) + F[i+1][j]*(1/4) + F[i][j+1]*(1/3)
                    if j == len(G)-2 : G[i][j] = F[i][j-1]*(1/3) + F[i+1][j]*(1/4) + F[i][j+1]*(1/2)
                    elif  1<  j < len(G)-2 :   G[i][j] = F[i][j-1]*(1/3) + F[i+1][j]*(1/4) + F[i][j+1]*(1/3)
                if i == len(G)-1 :
                    if j==0  :  G[i][j] = F[i][j+1]*(1/3) + F[i-1][j]*(1/3)
                    if j== len(G)-1 :  G[i][j] = F[i][j-1]*(1/3) + F[i-1][j]*(1/3)
                    if j==1 :  G[i][j] = F[i][j-1]*(1/2) + F[i-1][j]*(1/4) + F[i][j+1]*(1/3)
                    if j == len(G)-2 : G[i][j] = F[i][j-1]*(1/3) + F[i-1][j]*(1/4) + F[i][j+1]*(1/2)
                    elif  1<  j < len(G)-2 :   G[i][j] = F[i][j-1]*(1/3) + F[i-1][j]*(1/4) + F[i][j+1]*(1/3)
                ###########
                if i == 1 :
                    if j==0 : G[i][j] = F[i-1][j]*(1/2) + F[i][j+1]*(1/4) + F[i+1][j]*(1/3)
                    if j==len(G)-1 : G[i][j] = F[i-1][j]*(1/2) + F[i][j-1]*(1/4) + F[i+1][j]*(1/3)
                    if j==1 :  G[i][j] = F[i-1][j]*(1/3) + F[i][j+1]*(1/4) + F[i+1][j]*(1/4) + F[i][j-1]*(1/3)
                    if j == len(G)-2 :  G[i][j] = F[i-1][j]*(1/3) + F[i][j+1]*(1/3) + F[i+1][j]*(1/4) + F[i][j-1]*(1/4)
                    elif  1<  j < len(G)-2 :   G[i][j] = F[i-1][j]*(1/3) + F[i][j+1]*(1/4) + F[i+1][j]*(1/4) + F[i][j-1]*(1/4)
                if i == len(G) -2 :
                    if j==0 : G[i][j] = F[i-1][j]*(1/3) + F[i][j+1]*(1/4) + F[i+1][j]*(1/2)
                    if j==len(G)-1 : G[i][j] = F[i-1][j]*(1/3) + F[i+1][j]*(1/2) + F[i][j-1]*(1/4)
                    if j==1 :  G[i][j] = F[i-1][j]*(1/4) + F[i][j+1]*(1/4) + F[i+1][j]*(1/3) + F[i][j-1]*(1/3)
                    if j == len(G)-2 :  G[i][j] = F[i-1][j]*(1/4) + F[i][j+1]*(1/3) + F[i+1][j]*(1/3) + F[i][j-1]*(1/4)
                    elif  1<  j < len(G)-2 :   G[i][j] = F[i-1][j]*(1/4) + F[i][j+1]*(1/4) + F[i+1][j]*(1/3) + F[i][j-1]*(1/4)
                    ###########
                if 1< i < len(G)-2 :
                    if j ==0 :    G[i][j] = F[i-1][j]*(1/3) + F[i][j+1]*(1/4) + F[i+1][j]*(1/3)
                    if j == len(G)-1 : G[i][j] = F[i-1][j]*(1/3) + F[i][j-1]*(1/4) + F[i+1][j]*(1/3)
                    if j == 1 : G[i][j] = F[i-1][j]*(1/4) + F[i][j+1]*(1/4) + F[i+1][j]*(1/4) + F[i][j-1]*(1/3)
                    if j == len(G)-2 : G[i][j] = F[i-1][j]*(1/4) + F[i][j+1]*(1/3) + F[i+1][j]*(1/4) + F[i][j-1]*(1/4)
                    elif  1 <  j < len(G)-2  :    G[i][j] = F[i-1][j]*(1/4) + F[i][j+1]*(1/4) + F[i+1][j]*(1/4) + F[i][j-1]*(1/4)


    zero =  matrix_size**2 - np.count_nonzero(G)
    print('zeros =  ', zero ,'    G : \n' )
    print(G)
    ## Count probabilities > 1
    P1, Pz = 0 , 0
    for row in range(len(G)):
        for col in range(len(G[row])) :
            if G[row][col] > 1 :
                P1 += G[row][col]
            if G[row][col] < 1 :
                Pz += G[row][col]

    print('\n\nP1 = ', P1 , '     Pz = ', Pz ,'        total ', P1+Pz , '\n')

    return G

T = build_tranzition_matrix( 30 , 50 )
O = np.ones((30,30), dtype=float )

R = T.dot(O) / 30
print(R)
check, Prob = 0 , 0
for i in range(len(R)) :
    for j in range(len(R[i])) :
        check += R[i][j]
        if R[i][j] < 1 :
            Prob += 1

print('\n Check value : ', check ,'     Prob = ', Prob)



t2  = time.time()
print('\nCompleted in :', round((t2-t1),2), 's\n\n')


# print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
# print('\n--------------------------SOLUTION 1,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 2,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 3,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 4,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 5,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 6,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 7,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 8,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 9,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 10,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 11,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 12,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')

