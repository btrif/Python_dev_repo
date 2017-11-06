#!/usr/bin/python
# Solved by Bogdan Trif @
#The  Euler Project  https://projecteuler.net
'''
                            Path sum: four ways
Problem 83
NOTE: This problem is a significantly more challenging version of Problem 81.

In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right,
by moving left, right, up, and down, is indicated in bold red and is equal to 2297.


Find the minimal path sum, in matrix.txt (right click and "Save Link/Target As..."),
a 31K text file containing a 80 by 80 matrix,
from the top left to the bottom right by moving left, right, up, and down.
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

# for i in matrix :    print(i)

# mT = transpose(matrix)
# print('\n',mT)


print('\n----------------- TESTS  -----------------------\n')
t1  = time.time()

M=  [[131, 673, 234, 103, 18], \
        [201, 96,  342, 965, 150],\
        [630, 803, 746, 422, 111],\
        [537, 699, 497, 121, 956],\
        [805, 732, 524, 37,  331]]


grid = M

def build_Graph(grid, rules):

    rows, cols = len(grid), len(grid[0])
    # print(rows, cols)

    movedict = {  'u':(-1,0),  'd':(1,0), 'l':(0,-1), 'r':(0,1) }
    moves = [  movedict[rule] for rule in [ letter for letter in rules ] ]
#     print(movedict)
#     print( moves)
    Graph = dict()
    rules = 'drlu'

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            valid_moves = [k for k in [ u for u in moves if [ v for v in rules ]] if ( i+k[0] >=0 and j+k[1] >=0 )
                        if ( i+k[0] < len(grid) and j+k[1] < len(grid) ) ]
            nodes = [ tuple( a+b for a,b in zip( c , (i,j))) for c in valid_moves   ]
#             print(i,j, valid_moves ,'    ' ,nodes ,)
            Graph[(i,j)] = nodes

    # print(Graph)
    return Graph




def Djikstra(grid, rules):

    Graph = build_Graph( grid, rules  )
    print(Graph)
    N = deepcopy(grid)

    Passed = set()
    rows, cols = len(grid), len(grid[0])
    inf = float('inf')
    Step = [inf]* rows*cols

    POS = [(0,0)]
    pos = POS[0]
    ij = pos[0]*rows + pos[1]    # translated position in single row (3,0) = 12
    Step[ij] = N[pos[0]][pos[0]]

    iters = 0
    # while Step[-1] > 10**10  :
    # for o in range(12)  :
    while True  :

        J = POS[:]
        for pos in J :
            iters +=1
            ij = pos[0]*rows + pos[1]
            print('\niterations = ' , iters,  '    ##pos= ' , ij,'  pos= ' ,pos, '   Step[ij]=  ' ,Step[ij] )
            # print(Step)
            neighbors = Graph[pos]
            In_Grid =   [ grid[i][j]+ N[pos[0]][pos[1]]   for i, j in neighbors ]
            In_Step = [ Step[ u*cols + v] for u, v in neighbors ]


            # print('neighbors = ',neighbors,  '      In_grid=' ,In_Grid , '    In_Step = ' ,In_Step )

            Dist = [ min(a,b) for a,b in zip(In_Grid, In_Step ) ]
            for z in range(len(neighbors)) :   Step[neighbors[z][0]*rows+neighbors[z][1]] = Dist[z]
            for t in range(len(neighbors)) :  N[neighbors[t][0]] [neighbors[t][1]] = Dist[t]
            # for r in N : print(r)
            # print('Distance :  ', Dist , '      Step = ',    Step )

            Passed |= {pos}
            # print('POS='  ,POS )
            # print('Passed = ' , Passed )
            POS.remove(pos)                     # we remove the current position from the next search as is VISITED
            POS += list(set(neighbors))     # we add the next nodes, the neighbors
        # print('------------', pos  )
        POS = list(set(POS))

        print('POS = ',POS)
        print(N[rows-1][cols-1])

    return print('\nShortest path = ', N[rows-1][cols-1]   )

Djikstra(matricea ,  rules = 'drul'  )

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
# print('------------------------------------The Original Matrix --------------')
# for i in range(len(M)): print(M[i])




# print('\n----------------------------------- The Computed PATH ---------------------')

# M = [row[:] for row in mT]     # Making a copy of transposed matrix
# M = deepcopy(mT)          # deepcopy for cloning the transposed matrix
# B = zeros((len(M), len(M)), dtype=int)        # numpy Create a zeroed Matrix the same size
# print(B)




print('\n================  My FIRST SOLUTION,  ===============\n')
t1  = time.time()




import math as m

def PE_0082(filename= filename , sn='vl', fn='vr', rules='udr' ):

    M = readfile(filename)
    graph = gm(M, rules, sn, fn )
    print('\nMinimum path sum:',dijkstra(graph, sn , fn ))


def readfile(filename):
    """returns matrix as a list of rows"""
    with open(filename,'r') as file:
        data  = file.readlines()
    return [[int(x) for x in line.split(',')] for line in data]

def gm(M, rules, sn, fn ):
    """returns a graph as a dictionary,indexed by coordinate. The values of each
    element are a list of three components - the first is the total cost of visiting
    that element along the chosen path, the second is the cost of that element and
    the third is a list of coordinates of the elements to which the element is
    directly connected. as determined by the rules.

    sn and fn are the start and finish nodes

    'vl','vr','vt' and 'vb are virtual nodes. If used, they denote/finishing starting anywhere
    on the left, right, top or bottom  edges. .
    """
    rows, cols = len(M),len(M[0])
    nodes = {  (r,c):[m.inf,M[r][c],[]] for r in range(rows) for c in range(cols) }
    movedict = {  'u':(-1,0),  'd':(1,0), 'l':(0,-1), 'r':(0,1) }
    moves = [  movedict[rule] for rule in [ letter for letter in rules ]]

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

# PE_0082( filename )


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
# print('\n--------------------------SOLUTION 1,    --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
# print('\n--------------------------SOLUTION 2,  --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
# print('\n--------------------------SOLUTION 3,  Recursive solutions --------------------------')
# t1  = time.time()
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
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
# print('\n--------------------------SOLUTION 5,    --------------------------')
# t1  = time.time()
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
#
#
# print('\n--------------------------SOLUTION 7,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
#
#
# print('\n--------------------------SOLUTION 8,   --------------------------')
# t1  = time.time()
#
# # ===
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')








