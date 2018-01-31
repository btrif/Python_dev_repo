#  Created by Bogdan Trif on 06-10-2017 , 6:54 PM.
# https://stackoverflow.com/questions/46611258/partition-a-number-into-a-given-set-of-numbers

print('------------------------ My first function ---------------------')
S = [ 1, 4, 9, 16 ]

def partition_nr_into_given_set_of_nrs(nr , S):         # Very primitive function
    ''' Made by Bogdan Trif @ 2017-10-06, 20:00.
        :Description:  does the partition of a number into the given set of numbers. Example :
        take the number 9, and the set of numbers = {1, 4, 9}. It will yield the following partitions :

        { (1, 1, 1, 1, 1, 1, 1, 1, 1), (1, 1, 1, 1, 1, 4), (1, 4, 4), (9,)}

        No other possible partitions using the set {1, 4, 9} cannot be formed to sum the number 9.
        the partition of the given nu

    :param nr: int, the number to partition
    :param S: the set of integers to use for partitioning
    :return: lst, the list with all partitions
    '''
    lst = set()
    S = sorted(S, reverse=False)
    # Build the base case :
    M = [1]*(nr%S[0]) + [S[0]] * (nr //S[0])
    # print(M)
    if set(M).difference(S) == 0  :
            lst.add(M)
            # print('as a result',M)
    else :
        for x in S :
                # print('\n',nr//x, nr, x,'\n')
                for j in range(1, len(M)+1):
                    for k in range(1, nr//x +1 ) :
                        # print(x, j , '  k=',k)

                        if  k*x ==  sum(M[:j]) :
                            # print( [x]*k , M[:j] ,  '  the partition :    ', tuple(sorted([x]*k + M[j:])) )
                            lst.add(  tuple(sorted([x]*k + M[j:])) )
    return sorted(lst)


print ('\npartition_nr_into_given_set_of_nrs : \n' ,partition_nr_into_given_set_of_nrs(20, S  ) )


print('\n------------------- Nice solution using only two loops ---------------------- \n')

import itertools

x = [ 1, 4, 9, 16 ]
s = []
n = 9
#Remove elements >9
x = [ i for i in x if i <= n]

for i in range(1,n + 1):
    for j in itertools.product(x,repeat = i):
        if sum(j) == n:
            s.append(list(j))
        if sum(j) > n + 2:
            break

#Sort each combo
s =[sorted(i) for i in s]
#group by unique combo
print( list(k for k,_ in itertools.groupby(s)) )



print('\n-------------------  Recursive approach, Excelent Job, MUST STUDY IT !  ---------------------- \n')

def partition_nr_into_given_set_of_nrs(nr, S):
    S = sorted(S, reverse=True)
    def inner(n, i):
        if n == 0:
            yield []
        for k in range(i, len(S) ):
            if S[k] <= n:
                for rest in inner(n - S[k] , k):
                    yield [ S[k] ] + rest
    return list( inner(nr, 0) )

S = [ 1, 4, 9, 16 ]
print(partition_nr_into_given_set_of_nrs(9, S))
# [[9], [4, 4, 1], [4, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1]]





print('\n-------------------  Recursive approach, with LIMIT  ---------------------- \n')

def partition_nr_into_given_set_of_nrs(nr, S,  lim=10 ):
    ''' :Description: partition a number into a custom set of integers with a limit maximum number of terms
    :param n: number to partition
    :param S: integer set
    :return: list of partitions             '''
    S = sorted(S, reverse=True)
    def inner(n, i, lim ):
        if lim >= 0 :
            if n == 0:
                yield []
            for k in range(i, len(S)):
                if S[k] <= n:
                    for rest in inner(n - S[k], k , lim-1 ):

                        yield [ S[k] ] + rest
    return list(inner(nr, 0, lim))

S = [  1,4,9,16 ]
print(partition_nr_into_given_set_of_nrs(40, S, 10))


# def partition(number):
#     S = [2, 3 ]
#     answer = set()
#     answer.add((number, ))
#     for x in S :
#         for y in partition(number - x ):
#             answer.add(tuple(sorted((x, ) + y)))
#             #print(answer)
#     return answer
#
# print(partition(5))

