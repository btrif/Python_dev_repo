#!/usr/bin/python
# Solved by Bogdan Trif @   Completed on Thu, 8 Dec 2016, 23:05
#The  Euler Project  https://projecteuler.net
'''
Counting block combinations I       -       Problem 114

A row measuring seven units in length has red blocks with a minimum length of three units placed on it,
such that any two red blocks (which are allowed to be different lengths) are separated by at least one black square.
There are exactly 17 ways of doing this.

How many ways can a row measuring fifty units in length be filled?

NOTE: Although the example above does not lend itself to the possibility,
in general it is permitted to mix block sizes.
For example, on a row measuring 8 units in length you could use red (3), black (1), and red (4).

'''
import time
import gmpy2

def partitions(n):
    '''     Taken from http://code.activestate.com/recipes/218332-generator-for-integer-partitions/
            Created by David Eppstein on Wed, 27 Aug 2003
    :What it is:    A generator of number partition
    :Usage:     Example:    for i in partitions(5):    print(i)
    :param n:   the number you want the partitions
    :return:    set of lists with all the possible combinations                                                 '''
    # base case of recursion: zero is the sum of the empty list
    if n == 0:
        yield []
        return

    # modify partitions of n-1 to form partitions of n
    for p in partitions(n-1):
        yield [1] + p
        if p and (len(p) < 2 or p[1] > p[0]):
            yield [p[0] + 1] + p[1:]

def unique_permutations(lst):       # VERY EFFECTIVE
    ''':Description: Takes a list and makes ONLY Unique Permutations of a list with repeated elements.
        If one tries itertools.permutations on a list with 14 elements ==> BANG, computer freezes
    :Usage: list(unique_permutations([1,1,1,3]))
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


class GET_ROD_VARIATIONS(object):
    ''':Description: depends on the unique_permutations function.
            *Made by Bogdan Trif @ 2016-12-06, 22:00*
    :param lst: the list to analyze
    :return: int, the final number of available configurations
    '''
    def __init__( self, lst ):
        self.lst = lst
        self.threes = [i for i in self.lst if i >= 3]
        self.threes_nr = len(self.threes)
        self.ones = self.lst.count(1)
        self.mark = 0
        self.M = []
        self.up_range = len(self.lst)-2*(self.threes_nr-1)+1

    def unique_permutations(self):       # VERY EFFECTIVE
        ''':Description: Takes a list and makes ONLY Unique Permutations of a list with repeated elements.
            If one tries itertools.permutations on a list with 14 elements ==> BANG, computer freezes
        :Usage: list(unique_permutations([1,1,1,3]))
        :param lst: type list
        :return:    a list of lists containing all the permutations
        '''
        if len(self.lst) == 1:
            yield (self.lst[0],)
        else:
            unique_lst = set(self.lst)
            for first_element in unique_lst:
                remaining_lst = list(self.lst)
                remaining_lst.remove(first_element)
                for sub_permutation in unique_permutations(remaining_lst):
                    yield (first_element,) + sub_permutation

    def get_multiplier(self) :
        N = list(unique_permutations(self.threes ))
        # print(N)
        return len(N)

    def count_unique_perm(self, ones, threes_nr ) :
        ''':Description: Recursion Function to count blocks separated by one tile.
        :param ones: int , the number of ones from the list
        :param threes_nr: int, numbers of threes(numbers >= 3 in the list)
        :return: int, the number of possible configurations
        '''
        tmp = []

        if self.threes_nr > 2 :
            self.threes_nr = self.threes_nr-1
            self.count_unique_perm(  self.ones , self.threes_nr )
            self.mark+=1
            for j in range(1, self.up_range):
                tmp.append( sum( self.M[self.mark-1][0:j] ) )
                # print(tmp)
            self.M.append(tmp)
            # print(self.M)

        elif self.threes_nr == 2 :
            for i in range(1, self.up_range):
                tmp.append(i)
            self.M.append(tmp)
            # print(self.M)

        return sum(self.M[self.mark])

    def __str__(self):
        return self.lst

    def get_result(self):
        if self.threes_nr == 1 : return len(self.lst)
        if self.threes_nr -1 == self.ones :  return (1* self.get_multiplier() )
        if self.threes_nr  == self.ones :  return ( (self.ones +1 )* self.get_multiplier())
        if self.threes_nr  == 0 :  return 1
        if self.ones  == 0 :  return 1

        else :
            return self.count_unique_perm(self.ones, self.threes_nr) * self.get_multiplier()





############### END FUNCTIONS ##############

print('\n--------------------------TESTS------------------------------')
# Here we need to use partitioning of numbers and get for
# a number of lengths length of >1 a  (number) -1 of length of 1
#     +
# the one which don't have length
#
# @ 2016-12-05, 20:00
# Am ramas ca trebuie sa fixez functia de recursie pentru cazurile >= 3


print('\n----------TEST for VALID rods---------')
test = [ 1, 1, 1, 4, 3, 5]
def valid_rods_old(lst):
    lst = list(unique_permutations(lst))
    # print( len(lst), lst)
    l = len(lst[0])
    B = lst.copy()
    for i in range(len(lst)):
        for j in range(l-1):
            if  lst[i][j:j+2].count(1) == 0 :
                # print(lst[i])
                try : B.remove(lst[i])
                except : AttributeError
    return len(B)

print('\nTest for the valid_rods() Function :\t', valid_rods_old(test))

print('\n---------------MORE MECHANIC (MANUAL ) TESTING ----------------')

# L = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3]  #	   1-case
# L = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3]  #	   2-case
# L = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 3, 5]         #     3-case
# L = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 5, 3, 4] 	                #     4-case
# L = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3]             #     5-case
# L = [1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 3]         #     6-case
# L = [1, 1, 1, 1, 1, 3  4, 5, 6, 6]                                       #     custom case  three == one
# L = [1, 1, 1, 1,  3,  4, 5, 6, 6]                                       #     custom case  threes = ones + 1
# L =  [1, 1, 1, 1, 1, 1, 1, 3, 3]
L = [1, 1, 1, 1, 3, 3, 3]


print( len(L), L)

threes = [i for i in L if i >= 3]
threes_nr = len(threes)
ones = L.count(1)
print('Threes :',threes, len(threes), '\t \tOnes :' ,ones,  )
M = list(unique_permutations(threes))
print(len(M), M)
S=0
if len(threes) == 1 :
    print(' ========== CASE 1 ============')
    print('\nAnswer', len(L))
if len(threes) == 2 :
    print(' ========== CASE 2 ============')
    S = ones*(ones+1)/2
    f = len(list(unique_permutations(threes)))
    print('\nAnswer', int(S*f)  )

if len(threes) == 3  :
    print(' ========== CASE 3 ============')
    for i in range(1, ones):
        S += i*(i+1)/2
        print( i*(i+1)/2, '      total: ', S)
    print('\nResult:\t', S*len(M))

if len(threes) == 4:
    print(' ========== CASE 4 ============')
    for i in range(1, ones):
        s=0
        for j in range(1, i):
            s += j*(j+1)/2
        S+=s
        print(i, '       partial: ', s)
    print('\nAnswer:\t',S)

if len(threes) == 5:
    print(' ========== CASE 5 ============')
    for i in range(1, ones):
        ss =0
        for j in range(1, i):
            s = 0
            for k in range(1, j):
                s += k*(k+1)/2
            ss += s
        print(i,  '        partial:  ',ss)
        S+=ss

    print('\nAnswer:\t',S)

print('\n--------COMPARATION TEST-----------')

S = valid_rods_old(L)
print('\nTRUE RESULT :\t', S)


print('\n------------------ BUILDING THE RECURSION FUNCTION / CLASS  -------------------')

threes = [i for i in L if i >= 3]
ones = L.count(1)
threes_nr = len(threes)
up_range=len(L)-2*(threes_nr-1)
M, mark = [], 0
def count_unique_perm_rec(ones, threes_nr):
    ''':Description: Recursion Function to count blocks separated by one tile

    :param ones: int , the number of ones from the list
    :param threes_nr: int, numbers of threes(numbers >= 3 in the list)
    :return: int, the number of possible configurations
    '''
    global mark, up_range
    tmp = []
    if threes_nr ==1 : return ones+threes_nr

    if threes_nr > 2 :
        count_unique_perm_rec(ones, threes_nr-1)
        mark+=1
        for j in range(1, up_range+1):
            tmp.append( sum( M[mark-1][0:j] ) )
        M.append(tmp)
        print(M)

    elif threes_nr == 2 :
        for i in range(1, up_range+1):
            tmp.append(i)
        M.append(tmp)
        print(M)

    return sum(M[mark])


########################


# L = [1, 1, 1, 1, 3, 3, 3]
print('\nCLASS __str__ TESTING  for GET_ROD_VARIATIONS : ',GET_ROD_VARIATIONS(L).__str__() )
print('CLASS get_multiplier TESTING  for GET_ROD_VARIATIONS : ',GET_ROD_VARIATIONS(L).get_multiplier() )
print('CLASS unique_permutations TESTING  for GET_ROD_VARIATIONS : ',GET_ROD_VARIATIONS(L).unique_permutations() )
# print('CLASS TESTING  for GET_ROD_VARIATIONS : ',GET_ROD_VARIATIONS(L).threes_nr )
# print('CLASS TESTING  for GET_ROD_VARIATIONS : ',GET_ROD_VARIATIONS(L).ones )
print('CLASS count_unique_perm TESTING  for GET_ROD_VARIATIONS : ',GET_ROD_VARIATIONS(L).count_unique_perm(ones, threes) )
print('CLASS get_result TESTING  for GET_ROD_VARIATIONS : ',GET_ROD_VARIATIONS(L).get_result() )

print('\n FUNCTION count_unique_perm_rec : ',count_unique_perm_rec(ones, threes_nr) )



print('\n\n------------------- INITIAL SOLUTION, CORRECT SOLUTION -----------------------')
t1  = time.time()


# INITIAL SOLUTION, Use only for verification with  nr <23


def slow_count_block_combinations(rod_length) :
    cnt = 0
    for I in partitions(rod_length):
        # if len(I) == 1  :
        #     print(I)
        if I.count(2) == 0 :
            ones = I.count(1)
            threes = len([ i for i in I if i>=3 ])
            if  threes <= ones +1 :
                v = valid_rods_old(I)
                print(v,'\t', I)
                cnt += v
    return print('\nAnswer : ', cnt)

# slow_count_block_combinations(25)


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


# print('\n---------------------CLASS BENCH TESTING ---------')
# H =   [1, 1, 1, 1, 1, 1, 1, 3, 3]
# print('CLASS  GET_ROD_VARIATIONS, threes_nr : ',GET_ROD_VARIATIONS(H).threes_nr )
# print('CLASS  GET_ROD_VARIATIONS, ones : ',GET_ROD_VARIATIONS(H).ones )
# print('\nCLASS get_result TESTING  for GET_ROD_VARIATIONS : ',GET_ROD_VARIATIONS(H).get_result() )


print('\n================  My FIRST SOLUTION,  SLOW, 1 min ===============\n')
t1  = time.time()

def count_block_combinations(rod_length) :
    cnt = 0
    for K in partitions(rod_length):
        if K.count(2) == 0 :
            ones = K.count(1)
            threes_nr = len([ i for i in K if i>=3 ])
            if  threes_nr <= ones +1 :
                a = GET_ROD_VARIATIONS(K).get_result()
                # print(a,'\t', K, )#b, '  ; ones, threes :',c, d,'  ',e)
                cnt += a
    return print('\nAnswer : ', cnt)

# count_block_combinations(50)             #    Answer :  16475640049

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')          #  Completed in : 58133.3251 ms


print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')


print('\n--------------------------SOLUTION -1, RECURSION  --------------------------')
t1  = time.time()
# ===========Thu, 2 Jan 2014, 16:15,  linluk  , Austria
# Here is a simple, recursive solution (Python)


l={0:0}
def F(m , n ):
    x=1
    if n>m:
        return x
    if m in l:
        return l[m]
    for i in range( (m-n)+1 ):
        for j in range(n, (m-i)+1):
            x += F( m-i-j-1, n)
    l[m]=x
    return x

print (F(50,3))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 0, RECURSION  --------------------------')
t1  = time.time()
# ===========Tue, 10 Mar 2015, 21:55 , Dhufar, Python, France
# Here is a simple, recursive solution (Python)

accu = [1,1,1,1]
for i in range(4,52):
    prov = accu[-1]
    for j in range(4, i+1):
        prov += accu[j-4]
    accu.append(prov)

print(accu)
print('\nAnswer : ', accu[-1] )

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n------------------  SOLUTION 1,  Dictionary with Memoization, red & black 2 cases, VERY FAST & INGENIOUS --------------------------')
t1  = time.time()
# ============Tue, 22 Nov 2016, 08:07, mbh038, England

# 50−100μs50−100μs  in Python, using recursion and a memo.
# For block lengths up to 3 units I worked out the number of solutions that had a red left-most block,
# or a black left-most block, and put these pairs of values in a dictionary with the block length as key.
# Then, working upwards in block lengths one unit at a time, I imagined placing k=1 to n black blocks at  the left-most end.
# For each value k, this  gave a rightward space of n−k blocks in length that had to be filled with  any allowed combination
# of sub-blocks that had a red left-most edge. I could look this value up in the dictionary.
# The sum of these values for each k then gave the number of solutions for blocks of length nn with a black left edge.
# To find the solutions for n units that have a red edge, I do the same, starting this time with a red block of 3 units at the left edge.
#
# In fact, on inspecting the numbers for the first few block lengths, one sees that the recursion relation is:
#
#             n_(black left edge)(L) = n_(black left edge)(L−1) + n(red left edge)(L−1)
#
#             n_(red left edge)(L) = n_black left edge(L−3) + n_red left edge(L−1)


def F(m,n,memo={}):
    t=time.clock()
    blocks={k:[0, 1] for k in range (1, m)}
    blocks[0]=[0, 0]
    blocks[m]=[1, 1]
    try:
        print(m, n, memo[(m, n)],time.clock()-t)
        return
    except KeyError:
        for L in range (m+1, n+1):
            blocks.setdefault(L, []).append(blocks[L-1][0] + blocks[L-m][1]) #red left-edged solutions
            blocks.setdefault(L, []).append(blocks[L-1][0] + blocks[L-1][1]) #black left-edged solutions
        result =sum(blocks[L])
        memo[(m, n)]=result
    print(m, n, sum(blocks[L]), time.clock()-t)

F(3, 13, {})

# here are the values up to LL=20:
#             L R B,R+B
#             1 0 1 1
#             2 0 1 1
#             3 1 1 2
#             4 2 2 4
#             5 3 4 7
#             6 4 7 11
#             7 6 11 17
#             8 10 17 27
#             9 17 27 44
#             10 28 44 72
#             11 45 72 117
#             12 72 117 189
#             13 116 189 305
#             14 188 305 493
#             15 305 493 798
#             16 494 798 1292
#             17 799 1292 2091
#             18 1292 2091 3383
#             19 2090 3383 5473
#             20 3382 5473 8855

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------- SOLUTION 2, Dynamic Programming ,One Row Matrix, Super Fast & ELEGANT  --------------------------')
t1  = time.time()

# ============== Sat, 26 Mar 2016, 18:26, dellasantina, France
# Let F(n,m)F(n,m) be the number of ways to fill a row mesuring n units in length, using blocks with a minimum length of m units.
# To fill a row measuring n units length, we can apply this recursive method :
#
#    - choose a block measuring i units length (m≤i≤n)
#    - choose a starting square j ( 1≤j≤n−i+1 )
#    - loop with the remaining squares
#
# Then :
#
# F(n,m) = 1+∑(i=m,n)∑(j=1,n−i+1)F(n−i−j, m)
#
#
# 1 corresponds to the case where we leave an empty row.
#
# With some tricks, we can prove that :
#
# F(n,m)=1+∑(k=1, n−m+1)k×F(n−m−k, m)
#
#
# With this formula, we can find the solution very quickly.
#
# Python (takes ≃0,2≃0,2 ms) :


m = 3
n = 50

F = [1]*(n+2)
for i in range(3,n+2):
	F[i] = 1 + sum([k*F[i-m-k] for k in range(1, i-m+2)])

print ('Answer: ',F[-2])

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------- SOLUTION 3, Dynamic Programming,  nice --------------------------')
t1  = time.time()
# ========== Thu, 19 May 2016, 07:19, nandersen, USA
# A very fast DP in Python.

n = [1]
def tile_count(x):
    total = n[x-1]
    for i in range(3, x+1):
        if i is x: total += 1
        else: total += n[x-i-1]
    return total

for x in range(1,51):
    n.append(tile_count(x))

print(n[50])

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 4,   --------------------------')
t1  = time.time()
# ===========Sat, 4 Jun 2016, 04:44,  gregadoff
# Here is a simple, non-recursive solution (Python)

row_len = 50
block_min = 3
array = [1] * (row_len + 1)
for i in range(block_min, row_len + 1):
    array[i] = array[i - 1] + 1 + sum(array[0 : i - block_min])
print(array[row_len])

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 5,   --------------------------')
t1  = time.time()
# =========== Fri, 24 Jun 2016, 20:35, go_to_dmc, South Korea
# recurrence relation is:
# c(n)=c(n-1)+c(n-4)+c(n-5)+.....+c(1)+2
# c(n) refers to number of making with n blocks(e.g.:   c(7)=17)

flist=[1,1,2,4]
count=0
goal=4
while goal!=50:
    count=2
    count+=flist[goal-1]
    for i in range(goal-4,-1,-1):
        count+=flist[i]

    flist.append(count)
    goal+=1

print(flist[goal-1])



t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 6,   --------------------------')
t1  = time.time()
# =========  Fri, 2 Sep 2016, 01:06 ,payprplayn, USA, C/C++
# So I haven't read the whole thread, but I know the question is old and I'm sure someone has pointed this out already,
# but there's a natural simplification here expressed simply as a sum of binomial coefficients, which,
# at least on the first and last pages of the thread, no one mentioned.
# For any given covering with k tiles, perform the following transformation:
#         1. delete one black square from between every two successive tiles
#         2. shorten each tile by one square
#         3. blank (as in color black, not remove) the middle squares (that is, all but the leftmost and rightmost square) from each red tile
#
# The result is a row of 50-2k+1 tiles with 2k of them red.
# This process is reversible, and every possible choice of 2k red tiles from 50-2k+1 tiles corresponds
# to a unique initial covering of 50 squares with k tiles.
# In other words it is a bijection.  Thus given a function for binomial coefficients, the answer is simply
#
# Of course it is faster to use the recurrence relation in a loop, but the above still found the solution with no human-detectable delay.
# Thinking about it this way also makes finding the recurrence quite simple,
# as it follows directly from the recurrence relation of binomial coefficients.

def binomial(x, y):
    from math import factorial as fac
    try:
        binom = fac(x) // fac(y) // fac(x - y)
    except ValueError:
        binom = 0
    return binom

print(sum(binomial(50-2*k+1, 2*k) for k in range(13)) )



t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 7,   --------------------------')
t1  = time.time()
# ======= Thu, 10 Nov 2016, 02:40,  sesquiup, USA
# I came up with a nice recursion to solve the problem, gets the answer very quickly.

def main():
    start = time.clock()

    L = [1,1,2]
    while (len(L) < 50):
        L.append(2 + sum(L) - sum(L[-3:-1]))

    print (L[-1])

    print ("\nExecution time:  " + str((time.clock()-start)))

if __name__ == '__main__':
    main()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 8,   --------------------------')
t1  = time.time()
# ========= Fri, 3 Jul 2015, 02:44, Gurpreet Singh, India
# I'd count this problem in one of my favorites. I used simple Maths to solve this problem.
#
# I divided the line using 'r' no. of black boxes as partitions with 0, 3, 4, ... or 50 consecutive black boxes in between.
# The no. of spaces with 0 black boxes are represented by x.
#
# We can represent the solution in this way -
# Sum of coefficient of t**(50-r) in (1 + t**3 + ... t**50)r+1 for different r's.
# In order to compensate for 1, I used simple binomial with the rest together, and hence comes x.
#
# Here's my code in Python (runs in no time) -

def comb(a, b):
    if a == 0 and b == 0:
        return 1
    t = 1
    for i in range(b+1, a+1):
        t = t*i
    for i in range(1, a-b+1):
        t = t/i
    return t

ans = 1 #Using 1 as the solution skips for all blacks
l = 50

for r in range(0, l+1):
    for x in range(1, r+2):
        if 3*x > l - r:
            break
        ans += comb(r+1, x) * comb(l-1-r-2*x, x-1)

print(ans)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 9, RECURSION with Memoization  --------------------------')
t1  = time.time()
# =========== Fri, 28 Aug 2015, 10:06, lukius, Argentina
# Recursion plus memoization:

def p114(N=50):
    return B(N)

def B(n, k=3, cache=None):
    if cache is None:
        cache = dict()
    if n < k:
        cache[n] = 0
    if n == k:
        cache[n] = 2
    if n in cache:
        return cache[n]

    b = 1
    for i in range(1, n-k+2):
        for j in range(k, n-i+2):
            b += max(1, B(n-i-j, cache=cache))

    cache[n] = b
    return b

print(p114(50))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 10, RECURSION   --------------------------')
t1  = time.time()
# =========== Sat, 5 Dec 2015, 19:00,  dbydt, Hong Kong
# Done with simple recurrence relation in Python. Runs in 20 ms.

table0 = [1]
table1 = [1]

n = 1
while n <= 50:
	r0, r1 = table0[n-1], table0[n-1]
	if len(table0) >= 3:
		r0 += sum([table1[n-x] for x in range(3, len(table0) + 1)])
	table0.append(r0)
	table1.append(r1)
	n += 1

print (table0[len(table0) - 1])


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')



print('\n--------------------------SOLUTION 11, RECURSION   --------------------------')
t1  = time.time()
# =========== Sat, 20 Feb 2016, 06:06, sO3SrLCr4Rqb00Zr..., Japan
# Slightly different from other people, but general same approach with recursion:
# First, I broke it up into black-red pairs (of form BB...BRRR...R), then applied memorization and recursion.
# Runs in 35ms (incl. python compilation time).
# okay, let's break it down
# for all non-first and non-last iterations, change it into a black-red group,

# for 1<=len<=3, 4, no possible BR chains
cache = {0: 1, 1: 0, 2: 0, 3: 0}


def paths(rem):
    try:
        return cache[rem]
    except KeyError:
        myPaths = 0
        for myTwoBlockSize in range(4, rem+1):
            # 4 blocks, only BRRR, 5 blocks, BRRRR or BBRRR, etc.
            waysToTwoBlockSize = myTwoBlockSize-3
            myPaths += waysToTwoBlockSize * paths(rem-myTwoBlockSize)
        cache[rem] = myPaths
        return myPaths


def main_sol():
    # now, above, we assume our twoBlock combo starts with B
    # but the first block could start with R, or last block could be B
    # deal with that case manually here
    N = 50
    totPaths = 0
    for leadingRed in [0] + [i for i in range(3, N+1)] :
        for trailingBlack in range(0, N-leadingRed+1):
            # print leadingRed, trailingBlack, paths(N-leadingRed-trailingBlack)
            totPaths += paths(N-leadingRed-trailingBlack)
    print (totPaths)

main_sol()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')



print('\n--------------------------SOLUTION 11, SLOW, RECURSION without Memoization, SLOW  --------------------------')
t1  = time.time()
# =========== Sun, 11 Oct 2015, 09:32, GNFS, USA
# Neat little recurrence, same as previous answer. No need for memoization.

def f(n):
    if n < 3: return 1

    s = 1
    for i in range(1, n-1):
        s += i * f(n-i-3)
    return s

print(f(50))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')




