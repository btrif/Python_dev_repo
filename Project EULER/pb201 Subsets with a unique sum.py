#  Created by Bogdan Trif on 07-11-2017 , 6:42 PM.
# © o(^_^)o  Solved by Bogdan Trif  @
#The  Euler Project  https://projecteuler.net
'''
                            Subsets with a unique sum               -           Problem 201

For any set A of numbers, let sum(A) be the sum of the elements of A.

Consider the set B = {1,3,6,8,10,11}.
There are 20 subsets of B containing three elements, and their sums are:

sum({1,3,6}) = 10,
sum({1,3,8}) = 12,
sum({1,3,10}) = 14,
sum({1,3,11}) = 15,
sum({1,6,8}) = 15,
sum({1,6,10}) = 17,
sum({1,6,11}) = 18,
sum({1,8,10}) = 19,
sum({1,8,11}) = 20,
sum({1,10,11}) = 22,
sum({3,6,8}) = 17,
sum({3,6,10}) = 19,
sum({3,6,11}) = 20,
sum({3,8,10}) = 21,
sum({3,8,11}) = 22,
sum({3,10,11}) = 24,
sum({6,8,10}) = 24,
sum({6,8,11}) = 25,
sum({6,10,11}) = 27,
sum({8,10,11}) = 29.

Some of these sums occur more than once, others are unique.
For a set A, let U(A,k) be the set of unique sums of k-element subsets of A,
in our example we find U(B,3) = { 10, 12, 14, 18, 21, 25, 27, 29 } and sum(U(B,3)) = 156.

Now consider the 100-element set S = {1^2, 2^2, ... , 100^2}.
S has 100891344545564193334812497256 50-element subsets.

Determine the sum of all integers which are the sum of exactly one of the 50-element subsets of S,
i.e. find sum(U(S,50)).


'''
import time, zzz
from gmpy2 import comb
from itertools import combinations

print('Comb( 100, 50 ) = ', comb(100, 50) )

L = [ i*i for i in range(1,101) ]
S = set(L)
print(L)

smallest_set_sum = sum( [  i*i for i in range(1, 51)] )
greatest_set_sum = sum( [  i*i for i in range(51, 101)] )

print('smallest_set_sum = ', smallest_set_sum, ' ;   greatest_set_sum = ', greatest_set_sum )
print(' There are no more than ', greatest_set_sum-smallest_set_sum , '    unique sums' )


'''
https://stackoverflow.com/questions/12533302/project-euler-201

'''

print('\n--------------------------TESTS------------------------------')
t1  = time.time()

# What is the recursive solution for finding all subsets of a given array?
def subsets( nums ):      # Returns all the subsets of the main set
    if nums is None: return None
    subsets_ = [[]]
    next = []
    for n in nums:
        for s in subsets_ :
            next.append(s + [n])
        subsets_ += next
        next = []
    return subsets_

print(subsets( [ 2, 3, 5, 7, 11, 13 ] ) )



# def existsRepresentation( nr, max_nr ,nr_of_elem ):
#     n = 0
#     for i in range(nr_of_elem) :

def just_a_test(lim) :
    # lim = 20

    A, B = dict(), [0 for i in range(10*lim*lim+1)]
    for i in range(1, lim+1):
        for j in range(i+1, lim+1):
            print('i,j = ', i, j, '      ', i*i+j*j )
            B[i*i+j*j] += 1
            if i*i+j*j not in A :
                A[i*i+j*j] = []
                A[i*i+j*j].append({i, j})
            else : A[i*i+j*j].append({i, j})

    print('B :', len(B), B )
    print()
    A_ = dict()
    for k,v in A.items():
        if len(A[k]) == 1 :
            for i in range(1, lim +1) :
                if i not in v[0] :
                    S = v[0].union({i})
                #     print(S)
                    s_ = sum([i*i for i in S])
                    B[s_] += 1
                    if s_ not in A_ :
                        A_[s_] = []
                    if S not in A_[s_] :
                        A_[s_].append(S)

                    print(k, v , '      ', i,'     ' , S,'   ',s_ )

    cnt = 0
    for k,v in A_.items():
        if len(A_[k]) != 1 :
            cnt +=1
            print(' k, v = ', k, '    ',v, '    cnt = ', cnt)

    return A_

# just_a_test(20)

print('\n-------------------- Hard Brute Force -----------------------')
def hard_brute_force(lim, elem) :           #### @2018-05-28, 14:10        IT WORKS FINE !!!

    Y = dict()
    cnt = 0
    I = list(range(1, lim+1) )
    print(I)
    # I = [1,3,6,8,10,11]
    for cnt, i in enumerate(combinations( I, elem ) ):

        J = [ x*x for x in i  ]
        s = sum( J )


        if s not in Y :
            Y[s] = []
            # print(str(cnt+1)+ '.    ' , i,'      ', J, '       ', s)

        # else :
            # print('duplicate :     ' , i , '     cnt=', cnt ,'     ', J , '      s =', s )
        Y[s].append( set(J) )

    W =  [ k for k,v in Y.items() if len(v) ==1 ]

    print('W :',  W  )
    print( '\n Total sum = ', sum(W) )
    return set(W)

W = hard_brute_force(20, 5 )

t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')

print('\n==============   My FIRST SOLUTION, Exponential Algorithm , Correct, but it takes a lifetime   ===============\n')
t1  = time.time()

def subsets_unique_sum1(lim, elem_nr, visual ) :
    # elem_nr = 2             # number of elements in the set
    # lim = 20                    # maximum number to consider
    A = { k*k: [{k}] for k in range(1, lim+1)   }
    Aplus = dict()
    print('A :', A)

    elem = 1
    while elem < elem_nr :
        print('\n-------- elem =', elem ,'   ------   len(A )=  ', len(A) ,'    -------    ' +str( round( time.time() -t1 , 4 )) +' s' )
        # A_ = { k:v for k,v in Aplus.items() if v }
        A_ = dict()
        Aplus = dict()

        for k,v in A.items():

            if len(v) == 1 :
                for i in range(1, lim +1) :
                    if i not in v[0] :
                        S = v[0].union({i})

                        s_ = sum([i*i for i in S])

                        if s_ not in A_ :
                            A_[s_] = []

                        if S not in A_[s_] :
                            A_[s_].append(S)


                            # print('k=', k ,'  v= ' ,v , '      ', i,'     ' , S,'    s_= ', s_ , '       A_[s_] =   ' , A_[s_] )

            if len(v) > 1 :
                # print('k=', k ,'  v= ' ,v , '      ', i,'     ' , S,'    s_= ', s_ , '       A_[s_] =   ' , A_[s_] )
                for j in range(len(v)) :
                    Z = v[:j] + v[j+1:]
                    U = list(set().union(*Z))
                    W = set(U).difference( v[j] )
                    # print( v[j], '     Z =', Z,'        U :', U ,'      W :', W )
                    for el in W :
                        S2 = v[j].union({el})
                        s_2 = sum([i*i for i in S2])

                        if s_2 not in Aplus :
                            Aplus[s_2] = []

                        if S2 not in Aplus[s_2] :
                            Aplus[s_2].append(S2)
                            # print( v[j], '     Z =', Z,'        U :', U ,'      W :', W , '    just added S2 : ' , S2 )





        A = { k:v for k,v in A_.items() if v }
        # print('\nA : \n' , len(A), A )
        # print('\nAplus : \n' , len(Aplus), Aplus )
        ### Extend further A with Aplus :
        for k2, v2 in Aplus.items() :
            if k2 not in A :
                A[k2] = v2
            if k2 in A :
                for f in v2 :
                    if f not in A[k2]:
                        A[k2].append(f)


        elem+=1

    if visual == True :
        print('\n------------    Visualize  elements     ----------')
        cnt = 1
        S = 0
        for k,v in A.items():
            if len(v) == 1 :
                S += k
                print('k = ', k, '    v = ',  v, '        cnt = ', cnt ,'     S=', S )
                cnt +=1


    result = [ k  for k,v in A.items() if len(v) ==1 ]

    print('\nANSWER : ',  sum(result) )
    return set(result)

result = subsets_unique_sum1( 20, 10   , False  )

# print('W :', len(W), W)
# print('result :', len(result), result)
#
# print('\n Set dif : ', result.difference(W) )
# print('\n Set dif 2 : ', W.difference(result) )


# @2018-05-28 : 74:
# [{8, 1, 3}, {3, 4, 7}] <--- Here is the problem ! I neglected the fact that I must combine all elements of the two sets :
# to form set of 4 elements with them !! And I have seen this in the start but I neglected it !!!
# I must do the following :
# make set diff between each set in the list like :
# S1, S2 = {8, 1, 3} ,{3, 4, 7}
# S2.difference(S1)
# for i in S2.difference(S1) :
#     print(S1.union({i}) )
#
# for i in S1.difference(S2) :
#     print(S2.union({i}) )
#
# {8, 1, 3, 4}
# {8, 1, 3, 7}
# {8, 3, 4, 7}
# {1, 3, 4, 7}



t2  = time.time()
print('\n# Completed in :', round((t2-t1), 2 ), 's\n\n')


# print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
# print('\n--------------------------SOLUTION 1,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 2,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 3,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 4,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
print('\n--------------------------SOLUTION 5,   --------------------------')
t1  = time.time()

def main(lim, elem):
    S = [n*n for n in range(1, lim+1)]
    T = {}
    for i in range(len(S) + 1):
        T[i] = {}
    T[0][0] = 1

    for i in range(len(S)):
        print('''Current position:''', i)
        U = {}
        print('T : ', T)
        for subset_size in T:

            if subset_size > i or subset_size > lim:
                continue
            for subset_sum in T[subset_size]:
                curr_sum = subset_sum + S[i]
                curr_size = subset_size + 1
                if curr_size not in U:
                    U[curr_size] = {}
                if curr_sum not in U[curr_size]:
                    U[curr_size][curr_sum] = 0
                U[curr_size][curr_sum] += T[subset_size][subset_sum]
        for subset_size in U:
            for subset_sum in U[subset_size]:
                if subset_sum not in T[subset_size]:
                    T[subset_size][subset_sum] = 0
                T[subset_size][subset_sum] += U[subset_size][subset_sum]

    total_sum = 0
    for subset_sum in T[elem]:
        if T[elem][subset_sum] == 1:
            total_sum += subset_sum
    print(total_sum)

main(10, 5)

t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')


# print('\n--------------------------SOLUTION 6,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 7,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 8,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 9,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 10,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 11,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 12,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')




