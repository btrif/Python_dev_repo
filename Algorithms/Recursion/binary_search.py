#  Created by Bogdan Trif on 12-04-2018 , 1:11 PM.

L = [ 2, 4, 5, 7, 9, 11, 14, 16, 17, 19, 22, 25, 29, 34, 36, 38 ]


def binary_search_rec( lst, n, low, high) :     ### by Bogdan Trif, My implementation @  12-04-2018 , 1:11 PM.
    mid_point = ( low + high) // 2

    if  n == lst[mid_point] : return mid_point
    if mid_point == low or mid_point == high  : return False

    else :
        if  n <= lst[mid_point] :
            return binary_search_rec(lst, n, low, mid_point)
        if  n > lst[mid_point] :
            return binary_search_rec(lst, n, mid_point, high)

print( binary_search_rec(L, 10, 0, len(L)-1 ) )



def binary_search_rec2(data, target, low, high) :
    '''Return True if target is found in indicated portion of a Python list.

    The search only considers the portion from data[low] to data[high] inclusive.

        '''
    if low > high:
        return False # interval is empty; no match
    else:
        mid = (low + high) // 2
        if target == data[mid]: # found a match
            return True
        elif target < data[mid]:
            # recur on the portion left of the middle
            return binary_search_rec2(data, target, low, mid - 1)
        else:
            # recur on the portion right of the middle
            return binary_search_rec2(data, target, mid + 1, high)


print(binary_search_rec2(L, 10, 0, len(L)-1  )  )