#  Created by Bogdan Trif on 26-09-2017 , 6:29 PM.
import time
from pyprimes import factorise
import itertools, functools, operator

def square_factoring(nr) :

    F = list(factorise(nr))
    # print( F )
    L, R = [], set()
    for i in F :
        j = i[1]//2
        for k in range(j):
            L.append(i[0])
    # print(L)
    if len(L) ==1 :
        return set([1]+L)
    else :
        for o in range(1, len(L)+1 ) :
            C = list(itertools.combinations(L, o))
#             print(C)
            for q in C :
                K =  functools.reduce(operator.mul, q)
#                 print(K)
                R.add(K)
        return R.union({1})



def square_factoring_pair(nr1 , nr2 ) :

    F = []
    for l in list(factorise(nr1)) :
        F.append( (l[0], l[1]*2) )
#         print(F)
    F =  F + list(factorise(nr2))

    # print( F )
    L, R = [], set()
    for i in F :
        j = i[1]//2
        for k in range(j):
            L.append(i[0])
    # print(L)
    if len(L) ==1 :
        return set([1]+L)
    else :
        for o in range(1, len(L)+1 ) :
            C = list(itertools.combinations(L, o))
#             print(C)
            for q in C :
                K =  functools.reduce(operator.mul, q)
#                 print(K)
                R.add(K)
        return R.union({1})






##################
K =  list(range(400799 , 400799 +20 ))



print('\n------------------ function 1 test --------------------------')
t1  = time.time()

for k in K :
    a1, a2 = k+1 , 8*k+5
    bbc = a1*a1*a2
    print( len(square_factoring(bbc)), square_factoring(bbc)  )

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000 , 6 ), 'ms\n\n')



print('\n------------------ function 2 test --------------------------')
t3  = time.time()

for k in K :
    a1, a2 = k+1 , 8*k+5
    bbc = a1*a1*a2
    print( len(square_factoring_pair(a1, a2))  , square_factoring_pair(a1, a2)  )


t4  = time.time()
print('\nCompleted in :', round((t4-t3)*1000 , 6 ), 'ms\n\n')


print('\nfunction 2 is  : ' , (t2-t1)/(t4-t3) ,'   faster than the function 1 !!! ' )