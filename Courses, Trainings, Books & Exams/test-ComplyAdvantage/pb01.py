import random


A = [3, 5, 6, 3, 3, 5 ]

def solution1(A) :
    cnt = 0
    for i in range(len(A)) :
        for j in range(i+1, len(A)) :
            if A[i] == A[j] :
                print( i, j )
                cnt+=1
    if cnt > 10**9 : return 10**9

    return cnt

print('\n' , solution1(A)  )

print('\n-------------------- SOLUTION 2 ---------------')

def solution(A) :
    itr, D =  0, {}
    # cnt = 0
    for i in range(len(A)) :
        if A[i] not in D :
            D[ A[i] ] = [ i ]
        else :
            D[A[i]].append(i)
            itr += len( D[A[i]] )-1
    print(D)
    # c =  [ len(v)*(len(v)-1)//2 for k,v in D.items() ]
    # print( c )
    # if sum(c) > 10**9 : return 10**9
    if itr > 10**9 : return 10**9
    return itr

print('\n' , solution(A)  )

print('\n ------------------------- TEST CASES ------------------------------ ')


# print(   [ random.randint(11 ,20)  for i in range( random.randint(10 ,50)  )  ]    )

for i in range(1, 100) :
    B = [ random.randint(11 ,20)  for i in range( random.randint(10 ,50)  )  ]
    print('\t' , str(i) +'.       solution = ',  solution(B),'          ', B )
