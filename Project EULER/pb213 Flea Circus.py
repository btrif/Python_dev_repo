#  Created by Bogdan Trif on 10-09-2017 , 9:43 AM.
#!/usr/bin/python                   o(^_^)o         ( ͡° ͜ʖ ͡°)
# © Solved by Bogdan Trif @     Completed on Wed, 11 Oct 2017, 18:52
#The  Euler Project  https://projecteuler.net
'''
                Flea Circus     -       Problem 213

A 30×30 grid of squares contains 900 fleas, initially one flea per square.
When a bell is rung, each flea jumps to an adjacent square at random
(usually 4 possibilities, except for fleas on the edge of the grid or at the corners).

What is the expected number of unoccupied squares after 50 rings of the bell?
Give your answer rounded to six decimal places.


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

def one_jump_Monte_Carlo(G) :
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

print('One jump :\n' ,one_jump_Monte_Carlo(G) )




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

T = build_tranzition_matrix( 4 , 1 )
# O = np.ones((30,30), dtype=float )

# R = T.dot(O) / 30
# print(R)
# check, Prob = 0 , 0
# for i in range(len(R)) :
#     for j in range(len(R[i])) :
#         check += R[i][j]
#         if R[i][j] < 1 :
#             Prob += 1
#
# print('\n Check value : ', check ,'     Prob = ', Prob)


print('\n--------------------------TESTS------------------------------')
t1  = time.time()


def Monte_Carlo_custom_nr_of_jump(matrix_size , nr_of_jumps , runs ) :
    G = np.ones(( matrix_size, matrix_size) , dtype=int)
    x = len(G)
    S_zeros = 0

    for i in range(1, runs+1) :
        for j in range(nr_of_jumps) :
            Q = deepcopy(G)
            Q = one_jump_Monte_Carlo(Q)
            G = deepcopy(Q)

        zero =  x*x - np.count_nonzero(Q)
        # print('zeros =  ', zero ,'    Q : \n',Q)
        S_zeros += zero
        if i % 10000 == 0 : print(i)

        K = S_zeros / runs

    print(G)
    return print('\nExpected number of free squares after  ' +str(nr_of_jumps) +  ' jumps : \t', K ,'    and ' ,runs , ' simulations' , ' for a' , 'matrix_size =' ,matrix_size )

# Monte_Carlo_custom_nr_of_jump( matrix_size=30 , nr_of_jumps = 2 , runs = 10**2 )

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


# G = np.ones((4, 4) , dtype=int)
# # print(G)
#
# def fleas_50_jumps(G):
#     x = len(G)
#     for jump in range(1, 51):
#         one_jump_Monte_Carlo(G)
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


t2  = time.time()
print('\n#Completed in :', round((t2-t1), 2), 's\n\n')

print('\n================  My FIRST SOLUTION,  5 min ===============\n')
t1  = time.time()



def one_flea_jumps(matrix_size, pos , nr_of_jumps) :
    '''  Computes the probabilities of  a single feel to reach squares after a certain number of jumps '''
    F = np.zeros((matrix_size,matrix_size), dtype=float)
    F[pos[0] ][pos[1]] = 1
    G = deepcopy(F)

    for run in range( nr_of_jumps ) :
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

    return G


def solution_Flea_Circus(dim, jumps ):
    ''' Computes step by step the probabilities

    :param dim: dimension of the matrix
    :param jumps: number of jumps
    :return: Expected number of empty squares
    '''
    X = np.ones((dim,dim), dtype=float )

    # Takes a flea at a time and use the one_flea_jumps function to perform the probability
    # to be on a certain square
    for x in range(len(X)) :
        for y in range(len(X)) :
            print('x, y = ', x, y )

            T = one_flea_jumps( dim , ( x, y ), jumps )
            # print('\nT: \n ',T )
            U = np.zeros((dim,dim), dtype=float )

            # Takes each square and calculates probability to NOT be on that square 1-P
            # Stores the values in the matrix U
            for i in range(len(T)):
                for j in range(len(T[i])):
                    U[i][j] = 1 - T[i][j]

            # print('U :\n ',U)

            #  Matrix X is used to accumulate the stored probabilities from matrix U
            for i in range(len(U)):
                for j in range(len(U[i])):
                    X[i][j] = X[i][j] * U[i][j]

            # print('\nX :\n', X)
    # The EXPECTED NUMBER of Free Squares represents the sum of all X matrix probabilities
    FS = 0
    for k in range(len(X)) :
        FS+= sum(X[k])

    return print('\nExpected number of free squares  after ' + str(jumps) +' jumps  = ', round(FS, 6) )

# solution_Flea_Circus(30, 50)

t2  = time.time()
print('\nCompleted in :', round((t2-t1),2), 's\n\n')

# ====== GENERAL IDEAS =============
# === Mon, 5 Jan 2009, 08:38, tntncsu, USA
# Using markov chains, I created my 900*900 probability  matrix mostly by hand,
# setting the corner values and then looping through the innner and edge values seperately.
# the rest was just matrix exponentiation and addition



print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n---------------------- SOLUTION 1,  MARKOV CHAINS, Must study it  --------------------------')
t1  = time.time()

# === Mon, 12 Jul 2010, 18:42, johnlcf, Honk Kong
# I buy a book to study about Markov Chain and solve this question finally!
# Project Euler is really inspiring that make me pick up something that I missed in University:



from numpy import *

def copy2DArray(a):
    b = []
    for row in a:
        b.append(row[:])
    return b

def dotPower(m, n):
    cache = []*100

    currN = 1
    currAns = m
    cache.append(copy2DArray(m))
    d = 1

    while 2 ** d < n:
        currAns = dot(currAns, currAns)
        print ("dot", currN, currN)
        currN = 2 ** d
        cache.append(copy2DArray(currAns))
        d += 1

    while n - currN != 0:
        if n - currN >= 2 ** d:
            currAns = dot(currAns, cache[d])
            print ("dot", currN, 2**d)
            currN += 2 ** d
        else:
            d -= 1

    return currAns

matrix = zeros([900, 900])

for i in range(0,30):
    for j in range(0,30):
        currPos = i*30 + j

        choice = 2
        if i > 0 and i < 29:
            choice += 1
        if j > 0 and j < 29:
            choice += 1

        if i > 0:
            newPos = (i-1)*30 + j
            matrix[currPos][newPos] = 1.0/choice
        if i < 29:
            newPos = (i+1)*30 + j
            matrix[currPos][newPos] = 1.0/choice
        if j > 0:
            newPos = i*30 + j-1
            matrix[currPos][newPos] = 1.0/choice
        if j < 29:
            newPos = i*30 + j+1
            matrix[currPos][newPos] = 1.0/choice

ans = 0
matrix50 = dotPower(matrix, 50)

for j in range(0,30*30):
    currAns = 1
    for i in range(0,30*30):
        currAns *= (1 - matrix50[i][j])
    ans += currAns

print( round(ans, 6))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')


print('\n--------------------------SOLUTION 2,   --------------------------')
t1  = time.time()

# === Thu, 2 Apr 2015, 20:56, Tommy O, Norway
import matplotlib.pyplot as plt
import numpy as np
from numpy.linalg import matrix_power
import time

def inside(pos, size):
    '''
    Is the positin inside the grid?
    '''
    if pos[0] >= size or pos[1] >= size:
        return False
    if pos[0] < 0 or pos[1] < 0:
        return False
    return True

class Grid(object):
    def __init__(self, size):
        self.board = [[1 for i in range(size)] for i in range(size)]
        self.size = size
        self.iterations = 0 #So we don't have to recompute exponential of matrix
        self.matpow = 0 #So we don't have to recompute exponential of matrix

    def probability(self, row, col):
        '''
        Given a pair of coordinates, this method returns
        positions a flea can move to, and the probability.
        '''
        positions = [(row-1, col),(row+1, col),(row, col-1),(row, col+1)]
        availablePositions = [pos for pos in positions if inside(pos, self.size)]
        uniformProb = 1/len(availablePositions)
        return uniformProb, availablePositions

    def movementsMatrix(self):
        '''
        Returns the matrix with the movement mapping.
        '''
        mat = np.zeros((self.size**2, self.size**2))
        i = 0
        for row in range(self.size):
            for col in range(self.size):
                uniformprob, positions = self.probability(row, col)
                for pos in positions:
                    x, y = pos
                    mat[i,y+x*self.size] = uniformprob
                i+= 1
        return mat

    def probmap_onefly(self, iterations, startpos=(0,0), invert=False):
        '''
        Gives the probability map for a fly, given the numer of iterations (moves),
        the initial position, and whether or not the probability is inverted[so that it shows
        the probability of a fly NOT being in that square].
        '''
        if iterations != self.iterations:
            self.iterations = iterations
            movementsMatrix = self.movementsMatrix()
            self.matpow = matrix_power(movementsMatrix,self.iterations)

        rowvector = np.zeros((1,self.size**2))
        rowvector[0,startpos[0]*self.size+startpos[1]] = 1
        propmap_part = np.dot(rowvector, self.matpow)
        returnFormatted = np.zeros((self.size, self.size))
        i = 0

        for row in range(self.size):
            for col in range(self.size):
                returnFormatted[row,col] = propmap_part[0,i]
                i+= 1

        if invert:
            return 1- returnFormatted
        else:
            return returnFormatted

    def probmap(self, iterations, invert=False):
        '''
        Get the map for every position. It's just adding every initial fly map
        over each other. That is, a superposition.
        '''
        if iterations != self.iterations:
            self.iterations = iterations
        complete_map = np.ones((self.size, self.size))
        c = 0
        for x in range(self.size):
            for y in range(self.size):
                complete_map *= self.probmap_onefly( iterations, startpos=(x,y), invert=invert)
                c += 1
        return complete_map

grid = Grid(30)

probabilitymap = grid.probmap_onefly(50, startpos=(15,15))

#Single flea
plt.figure()
plt.pcolor(probabilitymap)
plt.colorbar()
plt.show()

#The full probability "map"
plt.figure()
fullmap = grid.probmap(50, invert = True)
print( np.sum(fullmap))
plt.pcolor(fullmap)
plt.colorbar()
plt.show()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')


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

