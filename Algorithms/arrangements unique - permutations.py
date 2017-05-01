from itertools import permutations, combinations
import time

'''
This functions make unique arrangements / permutations
Scope: because itertools.permutations make many duplicates for cases like L=[1,1,2,6] those algorithms
shorten the list of possible UNIQUE ARRANGEMENTS
'''
L = [1,1,2,6]
P = list(permutations(L))
print('We want to find all the unique permutations / arrangements of : ',L)
print(len(P), len(set(P)) , '    ',P, '\n Using itertools  means that :', len(P)- len(set(P)),' are duplicates !!!! This escalates even more for longer lists. If we Try : ')
L = [1,1,1,2,6]
print(L)
P = list(permutations(L))
print(len(P), len(set(P)) , '    ',P, '\n Using itertools  means that :', len(P)- len(set(P)),' are duplicates !!!! ')
L = [1,1,2,2,6]
print(L)
P = list(permutations(L))
print(len(P), len(set(P)) , '    ',P, '\n And a last example Using itertools  means that :', len(P)- len(set(P)),' are duplicates !!!! ')

print('\n\n--------------------BENCHMARK TEST --------------------------------')

L = [7, 7, 7, 11, 7, 5, 5, 5, 5, 5 ]
print('The list we perform the test with is : ', L)

t1  = time.time()

P = list(permutations(L))
print(len(P), len(set(P)) , '    ',set(P), '\n And a last example Using itertools  means that :', len(P)- len(set(P)),' are duplicates !!!! ')

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')



print('\n------------------BETTER FUNCTIONS ------------------')


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

t1  = time.time()

print('\n\nTest with unique_permutations Function : ',  list(unique_permutations(L)))
print('Length' ,len(list(unique_permutations(L))))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')










print('\n-------------------- My Very Worked Function, Better NO !!!!! ---------------------')

def nice_arrangements(lst):         # BETTER DON'T USE IT !!!! ----- TO DELETE !!!
    ''':Description: Function which makes nicer the arrangements/permutations of repeated values.
        The advantage becomes obvious when trying to permutate lists with length > 6

    :param lst: list
    :return:    list of lists
    '''

    F = lst

    def case_two_one(F) :
        Z , G , a = [], F[:], F[-1]
        G.remove(a)
        for i in range(len(G)):
            G.insert(i , a)
            A = tuple(G)
            Z.append(A)
            G.remove(a)
        return Z+[F]

    def case_two_two(F) :
        G = list(set(F))
        if F.count(G[0]) ==1 : a = G[0]
        else:  a = G[1]
        H, Z = F[:], []
        H.remove(a), H.remove(a)
        for x in range(len(F)+1):
            for y in range(x+1, len(F)):
                H.insert(x, a), H.insert(y, a)
                A = tuple(H)
                Z.append(A)
                H.remove(a), H.remove(a)
        return Z


    def case_three_one(F) :
        G = [i for i in F if F.count(i) == 1]
        a, b = G[0], G[1]
        H, Z = F[:], []
        H.remove(a), H.remove(b)
        for x in range(len(F)+1):
            for y in range(x+1, len(F)):
                H.insert(x, a), H.insert(y, b)
                A = tuple(H)
                Z.append(A)
                H.remove(a), H.remove(b)
                H.insert(x, b), H.insert(y, a)
                A = tuple(H)
                Z.append(A)
                H.remove(b), H.remove(a)
        return Z

    def case_two_three(F) :
        G = list(set(F))
        if F.count(G[0]) ==1 : a = G[0]
        else:  a = G[1]
        H, Z = F[:], []
        H.remove(a), H.remove(a)
        for x in range(len(F)+1):
            for y in range(x+1, len(F)):
                for z in range(y+1, len(F)):
                    H.insert(x, a), H.insert(y, a),  H.insert(z, a)
                    A = tuple(H)
                    Z.append(A)
                    H.remove(a), H.remove(a), H.remove(a)
        return Z

    def case_two_four(F) :
        G = list(set(F))
        if F.count(G[0]) ==1 : a = G[0]
        else:  a = G[1]
        H, Z = F[:], []
        H.remove(a), H.remove(a)
        for x in range(len(F)+1):
            for y in range(x+1, len(F)):
                for z in range(y+1, len(F)):
                    for w in range(z+1, len(F)):
                        H.insert(x, a), H.insert(y, a),  H.insert(z, a),  H.insert(w, a)
                        A = tuple(H)
                        Z.append(A)
                        H.remove(a), H.remove(a), H.remove(a), H.remove(a)
        return Z

    def case_four_one(F) :
        G = [i for i in F if F.count(i) == 1]
        a, b, c = G[0], G[1], G[2]
        H, Z = F[:], []
        H.remove(a), H.remove(b), H.remove(c)
        for x in range(len(F)+1):
            for y in range(x+1, len(F)):
                for z in range(y+1, len(F)):
                    P = list(permutations([a,b,c]))
                    for i in range(len(P)):
                        H.insert(x, P[i][0]), H.insert(y, P[i][1]), H.insert(z, P[i][2])
                        A = tuple(H)
                        Z.append(A)
                        H.remove(a), H.remove(b), H.remove(c)
        return Z

    def case_three_two_one(F) :
        R = [i for i in F if F.count(i) == 1 or F.count(i)==2 ]
        a, b, c = R[0], R[1], R[2]
        H, Z = F[:], []
        H.remove(a), H.remove(b), H.remove(c)
        for x in range(len(F)+1):
            for y in range(x+1, len(F)):
                for z in range(y+1, len(F)):
                    if a==b:  P1, P2, P3 = (a,b,c), (a,c, b), (c, a, b)
                    elif b==c : P1, P2, P3 = (a,b,c), (b,a,c), (c, b, a)
                    H.insert(x, P1[0]), H.insert(y, P1[1]), H.insert(z, P1[2])
                    A = tuple(H)
                    Z.append(A)
                    H.remove(a), H.remove(b), H.remove(c)
                    H.insert(x, P2[0]), H.insert(y, P2[1]), H.insert(z, P2[2])
                    A = tuple(H)
                    Z.append(A)
                    H.remove(a), H.remove(b), H.remove(c)
                    H.insert(x, P3[0]), H.insert(y, P3[1]), H.insert(z, P3[2])
                    A = tuple(H)
                    Z.append(A)
                    H.remove(a), H.remove(b), H.remove(c)
        return Z

    def case_five_one(F) :
        G = [i for i in F if F.count(i) == 1  ]
        a, b, c, d = G[0], G[1], G[2],  G[3]
        H, Z = F[:], []
        H.remove(a), H.remove(b), H.remove(c), H.remove(d)
        for x in range(len(F)+1):
            for y in range(x+1, len(F)):
                for z in range(y+1, len(F)):
                    for u in range(z+1, len(F)):
                        P = list(permutations([a,b,c,d]))
                        for i in range(len(P)):
                            H.insert(x, P[i][0]), H.insert(y, P[i][1]), H.insert(z, P[i][2]), H.insert(u, P[i][3])
                            A = tuple(H)
                            Z.append(A)
                            H.remove(a), H.remove(b), H.remove(c), H.remove(d)
        return list(set(Z))

    def case_five_two(F) :
        Q = [i for i in F if F.count(i) == 1 or F.count(i) == 2 ]
        a, b, c, d = Q[0], Q[1], Q[2],  Q[3]
        H, Z = F[:], []
        H.remove(a), H.remove(b), H.remove(c), H.remove(d)
        for x in range(len(F)+1):
            for y in range(x+1, len(F)):
                for z in range(y+1, len(F)):
                    for u in range(z+1, len(F)):
                        P = list(permutations([a,b,c,d]))
                        for i in range(len(P)):
                            H.insert(x, P[i][0]), H.insert(y, P[i][1]), H.insert(z, P[i][2]), H.insert(u, P[i][3])
                            A = tuple(H)
                            Z.append(A)
                            H.remove(a), H.remove(b), H.remove(c), H.remove(d)
        return list(set(Z))

    def case_five_three_one(F) :
        O = [i for i in F if F.count(i) == 1 or F.count(i) == 3 ]
        a, b, c, d = O[0], O[1], O[2], O[3]
        H, Z = F[:], []
        H.remove(a), H.remove(b), H.remove(c), H.remove(d)
        for x in range(len(F)+1):
            for y in range(x+1, len(F)):
                for z in range(y+1, len(F)):
                    for u in range(z+1, len(F)):
                        P = list(permutations([a,b,c,d]))
                        for i in range(len(P)):
                            H.insert(x, P[i][0]), H.insert(y, P[i][1]), H.insert(z, P[i][2]), H.insert(u, P[i][3])
                            A = tuple(H)
                            Z.append(A)
                            H.remove(a), H.remove(b), H.remove(c), H.remove(d)
        return list(set(Z))

    G = [i for i in F if F.count(i) == 1]
    if len(set(F)) == 2 and ( F.count(list(set(F))[0]) ==1 or F.count(list(set(F))[1]) ==1 )  :
        return case_two_one(F)

    if  len(set(F)) == 2 and  ( F.count(list(set(F))[0]) ==2 or F.count(list(set(F))[1]) ==2 ) :
        return case_two_two(F)

    if ( len(set(F)) == 3 and  len(G) ==2 ) :
        return case_three_one(F)

    if  len(set(F)) == 2 and ( F.count( list(set(F))[0]) == 3  or F.count( list(set(F))[1]) == 3 ) :
        return case_two_three(F)

    if  len(set(F)) == 2 and ( F.count( list(set(F))[0]) == 4  or F.count( list(set(F))[1]) == 4 ) :
        return case_two_four(F)

    if  len(set(F)) == 4 and  len(G) ==3  :
        return case_four_one(F)

    R = [i for i in F if F.count(i) == 1 or F.count(i)==2 ]
    if  len(F)>3 and len(set(F)) == 3 and len(R)==3 :
        return case_three_two_one(F)

    if  len(set(F)) == 5 and len(G)==4 :
        return case_five_one(F)

    Q = [i for i in F if F.count(i) == 1 or F.count(i) == 2 ]
    if  len(F)>4 and ( (len(set(F)) == 4 and len(G)==4 ) or (len(set(F)) == 3 and len(G)==4) ) :
        return  case_five_two(F)

    O = [i for i in F if F.count(i) == 1 or F.count(i) == 3 ]
    if  (len(set(F)) == 3 and len(O)==4 )   :
        return case_five_three_one(F)

    else:
        P = list(permutations(F))
        return list(set(P))


# L = [3, 3, 5, 2, 2, 2, 2]
# print('\nThe Ultimate Test for this Function : ', len(nice_arrangements(L)) ,nice_arrangements(L) )

