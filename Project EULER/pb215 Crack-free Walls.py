#  Created by Bogdan Trif on 18-09-2017 , 9:09 PM.
#                  o(^_^)o         ( ͡° ͜ʖ ͡°)
# © Solved by Bogdan Trif @     Completed on Tue, 1 May 2018, 10:44
#The  Euler Project  https://projecteuler.net
'''
                    Crack-free Walls        -           Problem 215

Consider the problem of building a wall out of 2×1 and 3×1 bricks (horizontal×vertical dimensions) such that,
for extra strength, the gaps between horizontally-adjacent bricks never line up in consecutive layers,
i.e. never form a "running crack".

For example, the following 9×3 wall is not acceptable due to the running crack shown in red:

There are eight ways of forming a crack-free 9×3 wall, written W( 9 , 3 ) = 8.

Calculate W( 32 , 10 ).

'''
import functools
import time, zzz


# must make a function which do a partition only in elements of 2 and 3
from functools import reduce


def partition_nr_into_given_set_of_nrs(nr, S):
    nrs = sorted(S, reverse=True)
    def inner(n, i):
        if n == 0:
            yield []
        for k in range(i, len(nrs)):

            if nrs[k] <= n:
                for rest in inner(n - nrs[k], k):

                    yield [nrs[k]] + rest
    return list(inner(nr, 0))


def combinations(N, length) :
    if length == 0:
        print('---'*20)
        yield []

    for i in range(len(N)) :
        for j in combinations( N[i+1:], length-1 ) :
            print(i,j ,  '       ', N[i+1:],  j , '       ' , [ N[i] ] + j )

            if [N[i]][-1] != 2 :
                yield [ N[i] ] + j

# N= [ 1, 2, 4, 8, 16, 32 ]
# print( '\nResult :\n',list( combinations(N, 4) ) )

def unique_permutations(lst):
    ''':Description: Takes a list and makes ONLY Unique Permutations of a list with repeated elements.
    :param lst: type list
    :return:    a list of lists containing all the permutations
    '''
    if len(lst) == 1:
        yield (lst[0],)
    else:
        unique_lst = set(lst)
        for first_element in unique_lst:
            remaining_lst = list(lst)
            remaining_lst.remove(first_element)
            for sub_permutation in unique_permutations(remaining_lst):
                yield (first_element,) + sub_permutation


def check_compatibility(prev_row, current_row):
    ''' Returns False if there is no compatibility, e.g. there are running cracks from a row to another '''
    if len(prev_row) == len(current_row) :
        length = len(prev_row)-1
    else :
        length = min( len(prev_row) , len(current_row) )

    l1, l2 = 0, 0
    S = set()
    for i in range( length ):
        l1 += prev_row[i]
        l2 += current_row[i]
        S = S.union({l1, l2})
#         print (l1, l2,'    ', S )

        if len(S) != 2*(i+1) :
            return False

    return True





print('\n--------------------------TESTS------------------------------')
t1  = time.time()



r1, r2 = (3, 3, 3), (2, 2, 2, 3)
check_compatibility(r1, r2)



print('-----'*20)


# def Walls(N , length, max, counter) :
#
#     if length == 0 : yield []
#
#     for i in range(len(N)) :
#         for j in Walls( N[i+1:], length-1, max, counter ) :
# #             print(i,j ,  '       ', N[i+1:], '  ', j , '       ' , [ N[i] ] + j ,'    ', length)
#             S = [ N[i] ] + j
#
#             if 1 < len( [ N[i] ] + j )  :
#
#                 print(S , '       comb this  ', S[0],'      with that    ' ,S[1], '     check_comp = ',check_compatibility( S[0], S[1] )  , '        ' ,length)
#                 # if not check_compatibility( S[0], S[1] )  :
#                 #     continue
#
#
#             if len( [ N[i] ] + j ) == max :
#                 counter +=1
#                 print(str(counter)+'.      ',  [ N[i] ] + j  )
#
#             yield [ N[i] ] + j
#
#
# K =  list( Walls( R , 3, 3 , 0 ) )
# print('\nThere are : ', len(K),'\n', K )

# def solve_Walls(R) :
#     pos = 0


def ugly_ugly_brute_force_small_case( cols  ) :
    S = [ 2 , 3 ]
    P = partition_nr_into_given_set_of_nrs( cols, S )
    print('P :', P)
    R = []
    for part in P :
        u = list(unique_permutations(part))
        R+= u

    print('R : ', len(R),'\n', R)

    good = 0
    for i in range(len(R)) :
        for j in range(len(R)) :
            if check_compatibility(R[i], R[j]  ) :
                for k in range(len(R)) :
                    if check_compatibility(R[j] ,  R[k]   ) :
                        for l in range(len(R)) :
                            if check_compatibility(  R[k] ,    R[l]   ) :
                                good += 1
                                print(str(good)+'.      ' ,  i, j, k, l,   '          ' , R[i] ,  R[j] ,  R[k],  R[l] )

    return print( '\nAnswer : ' + str(good) )

ugly_ugly_brute_force_small_case( 12 )


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')

print('\n================  My FIRST SOLUTION,   ===============\n')
t1  = time.time()

class Crack_Free_Walls(object):
    def __init__(self, max_length, lst_of_nrs, row_nr ):
        self.max_length = max_length
        self.lst_of_nrs = lst_of_nrs
        self.row_nr = row_nr
        self.all_Rows = self.generate_Rows(  )
        self.ROWS = self.build_data_Structure( )


    def generate_Rows(self ) :
        Rows = []
        P = partition_nr_into_given_set_of_nrs( self.max_length, self.lst_of_nrs )
        print(len(P), P)
        tot = 0
        for I in P :
            UP = list(unique_permutations(I))
            # print(len(UP), UP)

            for j in range(len(UP)) :
                # print(UP[j])
                X , x =set(), 0
                for k in UP[j] :
                    x += k
                    X.add(x)
                X.remove(self.max_length)
                # print(X)
                Rows.append(X)
            tot += len(UP)
        print('\nall_Rows number :', tot )
        print('all_Rows :', len(Rows), Rows[:100] )
        return Rows


    def check_compatibility(self, row1, row2):
        intersection = ( row1 & row2 )
        if len(intersection) == 0 :
            return True
        return False

# print('check_compatibility :',check_compatibility( {3, 6, 9}, {2, 4, 7, 9 }  ) )

    def build_data_Structure(self ) :        ### Build data structure of ROWS :
        ROWS = dict()
        ALL = self.all_Rows
        for i in range(len(ALL)):
            # L1, L2 = all_Rows[:i] , all_Rows[i+1:]
            # print(i, '    ', ALL[i], '      ' )
            for j in range(i+1, len(ALL)) :
                # print(' i, j  = ', ALL[i], '    ', ALL[j] )

                set_intersection =  ALL[i] & ALL[j]

                if len(set_intersection) == 0 :
                    a1, a2 = int(''.join( str(i) for i in  sorted(ALL[i] ) ) ), int(''.join( str(i) for i in  sorted( ALL[j] )))
                    # print(' a1, a2 =  ', a1, a2 )

                    if a1 not in ROWS :
                        ROWS[ a1 ] = [a2]
                    else :
                        ROWS[ a1 ].append(a2)

                    if a2 not in ROWS :
                        ROWS[ a2 ] = [a1]
                    else :
                        ROWS[ a2 ].append(a1)
        print('\nROWS : ', len(ROWS)    ,'\n' )
        return ROWS

    def good_fib(self, n, F ):
        if n==1 : return F[0]
        if n==2 : return F[1]
    #     F = [1, 1]
        for i in range(1,n) :
            F.append(F[:][-1]+F[:][-2])
            # print(F)
        return F[-1]

# good_fib(6, [1, 1])

    @functools.lru_cache(maxsize=None)
    def count_configurations( self, elem , rows ) :
        if rows == 1 :
            return len(self.ROWS[elem])
        else:
            return  sum( [ self.count_configurations( k, rows-1 ) for k in self.ROWS[elem] ] )

    def crack_free_walls(self):
        total = 0
        for elem, v in self.ROWS.items() :
            cnt = self.count_configurations( elem, self.row_nr )
            print(str(elem) + '   count = ', cnt )
            total += cnt

        return print('\nTotal_configurations :' , total )


# solution_iteration(ROWS, 2) #####   iter should be iter-1 = levels. Example if 3 rows => iter = 2
rows = 10
cols = 32
# SOL = Crack_Free_Walls( cols, [2, 3], rows-1 ).crack_free_walls()           # Answer : Total_configurations : 806844323190414


t2  = time.time()
print('\nCompleted in :', round((t2-t1), 2 ), 's\n\n')          #   Completed in : 6.75 s


# ============= IDEAS =============
# Sat, 15 Nov 2008, 01:43, Three3K
#
# W(w,h)
#
# 1.) Build all possible n lines, for W(9,3):
#
# |2223,2232,2322,3222,333|
#
# 2.) Construct n*n transition matrix T, for W(9,3):
#
# |0,0,1,0,0|
# |0,0,0,0,1|
# |1,0,0,0,0|
# |0,0,0,0,1|
# |0,1,0,1,0|
#
# 3.) Construct n-dimensional count vector C[h] using C[i] = T * C[i-1] and C[1] = |1,1,1..1|, for W(9,3):
#
# |0,0,1,0,0| * |1,1,1,1,1| = |1,1,1,1,2|
# |0,0,0,0,1|
# |1,0,0,0,0|
# |0,0,0,0,1|
# |0,1,0,1,0|
#
# |0,0,1,0,0| * |1,1,1,1,2| = |1,2,1,2,2|
# |0,0,0,0,1|
# |1,0,0,0,0|
# |0,0,0,0,1|
# |0,1,0,1,0|
#
# 4.) W(w,h) = |1,1,1..1| * C[h], for W(9,3):
#
# |1,1,1,1,1| * |1,2,1,2,2| = 8


print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1,   --------------------------')
t1  = time.time()


# ==== Tue, 1 Sep 2015, 17:20, jwpowell, USA
# DP solution.  Build base layer (all 32x1 walls) using recursion with memoization.
# Represent these layers by bitstrings as others did too.  Then compute which layers can stack (call these "friends")
# on top of a given layer in a custodial dictionary used to avoid repeatedly checking compatibility during the last step.
# Finally, we maintain a dictionary with pairs (height, top layer) as keys,
# and values equal to the number of ways to build the wall with given height and top layer.
# Then, walls of height n+1 with a given top layer number the sum of all height-n walls whose top layer is a friend of the new top layer.
# We want height 10 without caring what the top layer is, so we sum over all values with key (32, _)

memo = {0: [], 1: [], 2: [0], 3: [0]}


def build_base(N):
    """
    returns dict.  key = width of one-layer deep walls, values are bitstrings
    where a layer with cracks at positions a, b, c, ... is the bitstring
    1<<a + 1<<b + 1<<c + ....  This representation lets us easily check for a
    pair of compatible layers (no overlapping cracks) using bitwise AND
    """
    global memo
    if N not in memo:
        memo[N] = ([(x + 1) << 2 for x in build_base(N-2)] +
                   [(x + 1) << 3 for x in build_base(N-3)])

    return memo[N]


def get_friends(layers):
    """friends can stack: friend1 & friend2 == 0"""
    return {layer: [friend
                    for friend in layers
                    if friend & layer == 0]
            for layer in layers}


def stack_layers(M, N):
    """build dict which iteratively stack layers and counts how many walls
    exist with height m and top layer 'layer' rep'd by its bit string, holding
    this at key (m, 'layer') with value = the number of possible walls"""
    base_layer = build_base(N)
    friends = get_friends(base_layer)

    # initialize the stack
    stack = {(1, layer): 1
             for layer in base_layer}

    # build the stack up
    for m in range(2, M+1):
        for layer in base_layer:
            stack[(m, layer)] = sum([stack[(m-1, friend)]
                                     for friend in friends[layer]])

    return stack


def count_stacks(M, N):
    """helper method summing up the values of all walls with a given height
    regardless of the top layer"""
    return sum([v for (k, v) in stack_layers(M, N).items()
                if k[0] == M])


# if __name__ == '__main__':     print(count_stacks(10, 32))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')


print('\n--------------------------SOLUTION 2, Iterative solution  --------------------------')
t1  = time.time()

# ===Fri, 16 Aug 2013, 09:40, kubluck, USA
# Nothing new here, just happy that I got it first try so here's my solution. Iterative DP in Python, took about 4 seconds.

def createRows(n):
    if n == 2:
        return [[2]]
    if n == 3:
        return [[3]]
    if n == 4:
        return [[2, 2]]
    rows = []
    rows += [row + [3] for row in createRows(n - 3)]
    rows += [row + [2] for row in createRows(n - 2)]
    return rows

def accum(row):
    crack = [row[0]]
    for i in range(1, len(row) - 1):
        crack += [crack[-1] + row[i]]
    return crack

def disjoint(x,y):
    for i in x:
        if i in y:
            return False
    return True

def collect(n):
    cracks = [accum(row) for row in createRows(n)]
    v = [[]] * len(cracks)
    for i in range(len(cracks) - 1):
        for j in range(i + 1, len(cracks)):
            if disjoint(cracks[i],cracks[j]):
                v[i] = v[i] + [j]
                v[j] = v[j] + [i]
    return v

def go(a,b):
    walls = collect(a)
    v = [1] * len(walls)
    i = 1
    while i < b:
        v = [sum([v[j] for j in wall]) for wall in walls]
        i += 1
    print(sum(v))

# go(32,10)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')


print('\n--------------------------SOLUTION 3, SLOW, 3 min, Tranzition Matrix  --------------------------')
t1  = time.time()

# === Wed, 7 Jan 2015, 18:46, wakkadojo, USA
# Almost all the time is spent calculating the "transition matrix" that tells us which walls we can build into which others.
# Otherwise, straightforward DP


def generate_walls (w, n):
    if n not in w:
        w[n] = []
        for x in generate_walls (w, n-2):
            w[n] += [[2] + x]
        for x in generate_walls (w, n-3):
            w[n] += [[3] + x]
    return w[n]

def build_transition_matrix (w): # order of wall labeling doesn't matter
    t = [ [ 0 for _ in w ] for _ in w ]
    for i in range (len (w)):
        for j in range (i):
            si = [ sum (w[i][:k+1]) for k in range (len (w[i])) ]
            sj = [ sum (w[j][:k+1]) for k in range (len (w[j])) ]
            if len (set (si+sj)) < len (w[i]) + len (w[j]) - 1:
                t[i][j] = t[j][i] = 0
            else:
                t[i][j] = t[j][i] = 1
    return t

def mult (m, v):
    return [ sum (x[j]*v[j] for j in range (len (x))) for x in m ]

def main_3() :
    d = {}
    d[0], d[1], d[2], d[3] = [], [], [[2]], [[3]]
    w = generate_walls (d, 32)
    t = build_transition_matrix (w)
    print ('ho')
    num  = [ 1 for _ in w ]
    for i in range (10-1):
        num = mult (t, num)
    print (sum (num))

# main_3()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')


print('\n--------------------------SOLUTION 4,  12 sec --------------------------')
t1  = time.time()

# === Thu, 19 Apr 2012, 05:35, ving, USA
# DP. Again. :(  I represented rows as bitstrings; no cracks means row & next == 0.  10 secs in slow Python 3.

from time import clock
time1 = clock()

N, M = 12, 4  # Answer: 52
N, M = 32, 10  # Answer: 806844323190414

def all_rows(n, s = ""):
    h = len(s)
    if h == n:
        yield int(s[:-1], 2)
    else:
        if h <= n - 2:
            for row in all_rows(n,  s + "01"):
                yield row
        if h <= n - 3:
            for row in all_rows(n,  s + "001"):
                yield row

def update(rows, cnts):
    n = len(cnts)
    newcnts = n*[0]
    for i in range(1, n):
        x = rows[i]
        for j in range(i):
            if x & rows[j] == 0:  # no cracks
                newcnts[i] += cnts[j]
                newcnts[j] += cnts[i]
    return newcnts

def main_4() :
    rows = [x for x in all_rows(N)]
    cnts = len(rows) * [1]
    for r in range(1, M):
        cnts = update(rows, cnts)

    print(sum(cnts))

    time2 = clock()
    print("{0:d}x{1:d} Time = {2:.1f}".format(N, M, time2 - time1))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')


print('\n--------------------------SOLUTION 5,   --------------------------')
t1  = time.time()

# === Wed, 17 Dec 2008, 08:29, dho
# I applied for a job, and they emailed me this problem verbatim. Luckily I'm a project euler fan.
#
# Anyway, 9.8 seconds in python


def W(w,h):
    """
    Calculate the total number of crack-free walls of size w*h
    (Walls are made of bricks of lengths 2 and 3)

    Each layer of the wall is called a row.

    Rows are represented as a sequence of intermediate sums

    So if the layers of bricks looks like this:
    2, 2, 3, 2,
    3, 3, 3,
    2, 3, 2, 2,

    The intermediate sums looks like this:

    0, 2, 4, 7, 9
    0, 3, 6, 9
    0, 2, 5, 7, 9

    The first and last digits are removed, since they are always the same

    2,4,7
    3,6
    2,5,7

    Now we know that this is a crack-free wall, because adjacent rows share no common numbers

    """
    rows = [] ##number of possible brick rows

    def make_rows(row,width):
        """
        Create all the possible rows of a given width and using the given partial row
        """
        for brick in (2,3):
            test = row[-1]+brick
            if test==width:
                rows.append(row[1:])
                return
            if test>width: return
            make_rows(row+[test],width)

    ##Generate all possible rows of width w
    make_rows([0],w)

    N = len(rows) ##number of possible rows


    def crackfree(A,B):
        "Test if two rows would have a crack"
        for x in A:
            if x in B: return False
        return True


    ##Create a mapping from possible rows
    ##The mapping tells us which rows can be placed adjacent to each other

    rowMap = [[] for i in range(N)]
    for i in range(N):
        for j in range(i,N):
            if i==j: continue
            if crackfree(rows[i],rows[j]):
                rowMap[i].append(j)
                rowMap[j].append(i)

    M = sum([len(rowMap[i]) for i in range(N)]) ##number of row pairs (doubled)

    ##do some dynamic programming to assemble all walls of height h
    ##assemble smaller walls, and use the results to create larger walls

    count_runs = [[1] for i in range(N)]

    for r in range(h-1):
        for i in range(N):
            count_runs[i].append(sum([count_runs[j][r] for j in rowMap[i]]))

    return sum([count_runs[i][h-1] for i in range(N)])



    """
    ##this way is too slow
    def make_wall(i,num_rows,height):
        "assemble a crackfree wall from the list of rows"
        if num_rows==height: return 1
        return sum([make_wall(j,num_rows+1,height) for j in crack_map[i]])
    
    return sum([make_wall(i,1,h) for i in range(N)])
    """


print(W(32,10))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')


print('\n--------------------------SOLUTION 6,  Recursion to generate rows --------------------------')
t1  = time.time()


# ==== Fri, 31 Oct 2008, 15:39, sigh, Australia
# Used DP, can't really see any other way.
# Did it exactly the way DavidF described.
#
# Edit: A description of my algorithm:
# First I find all possible rows. This is done using the row_gen generator in my code.
# The rows are encoded as ints with the ith bit being set to 1 if there break at that point.
#
# Next I find all possible transitions. A transition is only possible if no breaks line up, thus the bitwise AND of my rows must be zero.
#
# I make a lookup table that maps the combinations to the range [0, number of combinations - 1].
#
# From there it's a bottom-up DP.
#
# Here is my python code:

import itertools

def row_gen(w, current):
    if w == 1:
        return
    elif w < 4:
        yield (current << w)
        return

    for r in row_gen(w-2, (current << 2) | 1):
        yield r

    for r in row_gen(w-3, (current << 3) | 1):
        yield r


def p215(w=32, h=10):
    combinations = list(row_gen(w,0))
    transitions = {}

    for c in combinations:
        transitions[c] = [x for x in combinations if  (x & c) == 0]

    value_map = dict(zip(combinations, itertools.count()))

    row_len = len(combinations)
    row = [1]*row_len

    for r in range(h-1):
        prev_row = row
        row = [0]*row_len

        for x in range(row_len):
            v = prev_row[x]
            for t in transitions[combinations[x]]:
                row[value_map[t]] += v

    return sum(row)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')


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




