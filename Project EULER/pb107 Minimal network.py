#!/usr/bin/python
# Solved by Bogdan Trif @       Completed on Mon, 9 Jan 2017, 23:26
#The  Euler Project  https://projecteuler.net
'''
                                    Minimal network     -       Problem 107

The following undirected network consists of seven vertices and twelve edges with a total weight of 243.

The same network can be represented by the matrix below.

However, it is possible to optimise the network by removing some edges and still ensure that all points on the network remain connected.
The network which achieves the maximum saving is shown below.
It has a weight of 93, representing a saving of 243 − 93 = 150 from the original network.

The following undirected network consists of seven vertices and twelve edges with a total weight of 243.

The same network can be represented by the matrix below.

Using network.txt (right click and 'Save Link/Target As...'), a 6K text file containing a network with forty vertices,
and given in matrix form, find the maximum saving which can be achieved by removing redundant edges
whilst ensuring that the network remains connected.

'''
import time
import  copy


#   Get the file into the python matrix
filename = "pb107_network.txt"
f = open (filename  , 'r')
text = f.read()
#print(text)
f.close()
network=[]
for row in text.split('\n'):
    # network.append(list(map(str, row.split(','))))         # This maps the strings into ints on the run, SMART TECHNIQUE
    # print(row)
    tmp = []
    for obj in row.split(',') :
        # if obj == '-'  : tmp.append(str('-'))
        if obj == '-'  : tmp.append(1111 )
        else  : tmp.append(int(obj))
        # print(obj, type(obj))
    network.append(tmp)

print(len(network), network,'\n')

for i in network :     print(i)


def initial_network_cost(T, nolink) :
    First_cost = 0
    U = copy.deepcopy(T)
    for i in range(len(U)) :
        for j in range(len(U[i])):
            if U[i][j] < nolink :
                First_cost += U[i][j]
                U[i][j] = nolink
                U[j][i] = nolink
            # print(U[i][j], end='  ')
    return First_cost

print('\n--------------------------TESTS------------------------------')
t1  = time.time()

T = [[99,16,12,21,99,99,99],
        [16,99,99,17,20,99,99],
        [12,99,99,28,99,31,99],
        [21,17,28,99,18,19,23],
        [99,20,99,18,99,99,11],
        [99,99,31,19,99,99,27],
        [99,99,99,23,11,27,99] ]

z = initial_network_cost(T, 99)
print('\nFirst cost : \t', z)

print('\n'+' ---------'*10)

def small_minimal_network_test( network ) :
    itr=0
    param = 1111
    NET = copy.deepcopy( network )
    R = [ 0 ]                            # The rows with the minimum costs, We start here
    M =[ min(NET[R[0]]) ]           # the list with the minimum values
    id = NET[R[0]].index(min(NET[R[0]])  )
    # print(M, id, '        Smallest value : ' , NET[R[0]][id] , NET[id][R[0]] , '   with indexes : ', 0, id, id, 0 )
    NET[R[0]][id], NET[id][R[0]] = param, param
    # print ( NET[R[0]][id], NET[id][R[0]])
    itr+=1
    R.append(id)
    # print(NET, '\n',R,'\n')
    while len(R) <  len(NET) :
        minv = 10**4
        for i in R :
            if minv > min(NET[i]) :
                minv = min(NET[i])
                id0 = i
                id = NET[i].index(minv)
        # print(minv, id0, id , NET[i]  )
        M.append(minv)
        for k in range(len(R)):             # Here we want to mark all the group  links as DEAD !!!
            # print(R[k], id, end='    ')
            NET[R[k]][id], NET[id][R[k]] = param, param
        R.append(id)
        itr+=1
        # print(R, '   ,   iter:',itr,'\n',M)
        # print(NET,'\t' ,R)

    # return print('\n\nAnswer :\t', sum(M) , '\n',M)
    return sum(M)

x = small_minimal_network_test(T)
print('\nsmall_minimal_network_test :\t' ,x )
print('\nTotal savings, Answer : ', z - x )

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n================  My FIRST SOLUTION,  PRIM s Algorithm  ===============\n')
t1  = time.time()

z = initial_network_cost(network, 1111)

def minimal_network( network ) :
    global WAN
    itr=0
    WAN = [[ '-' for i in range(40)] for i in range(40) ]
    param = 1111
    NET = copy.deepcopy( network )
    R = [ 0 ]                            # The rows with the minimum costs, We start here
    M =[ min(NET[R[0]]) ]           # the list with the minimum values
    id = NET[R[0]].index(min(NET[R[0]])  )
    # print(M, id, '        Smallest value : ' , NET[R[0]][id] , NET[id][R[0]] , '   with indexes : ', 0, id, id, 0 )
    WAN[R[0]][id], WAN[id][R[0]] = min(NET[R[0]]), min(NET[R[0]])
    NET[R[0]][id], NET[id][R[0]] = param, param
    # print ( NET[R[0]][id], NET[id][R[0]])
    itr+=1
    R.append(id)
    # print(NET, '\n',R,'\n')
    while len(R) <  len(NET) :
        minv = 10**4
        for i in R :
            if minv > min(NET[i]) :
                minv = min(NET[i])
                id0 = i
                id = NET[i].index(minv)
        # print(minv, id0, id , NET[i]  )
        M.append(minv)
        WAN[id0][id], WAN[id][id0] = minv, minv
        for k in range(len(R)):             # Here we want to mark all the group  links as DEAD !!!
            # print(R[k], id, end='    ')
            NET[R[k]][id], NET[id][R[k]] = param, param
        R.append(id)
        itr+=1
        # print(R, '   ,   iter:',itr,'\n',M)
        # print(NET,'\t' ,R)

    # return print('\n\nAnswer :\t', sum(M) , '\n',M)
    return sum(M)



print('\nFirst cost : \t', z,'\n')
x = minimal_network( network )
print('\nMinimal Network Cost :  ' ,x )

print('\nTotal savings, Answer : ', z - x ,'\n')        #   Total savings, Answer :  259679

# print(network)


# for i in WAN :   print(i)


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')            # Completed in : 19.001007 ms


print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1, Kruskal s algorithm  --------------------------')
t1  = time.time()

# ====un, 1 Jan 2017, 11:31, TheJuggernaut0, USA
# Kruskal's algorithm, shamelessly stolen from an earlier project...

from itertools import product

with open(filename) as f:
	graph = [[None if v == '-' else int(v) for v in line.strip().split(',')]for line in f.readlines()]

n = len(graph)

orig = sum(sum(0 if v is None else v for v in row) for row in graph)//2

# Kruskal's Algorithm
forest = [([i], []) for i in range(n)]
while len(forest) > 1:
	# pick the minimum edge
	e = min(((i, j, graph[i][j]) for i in range(n) for j in range(n) if i < j and graph[i][j] is not None), key=lambda e: graph[e[0]][e[1]])
	# find the trees that the edge connects
	for tree in forest:
		if e[0] in tree[0]:
			first = tree
		elif e[1] in tree[0]:
			second = tree
	# merge the trees
	first[0].extend(second[0])
	first[1].extend(second[1])
	first[1].append(e)
	# delete any other edges that connected the trees
	for i, j in product(range(n), range(n)):
		if i in first[0] and j in first[0] and i != j:
			graph[i][j] = None
	# purge all trace that the second tree ever existed (Big Brother is watching you)
	forest.remove(second)

opt = sum(e[2] for e in forest[0][1])

print(orig - opt)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 2,  PRIM Algorithm --------------------------')
t1  = time.time()

# ====    Wed, 28 Dec 2016, 15:59, NewtonPi
# Class Based O(n^2) Prim's Algorithim (2.175ms)

import math

# file parsing opening
file_adj = open(filename, 'r')
replaced_list = []
zero_replaced_l = []
engineers_infinity = 2**30  # larger int than any other network edge
for line in file_adj:
    replaced_list.append(line.replace(' ', '').replace('-', str(engineers_infinity)))
    zero_replaced_l.append(line.replace(' ', '').replace('-', "0"))
zero_l = []
for line in zero_replaced_l:
    zero_l.append([int(x) for x in line.replace('\n', '').split(',')])
numeric_rows = []
for line in replaced_list:
    numeric_rows.append([int(x) for x in line.replace('\n', '').split(',')])


"""
PRIMS ALGORITHIM

-Initialize a tree with a single vertex, chosen arbitrarily from the graph.

-Grow the tree by one edge: of the edges that connect the tree to vertices not yet in the tree,
    find the minimum-weight edge, and transfer it to the tree.

-Repeat step 2 (until all vertices are in the tree).
"""


class PrimTree:

    def __init__(self, adj_matrix):
        self.adj_matrix = adj_matrix
        self.vertices_in_tree = {0}
        self.vertices_not_in_tree = set(range(1, len(adj_matrix)))
        self.mst_edge_weight = 0

    def add_edge(self):
        minimum_edge_weight = math.inf
        vertex_to_add = None
        for _, tree_vert in enumerate(self.vertices_in_tree):
            for __, unconnected_vert in enumerate(self.vertices_not_in_tree):

                if self.adj_matrix[tree_vert][unconnected_vert] < minimum_edge_weight:
                    minimum_edge_weight = self.adj_matrix[tree_vert][unconnected_vert]
                    vertex_to_add = unconnected_vert

        self.vertices_not_in_tree.remove(vertex_to_add)
        self.vertices_in_tree.add(vertex_to_add)
        self.mst_edge_weight += minimum_edge_weight


def fully_connected_weight(adj_list):
    return sum([sum(x) for x in adj_list]) / 2


tree = PrimTree(numeric_rows)

while len(tree.vertices_not_in_tree) > 0:
    tree.add_edge()
fcw = fully_connected_weight(zero_l)
print("savings -> ", (fcw - tree.mst_edge_weight))


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 3,  Borůvka s greedy algorithm --------------------------')
t1  = time.time()

# ==== Fri, 18 Nov 2016, 09:04, mbh038, England
# First, I implemented Borůvka's greedy algorithm, in 40-45 ms.
# I found this easier to understand than to code, and judging by other Python times posted here,
# there must be some wasted time I can cut out. I have adapted hansaplast's concise i/o code to read
# in the original network, in my case as a dict of nodes, each with a list of weighted adjacancies as its value.

import numpy as np

def p107Boruvka(filename):
    """
   Uses Boruvka's algorithm to find the minimum spanning tree of a network and weight saving of this compared to the original.
    """
    #read in network from file as dict of adjacancies, with weights
    network=  {i+1:set([(j+1,int(c)) for j,c in enumerate(l.strip().split(',')) if
                c != '-' and i>j]) for i,l in enumerate(open(filename))}

    # 'trees' starts as dict of each vertex in network
    # 'where' keeps track of which sub-network to which each vertex belongs
    trees,where={},{}
    for i in range(1, len(network)+1):
        trees[i]=set([i])
        where[i]=i

    # create empty mst network
    mstEdges=set()
    #loop until we have just one sub-network - this will be the mst
    while len(trees)>1:
        #find minimum weighted edge out of each sub-network
        edges=set()
        for tree in trees:
            for node in trees[tree]:
                try:
                    minedges=[x for x in network[node] if x[0] not in trees[tree]]
                    v1,v2=[x for x in minedges if x[1] == min([x[1] for x in minedges])][0]
                    edges.add((node,v1,v2))
                except IndexError:
                    pass

        #find minimum of these and add it to the mst
        cost=np.inf
        for v1,v2,w in edges:
            if w<cost:
                cost=w
                c1,c2,cw=(v1,v2,w)
        mstEdges.add((c1,c2,cw))

        #update subnetworks in 'trees', and locations in 'where'.
        v1,v2=where[c1],where[c2]
        for node in trees[v1]:
            trees[v2].add(node)
            where[node]=v2
        del(trees[v1])

    mstWeight=sum([x[2] for x in mstEdges])
    originalWeight=sum([sum([x[1] for x in v]) for k,v in network.items()])
    print(originalWeight-mstWeight )
    return mstEdges

p107Boruvka(filename)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 4,  Prim  --------------------------')
t1  = time.time()

# Thu, 10 Nov 2016, 22:03, Khalid, Saudi Arabia
# I used prim's algorithm, was fun to implement.  The code is a bit verbose.

import csv
import heapq

class Edge:
    def __init__(self, u, v, weight):
        self.u = u
        self.v = v
        self.weight = weight

    def __str__(self):

        return "[({0}, {1}): {2}]".format(self.u, self.v, self.weight)

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return (self.u == other.u and self.v == other.v) or (self.v == other.u and self.u == other.v)
    def __ne__(self, other):
        return not __eq__(self, other)

    def __gt__(self, other):
        return self.weight > other.weight
    def __lt__(self, other):
        return self.weight < other.weight
    def __ge__(self, other):
        return self.weight >= other.weight
    def __le__(self, other):
        return self.weight <= other.weight

def prim(vertices, edge_count):
    q = []

    vertex_count = len(vertices.keys())
    result = {}

    visited = [False] * vertex_count

    current = 0
    i = 0
    while i < vertex_count:
        if (not visited[current]):
            visited[current] = True
            for edge in vertices[current]:
                if not visited[edge.v]:
                    heapq.heappush(q, edge)
            minEdge = heapq.heappop(q)

            if not visited[minEdge.v]:
                if minEdge.v not in result:
                    result[minEdge.v] = []
                if minEdge.u not in result:
                    result[minEdge.u] = []
                result[minEdge.v].append(minEdge)
                result[minEdge.u].append(minEdge)

            current = minEdge.v
            i += 1
        else:
            minEdge = heapq.heappop(q)

            if not visited[minEdge.v]:
                if minEdge.v not in result:
                    result[minEdge.v] = []
                if minEdge.u not in result:
                    result[minEdge.u] = []
                result[minEdge.v].append(minEdge)
                result[minEdge.u].append(minEdge)

            current = minEdge.v
    return result

def total_weight(network): # calculates double the weight and then divides by 2
    weight = 0
    for vertex in network:
        for edge in network[vertex]:
            weight += edge.weight
    return weight / 2

f = open(filename, 'r')

vertices = {}
edge_count = 0

try:
    reader = csv.reader(f)
    i = 0
    for vertex_data in reader:
        for j in range(len(vertex_data)):
            if i == j:
                break
            if vertex_data[j] != '-':
                edge_count += 1
                if i not in vertices:
                    vertices[i] = []
                if j not in vertices:
                    vertices[j] = []
                vertices[i].append(Edge(i, j, int(vertex_data[j])))
                vertices[j].append(Edge(j, i, int(vertex_data[j])))
        i += 1
finally:
    f.close()

result = prim(vertices, edge_count)
original_weight = total_weight(vertices)
final_weight = total_weight(result)

print (original_weight, "-", final_weight, "=", original_weight - final_weight)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 5,   --------------------------')
t1  = time.time()

from operator import itemgetter
import time

def gather_graph_data (filename):
    graph_matrix = []
    with open(filename, 'r') as f:
        for line in f:
            x_break = line.replace ('-', '0')
            x1 = (x_break.strip()).split(',')
            x_int = [int(x) for x in x1]
            graph_matrix.append(x_int)

    return graph_matrix
#------------------------------------------------------------------------------
# Create dictionary listing where each vertex connects to along with the
# weight of the edge
def clean_graph_data (graph_matrix):
    vertex_dict = {}
    for i in range(len(graph_matrix)):
        vertex_list = []
        for j in range(len(graph_matrix[i])):
            if graph_matrix[i][j] != 0:
                vertex_list.append((j, graph_matrix[i][j]))
        vertex_list.sort(key = itemgetter(1))
        vertex_dict[i] = vertex_list
    return vertex_dict
#-------------------------------------------------------------------------------
# For each component in the component list, finds the lowest weighted edge
# mapping outside of it
# This edge must be part of the minimal mapping, so the joined components
# and the edge are all listed in a new component. This list of new components
# is returned
def component_grouping (component_list, vertex_dict):
    new_component_list = []
    new_component_elts = set([])

    for component in component_list:
        vertex_list = component[0]
        min_weight, index = 0, 0
        for vertex in vertex_list:
            if min_weight == 0:
                min_weight = vertex_dict[vertex][0][1] # list sorted by weight
                vertex2 = vertex_dict[vertex][0][0]
                vertex1 = vertex
            else:
                if vertex_dict[vertex][0][1] < min_weight:
                    min_weight = vertex_dict[vertex][0][1]
                    vertex2 = vertex_dict[vertex][0][0]
                    vertex1 = vertex

        new_edge = (min(vertex1, vertex2), max(vertex1, vertex2))

        new_component_list, new_component_elts = combine_components (new_component_list,
                                                                     new_component_elts,
                                                                     component_list,
                                                                     new_edge)

    return new_component_list, new_component_elts

# Having found the minimum weight edge, this function decides how to
# combine the components of the two vertices of that edge
def combine_components  (new_component_list, new_component_elts,
                         component_list, new_edge):

    vertex1, vertex2 = new_edge[0], new_edge[1]

    index1, index2 = 0, 0
    flag1_new, flag2_new = 0,0
    if vertex1 in new_component_elts:
        flag1_new = 1
        while vertex1 not in new_component_list[index1][0]:
            index1 += 1
    else:
        while vertex1 not in component_list[index1][0]:
            index1 += 1
    if vertex2 in new_component_elts:
        flag2_new = 1
        while vertex2 not in new_component_list[index2][0]:
            index2 += 1
    else:
        while vertex2 not in component_list[index2][0]:
            index2 += 1

    new_component_elts = list(new_component_elts)

    if (flag1_new, flag2_new) == (1,1):  # both in new_components
        comp_index1, comp_index2 = min(index1, index2), max(index1, index2)
        if comp_index1 != comp_index2:
            combined_component = add_two_components (new_component_list[comp_index1],
                                            new_component_list[comp_index2], new_edge)
            new_component_list[comp_index1] = combined_component
            del new_component_list[comp_index2]
        else:
            new_component_list[comp_index1][1].add(new_edge)

    if (flag1_new, flag2_new) == (1,0):
        combined_component = add_two_components (new_component_list[index1],
                                            component_list[index2], new_edge)
        new_component_list[index1] = combined_component
        new_component_elts += component_list[index2][0]

    if (flag1_new, flag2_new) == (0,1):
        combined_component = add_two_components (component_list[index1],
                                            new_component_list[index2], new_edge)
        new_component_list[index2] = combined_component
        new_component_elts += component_list[index1][0]

    if (flag1_new, flag2_new) == (0,0):
        combined_component = add_two_components (component_list[index1],
                                                 component_list[index2], new_edge)
        new_component_list.append (combined_component)
        new_component_elts += (component_list[index1][0] +
                               component_list[index2][0])

    return new_component_list, set(new_component_elts)

# This combines two components' elements and returns the result as a single component
def add_two_components (component1, component2, new_edge):
    final_component = []
    final_component.append(component1[0] + component2[0])
    final_component.append(component1[1].union(component2[1]))
    final_component[1].add (new_edge)
    return final_component
#-------------------------------------------------------------------------------------------
# This alters the dictionary containing the vertices and weights that any given vertex
# maps to
# It mods out based on elements in the same component class. So it will only contain
# vertices that are outside of the mapped vertex's component class

def vertex_dict_component_mod (vertex_dict, component_list):

    for component in component_list:
        vertex_list = component[0]

        for vertex in vertex_list:
            prev_dict_list = vertex_dict[vertex]
            new_list = [vertex_pair for vertex_pair in prev_dict_list if vertex_pair[0]
                        not in vertex_list]
            vertex_dict[vertex] = new_list

    return vertex_dict

def calc_total_savings (graph_matrix, edge_list):
    orig_weight_sum = 0

    for vertex in graph_matrix:
        orig_weight_sum += sum(vertex)
    orig_weight_sum = orig_weight_sum / 2  # adjust for double count

    min_weight_sum = 0
    for edge_tuple in edge_list:
        min_weight_sum += graph_matrix[edge_tuple[0]][edge_tuple[1]]

    return (orig_weight_sum - min_weight_sum)


def main():
    start_time = time.time()

    graph_matrix = gather_graph_data (filename)
    vertex_dict = clean_graph_data (graph_matrix)
    component_list = [[[i], set([])] for i in range(len(graph_matrix))]

    while len(component_list) > 1:
        component_list, component_elts = component_grouping (component_list, vertex_dict)

        vertex_dict = vertex_dict_component_mod (vertex_dict, component_list)

    print (calc_total_savings (graph_matrix, list(component_list[0][1])))
    print (time.time() - start_time)

main()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 6, Prim Algorithm  --------------------------')
t1  = time.time()

# ===== Sat, 18 Jun 2016, 23:37, kakariko, Scotland
# Prim's algorithm runs in 315ms. One hit at the profiler said it spent most of it's time in the sort function so I added a line
# (#commented out in this source) to strip the closed_set nodes from the open_set which cut the time down to 45ms
# # by avoiding sorting and re-sorting entries it was never going to use.

graph = {}
total = 0

with open(filename) as f:
    for u, line in enumerate(f):
        for v, edge in enumerate(line.split(',')):
            if edge.rstrip() == '-':
                continue
            elif u in graph.keys():
                graph[u][v] = int(edge)
            else:
                graph[u] = {v:int(edge)}
            total += int(edge)
    total //= 2

def explore(start):
    open_set = [(start,0)]
    closed_set = []
    total = 0

    while len(open_set) > 0:
        current_node = sorted(open_set, key=lambda x: x[1])[0]
        open_set.remove(current_node)
        if current_node[0] in closed_set:
            continue

        closed_set.append(current_node[0])

        total += current_node[1]
        open_set.extend([(n, graph[current_node[0]][n]) for n in graph[current_node[0]].keys()])

        #trim the open set
        #open_set = [(a, b) for a, b in open_set if a not in closed_set]

    return total

print(total - explore(0))


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 7, Prim Algorithm  --------------------------')
t1  = time.time()

# ==== Fri, 1 Jan 2016, 17:39, rosetta
# Implemented Prim's algorithm using heaps. Takes 0.00134181976318 ms.

import heapq
f = open(filename, 'r')
# process data from file.
graph = {}
curr = 0
for line in f:
    graph[curr] = {}
    nodes = line.strip().split(",")
    number = len(nodes)
    for neighbour in range(number):
        if nodes[neighbour] != '-':
            graph[curr][neighbour] = int(nodes[neighbour])
    curr += 1



heap = []
start_node = 0
spanning_tree = set([start_node])

for neighbour in graph[start_node]:
    edge = graph[start_node][neighbour]
    heapq.heappush(heap, (edge, (start_node, neighbour)))

cost = 0
while len(spanning_tree) != len(graph):
    edge_cost, (a, b) = heapq.heappop(heap)
    if b not in spanning_tree:
        spanning_tree.add(b)
        cost += edge_cost
        for neighbour in graph[b]:
            edge = graph[b][neighbour]
            heapq.heappush(heap, (edge, (b, neighbour)))

def total_cost(graph):
    """
    Finds the total cost of edges.
    """
    nodes = len(graph)
    cost = 0
    for node in graph:
        for neighbour in graph[node]:
            if neighbour > node:
                cost += graph[node][neighbour]
    return cost

print (total_cost(graph) - cost)


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 8,  Algorithm  --------------------------')
t1  = time.time()

# ==== Sat, 20 Dec 2014, 08:55, skyivben, China

edges = set()
for v1,line in enumerate(open(filename)):
  for v2,weight in enumerate(line.split(',')):
    if weight.strip() != '-':
      i,j = v1 > v2 and (v1,v2) or (v2,v1)
      edges.add((int(weight), i, j))
gs = dict((i,i) for i in range(40))
total = 0 # Kruskal's algorithm
for w,v1,v2 in sorted(edges):
  if (gs[v1] != gs[v2]):
    for v in [v for (v,g) in gs.items() if g == gs[v2]]:
      gs[v] = gs[v1]
    total += w
    if(len(set(gs.values())) == 1): break
print(sum(w for (w,_,_) in edges) - total)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 9,  Algorithm  --------------------------')
t1  = time.time()
'''

import networkx as nx
import numpy as np
import time
import matplotlib.pyplot as plt

def intSpec(str_):
    if str_ == '-':
        return 0
    else:
        return int(str_)


f = open ( filename , 'r')               # Readin the text file.
matrix0 = [map(intSpec, row.strip().split(',')) for row in f]
len_ = len(matrix0)
matrix = np.arange(0, len_**2).reshape(len_, len_)


totalSum = 0  # Creating a matrix, array of numpy. Calculating the total of weights
for i in range(len_):
    for j in range(len_):
        if i > j:
            matrix[i, j] = matrix0[i][j]
            totalSum +=  matrix[i, j]

G = nx.cycle_graph(0) #Initialize the cycle_graph
e = []
nodeList = []
nodes =  'ABCDEFGHIJKLMNOPQRSTUVWXYabcdefghijklmno'

for i in range(len(nodes)):  #Entering the list of nodes.
    nodeList.append(nodes[i])

for i in range(len(nodeList)): #Entering tha data to create the graph
        for j in range(len(nodeList)):
            if i == j:
                continue
            if matrix[j][i] == 0:
                continue
            if matrix[i][j] != 0:
                edge_ij = (nodeList[i], nodeList[j], matrix[i][j])
                e.append(edge_ij)

G.add_weighted_edges_from(e)

#print "G", (sorted(G.edges(data=True))) #Printing the optimized graph
#print
T = nx.minimum_spanning_tree(G) #(Kruskal Algorithm)
#print "T", (sorted(T.edges(data=True)))
optimWeights = 0
for tuple_ in (sorted(T.edges(data=True))): # Obtaining the sum of weights for the optmized Graph
    dict_ = tuple_[2]
    weight = dict_.values()
    optimWeights += weight[0]

print ("Previous total weights ", totalSum)   # Printing results
print ("Optimized weights having all nodes connected ", optimWeights)
print ("Saved weights ", totalSum - optimWeights)

#nx.draw_random(G)  # Plotting the original graph
#plt.show()
#nx.draw_random(T)  #Plotting the optimized graph
#plt.show()
'''

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')



print('\n--------------------------SOLUTION 10,  Algorithm  --------------------------')
t1  = time.time()

# ==== Sat, 20 Dec 2014, 08:55, skyivben, China

edges = set()
for v1,line in enumerate(open(filename)):
  for v2,weight in enumerate(line.split(',')):
    if weight.strip() != '-':
      i,j = v1 > v2 and (v1,v2) or (v2,v1)
      edges.add((int(weight), i, j))
gs = dict((i,i) for i in range(40))
total = 0 # Kruskal's algorithm
for w,v1,v2 in sorted(edges):
  if (gs[v1] != gs[v2]):
    for v in [v for (v,g) in gs.items() if g == gs[v2]]:
      gs[v] = gs[v1]
    total += w
    if(len(set(gs.values())) == 1): break
print(sum(w for (w,_,_) in edges) - total)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 11,  PRIM Algorithm  --------------------------')
t1  = time.time()

# ==== Sat, 9 May 2015, 20:41, mmaximus, Portugal
# Solution implementing Prim's algorithm:

def convert(s):
    try:
        return int(s)
    except ValueError:
        return -1

with open(filename) as file:
    content = file.read().splitlines()
    m = [[convert(a) for a in line.split(',')] for line in content]

N = len(m)
V = {i for i in range(1, N)}
T = {0}
reduced_weight = 0
while V:
    local_min = 10 ** 5
    where_t = 100
    where_v = 100
    for t in T:
        for v in V:
            current = m[t][v]
            if current > 0:
                if current < local_min:
                    local_min = current
                    where_v = v
                    where_t = t
    reduced_weight += m[where_t][where_v]
    T.add(where_v)
    V.remove(where_v)

big_sum = 0
for i in range(N):
    for j in range(i, N):
        if m[i][j] > 0:
            big_sum += m[i][j]

print(big_sum - reduced_weight)



t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 12,  KRUSAL  Algorithm  --------------------------')
t1  = time.time()


# ==== Tue, 1 Nov 2005, 17:12, Brian, England
# I kept track of the vertices connected using a dict of vertex :
# group id, where all vertices with the same group id are connected, and used Kruskal's algorithm as below:


edges=set()
for v1,line in enumerate(open(filename)):
    for v2, weight in enumerate(line.split(',')):
        if weight.strip() != '-':
            i,j =  v1>v2 and (v1,v2) or (v2,v1)
            edges.add((int(weight), i, j))

tot =  sum(w for (w,v1,v2) in edges)
groups = dict((i,i) for i in range(40))
newtot=0
for w,v1,v2 in sorted(edges):
    if (groups[v1] != groups[v2]):
        for vert in [v for (v,g) in groups.items()
                     if g == groups[v2]]:
            groups[vert] = groups[v1] # Merge groups
        newtot += w
        if(len(set(groups.values())) == 1): break

print (tot - newtot)


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')