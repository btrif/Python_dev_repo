def test_func(x):
    """This function will try to calculate:

    .. math::
        \sum_{i=1}^{\\infty} x_{i}

    good luck!
    """
    pass



def check_doubles(M):
    ''':Description:    check if there are values 2 times or more at a position. Checks if
        there are >1 numbers on a row, a column or a 3x3 subMatrix. If there are duplicate
        numbers return True, returns False if all the numbers are Unique.
    :param M:   the matrix to test
    :return:    boolean:    True if there are duplicates, False if all are unique

        .. math::
                    n_{\mathrm{offset}} = \sum_{k=0}^{N‐1} s_k n_k
    '''
    for x in range(1,10):
        for i in range(1,10):
            row = M[i-1]
            col = transpose(M)[i-1].tolist()
            if row.count(x) > 1 == True or col.count(x) >1 == True :
                res1 = True
            else: return False
            # print(row.count(x) > 1 ,row.count(x) , type(row),x,i )
            # print( col.count(x) >1 , col.count(x) ,type(col),x,i )
        for i in range(2,10,3):
            for j in range(2,10,3):
                submatrix = [val for sublist in SubMatrix_3x3(i,j,M) for val in sublist]
                # print(submatrix, x,  i, j)
                if submatrix.count(x) > 1 == True  :
                    # print('True', x,i,j)
                    res2 = True
                else: return False
        if res1 == True and res2 == True:
            return True