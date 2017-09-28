######## @ 2017-02-23, 10:47 . Note: I finally learn how to replace those boring nested loops with itertools
import itertools

for a, b, c, d in itertools.product(range(1, 4+1), repeat=4):
    print(a, b,c, d, end='   ')


from itertools import combinations_with_replacement, product

print("j   ", "    i  ","       i+j")
print("------"*20)


for i in range(1, 5, 1):            # this is the list with : 1,2,3,4 ;     Starts at 1 end ENDS AT 4
     for j in range(1, i+1, 1):       # This is the list : 1,2,3,4 ;    i+1 is needed because i ends at 4
         if (i != j):
            print(j, ' + ', i,  '    Sum: ',i+j)


print("------"*20)

for i in range(1, 3, 1):
     for j in range(i+1, 0,-1):

        print(i,  j,  'Sum: ',i+j)

print("------"*20)

latin=['A', 'B', 'C', 'D', 'E', 'F']
greek=['alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta' , 'eta']

for x in range(1,len(latin)+1,1):
    print(x, latin[x-1],'   ',end=' ')

print('\n'*2,"------------------ LISTS COMBINATIONS & ASSOCIATIONS OF ELEMENTS ----------------------\n")

print(latin)
# This puts aside 2 elements from an array (list) , Combinations of elements in an array, NON-REPEATING,    !!!!
print('------This puts aside elements from an array (list) , Combinations of  2 elements in an array, NON-REPEATING,    !!!!\n')
counter=0
for x in range(len(latin)+1):
    for y in range(x+1, len(latin)):
        counter += 1
        print(str(counter)+".  ",latin[x],latin[y], end='    ')
print('\nThe number of combinations between two elements of the array is:  ',counter)

print('-----'*25)


print('\n-------Combinations of 2 elements from an array (list) , BACKWARDS, NON-REPEATING, Without FIRST Element  !!!!\n')
counter=0
for x in range(len(latin)-1,-1,-1):
    for y in range(1,x):                            # With first Element included is :     for z in range(0,y):
        counter += 1
        print(str(counter)+".  ",latin[y],latin[x], end='    ')
print('\nThe number of combinations between two elements of the array is:  ',counter)

print('\n-----------------------------------------')

print('This puts aside 3 elements from an array (list) , NON-REPEATING, BACKWARDS, Without FIRST Element    !!!!\n')
counter=0
for x in range(len(latin)-1,-1,-1):
    for y in range(1,x):
        for z in range(1,y):                # With first Element included is :     for z in range(0,y):
            counter += 1
            print(str(counter)+".  ",latin[z] ,latin[y],latin[x], end='    ')
print('\nThe number of combinations between 3 elements of the array is:  ',counter)

print('\n-----------------------------------------')
print(' Combinations of 3 elements from list , REPEATING, Euler PB86- Cuboid Route----------\n')
counter=0
for x in range(len(latin)):
    for y in range(x, len(latin)):
        for z in range(y, len(latin)):                # With first Element included is :     for z in range(0,y):
            counter += 1
            print(str(counter)+".  ",latin[x] ,latin[y],latin[z], end='    ')
print('\nThe number of combinations with replacement between 3 elements of the list is:  ',counter)
print('This is equivalent to itertools combinations with replacement: ' )
C=list(combinations_with_replacement(latin, 3))
print(len(C),C)
print('\n-------------------------------------------')


print('\nThis puts aside 4 elements from an array (list) , NON-REPEATING, BACKWARDS, Without FIRST Element    !!!!\n')
counter=0
for a in range(len(latin)-1,-1,-1):
    for b in range(1,a):
        for c in range(1,b):
            for d in range(1,c):                # With first Element included is :     for z in range(0,y):
                counter += 1
                print(str(counter)+".  ",latin[d] ,latin[c],latin[b],latin[a], end='    ')
print('\nThe number of combinations between 4 elements of the array is:  ',counter)

print('\n\n---------------EXTEND A SET (list) & Calculate ONLY the EXTENDED List, PB086 Euler -----------------')

digit=[1,2,3]
cnt = 0
BASIC_SET = []
for x in range(len(digit)):
    for y in range(x, len(digit)):
        for z in range(y, len(digit)):
            cnt += 1
            print(str(cnt)+".  ",digit[x] ,digit[y],digit[z], end='    ')
            BASIC_SET.append((digit[x] ,digit[y],digit[z]))
print('\n',BASIC_SET)
print('\nNr of Combinations with Replacement as 3 :', cnt)
EXTENDED_SET=BASIC_SET[:]
print('We extend the set with one element, we compute only the difference elements. Not all again :')
cont=0
for x in range(4 ,4+1 ):
    for y in range(1, 4+1):
        for z in range(y, 4+1):
            cont+=1
            print(str(cont)+".  ",x , y, z, end='    ')
            EXTENDED_SET.append((x,y,z))
print('\nIf we extend the set with an additional element the Nr of Combinations ONLY for the element  with Replacement as 3 :', cnt)
print('Total Elements of the Extended SET will be :', len(EXTENDED_SET), EXTENDED_SET)

print('\n---------------COMBINATIONS of All elements in All possible Numbers --------------------------')

A=[2,3,5,7,11,13]
from itertools import combinations

for i in range(1, len(A)+1):                       # If you don't want the last element of the list :     range(len(A))
    for j in  range(1, len(A)+1) :
        Comb = list(combinations(A[0:j],i))
    print(Comb, end='  ')

print('\n--------    # Without the last element and Listed only once each       --------- ')
# Without the last element and Listed only once each
for k in range(len(A)-1,len(A)):
    print('------------',A[0:k],'-------')
    for l in  range(len(A)) :
        Comb = list(combinations(A[:k],l))
        #print(Comb)
        for m in Comb:
            print(m, end ='   ')


print('\n---------------------------ASCENDING LIST ---------------------------')
fives=[5,10,15,20,25,30]
for i in range(len(fives)):
    print(fives[0:i+1])

print('\n---------------------------DESCENDING LIST ---------------------------')
fives=[5,10,15,20,25,30]
for i in range(len(fives), 0, -1):
    print(fives[0:i])


# To note that in general the break issue the break only on the iteration it is put on
print("\n-----------------  FOR LOOP BREAK --------------------")
for i in range(100):
    if i > 20 :
        print(i, end=' ')
        if i > 25:
            break

print("\n----------------- BREAK  MULTIPLE FOR LOOP BREAK IN A FUNCTION  --------------------")

def myfunc():               # Stops after finding the first result
    for i in range(200, 500):
        for i2 in range(i, 500):
            for i3 in range(i2, 500):
                if i*i + i2*i2 == i3*i3 and i + i2 + i3 == 1000:
                    print (i, i2, i3, i*i2*i3 )
                    return              # Exit the function (and stop all of the loops)
myfunc() # Call the function


print("\n----------------- BREAK MULTIPLE FOR LOOP GENERATOR & BREAK IN A FUNCTION  --------------------")
# why not use a generator expression:

def my_iterator():              # This is a GENERATOR FUNCTION
    for i in range(200, 500):
        for i2 in range(i, 500):
            for i3 in range(i2, 500):
                yield i, i2, i3

for i, i2, i3 in my_iterator():                 # Stops after finding the first result
    if (i*i + i2*i2 == i3*i3 and i + i2 + i3 == 1000 ) :
        print ( i, i2 ,i3 , i*i2*i3 )
        break

print("\n-----------------  BREAK MULTIPLE FOR LOOP, RAISE AN EXCEPTION AND BREAK  --------------------")
#You can raise an exception
try:
    for a in range(5):
        for b in range(5):
            if a==b==3 :
                print(b)
                raise StopIteration
            print (b, end= '  ')
except StopIteration : pass

try:
    for i in range(200, 500):
        for i2 in range(i, 500):
            for i3 in range(i2, 500):
                if (i*i + i2*i2 == i3*i3 and i + i2 + i3 == 1000 ) :
                    print ( i, i2 ,i3 , i*i2*i3 )
                    raise StopIteration
except StopIteration : pass

print('\n-------------------- RECURSION, Multiple Nested For Loops, Custom Levels ------------------')

def loop_rec(y, number):
    if (number >= 1):
        loop_rec( y+1, number - 1 )
        for i in range(y):
            print(i, end=' ')
        print('')
    else:
        return

loop_rec(1,5)


print('\n------------------- With Itertools product ------------------')

for i, j, k in itertools.product(*itertools.repeat(range(3), 3)) :
    print(i,j,k, end='   ')

for i,j,k in itertools.product(*[range(3)]*3):
    print(i,j,k, end='   ')


print('\n-------------------- DYNAMIC LOOPS,  ------------------')
# Nested Lists, Iterating over an unknown number of nested loops in python
from itertools import product

lists = [
    ['THE', 'A'],
    ['ELEPHANT', 'APPLE', 'CAR'],
    ['WALKED', 'DROVE', 'SAT']
]

for items in product(*lists):
    print (items)

print('\n--------------------RECURSION, Dynamic For Loop ----------------------')

def dynamic_for_loop(boundaries, *vargs):
    if not boundaries:
        print(*vargs, end='   ') # or whatever you want to do with the values
    else:
        bounds = boundaries[0]
        for i in range(*bounds):
            dynamic_for_loop(boundaries[1:], *(vargs + (i,)))

boundaries = [[ 0,2,1], [0,3,1], [0,3,1]]

print('dynamic_for_loop  :\n '   )
dynamic_for_loop(boundaries)


print('\n#########   MORE ADVANCED METHODS TO GENERATE PYTHAGOREAN TRIPLETS    #################\n')
import itertools
# Method I - With Only One variable :

print(list((a,b,c) for a,b,c in itertools.product(range(1, 100), repeat=3) if a<=b<=c and a**2 + b**2 == c**2))

# Method II - With Only One variable :

print(list(x for x in itertools.product(range(1, 100), repeat=3) if x[0]<=x[1] <=x[2] and x[0]**2 + x[1]**2 == x[2]**2))


print('------------------ RECURSIVE GENERATOR ------------------')

# RECURSIVE GENERATOR

def orduples(size, start, stop, step=1):
    if size == 0:
        yield ()
    elif size == 1:
        for x in range(start, stop, step):
            yield (x,)
    else:
        for u in orduples(size - 1, start, stop, step):
            for x in range(u[-1], stop, step):
                yield u + (x,)
if __name__ == "__main__":
    print(list(orduples(3, 0, 5)))


print('\n -------------------- Unique, non-reapeating , COMBINATIONS --------------------')
from itertools import combinations

for combination in combinations(range(1,6), 3):
    print (combination, end='   ')



print('\n----------------- Unique Custom List Non-reapeating Combinations')
for combination in combinations([2, 3, 5, 7, 11, 13], 3):
    print (combination, end='  ')

print('\n----------------- ALL Variable  Custom List Non-reapeating Combinations')
for i in range(1,6) :
    print('\n------')
    for c in combinations([2,3,5,7,11,13], i):
        print (c, end='   ')



