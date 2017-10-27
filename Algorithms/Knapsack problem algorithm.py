
Items = [ (100, 3), (20, 2), (60, 4), (40, 1)  ]        # The table with Items, first index :Values, Second : Weight
print(Items)

def Knapsack_algorithm(Items, weight) :   # by Bogdan Trif @ 2017-03-06, 16:45
    T_wt = weight        # Total weight

    V = [[0 for x in range(T_wt+1)] for x in range(len(Items)+1)]
    print(V,' <---- before \n')

    for i in range(1, len(V) ) :
        for w in range(1, len(V[i]) ) :
            if Items[i-1][1] > w :
                V[i][w] = V[i-1][w]

            elif Items[i-1][1] <= w :
                V[i][w] = max ( V[i-1][w] , Items[i-1][0] + V[i-1][ w- Items[i-1][1]  ]    )
        print(V[i])

    selected = []
    i, w = len(Items), T_wt
    while  i and w > 0 :
        if V[i][w]  != V[i-1][w] :
            w = w-Items[i-1][1]
            selected.append(Items[i-1])
            i = i-1
        else :
            i= i-1
    print('\nThe following items have been selected : \t',selected)
    return selected

Knapsack_algorithm(Items, weight = 5 )

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181]
P=[]
for p in primes :
    P.append( (p, 1 ) )

print(P)

# K = Knapsack_algorithm(P, weight= sum(primes)//2 )
#
# L1 = []
# for i in K :
#     L1.append(i[0])
# print('\nL1',L1)

