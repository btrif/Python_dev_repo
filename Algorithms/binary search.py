def binary_search(n, List):        # VERY FAST ALGORITHM
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


def binary_search(value, last, start, end):
    global rad_list
    cur_index = (start+end)/2
    if value == rad_list[cur_index][0] or (start,end) == last:
        return cur_index
    elif rad_list[cur_index][0] < value:
        return binary_search(value, (start,end), cur_index, end)
    return binary_search(value, (start,end), 0, cur_index)


