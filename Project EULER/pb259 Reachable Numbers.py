#  Created by Bogdan Trif on 11-07-2018 , 10:11 AM.
# © o(^_^)o  Solved by Bogdan Trif  @
#The  Euler Project  https://projecteuler.net
'''
                Reachable Numbers           -           Problem 259

A positive integer will be called reachable if it can result from an arithmetic expression obeying the following rules:

-   Uses the digits 1 through 9, in that order and exactly once each.
-   Any successive digits can be concatenated (for example, using the digits 2, 3 and 4 we obtain the number 234).
-   Only the four usual binary arithmetic operations (addition, subtraction, multiplication and division) are allowed.
-   Each operation can be used any number of times, or not at all.
-   Unary minus is not allowed.
-   Any number of (possibly nested) parentheses may be used to define the order of operations.

For example, 42 is reachable, since (1/23) * ((4*5)-6) * (78-9) = 42.

What is the sum of all positive reachable integers?

'''
import time, zzz
import itertools


L = [ 1, 4, 9, 16 ]
L = range(1, 10)

def decomp_rec(n, L ,tmp_lst=[], A=[] ):
    ''':Description:    Partition a number by using a list of numbers which will be used for this.
        :Observation: As the function is now it also generates all the permutations of each decomposition
    :param n:
    :param L: lst, list of numbers to be used
    :param tmp_lst: lst, temporary list
    :return:
    '''
    if n == 0:
        # print(tmp_lst)
        A.append( tmp_lst[:] )

    else :
        # offset = 0
        for i in range( 0, len(L) ) :

            if n >= L[i] :
                tmp_lst.append( L[i] )
                decomp_rec( n-L[i], L , tmp_lst, A )
                tmp_lst.pop()

            # offset+=1
    return A

def split_string(S, partition) :
    assert len(S) == sum(partition)

    print('init part : ', partition)
    E = [ i for i in itertools.accumulate(D) ]

    # print( 'E : ',E )

    G = []
    # print( S[:E[0]] )
    G.append(int( S[:E[0]] ) )

    for i in range(1, len(D) ):
        # print(i ,'    ' , E[i],'   '   , S[ E[i-1] :E[i]]  )
        G.append( int(S[ E[i-1] :E[i]])  )

    return G

print('\n--------------------------TESTS------------------------------')
t1  = time.time()

X = decomp_rec( 5, L  )
N='123456789'
for cnt, I in enumerate(X) :
    print(str(cnt+1),'      ', I  )
    # for j in range(len(I)-1 ) :
    #     print(j,'     ', I[j] ,'     ' , X[ I[j] ] )

t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')

print('\n================  My FIRST SOLUTION,   ===============\n')
# t1  = time.time()





# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')


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
# print('\n--------------------------SOLUTION 5,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
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

