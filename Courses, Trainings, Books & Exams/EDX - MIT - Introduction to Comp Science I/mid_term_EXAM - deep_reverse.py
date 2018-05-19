'''
Problem 6
Implement a function that meets the specifications below.
def deep_reverse(L):
    """ assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also
    reverses the order of the int elements in every element of L.
    It does not return anything.
    """
    # Your code here
For example, if L = [[1, 2], [3, 4], [5, 6, 7]] then deep_reverse(L) mutates L to be [[7, 6, 5], [4, 3], [2, 1]]
Paste your entire function, including the definition, in the box below. Do not leave any debugging print statements.
'''


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

deep_reverse(L)
print(L,'\n')

'''
if any(isinstance(i, list) for i in L) == True:
    for A in range(len(L)):
        L[A].reverse()
    L.reverse()
    print(L)
'''