import numpy as np
#           List going backwards. Reverse List
my_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print('Original list :  ', my_lst)
print('\nOutput the list forwards only the ODD INDEX terms  :', my_lst[::2])        # becomes [1, 3, 5, 7, 9, 11]

print('Output the list forwards only the EVEN INDEX terms  :', my_lst[1::2])        # becomes [2, 4, 6, 8, 10, 12]

print('Output the list backwards : ', my_lst[::-1],'\n')         # becomes  [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

print('Output the list backwards jumping 2 by 2, ODD Terms :  ', my_lst[10::-2])                # becomes 11 9 7 5 3 1

print('Output the list backwards jumping 2 by 2, EVEN Terms :  ', my_lst[::-2])                # becomes [12, 10, 8, 6, 4, 2]

print('Last few elements of my_lst list :',my_lst[-3:],'\n')               # Last few elements of a list [10, 11, 12]

print('Sum of the list is : ', sum(my_lst))

# Display ONLY ODD Index Terms from a list :
print(my_lst[1::2])

print('---------List slices with negative step -----------------' )
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print( a[::-1] )
print(  a[::-2] )

print(' ---------List slice assignment -----------------' )
a = [1, 2, 3, 4, 5]
a[2:3] = [0, 0]
print( a )
a[1:1] = [8, 9]
print( a )
a[1:-1] = []
print( a )

print(' ---------Naming slices (slice(start, end, step)) -----------------' )
a = [0, 1, 2, 3, 4, 5]
LASTTHREE = slice(-3, None)
print( LASTTHREE )
slice(-3, None, None)
print( a[LASTTHREE] )

print('\n-------------------------------- slice ------------------------')
sl = slice(0, 6, 1)
print ('Using slice we can build custom ranges :  ',my_lst[sl])


print('\n----------- Grouping adjacent list items using zip ---------------')

a = [1, 2, 3, 4, 5, 6]

# Using iterators
group_adjacent = lambda a, k: zip(*([iter(a)] * k))
print( list(group_adjacent(a, 3)) )
print( list(group_adjacent(a, 2)) )
print( list(group_adjacent(a, 1)) )

# Using slices
print('---- Using slices ----')
from itertools import islice
group_adjacent = lambda a, k: zip(*(islice(a, i, None, k) for i in range(k)))
print( list(group_adjacent(a, 3)) )
print( list(group_adjacent(a, 2)) )
print( list(group_adjacent(a, 1)) )


print('---------------------  PRODUCTS ---------------------')
print('\nProduct of the list is (FIRST METHOD): ', np.prod(my_lst))   # <------VERY VERY SLOW

print('\nProduct of the list is (SECOND METHOD): ')
P=1
for i in my_lst :   P *= i
print(P)

print('Product of a list using numpy :')
#from numpy import prod
print(np.prod([2,3,3,5]))                           # Product of the elements in a simple list
print(np.prod([[1.,2.],[3.,4.]]))                    # Even when the input array is two-dimensional:
print(np.prod([[1.,2.],[3.,4.]], axis=1))           # But we can also specify the axis over which to multiply:

print('\n================= LIST BASIC OPERATIONS ========================')

L=[9,6,16,0,54,11,3, 11, 0, 6, 11]
print('Return the maximum value from the list :', max(L))
print('Return the index with the maximum value from the list :', L.index(max(L)))

print('This prints a sorted list, the original remains unchanged:  ',sorted(L))
L.sort()
print('This sorts the list permanently:  ', L)
L.reverse()
print('This reverse the list permanently:  ', L)

print('List only unique elements : ', list(set(L)))

print("Join a list of numbers in a string :",  ''.join( str(i) for i in  L ) )

roman = ['MMMMDCLXXII', 'MMDCCCLXXXIII']
print("Join a list of strings :",  ''.join( roman ) , type( ''.join( roman )  ))


print('\n--------  CORECT WAY TO CREATE A NESTED LIST -  MATRIX -----------------')
# The correct way to create a Nested list (Matrix).
# If this method is not respected, when in some row an element is changed, it will be done in ALL
# previous ROWS !! That's very annoying

V = [[0 for x in range(5+1)] for x in range(4+1)]
print(V)

print('\n------------ CLONING, CLONE A LIST  ----------------------')
# Doing this way if you modify one list it will not affect the other as it will do with M=L where both will point out to the same list
M = L[:]        # However this doesn''t work for nested lists, like matrices ...etc...
print('M == L :  ',M==L,'         ;   M is L :  ', M is L)
M.insert(2,33)
print('First List : ',L,'   ;  Second List : ',M)

print('\n---------------Clone a Nested list, matrix : -----------------')
from copy import copy, deepcopy
A = [[1,2,3],[4,5,6],[7,8,9]]
B = deepcopy(A)
print(B)
# Using deepcopy() is a good solution. For a simple 2D-array case
C = [row[:] for row in A]
print(C)

# For 2D arrays it's possible use map function:
print(" For 2D arrays it's possible use map function: ")
old_array = [[2, 3], [4, 5]]
new_array = map(list, old_array)
print('old_array : ', old_array)
print('new_array : ', list(new_array))

print('\n---------- Replace an element in a simple list without affecting the indexing -----------')
print(my_lst)
my_lst.insert(my_lst.index(7),100)
del(my_lst[my_lst.index(7)])
print(my_lst)


print('\n ================== OPERATIONS WITH SUBLISTS =======================')
print('Changing a sublist will change also the list :\n')
warm = ['yellow', 'orange']
hot = ['red']
brightcolors = [warm]
print('brightcolors :',brightcolors)
brightcolors.append(hot)
print('brightcolors : ',brightcolors)
hot.append('pink')
print('hot : ',hot)
print('The list has been changed: ', brightcolors)
print('Concatenate lists : ', hot+warm)
print( 'Divide each element from a List  ' ,[ int(i / 2) for i in [2,4] ])      # List Comprehension to divide each element of a list



print('\n=================== JOIN,  FLATTEN A LIST =======================')
print('----------------- SINGLE FLATTEN , JOIN  ELEMENTS------------------')

# Method I
list_of_lists = [[180.0, 1, 2, 3], [173.8], [164.2], [156.5,[45,12,[81,41,[2,3,8],4,11]]], [147.2], [138.2]]
single_flattened = [val for sublist in list_of_lists for val in sublist]
print(single_flattened)

# Method II
import itertools
a = [[1, 2], [3, 4], [5, 6]]
print(list(itertools.chain.from_iterable(a)) )

# Method III
print(sum(a, []))

# Method IV
print( [x for l in a for x in l] )

# Method V
a = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
print( [x for l1 in a for l2 in l1 for x in l2] )

# Method VI
a = [1, 2, [3, 4], [[5, 6], [7, 8]]]
flatten = lambda x: [y for l in x for y in flatten(l)] if type(x) is list else [x]
print ( flatten(a) )




print('\n----------------------- Join two lists --------------------------')
l=[101, 107]
m=[10079, 10103]
lm = l+m
print(lm)

print('\n---------------- RECURSION FLATTENING, Many levels of sublists ------------------')

def flatten(lst):
	return sum( ([x] if not isinstance(x, list) else flatten(x)
		     for x in lst), [] )

flattened =  flatten(list_of_lists)
print(flattened)

print('\n---------------- ITERATIVE FLATTENING, Many levels of sublists ------------------')
def flat(lst):
    '''Function flat is iterative and flattens the list in-place.
     It follows the Python idiom of returning None when acting in-place:'''
    i=0
    while i<len(lst):
        while True:
            try:
                lst[i:i+1] = lst[i]
            except (TypeError, IndexError):
                break
        i += 1
fl = flat(list_of_lists)
print(fl)

print('\n---------------- GENERATIVE FLATTENING, Many levels of sublists ------------------')

def flatten(lst):
    ''' This method shows a solution using Python generators.
     flatten is a generator that yields the non-list values of its input in order.
     In this case, the generator is converted back to a list before printing.'''
    for x in lst:
        if isinstance(x, list):
            for x in flatten(x):
                yield x
        else:
            yield x

flt = flatten(list_of_lists)
print(flt)

print('\n-------------------------MUTATION & ITERATION ------------------------')
# AVOID MUTATIING A LIST  as you are iterating over it   !!!!!!!!!!!!!
L1 = [1, 2, 3, 4];  L2 = [1, 2, 5, 6] ; print('The original lists are : ', L1,'  ; ',L2)
def remove_dups(L1, L2):
    ''' Removes duplicates from L1, does nothing on L2 '''
    L1_copy = L1[:]
    for e in L1_copy:
        if e in L2:
            L1.remove(e)
remove_dups(L1, L2)
print('The lists with duplicates from L1 removed are : ', L1,'  ; ',L2)

print('\n------------------------- REMOVE AN ITEM ------------------------')
lll=['foo', 'bar', 'baz', 'bar', 'bar']
print(lll)
print('REMOVE method removes a string and an int :  ',lll.remove('bar'))
print(lll)
print('POP method removes only an integer by its index  :  ',my_lst.pop(4))

print('\n ------------------------ REMOVE MANY ITEMS with CONDITION, first CLONE The LIST -------------')
berbec = [1,3,4,56,2,1,42,5,1,54,2,1,5,1,3,1,6,54,1,43,1,1,4,1]
jaguar = berbec[:]
print(jaguar)
for i in range(len(berbec)) :
    if berbec[i] == 1 :
        jaguar.remove(berbec[i])
print(jaguar)

print('\n ------------------------ REMOVE/ DELETE MANY ITEMS at ONCE  -------------')
A = [3,5,4,7,9,8,1,2,10]
print('Original List : ', A)
rem = [3,4,5]
print('Items to remove/ delete at once: ', rem)
new_A = [i for i in A if i not in rem]
print('The new_A list after we deleted the elements from rem list: ', new_A)


print('\n ----------------------- Get the INDEX in a nested list : ------------------------')
my_array=[['1', '2', '3', '7'], ['0', '1', '6', '9'], ['0', '1', '3', '9'], ['1', '2', '5', '8'], ['0', '1', '5', '8']]
mtx = [[1,    2,    3,    4],\
           [5,    6,    7,    8],\
           [9,   10,   11,  12],\
          [13,  14,   15,  16]]
print(my_array[2].index('3'), type(my_array[0]))            # Prints 2    <class 'list'>
print(mtx[2-2].index(3), type(mtx[0][3]))                          # Prints   2 <class 'int'>

print('\n=====================    COUNT ELEMENTS     ==========================')
print(' -------------How to count the occurrences of a list item in Python ---------------------')
print(' -------------- Count the numbers of elements in a list ----------------------------')
# Function which counts the number of occurrences of elements in a list
test_list = [2, 2, 13, 5 , 2, 2, 3, 3, 7, 13, 5, 7, 19]
def occurDict(items):
    '''  Function which counts the number of occurrences of elements in a list'''
    d = {}
    for i in items:
        if i in d:
            d[i] = d[i]+1
        else:
            d[i] = 1
    return d

duplicates = {}
for i in test_list:
    if i in duplicates:
        duplicates[i] += 1
    else:
        duplicates[i] = 1
print(duplicates)

print('\n 2nd method to count the numbers of elements in a list ')
test_2=[2, 2, 8, 2, 5, 5, 6, 5, 6, 5, 6, 7, 2, 5, 5, 5, 6, 8]
for i in set(test_2):
    print(i, test_2.count(i), end='; ')

def count_elem(lst):        # Nice function, made by Bogdan Trif @ 2017-04-09, 13:30
    X = []
    for i in set(lst):
        print(i, lst.count(i), end='; ')
        X.append((i, lst.count(i) ))
    return X

count_elem([1,2,3,1,1,2,1,3,2,2])

print('Count a single element at a time :  ',[1, 2, 3, 4, 1, 4, 1].count(1))

print('\n ---------- Count the number of items in a list with collections Counter --------')
import collections

a = [1,1,9,1,7,3,1,2,7,2,2,7,9,2,3,3,4,5,5]

counter=collections.Counter(a)
print(counter)
# Counter({1: 4, 2: 4, 3: 2, 5: 2, 4: 1})
print(counter.values())
# [4, 4, 2, 1, 2]
print(counter.keys())
# [1, 2, 3, 4, 5]
print(counter.most_common(3))
# [(1, 4), (2, 4), (3, 2)]

print(counter.items())
print(counter[9])
print(type(counter))

for i in counter:
    print(i, counter[i],end=' ')



from collections import Counter
lst = ['blue', 'red', 'blue', 'yellow', 'blue', 'red']
print(Counter(lst))


print ('Count only the elements which occur two or more times ' ,[item for item, count in Counter(test_2).items() if count > 1] )
print ('Count only the elements which occur two  times ' ,[item for item, count in Counter(test_2).items() if count == 2] )


print ('\nUsing LIST COMPREHENSION count all elements : ',[[x, lst.count(x)] for x in set(lst)] )

print('\n Another way to get the number of occurrences of each item, is/in a DICTIONARY :  ',dict((i, lst.count(i)) for i in lst))


lst = [True, False, False, True, True, True, True, True, True]
def duplicates(lst, item):
    ''':Description:    index-of-duplicates-items-in-a-python-list
    :param lst: list
    :param item: argument : boolean: True , False, integer, anything
    :return:  A list containing the index of the element which is duplicate
    '''
    return [i for i, x in enumerate(lst) if x == item]

print(duplicates(lst, False) )


def count_repetitions(lst):
    ''':Description: Counts how many consecutive occurrences there are in a list
    '''
    pos = 0
    cnt=0
    for i in range(1,len(lst)):
        if lst[i] == lst[i-1]:
            pos += 1
        if lst[i] != lst[i-1]:
            pos = 0
        # print(pos , end='  ')
        if pos == 1 : cnt +=2
        if pos == 2 or pos == 3 or pos ==4 : cnt +=1
    return cnt

##############################

print('\n----------- Finding consecutive numbers in a list -----------------')

import itertools
from operator import itemgetter
# Find runs of consecutive numbers using groupby.  The key to the solution
# is differencing with a range so that consecutive numbers all appear in
# same group.
L = [ 1, 4, 5, 6, 10, 15, 16, 17, 18, 22, 25, 26, 27, 28]
for k, g in itertools.groupby( enumerate(L), lambda x: x[1]-x[0] ) :
    print (list(map(itemgetter(1), g)))


print('\n ------------ Most common elements in an iterable (collections.Counter) -------------')
import  collections
A = collections.Counter([1, 1, 2, 2, 3, 3, 3, 3, 4, 5, 6, 7])
print(A )
print( A.most_common(1) )

print ( A.most_common(3) )

######################################
print('\n-------------------    Finding the index of an item given a list containing it in Python  -----------------------')
# It always finds the index of the first element in the list, so if there are many the next ones will not be listed:
print(["foo", "bar", "baz", "bar"].index("bar"))
print(test_list.index(13),end=' ')

#       Using Enumerate :
print('\nUsing Enumarate : ')
xs = ['foo', 'bar', 'baz', 'bar','Dan', 'bar']
for i, j in enumerate(xs):
    if j == 'bar': print (i, end= ' ' )
# This can be more useful than index if there are duplicates in the list, because index() only returns the first occurrence,
# while enumerate returns all occurrences.    As a list comprehension:
f = [i for i, j in enumerate(['foo', 'bar', 'baz', 'bar', 'bar']) if j == 'bar']
print('\n',f)

print('-------'*20)

# Boolean, Get information about the existence of an element in a list:
print('\nBOOLEAN, Get information about the existence of an element in a list:')
print(15 in test_2)
print(7 in test_2)


print('\n------------------------ Find the closest element of a number in a list------------------------------')

print('--------------------------BINARY SEARCH ALGORITHM , VERY VERY FAST ----------------')
def bin_search(n, List):        # VERY FAST ALGORITHM
    ''':Description: Search for an element in the list and returns the index of it. If it not finds it returns
        the index of the element closest to its left, the smaller number.
    :param: **n**- integer, the number to find
                **List** - lst type, the list to search for
    :returns:   int, the index of the element
    '''
    left = 0
    right = len(List) -1

    while left <= right:
        midpoint = (left+right)//2
        if List[midpoint] == n: return midpoint
        elif List[midpoint] > n: right = midpoint-1
        else: left = midpoint+1
    if n > List[midpoint]: return midpoint
    else: return (midpoint-1)

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
myNumber = 87
print(primes)
print("I don't have the number",myNumber,"in the list. But I can get the INDEX left close to it it :", bin_search(myNumber, primes ))


print('\n------------------------SLOWER METHODS, Only for lists <1000 elements  :------------------------------')

myNumber = 87
print("I don't have the number",myNumber,"in the list. But I can get the closest value to it :")
print('Closest number to :',myNumber,'is :  ' ,min(primes, key=lambda x: abs(x-myNumber)),'\n')

print('If one want to find more elements nearby :')
from heapq import nsmallest
print(nsmallest(3, primes, key=lambda x: abs(x-myNumber) ))
# or
# This does the following:
# Create a sequence of tuples (d, x) where d is the distance to your target
# Select the first k elements of that list
# Extract just the number values from the result, discarding the distance
print(  [n for d, n in sorted((abs(x-myNumber), x) for x in primes)[:3]]  )

print('\n------------------------MIN, Max of TWO LISTS :------------------------------')
pth1=[131, 201, 96, 342, 746, 422, 111, 956, 331]
pth2=[131, 201, 96, 342, 746, 422, 121, 37, 331]

for x, y in zip(pth1, pth2[::-1]):
    print(min(x, y),end='  ')

print('\n\n------------------------ INTERSECTION, Common elements of TWO Sublists :------------------------------')
# Method 1
A=[1,3,5,'a','c',7]
B=[1,2,3,'c','b','a',6]
print('Method 1 : ',A,B ,  '\n' ,set(A).intersection(B))

# Method 2
b1 = [1,2,3,4,5,9,11,15]
b2 = [4,5,6,7,8]
b3 = [val for val in b1 if val in b2]
print('Method 2 : ',b1,b2,'\n',b3)

# Method 3
def intersect(a, b):
    '''  Returns the intersection of two lists. Only the common elements will be displayed.  '''
    return list(set(a) & set(b))
print ('Method 3 : \n',intersect(b1, b2))


print('\n---------------- SUBSet of another List -------------------------')
def isSubset(L1, L2):
    '''  Returns True if the first list is a subset of the second list, otherwise returns False'''
    for e1 in L1:
        matched = False
        for e2 in L2:
            if e1 == e2:
                matched = True
                break
        if not matched:
            return False
    return True
L1 = [1,2,3]
L2 = [1,2,3,4]
print(isSubset(L2, L1))

print('\n--------------------Generate all the Subsets of a List, RECURSION ---------------------')
def genSubsets(L):
    ''' Generates all the possible Subsets of a List. Has O(c^n) complexity (Exponential) '''
    res = []
    if len(L) == 0:
        return[[]] #list of empty list
    smaller = genSubsets(L[:-1])# all subsets without last element
    extra = L[-1:]# create a list of just last element
    new = []
    for small in smaller:
        new.append(small+extra) # for all smaller solutions, add one with last element
    return  smaller+new# combine those with last element and those without

print(genSubsets(L2))

print('\n------------------ Instances of a list ------------------------')
L = [10, 4, 3, 8, 3, 4, 5, 7, 7, 2]
print(isinstance(2,list))                   # Returns False, because  2 is NOT a list, is an integer
print(isinstance([5],list))                 # Returns True, because [5] is a list  with a single element
print(isinstance([5,6,2,5,9],list))     # Returns True, because [5,6,2,5,9] is a list
print(any(isinstance([5,6,2,5,9],list)) for i in L)     # generator object
print(any(isinstance(i , list)) for i in L)     # This expression is a type boolean to check if a sublist is a part of a list

########################################
def deep_reverse(L):
    """ assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also
    reverses the order of the int elements in every element of L.
    It does not return anything.
    """
    if any(isinstance(i, list) for i in L) == True:
        for A in range(len(L)):
            L[A].reverse()
        L.reverse()
        return L
L = [[2, -1, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 101, 10, 1, 1, 5, 4, 3]]
print(deep_reverse(L),'\n')

print('---------------------- Checks if a sublist is part of a composed list of lists -------------------------------- ')
if any(isinstance(i, list) for i in L) == True:     # isinstance(i,list) checks if i is a type list from a larger composed list of lists L
        for j in range(len(L)): print(L[j])             # prints the sublists of L


print('\n================== SEARCH in MATRICES, LIST of Lists ==================')
print('\n-------------- Search for an element in a list of list if the position in the sublist is known------------------')
my_list = [['a','b'], ['a','c'], ['b','d']]
search = 'c'
print(any('c' == x[1] for x in my_list))
print('d' in (x[1] for x in my_list))

print('\n--------------- Get the index of a searched element from a matrix ------------')
mymatrix=[[1,2,19],[4,19,6],[7,8,9]]
val = 9
print([(index, row.index(val)) for index, row in enumerate(mymatrix) if val in row])

print('\n--------------- Returns TRUE if an element is in a matrix, Else return FALSE ------------')
print( [val in row for row in mymatrix])
print( True  if  True in [ val in row for row in mymatrix ]  else False)    # Nice List Comprehension Construction, by Bogdan Trif, 2016-11-01

print('\n------------------Swapping, interchanging, moving elements in a list -----------------')
# keywords :    swap, move, change, interchange, shift elements in a list
enigma=[3, 1, 9, 6, 8, 0]
print(enigma)
print('Suppose you want to swap elements between them, here we swap 1 with 8 :')
enigma[1], enigma[4] = enigma[4], enigma[1]
print(enigma)


print('\n -----------NESTED LIST , Iteration over an unknown Number of Sublists----------- ')

from itertools import product

lists = [    ['THE', 'A'],
    ['ELEPHANT', 'APPLE', 'CAR'],
    ['WALKED', 'DROVE', 'SAT'] ]

for items in product(*lists):
    print (items)

print('\n---------  GROUP A LIST INTO SEQUENTIAL N-TUPLES   ----------')

import itertools

def group(lst, n):
    """group([0,3,4,10,2,3], 2) => iterator

    Group an iterable into an n-tuples iterable. Incomplete tuples
    are discarded e.g.

    # >>> list(group(range(10), 3))
    [(0, 1, 2), (3, 4, 5), (6, 7, 8)]
    """
    return itertools.zip_longest(*[itertools.islice(lst, i, None, n) for i in range(n)])

print( list(group(range(10), 4)))

####################

import itertools
def group_ranges(L):
    """
    Collapses a list of integers into a list of the start and end of
    consecutive runs of numbers. Returns a generator of generators.
    # >>> [list(x) for x in group_ranges([1, 2, 3, 5, 6, 8])]
    [[1, 3], [5, 6], [8]]
    """
    for w, z in itertools.groupby(L, lambda x, y=itertools.count(): next(y)-x) :
        grouped = list(z)
        yield (x for x in [grouped[0], grouped[-1]][:len(grouped)])


S= {1, 4, 5, 6, 10, 15, 16, 17, 18, 22, 25, 26, 27, 28}
print(S)
print([list(x) for x in group_ranges(S)])


print('\n----------- Largest and smallest elements (heapq.nlargest and heapq.nsmallest) ------------')
import random, heapq
a = [ random.randint(0, 100) for __ in range(100)]
print ( heapq.nsmallest(5, a) )
print( heapq.nlargest(5, a) )


print('\n----------------------- List Rotation --------------------')

# Method I
def rotate(l, n):     return l[-n:] + l[:-n]

A = [ 1, 2, 3, 4, 5, 6 ]
print('Initial string: \t', A, '          Right rotation 1 unit :\t' , rotate(A,-1)  )
print('Initial string: \t', A, '          Left rotation with 2 units :\t' , rotate(A, 2)  )

# Method II
import collections
d = collections.deque( A )
d.rotate(3)

print('Initial string: \t', A, '          Right rotation 3 units :\t' , d )


print('\n--------- Multiply a list or tuple each element with a number -----------')

print('Initial list :', A)
print('Multiple each element of the LIST with a number : \t ',list(map(5 .__mul__, A )) )
print('Multiple each element of the TUPLE with a number : \t ', tuple(map(5 .__mul__, A)) )


print('\n-------------- Perform tuple element wise operations ------------')
### Method I - Using numpy
import numpy
a = numpy.power((5, 9), (5, 2 ))
print('Element wise power operation on tuples : ', a)

### Method II , Using zip:
a = [1,2,3,4]
b = [2,3,4,5]
print('Element wise power operation on tuples : ',   [ a**b for a,b in zip(a,b)] )

print('\n---------------- Second, Third Largest Number in the list using heapq----------------')
el = [20,67,3,2.6,7,74,2.8,90.8,52.8,4,3,2,5,7]
import heapq
print( 'Second Largest element in the list : ',heapq.nlargest(2, el) )
print( 'Third Largest element in the list : ',heapq.nlargest(3, el) )

