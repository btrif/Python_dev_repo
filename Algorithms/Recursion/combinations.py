#  Created by Bogdan Trif on 31-10-2017 , 3:49 PM.

N = [ 1, 2, 3, 4, 5, 6 ]

def xuniqueCombinations(items, n):
    if n==0: yield []

    else:
        for i in range(len(items)):
            for cc in xuniqueCombinations(items[i+1:], n-1):
                yield [items[i]]+cc


print( list( xuniqueCombinations(N, 4) ) )




def combinations(N, length) :
    if length == 0:
        print('---'*20)
        yield []

    for i in range(len(N)) :
        for j in combinations( N[i+1:], length-1 ) :
            print(i,j ,  '       ', N[i+1:],  j , '       ' , [ N[i] ] + j )

            if [N[i]][-1] != 2 :
                yield [ N[i] ] + j


print( list( combinations(N,4) ) )