#  Created by Bogdan Trif on 16-11-2017 , 11:42 AM.
"""
Author: Valerio Velardo
Email: valerio@melodrive.com

This file contains an implementation of breadth-first search (BFS) for
traversing a graph, and for getting the shortest path between 2 nodes
of a graph.
"""

# https://pythoninwonderland.wordpress.com/2017/03/18/how-to-implement-breadth-first-search-in-python/
# In particular, BFS follows the following steps:
#
# 1.  Check the starting node and add its neighbours to the queue.
# 2.  Mark the starting node as explored.
# 3.  Get the first node from the queue / remove it from the queue
# 4.  Check if node has already been visited.
# 5.  If not, go through the neighbours of the node.
# 6.  Add the neighbour nodes to the queue.
# 7.  Mark the node as explored.
# 8.  Loop through steps 3 to 7 until the queue is empty.
#
# To implement the BFS queue a FIFO (First In, First Out) is used. In FIFO queues,
# the oldest (first) entry is processed first.
# The process is similar to what happens in queues at the post office.
# Who arrives first is served first.



# visits all the nodes of a graph (connected component) using BFS
def bfs_connected_component(graph, start):
    # keep track of all visited nodes
    explored = []
    # keep track of nodes to be checked
    queue = [start]

    # keep looping until there are nodes still to be checked
    while queue:
        # pop shallowest node (first node) from queue
        node = queue.pop(0)
        if node not in explored:
            # add node to list of checked nodes
            explored.append(node)
            neighbours = graph[node]

            # add neighbours of node to queue
            for neighbour in neighbours:
                queue.append(neighbour)
    return explored


# finds shortest path between 2 nodes of a graph using BFS
def bfs_shortest_path(graph, start, goal):
    # keep track of explored nodes
    explored = []
    # keep track of all the paths to be checked
    queue = [[start]]

    # return path if start is goal
    if start == goal:
        return "That was easy! Start = goal"

    # keeps looping until all possible paths have been checked
    while queue:
        # pop the first path from the queue
        path = queue.pop(0)
        # get the last node from the path
        node = path[-1]
        if node not in explored:
            neighbours = graph[node]
            # go through all neighbour nodes, construct a new path and
            # push it into the queue
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                # return path if neighbour is goal
                if neighbour == goal:
                    return new_path

            # mark node as explored
            explored.append(node)

    # in case there's no path between the 2 nodes
    return "So sorry, but a connecting path doesn't exist :("


if __name__ == '__main__':

    # sample graph represented by a dictionary
    graph = {'A': ['B', 'C', 'E'],
             'B': ['D', 'E'],
             'C': ['A', 'F', 'G'],
             'D': ['B'],
             'E': ['B', 'A'],
             'F': ['C'],
             'G': ['C']
             }

    print("\nHere's the nodes of the graph visited by "
          "breadth-first search, starting from node 'A': ",
          bfs_connected_component(graph, 'A'))

    print("\nHere's the shortest path between nodes 'G' and 'D':",
          bfs_shortest_path(graph, 'G', 'D'))


############### Using deque from collections    ##############

# https://codereview.stackexchange.com/questions/135156/bfs-implementation-in-python-3
# sets perform containing checks (w in visited) O(1) rather than O(n) for lists.
# collections.deque are better than lists for poping elements at the front (popleft).
# you should put your example code under an if __name__ == '__main__' clause.
# w as a variable name does not convey meaning, you should try to come up with something more explicit.




import collections

def breadth_first_search(graph, root):
    visited, queue = set(), collections.deque([root])
    while queue:
        vertex = queue.popleft()
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)


if __name__ == '__main__':
    graph = {0: [1, 2], 1: [2], 2: []}
    breadth_first_search(graph, 0)


#################

# I agree with Mathias Ettinger's use of sets and deques, with two changes:
#
# name the set seen instead of visited, because your algorithm adds to set before visiting.
# add the root to seen before entering while loop.
# Otherwise the root may be revisited (eg test case below where 1 points back to 0).


def bfs(graph, root):
    seen, queue = set([root]), collections.deque([root])
    while queue:
        vertex = queue.popleft()
        visit(vertex)
        for node in graph[vertex]:
            if node not in seen:
                seen.add(node)
                queue.append(node)

def visit(n):
    print(n, end = '     ')

if __name__ == '__main__':
    graph = {0: [1, 2], 1: [2, 0], 2: []}
    bfs(graph, 0)







