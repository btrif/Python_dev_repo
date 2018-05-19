# Problem 4           # Made by Bogdan Trif @ 2016-10-31, 00:01
'''
Problem 4       -   20 points possible (graded)
You are given the following definitions:

A run of monotonically increasing numbers means that a number at position k+1 in the sequence is
greater than or equal to the number at position k in the sequence.

A run of monotonically decreasing numbers means that a number at position k+1 in the sequence
is less than or equal to the number at position k in the sequence.

Implement a function that meets the specifications below.

For example:

If L = [10, 4, 3, 8, 3, 4, 5, 7, 7, 2] then the longest run of monotonically increasing numbers in L is [3, 4, 5, 7, 7]
and the longest run of monotonically decreasing numbers in L is [10, 4, 3].
Your function should return the value 26 because the longest run of monotonically increasing integers is longer
than the longest run of monotonically decreasing numbers.

If L = [5, 4, 10] then the longest run of monotonically increasing numbers in L is [4, 10] and the longest run
of monotonically decreasing numbers in L is [5, 4]. Your function should return the value 9 because
the longest run of monotonically decreasing integers occurs before the longest run of monotonically increasing numbers.

'''

def longest_run(L):
    """
    Assumes L is a list of integers containing at least 2 elements.
    Finds the longest run of numbers in L, where the longest run can
    either be monotonically increasing or monotonically decreasing.
    In case of a tie for the longest run, choose the longest run
    that occurs first.
    Does not modify the list.
    Returns the sum of the longest run.
    """
    # Your code here

    def monotony(a, b):
        if a < b : return '1'
        if a > b : return '-1'
        if a == b : return '0'

    M=[]

    for i in range(0 , len(L)-1) :
        if monotony(L[i],L[i+1]) == '1' :        M.append(1)
        elif monotony(L[i],L[i+1]) == '-1' :        M.append(-1)
        else:   M.append(0)

    L11, L22 = [], []
    L1, L2 = [], []
    indexi , indexd = 0, 0
    l1, l2 = 0, 0
    for i in range(1, len(L)) :
        if M[i-1] == 1 or M[i-1] == 0 :
            if M[i-1] == 1 :  L2  = []
            if len(L1) == 0  :
                L1.append(L[i-1])
            L1.append(L[i])
            # print(L1, sum(L1))
        if len(L1) > l1 :
            l1 = len(L1)
            indexi = i-len(L1)+1
            L11 = L1[:]

        if M[i-1] == -1 or M[i-1] == 0 :
            if M[i-1] == -1 : L1 =[]
            if len(L2) == 0:
                L2.append(L[i-1])
            L2.append(L[i])
            # print(L2, sum(L2))
        if len(L2) > l2 :
            l2 = len(L2)
            indexd = i-len(L2)+1
            L22 = L2[:]

    if l1 > l2 :
        return sum(L11)
    elif l1 < l2 :
        return sum(L22)

    if l1 == 0:
        return sum(L22)
    if l2 == 0:
        return sum(L11)

    elif l1 == l2 :
        if indexi < indexd :
            return sum(L11)
        else:
            return sum(L22)






print('---------------TEST CASES -------------------------')
# L = [10, 4, 3, 8, 3, 4, 5, 7, 7, 2]
# L = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# L = [3, 2, 1, 2, 3]
# L=1, 2, 1, 2, 1, 2, 1, 2, 1
# L = [1, 2, 3, 4, 5, 0, 10, 1, 2, 3, 4, 5]
L = [1, 2, 3, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# L = [3, 2, -1, 2, 7]
# L = [100, 200, 300, -100, -200, -1500, -5000]
# L = [1, 2, 3, 2, -1, -10]
# L = [3, 3, 3, 3, 3, 3, 3, -10, 1, 2, 3, 4]
# L = [3, 3, 3, 3, 3]
# L = [-3, -3, -3, -3, -3]
# L = [1, 2, 3, 2, 1, -10, -20, 3, 3, 3, 3, 3, 3, 3, 3, 3]
# L = [1, 2, 3, 2, 1, -10, -20, 3, 4, 5, 7, 7, 8, 9, 11, 11]
# L = [-10, -9, -8, -7, -6, -5, -3, -1, 1, 3, 5, 8, 10, 100, 1000, 10000]
print(L)

# def monotony(a, b):
#     if a <= b : return '1'
#     if a > b : return '0'

def monotony(a, b):
    if a < b : return '1'
    if a > b : return '-1'
    if a == b : return '0'

M=[]

for i in range(0 , len(L)-1) :
    if monotony(L[i],L[i+1]) == '1' :        M.append(1)
    elif monotony(L[i],L[i+1]) == '-1' :        M.append(-1)
    else:   M.append(0)
print(' ',M)
print('----------   Simple Tests   ---------')

L11, L22 = [], []
L1, L2 = [], []
indexi , indexd = 0, 0
l1, l2 = 0, 0
for i in range(1, len(L)) :
    if M[i-1] == 1 or M[i-1] == 0 :
        if M[i-1] == 1 :  L2  = []
        if len(L1) == 0  :
            L1.append(L[i-1])
        L1.append(L[i])
        print(L1, sum(L1))
    if len(L1) > l1 :
        l1 = len(L1)
        indexi = i-len(L1)+1
        L11 = L1[:]

    if M[i-1] == -1 or M[i-1] == 0 :
        if M[i-1] == -1 : L1 =[]
        if len(L2) == 0:
            L2.append(L[i-1])
        L2.append(L[i])
        print(L2, sum(L2))
    if len(L2) > l2 :
        l2 = len(L2)
        indexd = i-len(L2)+1
        L22 = L2[:]



print('------------------')
print(l1 , indexi , L11, '  Sum: ',sum(L11))
print(l2, indexd , L22, '  Sum: ', sum(L22))


print('\n------------Function Test -----------------')

print(longest_run(L))
# print(longest_run([1, 2, 3, 4, 5, 6, 7, 8, 9]))


def mCount(L):
    count=1

    maxCount=0
    for i in range(len(L)-1):
        if L[i+1] >= L[i]:
            count +=1
        else:

            count =1
        if maxCount<count:
            maxCount=count
    return maxCount

print(mCount(L))