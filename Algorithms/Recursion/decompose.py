#  Created by Bogdan Trif on 30-06-2018 , 3:26 PM.

def partition_nr_into_given_set_of_nrs( nr, S  ):
    ''' :Description: partition a number into a custom set of integers with a limit maximum number of terms
    :param n: number to partition
    :param S: integer set
    :return: list of partitions             '''

    Lst = sorted(S, reverse=True)

    def decompose( n, i ) :
            if n == 0:
                yield []
            for k in range(i, len(Lst)) :
                if Lst[k] <= n:
                    for rest in decompose(n - Lst[k], k) :

                        yield [ Lst[k] ] + rest

    return list(decompose( nr, 0 ))


S = [ 1, 4, 9, 16 ]
print(partition_nr_into_given_set_of_nrs( 13, S ))

print('\n---------------- Decompose, METHOD II - Recursive Example--------')

L = [ 1, 4, 9, 16 ]
## Recursion with maintaining state :
def decompose( n , L , answerSoFar=[]  ):
    if n == 0 :
        print(answerSoFar)

    else :
        offset = 0
        for a in L :
            if a <= n :
                answerSoFar.append(a)
                decompose( n-a, L[ offset: ], answerSoFar )
                ## Backtrack
                answerSoFar.pop()
            offset += 1


decompose(13, L )

print('\n------------------------ METHOD II, list append ----------------------')
''' Now if we want to put all the subset in a list we have to have list container for the subsets.
There are two possibilities :
    1. either we put the list container A in the function scope argument where we maintain it and update it
      each time the condition is met
    2. or declare a global list container as A and only append the list each time the condition is met.
    
    OBSERVATION : When dealing with lists a known problem is the list overwrite with null.
    This is because the list points to the same address space and get overwritten each time it is called.
    The trick to avoid this is to make a copy of the list with lst[:]
    lst[:] creates a copy of the initial list       !!!!
'''
## Here the list A is an argument
def decompose2( n , candidatelist , answerSoFar=[] , A=[] ):

    if (n==0):
#         print( answerSoFar )
        A.append(answerSoFar[:])

    offset = 0
    for a in candidatelist:
        if ( a <= n):
            answerSoFar.append(a)
            decompose2( n-a , candidatelist[offset:] , answerSoFar, A )
            # Backtracking
            answerSoFar.pop() # remove a from the list, so we can try replacing by later items too.

        offset += 1
    return A

print(decompose2( 13, [1, 4, 9] ))

print('\n------------------------   METHOD II, list container as global variable   ----------------------')
## Here the list container A is declared as global and we do not need to maintain the scope in the recursive function

A=[]
def decompose3( n , candidatelist , answerSoFar=[] ):
    global A
    if (n==0):
#         print( answerSoFar )
        A.append(answerSoFar[:])

    offset = 0
    for a in candidatelist:
        if ( a <= n):
            answerSoFar.append(a)
            decompose3( n-a , candidatelist[offset:] , answerSoFar )
            # Backtracking
            answerSoFar.pop() # remove a from the list, so we can try replacing by later items too.

        offset += 1


print(decompose3( 13, [1, 4, 9] ))
print('A : ', A )

