#  Created by Bogdan Trif on 06-06-2018 , 2:29 PM.

# http://www.inference.org.uk/mackay/python/examples/decompose.shtml

def decompose( n , candidatelist , answerSoFar=[] ):
    """ Decomposes an integer n in as many ways as possible
    using the offered list of candidates,
    each of which may be used many times.
    It's recommended that the candidatelist be
    ordered from big to small. WARNING - if the list does
    not include '1' at the end, bad things could happen!

    >>> decompose(3, [9,4,1] )
    [1, 1, 1]
    >>> decompose( 5, [4,1] )
    [4, 1]
    [1, 1, 1, 1, 1]

    For the output from decompose(13, [9,4,1] ), see
    decomposeSquares(13) below.
    """
    assert(n>=0)
    if (n==0):
        # recursion has finished, print the list
        print(answerSoFar)
        return
    offset = 0
    for a in candidatelist:
        if ( a <= n):
            answerSoFar.append(a)
            decompose( n-a , candidatelist[offset:] , answerSoFar )
            answerSoFar.pop() # remove a from the list, so we can try replacing by later items too.
            pass
        pass
        offset += 1
    pass


def decomposeSquares(n):
    """
    Decomposes an integer n into sum of squares in as many ways as possible.

    >>> decomposeSquares(13)
    [9, 4]
    [9, 1, 1, 1, 1]
    [4, 4, 4, 1]
    [4, 4, 1, 1, 1, 1, 1]
    [4, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    """
    assert(n>=1)
    a=[]; i=1;
    # create the list of squares up to n
    while ( i*i <= n ):
        a.append(i*i)
        i += 1
        pass
    a.reverse()
    decompose(n,a)
    pass

def decomposeFibo(n):
    """
    Decomposes an integer n into sum of fibonacci numbers in as
    many ways as possible.
    >>> decomposeFibo(13) # doctest: +NORMALIZE_WHITESPACE, +ELLIPSIS
    [13]
    [8, 5]
    [8, 3, 2]
    [8, 3, 1, 1]
    [8, 2, 2, 1]
    ...
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    """
    a=[1]; previous=1
    next = a[-1]+previous
    while( n >= next ):
        previous=a[-1]
        a.append(next)
        next = a[-1]+previous
    a.reverse()
    decompose(n, a)


def test():
    import doctest
    verbose=1
    if(verbose):
        doctest.testmod(None,None,None,True)
    else:
        doctest.testmod()
    pass
    print("Running some examples...")
    decomposeSquares(13)

import sys
if __name__ == '__main__':
    test()
    pass

