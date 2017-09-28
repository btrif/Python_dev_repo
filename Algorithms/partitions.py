

import time

# http://stackoverflow.com/questions/18503096/python-integer-partitioning-with-given-k-partitions
# https://www.ics.uci.edu/~eppstein/PADS/IntegerPartitions.py
# http://math.stackexchange.com/questions/18659/algorithm-for-generating-integer-partitions

print('------------------ Partitions of a number ---------------------')

def partitions1(n):

    a = [0 for i in range(n + 1)]
    k = 1
    a[0] = 0
    a[1] = n
    while k != 0:
        x = a[k - 1] + 1
        y = a[k] - 1
        k -= 1
        while x <= y :
            a[k] = x
            y -= x
            k += 1
        a[k] = x + y
        yield a[:k + 1]

Pnk_max = list(partitions1(8))
print(Pnk_max)


print('\n-------------------------- Partitions in three, I have better algorithms --------------------------------')

def partition_in_three(n):     #2017-02-06 Some minor losses, but no time to fix it now
    ''':Description: Partition a number in three in the form (a, b, c) where a>=b>=c
    :Usage:  >>> for i in P :  print( i )
    :param n: int, number
    :return: generator, tuple with partitions : (9, 1, 1), (8, 2, 1), (7, 3, 1) ....            '''
    a, b, c = n-1, 0, 1
    bc = b+c
    while a > n/3+1 :
        a-=1
        bc+=1
        for i in range( 1, bc//2+1):
            b=bc-i ; c=bc-b
            if a>=b :
                yield a, b, c
    if n%3 == 0 :
        yield n//3, n//3, n//3

PT = partition_in_three(6)

cnt=0
for i in PT :
    cnt+=1
    print(str(cnt)+'.       ', i )



########### Number partition - Recursion with Elegant Memoization ###############
print('########### Number partition - Recursion with Elegant Memoization ###############')
def memoize(f):
    memo={}
    def helper(x):
        if x not in memo:
            memo[x]=f(x)
        return memo[x]
    return helper

@memoize
def A000041(n):
    if n == 0: return 1
    S = 0
    J = n-1
    k = 2
    while 0 <= J:
        T = A000041(J)
        S = S+T if k//2 % 2 != 0 else S-T
        J -= k if k % 2 !=0 else k//2
        k += 1
    return S

print( A000041(7)) #the 100's number in this series, as an example



############################
print('\n------------------- Coins Partition -----------------')
def partition_coins(value=5):
        #value = 5
        coins = [1,2,5,10,20,50,100,200]

        ways = [1] +[0]*value
        ways[0] = 1
        print(ways)

        # Remove superior values than the actual number
        while coins[-1] > value  :
            del(coins[-1])

        for i in range(len(coins)) :
            for j in range(coins[i], value+1):
                #print(i,j, end=' ;  ')
                ways[j] += ways[ j - coins[i] ]
                #print(ways)
        print(ways[-1])

partition_coins(5)

total = 5
combinations = [1] + [0]*total
monies = [1,2,5,10,20,50,100,200]

print('\n--------------------------NUMBER PARTITION RECURSIVE FUNCTION  ----------------------------')
def partition(number):
    answer = set()
    answer.add((number, ))
    for x in range(1, number):
        for y in partition(number - x):
            answer.add(tuple(sorted((x, ) + y)))
            #print(answer)
    return answer

print(partition(4))

##########################          Most Efficient Algorithm ############
# If it's speed you're looking for, here is the most efficient known algorithm to generate all partitions of a positive integer.
# http://jeromekelleher.net/category/combinatorics.html
print('\n------------ ALL PARITIONS of a number -  An efficient Algorithm - Must still test it -------------------')

def accel_asc(n):
    a = [0 for i in range(n + 1)]
    k = 1
    y = n - 1
    while k != 0:
        x = a[k - 1] + 1
        k -= 1
        while 2 * x <= y:
            a[k] = x
            y -= x
            k += 1
        l = k + 1
        while x <= y:
            a[k] = x
            a[l] = y
            yield a[:k + 2]
            x += 1
            y -= 1
        a[k] = x + y
        y = x + y - 1
        yield a[:k + 1]

print(list(accel_asc(10)))



##############################################
t1  = time.time()

print('\n---------------------- Partition a number into MAXIMUM k parts ------------------')
# http://math.stackexchange.com/questions/18659/algorithm-for-generating-integer-partitions
def ruleAscLen(n, l):

    a = [0 for i in range(n + 1)]
    k = 1
    a[0] = 0
    a[1] = n
    while k != 0:
        x = a[k - 1] + 1
        y = a[k] - 1
        k -= 1
        while x <= y and k < l - 1:
            a[k] = x
            y -= x
            k += 1
        a[k] = x + y
        yield a[:k + 1]

Pnk_max = list(ruleAscLen(15 , 3))
print('Partition a number in maximum k parts :', len(Pnk_max) ,' \n', Pnk_max[:300] )

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n------------------Partition a number into EXACTLY k parts, with a MIN constraint ------------------')
t1  = time.time()

def partitionfunc(n, k, l = 2 ):
    '''n is the integer to partition, k is the length of partitions, l is the min partition element size'''
    if k < 1:
        raise StopIteration
    if k == 1:
        if n >= l:
            yield (n,)
        raise StopIteration
    for i in range( l, n+1):
        for result in partitionfunc(n-i, k-1 , i ):
            yield (i,)+result

P_exactly = list(partitionfunc(15, 3 ))
print('Partition a number in EXACTLY k parts :', len(P_exactly) ,' \n', P_exactly[:300] )


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n-------------- Partition a number into EXACTLY k parts, with MIN AND MAX constraints ------------------')

def partition_min_max(n, k, l, m):
    ''':Description:  n - is the integer to partition, k -  is the length of partitions,
    l - is the min partition element size, m - is the max partition element size '
   Taken from http://stackoverflow.com/questions/18503096/python-integer-partitioning-with-given-k-partitions
   **©** Modified by Bogdan Trif @ 2017-03-25, 12:20,
    :param n: n is the integer to partition
    :param k: k is the length of partitions
    :param l: l is the min partition element size
    :param m: m is the max partition element size
    :return: list of partition lists                        '''

    if k < 1:
        raise StopIteration
    if k == 1:
        if n <= m and n>=l :
            yield (n,)
        raise StopIteration
    for i in range(l,m+1):
        for result in partition_min_max(n-i, k-1, i, m):
            yield result+(i,)

x = list(partition_min_max(20 ,3, 3, 12 ))
print(x)

y = list(partition_min_max(15 ,3, 1, 6 ))
print(y)


