
A = [ -1, 3,- 4, 5, 1 , -6, 2, 1 ]

def solution1(A) :
    indeces = []
    for i in range(len(A)) :
        for j in range(i, len(A)) :
            if  sum( A[: i+1] ) == sum( A[j+1 :] ) :
                print(A[:i+1] , A[j+1:] )
                indeces.append(i+1 )
    return indeces

print(solution1(A))