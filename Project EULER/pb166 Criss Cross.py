#!/usr/bin/python
# Solved by Bogdan Trif @   Completed on Wed, 18 Jan 2017, 18:54
#The  Euler Project  https://projecteuler.net
'''
                        Criss Cross     -       Problem 166

A 4x4 grid is filled with digits d, 0 ≤ d ≤ 9.
It can be seen that in the grid
                                                                6 3 3 0
                                                                5 0 4 3
                                                                0 7 1 4
                                                                1 2 4 5

the sum of each row and each column has the value 12. Moreover the sum of each diagonal is also 12.

In how many ways can you fill a 4x4 grid with the digits d, 0 ≤ d ≤ 9 so that each row,
each column, and both diagonals have the same sum?

'''
import time
from itertools import combinations, permutations
import numpy as np

def unique_permutations(lst):       # VERY EFFECTIVE
    ''':Description: Takes a list and makes ONLY Unique Permutations of a list with repeated elements.
        If one tries itertools.permutations on a list with 14 elements ==> BANG, computer freezes
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


print('\n--------------------------TESTS------------------------------')
t1  = time.time()

def number_part(nr, parts) :
    ''':Description:  Function which partition a number in fixed sizes of parts .
         !!! this function work on maximum 3 parts. For bigger > 3 must extend it
        and generalize it. for the purpose of this puzzle works fine.
         It also depends on the unique_permutations function.
    :Example: number_part(17, 3) will generate lists with sum = nr  like : [9, 8, 0],
        [9, 7, 1], [9, 6, 2],  [9, 4, 4], [8, 6, 3], [7, 6, 4] and their permutations
     '''
    M =[]
    #### Decompose initial sum :
    if nr > parts*9 : return False
    r = nr//parts
    o = min(9, nr)
    for i in range(o, r, -1):
        L, n = [ ], nr
        while n >= i:
            L.append(i)
            # print(nr, n)
            n -= i
        if len(L) < parts: L.append(n)
        # print(L)
        if len(L) < parts : L.extend([0]*(parts-len(L)) )
        P = list(unique_permutations(L))
        # print(L, n, nr ,'       ', P)
        M.extend(P)
        if parts > 2 :
            while L[-1] < L[-2]-1 :     # Here must be extended if needed parts > 3
                L[-1]+=1
                L[-2]-=1
                P = list(unique_permutations(L))
                # print(L, '\t\t       ' ,P)
                M.extend(P)
    if nr%parts ==0 : M.append(tuple([r]*parts))

    return M

print('\nnumber_part function :\t' ,number_part(3, 3) )

t1  = time.time()

### Here we Pregenarate all the number fixed partitions :
T, D = dict(), dict()
for i in range(0,28):           # 3 digit partitions
    T[i] = number_part(i, 3)
    print(i, '    ',T[i])
for i in range(0,19):           # 2 digit partitions
    D[i] = number_part(i, 2)
    print(i, '    ',D[i])

print(len(D[9]) ,  D[9] )
print(len(T[14]), T[14])

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n---------------Matrix with numpy tests-------------------\n')

M = np.zeros((4,4), dtype=int)
M[1], M[2] = [3,4,5,2], [7, 4, 2, 8]
print(M)
print( '\n columns sum :',  np.sum(M, axis=0) , np.sum(M, axis=0)  ,'    Main diagonal sum : \t' ,
       np.sum(M.diagonal(axis1=0)) , M.diagonal(axis1=0)  )
print( '\n  Secondary Diagonal : \t' , np.diag(np.fliplr(M)) ,'    Secondary diagonal sum : \t' ,sum(np.diag(np.fliplr(M)))  )
M[:,0] = [3,8,9,1]
print('\n',M)
M[:,3] = [7,5,3,1]
print('\n', M )





t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n================  My FIRST SOLUTION,  VERY SLOW > 2 hours ===============\n')
t1  = time.time()


def smart_brute_force():
    cnt=0
    M = np.zeros((4,4), dtype=int)
    for i in range(0, 10000):      ##### STEP 1, first row
        i = str(i).zfill(4)
        M[0] = r1 = [int(j)for j in i]
        print(i,'       ', cnt)
        sc1, S = sum(r1[1:]), sum(r1)      # partial sum, and GENERAL SUM
        # print(i, r1, sum(r1),'     ',   sum(r1[1:]) ,r1[0]   )
        A = T[sc1]      #  number_part(sc1, 3)
        for c1 in A :                     ##### STEP 2, First column,remainder of c1 -> M[0][1:4]
            M[:,0]= [r1[0]] +list(c1)
            sd2 = S - M[0][3]-M[3][0]
            # print(c1, sum(c1),'\n',M, S, sum(M[:,0]) , sum(np.diag(np.fliplr(M))), sd2 ,'\n')
            if 0 <= sd2 <=18 :
                B = D[sd2]       #number_part(sd2, 2)         #####   STEP 3, Second Diagonal , Remainder : M21, M12 elements
                # print('-------------',S, sum(np.diag(np.fliplr(M))) , sd2  ,'\n' ,M,'\n',B,'\n--------------')
                for d2 in B :
                    # print(d2)
                    (M[1][2], M[2][1]) = d2
                    # print(S , sum(np.diag(np.fliplr(M))),sd2 , d2, (M[1][2], M[2][1]) , B ,' \n',M, '\n' )
                    if S == sum(np.diag(np.fliplr(M)) ) :
                        # print(d2 , np.diag(np.fliplr(M)) , S, sum(np.diag(np.fliplr(M)) ) , sum(M[:,0]) )
                        sd1 = S - r1[0]                    #####   STEP 4, Main Diagonal, Remainder :   M11, M22, M33 elements
                        if 0<=sd1 <= 27 :
                            C = T[sd1]                #number_part(sd1, 3)
                            # print(C)
                            for d1 in C :
                                (M[1][1], M[2][2], M[3][3]) = d1
                                # print(M , S, sum(np.diag(np.fliplr(M))) , np.sum(M.diagonal(axis1=0)) , sum(M[:,0]),'\n' )

                               #####   STEP 5, Filling the last elements : M31, M32, M13, M23
                                M[3][1], M[3][2] = S-sum(M[:,1][:3]), S-sum(M[:,2][:3])
                                M[1][3], M[2][3] = S-sum(M[1][:3]), S-sum(M[2][:3])
                                if 9>=M[3][1] >=0 and 9>=M[3][2]>=0 and 9>=M[1][3]>=0 and 9>=M[2][3]>=0 :
                                 ##### FINAL CHECK ##########
                                    D1, D2 = np.sum(M.diagonal(axis1=0)), sum(np.diag(np.fliplr(M)))
                                    if ( S==sum(M[1])==sum(M[2])==sum(M[3])==sum(M[:,1])==sum(M[:,2]) ==sum(M[:,3]) ) :
                                        cnt+=1
                                        # print(M, np.sum(M, axis=0),S, sum(M[1]),sum(M[2]), sum(M[3]), D1 , D2,'\n' )


    return print('\n\nAnswer: ', cnt)

# smart_brute_force()                   #    Answer:  7130034


t2  = time.time()
print('\nCompleted in :', round((t2-t1),6), 's\n\n')           #    Completed in : 9170.834542


print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1,  INCREDIBLE FAST --------------------------')
t1  = time.time()

# === Tue, 2 Feb 2016, 11:49, Blebg, Sweden
# About 2 sec in Python.
# Need to go trough 6 unknowns to get the diagonals and then the rest can be calculated.
# Two sub-problems appear where each digit is part of two d1+d2=k equations
# (4 equations in total for each sub-problem).
# I hash the list of k values to avoid repeated calculations.
# Two optimizations or stolen from a post on the first page,

save = {}

def  possibilities(seq):
    hashed = hash(frozenset(seq))
    if hashed in save:
        return save[hashed]

    poss = 10
    for l in range(0,3):
        q, w = seq[l], seq[l+1]
        poss = min(poss,(1+min(9, q, w)-(max(9, q, w)-9)))
        if poss <= 0:
            save[hashed] = 0
            return 0
    save[hashed] = poss
    return poss


def gen_numbers():
    xy = [[0 for x in range(0,4)] for y in range(0,4)]
    for x00 in range(0,5):
        xy[0][0] = x00
        for x11 in range(0,10):
            xy[1][1] = x11
            for x22 in range(x11,10):
                xy[2][2] = x22
                for x33 in range(0,10):
                    xy[3][3] = x33
                    d = x00 + x11 + x22 + x33
                    yield d,xy


k1 = [0 for x in range(0,4)]
k2 = [0 for x in range(0,4)]
tot = 0

for d,xy in gen_numbers():
    double = 1
    if xy[1][1] != xy[2][2]:
        double = 2

    t1 = d - xy[0][0] - xy[3][3]
    t2 = d - xy[1][1] - xy[2][2]

    for i in range(max(0,t1-9),min(10,t1+1)):
        xy[0][3] = i
        xy[3][0] = t1 - i

        k1[0] = d - xy[0][0] - xy[0][3]
        k1[2] = d - xy[3][3] - xy[3][0]
        k2[0] = d - xy[0][0] - xy[3][0]
        k2[2] = d - xy[0][3] - xy[3][3]

        for j in range(max(0,t2-9),min(10,t2+1)):
            xy[2][1] = j
            xy[1][2] = t2 - j

            k1[1] = d - xy[1][2] - xy[2][2]
            k1[3] = d - xy[1][1] - xy[2][1]
            k2[1] = d - xy[2][1] - xy[2][2]
            k2[3] = d - xy[1][1] - xy[1][2]

            poss1 = possibilities(k1)
            poss2 = possibilities(k2)

            #2 and double comes from the optimizations
            tot += 2 * double * poss1 * poss2

print(tot)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 2,  80 sec --------------------------')
t1  = time.time()

# ===== Fri, 14 Aug 2015, 17:01, Haroun, Saudi Arabia
#
# I looped on the red elements, the rest I deduced them
# a1 a2 a3 a4
# b1 b2 b3 b4
# x1 x2 x3 x4
# y1 y2 y3 y4
#
# Here's what I did :
# 1) we take all possibilities a1,a2,a3,a4a1,a2,a3,a4 for the first row and we set AA to be their sum.
# 2) take all possible b1,b2,b3,b4=A−b1−b2−b3b1,b2,b3,b4=A−b1−b2−b3, for the second line.
# 3) loop conditionaly on x1x1.
# 4) we calculate y1,x2,y2y1,x2,y2 in this order.
# 5) we solve the system for x3,x4,y3,y4x3,x4,y3,y4.
#
# Python is not the best language for this, it takes 50 secs to complete.
# I guess that the C version wouldn't take more that 4 secs (just a guess).


def haroun():
    s=range(10);se=set(s);sol=0;
    def f(a1,a2,a3,a4,b1,b2,b3,b4,sum):
        r=0
        for x1 in s:
            y1=sum-x1-b1-a1;
            if y1 not in se : continue;
            x2=sum-y1-b3-a4;
            if x2 not in se : continue;
            y2=sum-a2-b2-x2;
            if y2 not in se : continue;
            x3=(-a1-a3-b2-b3+sum+y1+y2);
            x4=(a1+a3+b2+b3+sum-2* x1-2* x2-y1-y2);
            y3=(a1-a3+b2-b3+sum-y1-y2);
            y4= (-a1+a3-b2+b3+sum-y1-y2);
            if x3%2==0 and x3/2 in se :
                if x4%2==0 and x4/2 in se :
                    if y3%2==0 and y3/2 in se :
                        if y4%2==0 and y4/2 in se :
                            r+= 1
        return r;
    for a1 in s:
        for a2 in s:
            for a3 in s :
                for a4 in s :
                    sum=a1+a2+a3+a4;
                    for b1 in s:
                        if a1+b1>sum: break;
                        for b2 in s :
                            if b1+b2>sum or a2+b2>sum or a1+b2>sum: break;
                            for b3 in s :
                                if b1+b2+b3>sum or a3+b3>sum or a4+b3>sum : break;
                                b4=sum-b1-b2-b3;
                                if b4 in se :
                                    sol+=f(a1,a2,a3,a4,b1,b2,b3,b4,sum)

    return print ("the answer is :", sol)

# haroun()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 3,  1 min  --------------------------')
t1  = time.time()

# ==== Thu, 20 Aug 2015, 10:57, bukebuer, China
#
# By using Gauss-Jordan elimination algorithm, I reduced the initial 9 equations with 16 variables to 7 independent variables
# and 9 dependent variables. (It reminds me the difficult days when taking linear algebra in university.)
#
# a, b, c, d
# e, f, g, h
# i, j, k, l
# m, n, o, p
#
# independent variables: h, j, k, l, n, o, p
#
# Then brute-force loop 10^7 permutations of independent variables and check each permutation is valid when magic sum is 0~37.
#
# Optimizations:
# (1) [a, b, c, d, e, f, g] if symmetric with [9-a, 9-b, 9-c, 9-d, 9-e, 9-f, 9-g]. So just need to loop up to 4999999 instead of 9999999.
# (2) One condition in the formula to calculate out the whole square does not dependent on the magic sum.
# (3) Using the row and column sum of independent variables can limit possible values of magic sum.
#
# Finally, a Python function runs around 18 seconds.



def pe166():
    """
    Using Gauss-Jordan eliminate algorithm to simplify to 7 variables.
    Enumerating all possible 1e7 permutations, checking possible magic sum, and counting.
    """

    magicsum = {}
    for a in range(37):
        bmax = min(a+10, 37)
        for b in range(a, bmax):
            magicsum[(a, b)] = range(b, bmax)

    # v and (9-n for n in v) are symmetric.
    # so look up to 4999999 is enough.
    def vecgen(n):
        v = [0] * (n-1) + [1]
        while v < [5] + [0] * (n-1):
            yield v

            i = 1
            while v[-i] == 9:
                i += 1
            v = v[:-i] + [v[-i]+1] + [0]*(i-1)

    def check(v, vsum, nlist):
        # using the reduced matrix and magic sum to
        # check the validation of vector

        # VARMAT = [[-1.,  0.,  0., -1., -1., -1., -1.],
        #           [-1.,  1., -1., -1.,  0., -1., -2.],
        #           [ 1., -1.,  1.,  1.,  1.,  2.,  2.],
        #           [ 1.,  0.,  0.,  1.,  0.,  0.,  1.],
        #           [ 1., -1., -1.,  0.,  0.,  0.,  0.],
        #           [ 1.,  0.,  1.,  1.,  1.,  1.,  2.],
        #           [-1.,  1.,  0., -1., -1., -1., -2.],
        #           [ 0.,  1.,  1.,  1.,  0.,  0.,  0.],
        #           [ 0.,  0.,  0.,  0.,  1.,  1.,  1.]]
        # RHSCOEF = [ 1.,  1., -2., -1., 0., -2.,  1., -1., -1.]
        a, b, c = vsum[0], vsum[1], vsum[2]
        count = 0
        for n in nlist:
            if not (0 <= n - a <= 9):
                continue
            if not (0 <= n - b <= 9):
                continue
            if not (0 <= n - c <= 9):
                continue
            if not (0 <= v[0] + v[3] + b - n <= 9):
                continue
            if not (0 <= b + c - v[1] - n <= 9):
                continue
            if not (0 <= 2*n - b - c - v[2] <= 9):
                continue
            if not (0 <= 2*n - b - c + v[1] - v[2] - v[5] <= 9):
                continue
            if not (0 <= c - v[1] + v[2] + v[5] + v[6] - n <= 9):
                continue
            count += 1
        return count

    # there's only 1 sol for all-0s and all-9s, count from 2
    c = 2
    for v in vecgen(7):
        if not (0 <= v[1] + v[2] - v[0] <= 9):
            continue

        vsum = v[1]+v[2]+v[3], v[4]+v[5]+v[6], v[0]+v[3]+v[6]
        vmin, vmax = min(vsum), max(vsum)
        if vmax - vmin > 9:
            continue

        c += 2 * check(v, vsum, list(magicsum[(vmin, vmax)]) )

    return print(c)

# pe166()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 4, VERY ELEGANT,  30 sec  --------------------------')
t1  = time.time()

# ==== Sat, 11 May 2013, 14:09, tom.wheldon, England
# My solution is similar to wrongrook's, though I use Python counters rather than regular dictionaries -
# counters have some nice features, like returning zero in the event of a missing key (though they are slower).
# For each magic number I run through all combinations of two columns calculating
# the partial row and diagonal sums for each pair.
# These sets of six numbers are used as dictionary keys to maintain a count of similar pairs.
# This count is multiplied by the value at the complementary key got by subtracting each key element
# from the magic number to deal with columns 3 and 4.  Less than five million cases need to be considered.
# Runs in 18 seconds and would probably be quicker if I hadn't used counters.
# Interestingly, the code doesn't use any if statements - this wasn't deliberate.

from itertools import product
from collections import Counter

lines = [[] for i in range(37)]

for p in product(range(10),repeat=4):
    lines[sum(p)].append(p)

total = 0
for n in range(37):
    col_12 = Counter()
    col_34 = Counter()
    for a1,b1,c1,d1 in lines[n]:
        for a2,b2,c2,d2 in lines[n]:
            col_12[a1+a2, b1+b2, c1+c2, d1+d2, a1+b2, d1+c2] += 1
            col_34[a1+a2, b1+b2, c1+c2, d1+d2, c1+d2, b1+a2] += 1
    for a,b,c,d,e,f in col_12.keys():
        total += col_12[a,b,c,d,e,f] * col_34[n-a,n-b,n-c,n-d,n-e,n-f]

print(total)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 5,  20 seconds --------------------------')
t1  = time.time()

# ==== Fri, 11 Nov 2011, 22:00, Tad A Getachew, Ethiopia
# Love constructing magic squares my self so I loved solving this problem.
# I used a 4th order magic square solving algorithm by P.K. Srinivasan.
# The algorithm is used for generating all possible squares when it is given the values for the top most row.
# So I have to loop through all the possible values of the top four cells.
# Here is the link for the description of the algorithm.
# http://www.nrich.maths.org/1380
# It runs well under a minute.
# Here is my solution in python

def up_to(n):
    return range(n+1)

def no_sols(a,b,c,d,z):
    sols=set([])
    for m in up_to(b+c):
        if m>z:break
        p = b+c-m
        if p>z:continue
        for g in up_to(a+p):
            if g>z:break
            j = a+p-g
            if j>z:continue
            for f in up_to(d+m):
                if f>z:break
                k = d+m-f
                if k>z:continue
                n = g+k-b
                if n<0 or n>z: continue
                o = f+j-c
                if o<0 or o>z: continue
                for h in up_to(a+m):
                    if h>z:break
                    l = a+m-h
                    if l>z:continue
                    e = j+k-h
                    if e>z:continue
                    i = f+g-l
                    if i>z:continue
                    if e<0 or i<0 or e>z or i>z: continue
                    sols.add((a,b,c,d,e,f,g,h,i,j,k,m,n,o,p))
    return len(sols)
counter=0
for a in range(0,10):
    for b in range(0,10):
        for c in range(0,10):
            for d in range(0,10):
                counter+=no_sols(a,b,c,d,9)
print (counter)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 6, 12 sec  --------------------------')
t1  = time.time()

# ==== Tue, 16 Feb 2010, 16:33, Obergscheidle, AWK  , Luxemburg

# Slightly optimized brute-force, based on the following consideration:
# * The outer cells of one diagonal have the same sum as the inner cells of the other diagonal
# * For the outer cells of one diagonal and the distribution over the inner cells of the other diagonal, there are 670 possibilities
# * The same choices exist for the assignments in the other direction
# * once the diagonals are set, this leaves one degree of freedom for the distribution over the remaining cells in top and bottom rows,
# and another degree of freedom for the cells in the first and last column
# * in both cases, the number of choices is limited by the diagonals, and the number of combinations is the product of these two counts
# The following non-optimized code takes 11 seconds


def quad():
    for i in range(10):
        for j in range(10):
            s = i+j
            for k in range(min(s+1,10)):
                if s-k<10:
                    yield i, j, k, s-k

def pair(n):
    if n<10:
        for i in range(n+1): yield i,n-i
    else:
        for x,y in pair(18-n): yield 9-x,9-y

count = 0

for d1,d4,e2,e3 in quad():
    for e1,e4,d2,d3 in quad():
        s = d1+d2+d3+d4
        count1 = sum(1 for x,y in pair(s-d1-e1) if 0<= s-x-d2-e3 <=9 and 0 <= s-y-e2-d3 <= 9)
        count2 = sum(1 for x,y in pair(s-d1-e4) if 0<= s-x-d2-e2 <=9 and 0 <= s-y-d3-e3 <= 9)
        count += count1*count2

print (count)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

