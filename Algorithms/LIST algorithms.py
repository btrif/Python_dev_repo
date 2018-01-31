print('\n-----------   Pattern repetition in a list --------------------')

def guess_seq_len_orig(seq):
    ''' :SCOPE: Search for a pattern repetition in a list
        '''
    guess = 1
    max_len = len(seq) // 2
    for x in range(2, max_len):
        if seq[0:x] == seq[x:2*x] :
#             if seq[0:x][0] == seq[0:x][-1] :
#                 return seq[0:x][0]
#             else : return seq[x:2*x]
            return seq[x:2*x]
    return seq[0]


print('---------TEST CASES ------------')

list_a = [111, 0, 3, 1, 111, 0, 3, 1, 111, 0, 3, 1 ]
list_b = [7, 14, 7, 14, 7, 14, 7, 14, 7, 14, 7, 14, 7, 11, 4, 2, 1, 6, 4, 1, 3, 4, 7, 1, 1, 5, 1, 1, 1, 1, 21, 62, 2, 1, 2, 1, 1, 1, 8] # 51
list_c = [1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,23,18,10]
list_d = [18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 17, 1, 24, 1, 7, 7, 1, 1, 4, 3, 1, 1, 1, 1, 2, 15, 2, 5, 1]
list_e = [1, 7, 1, 16, 1, 7, 1, 16, 1, 7, 1, 16, 1, 7, 1, 16, 1, 7, 1, 16, 1, 7, 1, 16, 1, 2, 1, 22, 28]
list_f =[1, 2, 3, 1, 1, 5, 1, 8, 1, 5, 1, 1, 3, 2, 1, 18, 1, 2, 3, 1, 1, 5, 1, 8, 1, 5, 1,1, 3, 2, 1, 18, 1, 2, 2, 5, 2, 9, 2] # 94
list_g=[1, 1, 1, 4, 6, 4, 1, 1, 1, 18, 1, 1, 1, 4, 6, 4, 1, 1, 1, 18, 1, 1, 1, 4, 6, 4, 1, 1, 1] # 93
list_h = [2, 2, 2, 14, 2, 2, 2, 14, 2, 2, 2, 14, 2, 2, 2, 14, 2, 2, 2, 14, 2, 2, 2, 14, 1, 1, 1, 1, 3, 2, 4, 1, 6, 1, 1, 16, 3, 1, 8]
list_i= [3, 1, 1, 3, 14, 3, 1, 1, 3, 14, 3, 1, 1, 3, 14, 3, 1, 1, 3, 14, 3, 1, 1, 3, 14, 3, 1, 4, 1, 1, 1, 4, 2, 2, 16, 2, 1, 1, 1]  # 53
list_j = [1, 1, 1, 1, 6, 1, 1, 1, 1, 6, 1, 1, 1, 1, 6, 1, 1, 1, 1, 6, 1, 1, 1, 1, 6, 1, 1, 1, 1, 6, 1, 1]  #13
list_k = [1, 1, 1, 1, 1, 1, 14, 1, 1, 1, 1, 1, 1, 14, 1, 1, 1, 1, 1, 1, 14, 1, 1, 1, 1, 1, 1, 14, 1, 1, 1, 1]
list_l=[1, 4, 3, 1, 2, 2, 1, 3, 4, 1, 14, 1, 4, 3, 1, 2, 2, 1, 3, 4, 1, 14, 1, 4, 3, 1, 2, 2, 1, 3, 4, 1, 15, 5, 2, 1, 2, 6, 3]
list_m=[2, 3, 3, 2, 18, 2, 3, 3, 2, 18, 2, 3, 3, 2, 18, 2, 3, 3, 2, 18, 2, 3, 3, 4, 1, 1, 13, 1, 25, 3, 8, 6, 1, 11, 1, 1, 1, 14, 2]
list_n = [2, 3, 1, 2, 4, 1, 6, 6, 1, 4, 2, 1, 3, 2, 20, 2, 3, 1, 2, 4, 1, 6, 6, 1, 4, 2, 1, 3, 2, 1, 5, 1, 6, 1, 2, 1, 2, 1, 4] # 109
list_o = [9, 2, 1, 2, 2, 5, 4, 1, 1, 13, 1, 1, 4, 5, 2, 2, 1, 2, 9, 28, 9, 2, 1, 2, 2, 4, 2, 2, 1, 1, 8, 1364, 1, 2, 1, 1, 1, 3, 3] # 199
list_p = [1, 4, 1, 1, 3, 2, 2, 13, 2, 2, 3, 1, 1, 4, 1, 26, 1, 4, 1, 1, 3, 2, 2, 13, 2, 2, 3, 1, 1, 5, 2, 1, 339, 1, 1, 1, 4, 1, 8] # 191
list_q = [2, 4, 1, 8, 6, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 6, 8, 1, 4, 2, 26, 2, 4, 1, 8, 6, 1, 1, 1, 1, 3, 1, 51, 1, 7, 1, 1, 1, 42] #181


L = [ list_a, list_b, list_c, list_d, list_e, list_f, list_g, list_h, list_i, list_j, list_k, list_l, list_m, list_n , list_o, list_p, list_q ]

def inside_loop(seq):
    guess = len(seq)//2
    for guess in range(guess, 1, -1 ):
        guess-=1
        s1, s2 = seq[0:guess], seq[guess: 2*guess ]
        # print(s1)
        # print(s2)
        if s1 == s2 : break
    return s1

print('\n---------------Function to search for a specific sequence in a list ------------------  ')

def seq_from_list_in_another(L1, L2) :
    ''':Scope: Function which search for a specific sequence in a list
    :param L1: sequence to search from
    :param L2: the object of search
    :return: list, sequence    '''
    s1 = ''.join( str(i) for i in  L1 )
    s2 = ''.join( str(i) for i in  L2 )
    if s1 in s2 :
        return L1

print('seq_from_list_in_another  :\t',seq_from_list_in_another( [111, 0, 3, 1] , list_a ))

###################
print('\n------------Function to return a repeating sequence within a list of integers -------------')

def guess_seq_len(seq):         # MY FUNCTION
    '''    :SCOPE: Functions which returns a repeating sequence within a list of integers.
        If  it not finds a sequence it will return just the first element of the sequence
        Observation : It may not work properly if the sub sequence ends with double, triple ... of the same digit.
        In this case it needs adjustments. However, in the case of lists of partial fractions where the function was used,
        this never happens.
        :param:
        :seq:     List of integers
        :return:     The unique  sequence of numbers from the list        '''
    def inside_loop(seq):
        guess = len(seq)//2
        for guess in range(guess, 1, -1 ):
            guess-=1
            s1, s2 = seq[0:guess], seq[guess: 2*guess ]
            # print(len(s1), s1, end='     ')
            # print(len(s2) , s2)
            if s1 == s2 : break
        if s1 != s2 :  return seq
        else: return s1

    s = inside_loop(seq)
    if len(list(set(s))) == 1 :
        return [s[0]]
    else:                   #return  s
        l1 = len (list(set(s)))
        lst=[]
        for i in range(len(s)):
            lst.append(s[i])
            if l1 == len(list(set(lst))) :
                break
        return lst

# Main Test Case
for i in L :
    print( len(guess_seq_len(i)) ,guess_seq_len(i) ,'                        ',i)


#######################  MONOTONY  ##################
print('\n-----------monotonically increasing or monotonically decreasing sequence in a list ---------------- ')

def strictly_increasing(L):
    return all(x<y for x, y in zip(L, L[1:]))

def strictly_decreasing(L):
    return all(x>y for x, y in zip(L, L[1:]))

def non_increasing(L):
    return all(x>=y for x, y in zip(L, L[1:]))

def non_decreasing(L):
    return all(x<=y for x, y in zip(L, L[1:]))



is_increasing = lambda L: operator.reduce(lambda a,b: b if a < b else 9999 , L)!=9999

is_decreasing = lambda L: operator.reduce(lambda a,b: b if a > b else -9999 , L)!=-9999



import itertools
import operator

def monotone_increasing(lst):
    pairs = zip(lst, lst[1:])
    return all(itertools.starmap(operator.le, pairs))

def monotone_decreasing(lst):
    pairs = zip(lst, lst[1:])
    return all(itertools.starmap(operator.ge, pairs))

def monotone(lst):
    return monotone_increasing(lst) or monotone_decreasing(lst)


import numpy as np

def monotonic(x):
    dx = np.diff(x)
    return np.all(dx <= 0) or np.all(dx >= 0)


def monotonic_increase(L) : # Very simple function which must work in many programming languages,  O(n)
    for i in range(len(L)-1) :
        if L[i] > L[i+1] :
            return False
    return True

#########################################

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

print('longest_run : \t', longest_run(L) )

#################### Monotony of the last two pairs in a list ############
print('\n------- Function to compare ONLY the  last three numbers in a list to detect monotony ----------')

lst1 = [3, 5, 7, 9 ,8 ,7, 3,6]
lst2 = [3, 5, 7, 9 ,8 ,7, 8, 10]
def non_monotonic(L) :
    ''':Scope:   Function which checks the last three elements in a list for monotony.
    If the elements are monotonic return False,
    If the elements are NON-monotonic return True'''
    a, b, c = L[-3::]
    if a<=b <=c or a>=b >=c : return False
    return True


print('non_monotonic : \t', non_monotonic(lst1)  )
print('non_monotonic : \t', non_monotonic(lst2)  )