#  Created by Bogdan Trif on 18-09-2017 , 9:09 PM.

#                  o(^_^)o         ( ͡° ͜ʖ ͡°)
# © Solved by Bogdan Trif @
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
import time, zzz

# must make a function which do a partition only in elements of 2 and 3
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

N= [ 1, 2, 4, 8, 16, 32 ]
print( '\nResult :\n',list( combinations(N, 4) ) )

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


def ugly_ugly_brute_force_small_case( cols , rows) :
    S = [ 2 , 3 ]
    P = partition_nr_into_given_set_of_nrs( cols, S )
    print(P)
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
                        good += 1
                        print(str(good)+'.      ' ,  i, j, k,  '          ' , R[i] ,  R[j] ,  R[k] )

    return print( '\nAnswer : ' + str(good) )

ugly_ugly_brute_force_small_case( 9 , 3)


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')

print('\n================  My FIRST SOLUTION,   ===============\n')
# t1  = time.time()







# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')


# print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
# print('\n--------------------------SOLUTION 1,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 2,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 3,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 4,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 5,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 6,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
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




