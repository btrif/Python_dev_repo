#!/usr/bin/python
# Solved by Bogdan Trif @   Completed on Tue, 29 Nov 2016, 16:57
#The  Euler Project  https://projecteuler.net
'''
                                Dice Game       -       Problem 205

Peter has nine four-sided (pyramidal) dice, each with faces numbered 1, 2, 3, 4.
Colin has six six-sided (cubic) dice, each with faces numbered 1, 2, 3, 4, 5, 6.

Peter and Colin roll their dice and compare totals: the highest total wins. The result is a draw if the totals are equal.

What is the probability that Pyramidal Pete beats Cubic Colin?
Give your answer rounded to seven decimal places in the form 0.abcdefg

'''
import time
from random import randint
from itertools import count, permutations, combinations_with_replacement, combinations



print('\n--------------------------AUTOMATED TESTS------------------------------')

print(randint(1,6),'\n')
P = list(permutations([2,1,1,1,1,1],6))
print('Perm Test : ', len(P) ,P)

# p_cnt, c_cnt = 0, 0
# for i in range(1,1000):
#     P = [randint(1,4), randint(1,4), randint(1,4), randint(1,4), randint(1,4), randint(1,4), randint(1,4), randint(1,4), randint(1,4)]
#     C = [randint(1,6), randint(1,6), randint(1,6), randint(1,6), randint(1,6), randint(1,6)]
#     if sum(P) > sum(C) :
#         p_cnt+=1
#     if sum(P) < sum(C) :
#         c_cnt+=1
#     elif sum(P) == sum(C) :
#         p_cnt += 0.5
#         c_cnt += 0.5
#     print(str(i)+'.     P :  ' , p_cnt/i ,'       C : ' ,c_cnt/i ,  '         P ', P, sum(P),'        C  ',C , sum(C),  '     ',p_cnt/i + c_cnt/i)
#     if i % 1e6 == 0: print(i)
#     # if i == 2e7 :
#     #     print(str(i)+'.     P :  ' , p_cnt/i ,'       C : ' ,c_cnt/i , p_cnt/i + c_cnt/i   , '         P ', P, sum(P),'        C  ',C , sum(C),  '     ',p_cnt/i + c_cnt/i)
#     #     break




# Tried :  P :   0.608528675        C :  0.391471325 1.0,





print('\n================  My FIRST SOLUTION,   ===============\n')
t1  = time.time()
# Must do a recursive function to generate  https://wizardofodds.com/gambling/dice/2/


# D66 = np.zeros((6 , 36), dtype=int)
D66 =  [[0 for x in range(36)] for x in range(6)]
for i in range(6) : D66[0][i] = 1

for i in range(1, 6):
    for j in range(i , 6*i+6):
        if j <= 6 :
            D66[i][j] += sum(D66[i-1][ :j  ])
        if j >6 :
            D66[i][j] += sum(D66[i-1][ j-6 : j ])

# for i in range(len(D66)) : print(D66[i])
print('The coefficients of 6D6 : ',D66[5])

P66=[]
for i in range(36) :  P66.append(D66[5][i]/6**6)
print('\nProbabilities 6 Die of 6 : ',sum(P66) ,P66)


print('------------------------')

D49 =  [[0 for x in range(36)] for x in range(9)]
for i in range(4) : D49[0][i] = 1

for i in range(1, 9):
    for j in range(i , 4*i+4):
        if j <= 4 :
            D49[i][j] += sum(D49[i-1][ :j  ])
        if j >4 :
            D49[i][j] += sum(D49[i-1][ j-4 : j ])

for i in range(len(D49)) : print(D49[i])

P49=[]
for i in range(36) :  P49.append(D49[8][i]/4**9)
print('\nProbabilities 9 Die of 4 : ',sum(P49) ,P49)

S, S2 = 0, 0
for i in range(5,36):    print(str(i+1)+'.   ' ,P66[i], '     ' , P49[i] )

# The idea is that the following :
# example : the 6 -sided hits 10. Q: What's the probability that the 4 sided wins ?
# Answer: you must multiply all the bigger >10 probabilities of the 4-sided with the 10 from 6-sided and
# add them together. Of course they must be normalized !



for i in range(5,36):
    print('----------   '+str(i+1)+'   ---------------')
    for j in range(i+1, 36):
        S += P49[j]*P66[i]
        S2 += D49[8][j]*D66[5][i]
        print('P49  '+str(j+1)+' = ' , D49[8][j] , ' ;    P66  '+str(i+1)+' = ',D66[5][i],'    ', D49[8][j]*D66[5][i] )


print('\nProbability that 9 Pyramidal Dices  beats 6 Cubic Dices : ', round(S,7), S2/(4**9*6**6))   # Answer :   0.5731441


# It works, just uncomment it  !!!

print('\n------------------------    PLOTTING   -----------------------')

def plot() :
    import numpy as np
    import matplotlib.pyplot as plt

    fig = plt.figure(num=None, figsize=(16, 10), dpi=80, facecolor='w', edgecolor='#33ff88')

    ax = fig.add_subplot(1,1,1)

    ## the data
    N = 36
    D66 = P66
    D49 = P49

    ## necessary variables
    ind = np.arange(N)                # the x locations for the groups
    width = 1                      # the width of the bars

    ## the bars
    rects1 = ax.bar(ind, D66, width, color='blue' , alpha=0.7 )
    rects2 = ax.bar(ind, D49, width, color='red', alpha=0.5)

    # axes and labels
    ax.set_xlim(-width , len(ind)+width)
    ax.set_ylim(0, 0.12)
    ax.set_ylabel('Scores')
    ax.set_title('Probabilities ')
    xTickMarks = [str(i) for i in range(1,37)]
    ax.set_xticks(ind+width)
    xtickNames = ax.set_xticklabels(xTickMarks)
    plt.grid(True)

    plt.setp(xtickNames, rotation=15, fontsize=14)

    ## add a legend
    ax.legend( (rects1[0], rects2[0]), ('D66', 'D49') )
    # ax.legend( rects1, 'D66' )
    # fig = plt.gcf()
    # fig.set_size_inches(20, 15)
    plt.show()

plot()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


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
