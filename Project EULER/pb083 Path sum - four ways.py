#!/usr/bin/python
# Solved by Bogdan Trif @   Completed on Thu, 9 Nov 2017, 17:36
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

M=  [[131, 673, 234, 103, 18],
        [201, 96,  342, 965, 150],
        [630, 803, 746, 422, 111],
        [537, 699, 497, 121, 956],
        [805, 732, 524, 37,  331]]


grid = M

def build_Graph(grid, rules):

    rows, cols = len(grid), len(grid[0])
    big_Grid =  [ [0]*cols*rows for i in range(cols*rows) ]

    movedict = {  'u':(-1,0),  'd':(1,0), 'l':(0,-1), 'r':(0,1) }
    moves = [  movedict[rule] for rule in [ letter for letter in rules ] ]
#     print(movedict)
#     print( moves)
    Graph = dict()


    for i in range(len(grid)):
        for j in range(len(grid[i])):
            valid_moves = [k for k in [ u for u in moves if [ v for v in rules ]] if ( i+k[0] >=0 and j+k[1] >=0 )
                        if ( i+k[0] < len(grid) and j+k[1] < len(grid) ) ]
            nodes = [ tuple( a+b for a,b in zip( c , (i,j))) for c in valid_moves   ]
#             print(i,j, valid_moves ,'    ' ,nodes ,)
            Graph[(i,j)] = nodes

    # print(Graph)

    # big_Grid[0][0] = grid[0][0]
    for k,v in Graph.items():
        for l in v :
            i, j =  k[0]*rows+k[1] , l[0]*rows+l[1]
            # print(k , i ,'         ' , l , j , '        ',  M[l[0]][l[1]] )
            big_Grid[ i ] [ j ] = grid[l[0]][l[1]]
            big_Grid[ j ] [ i ] = grid[k[0]][k[1]]

    # for i in big_Grid :    print(i)

    return big_Grid
    # return Graph




def Djikstra(grid, rules):

    Graph = build_Graph( grid, rules  )
#     print(Graph)
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
    while pos != ( len(grid)-1, len(grid)-1   )  :

        Passed |= {pos}
        ij = pos[0]*rows + pos[1]
        print('\niterations = ' , iters,  '    ##pos= ' , ij,'  pos= ' ,pos, '   Step[ij]=  ' ,Step[ij] )

        neighbors = [ i for i in Graph[pos] if i not in Passed ]
        In_Grid =   [ grid[i][j]+ N[pos[0]][pos[1]]   for i, j in neighbors ]
        In_Step = [ Step[ u*cols + v] for u, v in neighbors ]

        print('neighbors = ',neighbors,  '      In_grid=' ,In_Grid , '    In_Step = ' ,In_Step )
        print('Visited = ', Passed)

        Dist = [ min(a,b) for a,b in zip(In_Grid, In_Step ) ]
        for z in range(len(neighbors)) :   Step[neighbors[z][0]*rows+neighbors[z][1]] = Dist[z]
        for t in range(len(neighbors)) :  N[neighbors[t][0]] [neighbors[t][1]] = Dist[t]
        # print(Step)

        min_distance = min(In_Grid)
        pos = neighbors[In_Grid.index(min_distance)]
        print('pos (next_pos) = ', pos)

        iters += 1

    return print('\nShortest path = ', N[rows-1][cols-1]   )

# Djikstra( matricea ,  rules = 'drul'  )



t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n==========  My FIRST SOLUTION, Djikstra , Needs optimization,  SLOW, 25 sec ===============\n')
t1  = time.time()


def build_Graph(grid, rules):

    rows, cols = len(grid), len(grid[0])
    big_Grid =  [ [0]*cols*rows for i in range(cols*rows) ]

    movedict = {  'u':(-1,0),  'd':(1,0), 'l':(0,-1), 'r':(0,1) }
    moves = [  movedict[rule] for rule in [ letter for letter in rules ] ]

    Graph = dict()

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
    while iters < 4*10**5 :
    # while True  :

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

        # print('POS = ',POS)

    return print('\nShortest path = ', N[rows-1][cols-1]   )

# Djikstra(matricea ,  rules = 'drul'  )


t2  = time.time()
print('\nCompleted in :', round((t2-t1) , 4 ), 's\n\n')


print('\n============ My Second SOLUTION,  Messy, Taken from , SLOW, 25 sec ===============\n')
t1  = time.time()

# http://www.geeksforgeeks.org/greedy-algorithms-set-6-dijkstras-shortest-path-algorithm/


def build_Graph(grid, rules):

    rows, cols = len(grid), len(grid[0])
    big_Grid =  [ [0]*cols*rows for i in range(cols*rows) ]

    movedict = {  'u':(-1,0),  'd':(1,0), 'l':(0,-1), 'r':(0,1) }
    moves = [  movedict[rule] for rule in [ letter for letter in rules ] ]
    Graph = dict()


    for i in range(len(grid)):
        for j in range(len(grid[i])):
            valid_moves = [k for k in [ u for u in moves if [ v for v in rules ]] if ( i+k[0] >=0 and j+k[1] >=0 )
                        if ( i+k[0] < len(grid) and j+k[1] < len(grid) ) ]
            nodes = [ tuple( a+b for a,b in zip( c , (i,j))) for c in valid_moves   ]
#             print(i,j, valid_moves ,'    ' ,nodes ,)
            Graph[(i,j)] = nodes

    # print(Graph)

    # big_Grid[0][0] = grid[0][0]
    for k,v in Graph.items():
        for l in v :
            i, j =  k[0]*rows+k[1] , l[0]*rows+l[1]
            # print(k , i ,'         ' , l , j , '        ',  M[l[0]][l[1]] )
            big_Grid[ i ] [ j ] = grid[l[0]][l[1]]
            big_Grid[ j ] [ i ] = grid[k[0]][k[1]]

    # for i in big_Grid :    print(i)

    return big_Grid
    # return Graph

inf = float('inf')

# Python program for Dijkstra's single
# source shortest path algorithm. The program is
# for adjacency matrix representation of the graph

class Graph():

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]  for row in range(vertices)]

    def printSolution(self, dist):
        print( "Vertex tDistance from Source")
        for node in range(self.V):
            print( node,   "t" ,   dist[node])

    # A utility function to find the vertex with
    # minimum distance value, from the set of vertices
    # not yet included in shortest path tree
    def minDistance(self, dist, sptSet):

        # Initialize minimum distance for next node
        min = inf

        # Search not nearest vertex not in the
        # shortest path tree
        for v in range(self.V):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v

        return min_index

    # Funtion that implements Dijkstra's single source
    # shortest path algorithm for a graph represented
    # using adjacency matrix representation
    def dijkstra(self, src):

        dist = [inf] * self.V
        dist[src] = 0
        sptSet = [False] * self.V

        for cout in range(self.V):

            # Pick the minimum distance vertex from
            # the set of vertices not yet processed.
            # u is always equal to src in first iteration
            u = self.minDistance(dist, sptSet)

            # Put the minimum distance vertex in the
            # shotest path tree
            sptSet[u] = True

            # Update dist value of the adjacent vertices
            # of the picked vertex only if the current
            # distance is greater than new distance and
            # the vertex in not in the shotest path tree
            for v in range(self.V):
                if self.graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + self.graph[u][v] :
                    dist[v] = dist[u] + self.graph[u][v]

        self.printSolution(dist)

        return print('\nPath =  ', dist[-1] + self.graph[1][0] )

### =====Driver program
# g  = Graph(6400)
# g.graph = build_Graph(matricea, rules = 'rdul' )
# g.dijkstra(0)

t2  = time.time()
print('\nCompleted in :', round((t2-t1) , 4 ), 's\n\n')

# ==== GENERAL IDEAS & LINKS
# I used networkx.  Solutions to 81, 82 and 83 are identical, just add more edges.
# I use dijkstra to and i use priority queue so it in O(n^2log(n))

print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 0,  Work Example  --------------------------')
t1  = time.time()

# http://www.geeksforgeeks.org/greedy-algorithms-set-6-dijkstras-shortest-path-algorithm/
# Python program for Dijkstra's single
# source shortest path algorithm. The program is
# for adjacency matrix representation of the graph


inf = float('inf')

class Graph():

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]  for row in range(vertices)]

    def printSolution(self, dist):
        print( "Vertex tDistance from Source")
        for node in range(self.V):
            print( node,"t",dist[node])

    # A utility function to find the vertex with
    # minimum distance value, from the set of vertices
    # not yet included in shortest path tree
    def minDistance(self, dist, sptSet):

        # Initilaize minimum distance for next node
        min = inf

        # Search not nearest vertex not in the
        # shortest path tree
        for v in range(self.V):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v

        return min_index

    # Funtion that implements Dijkstra's single source
    # shortest path algorithm for a graph represented
    # using adjacency matrix representation
    def dijkstra(self, src):

        dist = [inf] * self.V
        dist[src] = 0
        sptSet = [False] * self.V

        for cout in range(self.V):

            # Pick the minimum distance vertex from
            # the set of vertices not yet processed.
            # u is always equal to src in first iteration
            u = self.minDistance(dist, sptSet)

            # Put the minimum distance vertex in the
            # shotest path tree
            sptSet[u] = True

            # Update dist value of the adjacent vertices
            # of the picked vertex only if the current
            # distance is greater than new distance and
            # the vertex in not in the shotest path tree
            for v in range(self.V):
                if self.graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + self.graph[u][v] :
                    dist[v] = dist[u] + self.graph[u][v]

        self.printSolution(dist)

# Driver program
# g  = Graph(9)
# g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
#            [4, 0, 8, 0, 0, 0, 0, 11, 0],
#            [0, 8, 0, 7, 0, 4, 0, 0, 2],
#            [0, 0, 7, 0, 9, 14, 0, 0, 0],
#            [0, 0, 0, 9, 0, 10, 0, 0, 0],
#            [0, 0, 4, 14, 10, 0, 2, 0, 0],
#            [0, 0, 0, 0, 0, 2, 0, 1, 6],
#            [8, 11, 0, 0, 0, 0, 1, 0, 7],
#            [0, 0, 2, 0, 0, 0, 6, 7, 0]  ]
#
#
# g.dijkstra(0);


############        heapq implementation        ##############
# Fri, 4 Sep 2015, 19:10, georgri, Russia

# It actually takes linear time to do that! Dictionaries in Python are based on hash tables, not on binary search trees...
#
#
# Python doesn't have any native structure with a true sorted set functionality, that would support both changing and find_min operations in no worse than log(n) time.
#
# So we have to use a heap with a little modification instead.
#
# Heap already supports get_min operation, so we only need to work on a change operation.
# For that, we will just leave the node in the heap, but we will change the path weight in the path matrix to
# 'invalidate' the node with the old weight in the heap.
# When popping a min, we check that the weight of the popped element is equal to the weight of that
# same element in the path matrix.
# If the weights are different, we know that the element has been "deleted", and immediately proceed to popping another one.
#
# Check out this note in the heapq documentation:
# http://docs.python.org/2/library/heapq.html#priority-queue-implementation-notes
# It addresses exactly this issue.
#
# EDIT:
# Thanks to fkoprivec's solution above, I realized that we don't even have to do the full Dijkstra!
#
# We don't have to try to relax the vertices that have been already visited.
# The property of a rectangular grid we solve for is that when we visit a vertex for the first time,
# we are guaranteed to set the smallest path value for it.
# It is because all the (virtual) edges that lead to any single vertex have the same weight!
#
# Check out my python implementation using heapq with comments:

from heapq import *

""" test scenario from the problem text with the answer 2297 """
txt = """
131,673,234,103,18 
201,96,342,965,150 
630,803,746,422,111 
537,699,497,121,956 
805,732,524,37,331
"""

m = [[int(n) for n in line.split(',') if n != ''] for line in txt.split('\n') if line != '']
heap = []
path = [[0] * len(m) for i in range(len(m))]

def relax(i, j, ito, jto):
	if path[ito][jto] == 0: # considering only unvisited vertices
		path[ito][jto] = path[i][j] + m[ito][jto]
		heappush(heap, (path[ito][jto], ito, jto))

# push the start vertex to the queue
relax(0, 0, 0, 0)

while heap:
	p, i, j = heappop(heap)

	# look at the adjacent edges, try to relax them
	if i > 0: # left vertex exists
		relax(i, j, i - 1, j)
	if i < len(m) - 1: # right vertex exists
		relax(i, j, i + 1, j)
	if j > 0: # top vertex exists
		relax(i, j, i, j - 1)
	if j < len(m) - 1: # bottom vertex exists
		relax(i, j, i, j + 1)

print (path[len(m) - 1][len(m) - 1])


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')





print('\n--------------------------SOLUTION 1, Dijkstra --------------------------')
t1  = time.time()

# ==== Wed, 5 Oct 2016, 16:15, eltong, Albania
# Thanks, Dijkstra.
# Obviously I used the Dijkstra algorithm (that's what it is, although that's also what someone would do
# out of the top of their head without realizing :D).
#
# I copied the matrix into my Python code, as you can see it's a global (not included for obvious reasons).
# Takes 0.14 seconds.

matrix = matricea

class GraphNode:
    def __init__(self, weight=0, id=None):
        self.id = id
        self.weight = weight
        self.dist = 0
        self.children_set = set()

    def add_child(self, child):
        self.children_set.add(child)

    def children(self, **kwargs):
        return self.children_set - kwargs.get('without', set())

def min_node(nodes):
    min,n = 0,None

    for node in nodes:
        if node.dist < min or min == 0:
            min,n = node.dist, node
    return n

def main1():
    global matrix
    node_matrix = []

    for i in range(len(matrix)):
        node_matrix.append([])
        for j in range(len(matrix)):
            node_matrix[i].append( GraphNode(id=(i,j), weight=matrix[i][j]) )

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            node = node_matrix[i][j]
            if i > 0:
                node.add_child(node_matrix[i - 1][j])
            if j > 0:
                node.add_child(node_matrix[i][j - 1])
            if i < len(matrix) - 1:
                node.add_child(node_matrix[i + 1][j])
            if j < len(matrix) - 1:
                node.add_child(node_matrix[i][j + 1])


    root = node_matrix[0][0]
    root.dist = root.weight
    spt = set()
    discovered = set([root])

    while len(spt) < len(matrix)*len(matrix):
        nearest_node = min_node(discovered)

        spt.add(nearest_node)

        children = nearest_node.children(without=spt)

        for child in children:
            if child.dist == 0 or child.dist > child.weight + nearest_node.dist:
                child.dist = child.weight + nearest_node.dist
            if child not in discovered:
                discovered.add(child)

        discovered.remove(nearest_node)

    print (node_matrix[-1][-1].dist) # distance to last element

main1()


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 2, Dijkstra --------------------------')
t1  = time.time()

# ==== Thu, 25 Aug 2016, 13:51, mbh038, England
# Dijkstra's algorithm in Python, in about 200 ms. The code is exactly as for problems 81 and 82, ' \
# but with different start and end nodes and a different movement rule.

from timeit import default_timer as timer
import math as m

def PE_0083(filename='p083_matrix.txt',sn=(0,0),fn=(79,79),rules='udlr'):
    start=timer()
    M=readfile(filename)
    graph=gm(M,rules,sn,fn)
    print('Minimum path sum:',dijkstra(graph,sn,fn))
    print ('Elapsed time: ',timer()-start,'s')

def readfile(filename):
    """returns matrix as a list of rows"""
    with open(filename,'r') as file:
        data  = file.readlines()
    return [[int(x) for x in line.split(',')] for line in data]

def gm(M,rules,sn,fn):
    """returns a graph as a dictionary,indexed by coordinate. The values of each
    element are a list of three components - the first is the total cost of visiting
    that element, along the chosen path, the second is the cost of that element and
    the third is a list of coordinates of the elements to which the element is
    directly connected. as determined by the rules.

    sn and fn are the start and finish nodes

    'vl','vr','vt' and 'vb are virtual nodes. If used, they denote/finishing starting anywhere
    on the left,right, top or bottom  edges.
    """
    rows,cols=len(M),len(M[0])
    nodes={(r,c):[m.inf,M[r][c],[]] for r in range(rows) for c in range(cols)}
    movedict={'u':(-1,0),'d':(1,0),'l':(0,-1),'r':(0,1)}
    moves=[movedict[rule] for rule in [letter for letter in rules]]
    for node in nodes:
        for n in moves:
            nodes[node][2].append(tuple(p+q for p, q in zip(node, n)))
    if sn=='vl':
        nodes['vl']=[m.inf,0,[(r,0) for r in range(rows)]]
        for r in range(rows):
            nodes[(r,0)][2].append('vl')
    if fn=='vr':
        nodes['vr']=[m.inf,0,[(r,cols-1) for r in range(rows)]]
        for r in range(rows):
            nodes[(r,cols-1)][2].append('vr')
    if fn=='vt':
        nodes['vt']=[m.inf,0,[(0,c) for c in range(cols)]]
        for c in range(cols):
            nodes[(0,c)][2].append('vt')
    if fn=='vb':
        nodes['vb']=[m.inf,0,[(rows-1,c) for c in range(cols)]]
        for c in range(cols):
            nodes[(rows-1,c)][2].append('vb')
    return nodes

def dijkstra(graph,sn,fn):
    """uses Dijkstra's algorithm to find the lowest cost path between the start
      and finish nodes in the graph. Returns the cost of that path.
    """
    nv={}
    cn=sn
    graph[cn][0]=graph[cn][1]
    while 1:
        for nn in graph[cn][2]:
            try:
                value=graph[cn][0]+graph[nn][1]
                if value<graph[nn][0]:
                    graph[nn][0]=value
                    nv[nn]=graph[nn]
            except KeyError:
                pass
        cnv,cn = min((v[0],k) for k,v in nv.items())
        if cn==fn: break
        del(nv[cn])
    return int(nv[fn][0])

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

# print('\n--------------------------SOLUTION 3,  Recursive solutions --------------------------')
# t1  = time.time()
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
print('\n--------------------------SOLUTION 4, PriorityQueue  --------------------------')
t1  = time.time()

from queue import PriorityQueue
matrix = matricea

size = len(matrix)
limit = sum([j for i in matrix for j in i])
value = [[limit]*size for x in range(size)]
queue = PriorityQueue()
queue.put((matrix[0][0],(0,0)))
position = (0,0)

def neighbours(k):
    u,v = k
    if u != 0:
        yield (u-1,v)
    if u != size-1:
        yield  (u+1,v)
    if v != 0:
        yield (u,v-1)
    if v != size-1:
        yield (u,v+1)

while position != (size-1,size-1):
    a,(b,c) = queue.get()
    position = (b,c)
    if value[b][c] > a:
        value[b][c] = a
        for i,j in neighbours(position):
            queue.put((a+matrix[i][j],(i,j)))

print(a)


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 5,  FASTEST, Very elegant   --------------------------')
t1  = time.time()


# ==== Tue, 4 Jul 2017, 21:43, SafassThin, France
# I've been working on this for a few days - really trying to get the Dijkstra and A* algorithms.
# I really like hansaplast's implementation and I took some idea's from it.
# Dijkstra runs in about 35ms, A* in 50ms.
#
# A bit disapointed by A*, but I suppose that since there are no 'barriers',
# this is not the best example for this algorithm to shine? Or is there a better heuristic?


from heapq import heappop, heappush
def method1(m=matrix):
    """
    Using point-to-point implementation of Dijkstra's shortest path algorithm
    (http://en.wikipedia.org/wiki/Dijkstra%27s_algorithm)
    Some good idea's from:
    (hansaplast @ https://projecteuler.net/thread=83&page=6)
    """
    size = len(m)
    def dijkstra(m, start, end, cost=0):
        q, path = [(cost, start, None)], {}
        while q:
            cost, vertex, predecessor = heappop(q)
            if vertex == end: return cost
            r, c = vertex
            for neighbour in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                if neighbour in path: continue
                r, c = neighbour
                if (size > r >= 0) and (size > c >= 0):
                    heappush(q, (cost+m[c][r], neighbour, vertex))
                    path[neighbour] = vertex
        return float('inf') # Not reached

    return dijkstra(m, (0, 0), (size-1, size-1), m[0][0])


def method2(m=matrix):
    """
    Using A★, with Manhattan distance as heuristic.
    (http://theory.stanford.edu/~amitp/GameProgramming/Heuristics.html)
    ("Python Algorithms"/Hetland - p204 - modified)
    """
    size, lowest_cost = len(m), min(min(r) for r in m)

    def manhattan(a, b, w=lowest_cost):
        (ra, ca), (rb, cb) = a, b
        return w*(abs(ra-rb) + abs(ca-cb))

    def Astar(m, start, end, cost=0, h=manhattan):
        q, path = [(0, cost, start, None)], {}
        while q:
            estimate, cost, vertex, predecessor = heappop(q)
            if vertex == end: return cost
            r, c = vertex
            for neighbour in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                if neighbour in path: continue
                r, c = neighbour
                if (size > r >= 0) and (size > c >=0):
                    estimate = cost + m[c][r] - h(vertex, end) + h(neighbour, end)
                    heappush(q, (estimate, cost+m[c][r], neighbour, vertex))
                    path[neighbour] = vertex
        return float('inf') # Not reached

    return Astar(m, (0, 0), (size-1, size-1), m[0][0])


method1(matrix)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 6,  INTERESTING  --------------------------')
t1  = time.time()

# ==== Sat, 15 Jul 2017, 14:21, aditya-r-m, India
# Just a simple dp in python similar to previous problems.
# first minimize the path from top left to bottom right using just right/bottom movement,
# then keep reversing the direction and and minimize again till no updates are made.

from urllib.request import urlopen
import math, copy

file_url = 'https://projecteuler.net/project/resources/p082_matrix.txt'
matrix = list(map(lambda s: list(map(int, s[0].split(','))), (line.decode('UTF-8').split() for line in urlopen(file_url))))

solution = [[math.inf] * len(matrix) for i in matrix]
solution[0][0] = matrix[0][0]

unstable = True
x, y, dx, dy, lx, ly = -1, -1, 1, 1, len(solution), len(solution)
while unstable:
    unstable = False
    for i in range(x + dx, lx, dx):
        for j in range(y + dy, ly, dy):
            new_solution = solution[i - dx][j] + matrix[i][j] if i - dx != x else math.inf
            if solution[i][j] > new_solution:
                solution[i][j], unstable = new_solution, True
            new_solution = solution[i][j - dy] + matrix[i][j] if j - dy != y else math.inf
            if solution[i][j] > new_solution:
                solution[i][j], unstable = new_solution, True
    x, y, dx, dy, lx, ly = lx, ly, -dx, -dy, x, y
print(solution[-1][-1])

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')



print('\n--------------------------SOLUTION 7,  BFS , Very fast --------------------------')
t1  = time.time()

# ===Fri, 11 Mar 2016, 14:54, hansaplast, Switzerland
# A breadth first search (weighted by the sum of values along the path) with check that every field is checked only once.
#
# I tried to make the python code as short (13 lines) but still as readable as possible (input welcome!). Runs in 0.1s.


import bisect

m = matrix
seen = dict()
q = [(m[0][0],0,0)]
for val,i,j in q:
	if i==j==len(m)-1:
		print(val)
		break
	for _i,_j in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
		if _i in range(len(m)) and _j in range(len(m)) and (_i,_j) not in seen:
			bisect.insort(q, (val+m[_i][_j], _i, _j))
			seen[(_i,_j)] = 1

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')



print('\n--------------------------SOLUTION 8, NetworkX in Python  --------------------------')
t1  = time.time()

# === Mon, 28 Mar 2016, 18:39, juancroldan, Spain
# NetworkX in Python

import networkx as nx
import matplotlib.pyplot as plt

g = nx.DiGraph()


# weight considered when entering the node
height = len(matrix)
width = len(matrix[0])
for y in range(0,height):
	# horizontal edges
	for x in range(0,width-1):
		g.add_edge((x,y),(x+1,y),weight=matrix[y][x+1])
	for x in range(1,width):
		g.add_edge((x,y),(x-1,y),weight=matrix[y][x-1])

# add vertical edges
for x in range(0,width):
	for y in range(0,width-1):
		g.add_edge((x,y),(x,y+1),weight=matrix[y+1][x])
	for y in range(1,width):
		g.add_edge((x,y),(x,y-1),weight=matrix[y-1][x])

path = nx.astar_path(g,(0,0),(width-1,height-1))
print(path)
total = sum(g[n1][n2]['weight'] for n1,n2 in zip(path[:-1],path[1:])) + matrix[0][0]
print(total)


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')






print('\n--------------------------SOLUTION 9,   --------------------------')
t1  = time.time()

# === Mon, 7 Sep 2015, 02:01, Gomoto, Germany

data = []
f = open(filename ,'r')
for line in f.readlines():
	line = list(map(int,line.strip().split(',')))
	data.append(line)
f.close()
size = len(line)
infinity = 10**10

minimum = {}
for x in range(0,size):
	for y in range(0,size):
		minimum[y,x] = infinity

new_minimums = []
def next_steps(pos):
	(y,x) = pos
	if x+1 < size:
		right = minimum[y,x] + data[y][x+1]
		if right < minimum[y,x+1]:
			minimum[y,x+1] = right
			new_minimums.append((y,x+1))
	if y+1 < size:
		down = minimum[y,x] + data[y+1][x]
		if down < minimum[y+1,x]:
			minimum[y+1,x] = down
			new_minimums.append((y+1,x))
	if x-1 > -1:
		left = minimum[y,x] + data[y][x-1]
		if left < minimum[y,x-1]:
			minimum[y,x-1] = left
			new_minimums.append((y,x-1))
	if y-1 > -1:
		down = minimum[y,x] + data[y-1][x]
		if down < minimum[y-1,x]:
			minimum[y-1,x] = down
			new_minimums.append((y-1,x))

minimum[0,0]= data[0][0]
test = [(0,0)]

while (test != []):
	new_minimums = []
	for el in test:
		next_steps(el)
	test = new_minimums

print(minimum[size-1,size-1])

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')



print('\n--------------------------SOLUTION 10,  Interesting  --------------------------')
t1  = time.time()

# === Wed, 30 Sep 2015, 10:15, slingeraap, Netherlands
# I have been struggling for three nights in a row now with 'optimized' brute force algorithms,
# that would recursively try many different paths.
# I found optimizations such as that the path should never contain two adjacent cells -
# because then a shortcut could have been made.
#
# Although my algorithms worked perfectly for the 5x5 example matrix,
# they failed to complete for the 80x80 matrix in a night (and I seriously doubt that they would manage in a week!)
#
# I should have know better and suddenly in the shower (isn't it always?) the iterative solution below hit me.
# It probably is a well-known method to do this, but since I am not familiar with them,
# I can proudly say I invented it myself :-)
#
# The algorith will first seed all cells with a naive calculation of their distance from the start cell.
# It will then iteratively check if it could have arrived there through a shorter path through any of their direct neighbours.
# It iterates until no more improvements are found, which was the case after 12 iterations.
# The correct answer was already found after the 3rd iteration.
#
# Executes in 400 ms in python.


m = []
mc = []
for line in open(filename, 'r').readlines():
    newrow = []
    for tok in line.split(','):
        newrow.append(int(tok))
    m.append(newrow)
    mc.append([0]*len(newrow))

# initial seed
mc[0][0] = m[0][0]
for col in range(1, len(m[0])):
    mc[0][col] = m[0][col] + mc[0][col - 1]
for row in range(1,len(m)):
    mc[row][0] = m[row][0] + mc[row - 1][0]
    for col in range(1, len(m[row]) ):
        mc[row][col] = m[row][col] + mc[row][col - 1]

changed = True
i = 0
# iterative optimization
while changed:
    changed = False
    for row in range(len(m)):
        for col in range(0, len(m[row])):
            oldval = mc[row][col]
            if col > 0:
                mc[row][col] = min(mc[row][col], m[row][col] + mc[row][col - 1])
            if col < len(m[row]) - 1:
                mc[row][col] = min(mc[row][col], m[row][col] + mc[row][col + 1])
            if row > 0:
                mc[row][col] = min(mc[row][col], m[row][col] + mc[row - 1][col])
            if row < len(m) - 1:
                mc[row][col] = min(mc[row][col], m[row][col] + mc[row + 1][col])
            changed = changed or oldval != mc[row][col]
    print( 'after iteration %d: %d' % (i+1, mc[len(mc) - 1][len(mc[0]) - 1]))
    i += 1

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 11,  PriorityQueue --------------------------')
t1  = time.time()

from heapq import heapify, heappush, heappop
class PriorityQueue(dict):
    """Dictionary that serves as a priority queue.

    Keys of the dictionary are items to be put into the queue, and values
    are their respective priorities. Most dictionary methods work as expected.
    The advantage over a standard heapq-based priority queue is
    that priorities of items can be efficiently updated using code as
    'thedict[item] = new_priority.'

    The 'popitem' method, unlike the usual dict method, returns the (key,value)
    pair with the lowest value and removes it from the queue.

    Based on an ASPN recipe by Matteo Dell'Amico.
    """
    def __init__(self, *args, **kwargs):
        super(PriorityQueue, self).__init__(*args, **kwargs)
        self._rebuild_heap()

    def _rebuild_heap(self):
        self._heap = [(v, k) for k, v in self.iteritems()]
        heapify(self._heap)

    def popitem(self):
        """Return the (key, priority) pair with the lowest priority and remove it from the queue.

        Raises IndexError if the object is empty.
        """
        heap = self._heap
        v, k = heappop(heap)
        while k not in self or self[k] != v:
            v, k = heappop(heap)
        del self[k]
        return k, v

    def __setitem__(self, key, val):
        # We are not going to remove the previous value from the heap,
        # since this would have a cost O(n).
        super(PriorityQueue, self).__setitem__(key, val)
        if len(self._heap) < 2 * len(self):
            heappush(self._heap, (val, key))
        else:
            # When the heap grows larger than 2 * len(self), we rebuild it
            # from scratch to avoid wasting too much memory.
            self._rebuild_heap()



t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')



print('\n--------------------------SOLUTION 12,  Priority Queue --------------------------')
t1  = time.time()

# ===Sat, 15 Nov 2008, 10:45, Jepso, finland
# I first tried to solve this with a recursive algorithm, but it didn't work because maximum recursion depth was exceeded.
# Then I removed the recursion by using a queue. Runs in 0.5 seconds.

def find_minimal_path(matrix):
    size = len(matrix)
    minimal_path = [[None for i in range(size)] for j in range(size)]
    minimal_path[0][0] = matrix[0][0]
    visit = [(0, 0)]

    while len(visit) > 0:
        x, y = visit.pop(0)
        if x > 0 and (not minimal_path[y][x-1] or \
                      minimal_path[y][x-1] > minimal_path[y][x] + matrix[y][x-1]):
            minimal_path[y][x-1] = minimal_path[y][x] + matrix[y][x-1]
            visit.append((x-1, y))
        if x < size - 1 and (not minimal_path[y][x+1] or \
                      minimal_path[y][x+1] > minimal_path[y][x] + matrix[y][x+1]):
            minimal_path[y][x+1] = minimal_path[y][x] + matrix[y][x+1]
            visit.append((x+1, y))
        if y > 0 and (not minimal_path[y-1][x] or \
                      minimal_path[y-1][x] > minimal_path[y][x] + matrix[y-1][x]):
            minimal_path[y-1][x] = minimal_path[y][x] + matrix[y-1][x]
            visit.append((x, y-1))
        if y < size-1 and (not minimal_path[y+1][x] or \
                      minimal_path[y+1][x] > minimal_path[y][x] + matrix[y+1][x]):
            minimal_path[y+1][x] = minimal_path[y][x] + matrix[y+1][x]
            visit.append((x, y+1))

    return minimal_path[-1][-1]

matrix = [[int(string) for string in line.strip().split(',')] for line in open(filename, 'r')]
print( find_minimal_path(matrix))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')








