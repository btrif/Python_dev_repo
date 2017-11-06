#!/usr/bin/python
# Solved by Bogdan Trif @   Completed on Fri, 1 Sep 2017, 22:15
#The  Euler Project  https://projecteuler.net
'''
                            Path sum: three ways        -       Problem 82
NOTE: This problem is a more challenging version of Problem 81.

The minimal path sum in the 5 by 5 matrix below, by starting in any cell in the left column and
finishing in any cell in the right column, and only moving up, down, and right, is indicated in red and bold;
the sum is equal to 994.

                           131 673 234 103 18
                           201 96  342 965 150
                           630 803 746 422 111
                           537 699 497 121 956
                           805 732 524 37  331

Find the minimal path sum, in matrix.txt (right click and "Save Link/Target As..."), a 31K text file containing a 80 by 80 matrix,
from the top left to the bottom right by only moving right and down.
'''

import time
from numpy import transpose, zeros
from copy import copy, deepcopy

filename = "pb081_matrix.txt"
def load_file(filename):
    with open(filename) as f:
        matrix = [list(map(int, line.split(","))) for line in f.readlines()]
    f.close()
    return matrix

matrix = load_file(filename)
matricea = deepcopy(matrix)

for i in matrix :    print(i)

# mT = transpose(matrix)
# print('\n',mT)


print('\n----------------- TEST FOR Smaller MaTriX -----------------------\n')

# m =[[150, 650, 250, 100, 50], \
#        [200, 100,  350, 950, 150],\
#        [650, 800, 750, 400, 100],\
#        [550, 700, 500, 150, 950],\
#        [800, 750, 500, 50,  350]]

M=  [[131, 673, 234, 103, 18], \
        [201, 96,  342, 965, 150],\
        [630, 803, 746, 422, 111],\
        [537, 699, 497, 121, 956],\
        [805, 732, 524, 37,  331]]

# M = [ [100,	100,	90,	100,	100],
#         [95,	   80	,   105,	110,	 100],
#         [100,	   20,	   150,	115,	100],
#         [125,   	95,	35,	100,	100],
#         [90,    	95,	100,	95,	100] ]

print('------------------------------------The Original Matrix --------------')
for i in range(len(M)): print(M[i])

print('\n----------------------------------- The Computed PATH ---------------------')

# M = [row[:] for row in mT]     # Making a copy of transposed matrix
# M = deepcopy(mT)          # deepcopy for cloning the transposed matrix
# B = zeros((len(M), len(M)), dtype=int)        # numpy Create a zeroed Matrix the same size
# print(B)


M_test = [ [100,	100,	90,	100,	100],
                    [95,	80	,   105,	110,	100],
                    [100,	20,	150,	115,	100],
                    [125,	95,	35,	100,	100],
                    [90,	95,	100,	95,	100] ]

# min_three_ways_path(M_test)
# min_three_ways_path(matrix)

# Characters :  ∟ ∟  ┐ ┐  ┐ ∟  ┌ ┌ ┐ _|



print('\n================  My FIRST SOLUTION,  DP ===============\n')
t1  = time.time()

def three_ways_path( matrix ) :

    M = matrix
    gridSize = len(M)
    sol = [0 for i in range(gridSize)]

    #   initialise solution :
    for i in range(0, gridSize ) :
        sol[i] = M[i][gridSize - 1]

    for i in range(gridSize-2,-1, -1 ) :
        #   Traverse down :
        sol[0] += M[0][i]
        for j in range(1, gridSize) :
           sol[j] = min ( sol[j - 1] + M[j][i], sol[j] + M[j][i] )

        #   Traverse up :
        for j in range(gridSize -2, -1, -1) :
            sol[j] = min( sol[j], sol[j+1] + M[j][i] )

    print('The Complete path is : ',sol)
    return print('\nThe minimal path is : \t', min(sol))

three_ways_path(matrix)             #       Answer  : 260324


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1, Dynamic Programming   --------------------------')
t1  = time.time()

# ====== Fri, 25 Aug 2017, 00:18 FergusonTG  ,
# Another python solution, using DP and sweeping backwards from right to left. Comments in line
#
# Biggest problem for me was realising I had to scan downwards and upwards on each column in order to
# get costs for moving down and up respectively.


import math

def costValue(row, col):
    if row<0 or row > len(costs)-1:
        return math.inf
    if col < 0 or col > len(costs[row])-1:
        return math.inf
    return costs[row][col]

def leastCost () :
    # start at last column: this is copy of matrix column
    for row in range(len(matrix)): costs[row][-1] = matrix[row][-1]

    # next, look to the previous column and get cost of coming
    # from the left
    # then we go down looking for cost of moving upards
    # and afterwards sweep up looking at cost of moving down
    for col in range(len(matrix[0])-2,-1,-1):
        # scanning downwards
        for row in range(len(matrix)):
            # cost of going right
            costs[row][col] = matrix[row][col] + costValue(row,col+1)
            # cost of going up
            costs[row][col] = min(costValue(row,col),
                        matrix[row][col]+costValue(row-1,col))
        # scanning upwards
        for row in range(len(matrix[row])-1,-1,-1):
            costs[row][col] = min(costValue(row,col),
                        matrix[row][col]+costValue(row+1,col))
        # helps with debugging
        # showCosts()

    return min(row[0] for row in costs)

def showCosts():
    for row in costs:
        print(row)
    print()


if __name__ == "__main__":
    with open("pb081_matrix.txt","r") as matrixFile:
        matrix = [[int(w) for w in line.split(",")] for line in matrixFile]


    costs = [[math.inf]*len(row) for row in matrix]

    answer = leastCost()
    print(answer)


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 2,  --------------------------')
t1  = time.time()

# ==== Tue, 15 Nov 2016, 01:14, rtoscani, Netherlands

# First, the matrix is stored in a nested (2D-)list.
# Then, starting with the second column and working top-down, each subsequent value is gradually replaced
# by a minimum path sum value. For each cell, this is done by determining all possible sums through adjacent cells underneath,
# until one cell in the neighbouring column on the left is reached (which is also included in the sum).
# Of the values on top, only the one immediately above is added, this is already a replaced minimal value!
# The smallest of the sums found is then used to replace the original value in the cell.
# This procedure is repeated in the next column and so on until the last column is reached.
# Finally, the smallest value in the last column yields the answer to the problem.


minimum = 1000000
matrix = []
f = open(filename,'r')
for line in f.readlines():
    if not line:
        break
    lis = [int(i) for i in line.split(',')]
    matrix.append(lis)
f.close()
for i in range(1,len(matrix[0])):
    for j in range(len(matrix)):
        min_sum = minimum
        col_sum = 0
        for k in range(j,len(matrix)):
            col_sum += matrix[k][i]
            _sum = col_sum + matrix[k][i-1]
            if _sum < min_sum:
                min_sum = _sum
        if j > 0:
            _sum = matrix[j][i] + matrix[j-1][i]
            if _sum < min_sum:
                min_sum = _sum
        matrix[j][i] = min_sum
min_path = minimum

for m in range(len(matrix)):
    if matrix[m][i] < min_path:
        min_path = matrix[m][i]
print (min_path)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 3,  Recursive solutions --------------------------')
t1  = time.time()

from functools import reduce

def euler82():
    # f = open(filename, 'r' ).read()
    # f = list( map(lambda x:  map( int, x.split(',')), f.splitlines() ) )
    # f =  map( list, zip(*f))[::-1]
    f = matrix

    def func(x,y):
        s = map(reduce.add,x,y)
        def part(s,x):
            smin = min(s)
            k = s.index(smin)
            if k == 0:
                left = []
            else:
                temp = min(x[k-1],smin)
                s[k-1] += temp - x[k-1]
                x[k-1] = temp
                left = part(s[:k],x[:k])
            if k == len(s)-1:
                right = []
            else:
                temp = min(x[k+1],smin)
                s[k+1] += temp - x[k+1]
                x[k+1] = temp
                right = part(s[k+1:],x[k+1:])
            return left + [smin] + right
        return part(s,x)
    return min(reduce(func,f))

# euler82()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 4,   --------------------------')
t1  = time.time()

import math

matrix = deepcopy(matricea)

def costValue(row, col):
    if row<0 or row > len(costs)-1:
        return math.inf
    if col < 0 or col > len(costs[row])-1:
        return math.inf
    return costs[row][col]

def leastCost () :
    # start at last column: this is copy of matrix column
    for row in range(len(matrix)): costs[row][-1] = matrix[row][-1]

    # next, look to the previous column and get cost of coming
    # from the left
    # then we go down looking for cost of moving upards
    # and afterwards sweep up looking at cost of moving down
    for col in range(len(matrix[0])-2,-1,-1):
        # scanning downwards
        for row in range(len(matrix)):
            # cost of going right
            costs[row][col] = matrix[row][col] + costValue(row,col+1)
            # cost of going up
            costs[row][col] = min(costValue(row,col),
                        matrix[row][col]+costValue(row-1,col))
        # scanning upwards
        for row in range(len(matrix[row])-1,-1,-1):
            costs[row][col] = min(costValue(row,col),
                        matrix[row][col]+costValue(row+1,col))
        # helps with debugging
        # showCosts()

    return min(row[0] for row in costs)

def showCosts():
    for row in costs:
        print(row)
    print()



costs = [[math.inf]*len(row) for row in matrix]

answer = leastCost()
print(answer)




t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 5, Dijkstra  algorithm   --------------------------')
t1  = time.time()

# ==== Thu, 25 Aug 2016, 20:32, mbh038, England
# About 160 ms in Python.
#
# I use Dijkstra's algorithm ( I wanted to get the hang of this),
# and construct a graph of the matrix as a dictionary (hash table),
# indexed by coordinate and with the coordinates of all directly connected points as a list among
# the values attached to each index, as defined by the movement rules.
#
# If, as in this problem, the start node and end node are anywhere along an edge,
# then I add virtual nodes to the graph, one for each edge on which the path starts or finishes,
# of zero value but connected to all real points along its corresponding edge, as they are to it.
#
# The code is exactly the same as for problems 81 and 83.


from timeit import default_timer as timer
import math as m

def PE_0082(filename = filename , sn='vl',  fn='vr',  rules='udr' ):
    start = timer()
    M = readfile(filename)
    graph = gm(M,  rules , sn , fn )
    print('Minimum path sum:',dijkstra(graph,sn,fn))
    print ('Elapsed time: ',timer()-start,'s')

def readfile(filename):
    """returns matrix as a list of rows"""
    with open(filename,'r') as file:
        data  = file.readlines()
    return [[int(x) for x in line.split(',')] for line in data]

def gm(M,  rules, sn, fn ):
    """returns a graph as a dictionary,indexed by coordinate. The values of each
    element are a list of three components - the first is the total cost of visiting
    that element along the chosen path, the second is the cost of that element and
    the third is a list of coordinates of the elements to which the element is
    directly connected. as determined by the rules.

    sn and fn are the start and finish nodes

    'vl','vr','vt' and 'vb are virtual nodes. If used, they denote/finishing starting anywhere
    on the left,right, top or bottom  edges. .
    """
    rows, cols = len(M),len(M[0])
    nodes = {(r,c):[m.inf,M[r][c],[]] for r in range(rows) for c in range(cols)}
    movedict = {'u':(-1,0),'d':(1,0),'l':(0,-1),'r':(0,1)}
    moves = [movedict[rule] for rule in [letter for letter in rules]]

    for node in nodes:
        for n in moves:
            nodes[node][2].append(tuple(p+q for p, q in zip(node, n)))

    if sn=='vl':
        nodes['vl'] = [m.inf,0,[(r,0) for r in range(rows)]]
        for r in range(rows):
            nodes[(r,0)][2].append('vl')

    if fn == 'vr':
        nodes['vr'] = [m.inf,0,[(r,cols-1) for r in range(rows)]]
        for r in range(rows):
            nodes[(r,cols-1)][2].append('vr')

    if fn == 'vt':
        nodes['vt'] = [m.inf,0,[(0,c) for c in range(cols)]]
        for c in range(cols):
            nodes[(0,c)][2].append('vt')

    if fn == 'vb':
        nodes['vb'] = [m.inf,0,[(rows-1,c) for c in range(cols)]]
        for c in range(cols):
            nodes[(rows-1,c)][2].append('vb')
    return nodes

def dijkstra( graph, sn , fn ):
    """uses Dijkstra's algorithm to find the lowest cost path between the start
      and finish nodes in the graph. Returns the cost of that path.
    """
    nv = {}
    cn = sn
    graph[cn][0] = graph[cn][1]
    while 1:
        for nn in graph[cn][2]:
            try:
                value = graph[cn][0] + graph[nn][1]
                if value < graph[nn][0]:
                    graph[nn][0] = value
                    nv[nn] = graph[nn]
            except KeyError:
                pass
        cnv, cn = min((v[0],k) for k,v in nv.items())
        if cn == fn: break
        del(nv[cn])
    return int(nv[fn][0])

PE_0082(filename,  sn='vl', fn='vr',rules='udr'  )

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 6, NetworkX library  --------------------------')
t1  = time.time()

# === Mon, 28 Mar 2016, 17:52, juancroldan , Spain
# Using Python NetworkX library

import networkx as nx
import matplotlib.pyplot as plt

g = nx.DiGraph()

with open(filename , "r") as f:
	rows = f.read().split("\n")
matrix = [list(map(int,n.split(","))) for n in rows]

# weight considered when entering the node
height = len(matrix)
width = len(matrix[0])
for y in range(0,height):
	# add origin and end edges
	g.add_edge("origin",(0,y),weight=matrix[y][0])
	g.add_edge((width-1,y),"end",weight=0)
	# horizontal edges
	for x in range(0,width-1):
		g.add_edge((x,y),(x+1,y),weight=matrix[y][x+1])

# add vertical edges
for x in range(0,width):
	for y in range(0,width-1):
		g.add_edge((x,y),(x,y+1),weight=matrix[y+1][x])
	for y in range(1,width):
		g.add_edge((x,y),(x,y-1),weight=matrix[y-1][x])

path = nx.astar_path(g,"origin","end")

total = sum(g[n1][n2]['weight'] for n1,n2 in zip(path[:-1],path[1:]))
print(total)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')



print('\n--------------------------SOLUTION 7,   --------------------------')
t1  = time.time()

# ===Fri, 8 Jul 2016, 12:35,  merkez3110, Turkey
# Too long for a python code, clear though.

def main():
    n = 80
    matrix = [[0 for col in range(n)] for row in range(n)]
    data_file = open(filename, 'r')

    row = 0
    for line in data_file.readlines():
        col = 0

        for num in line.split(','):
            matrix[row][col] = int(num)
            col += 1

        row += 1

    data_file.close()
    vector_min_next = [matrix[row][n - 1] for row in range(n)]

    for col in range(n - 2, -1, -1):
        vector_min_hist = list.copy(vector_min_next)

        for row in range(n):
            min_tmp_upward = vector_min_hist[row]
            min_tmp_downwd = vector_min_hist[row]
            sum_tmp_downwd = 0
            sum_tmp_upward = 0

            for row_downwd in range(row - 1, -1, -1):
                sum_tmp_downwd += matrix[row_downwd][col]
                tot_tmp = sum_tmp_downwd + vector_min_hist[row_downwd]

                if tot_tmp < min_tmp_downwd:
                    min_tmp_downwd = tot_tmp

            for row_upward in range(row + 1, n):
                sum_tmp_upward += matrix[row_upward][col]
                tot_tmp = sum_tmp_upward + vector_min_hist[row_upward]

                if tot_tmp < min_tmp_upward:
                    min_tmp_upward = tot_tmp

            vector_min_next[row] = min(min_tmp_downwd, min_tmp_upward) + matrix[row][col]

    print(min(vector_min_next[row] for row in range(n)))
    return


main()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')



print('\n--------------------------SOLUTION 8,   --------------------------')
t1  = time.time()

# ===


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')








