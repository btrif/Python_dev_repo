#  Created by Bogdan Trif on 02-08-2018 , 6:13 PM.
# http://interactivepython.org/runestone/static/pythonds/SortSearch/TheSequentialSearch.html

'''
                                        ===     5.3. The Sequential Search      ===

When data items are stored in a collection such as a list, we say that they have a linear or sequential relationship.
Each data item is stored in a position relative to the others.
In Python lists, these relative positions are the index values of the individual items.
Since these index values are ordered, it is possible for us to visit them in sequence.
This process gives rise to our first searching technique, the sequential search.

Figure 1 shows how this search works.
Starting at the first item in the list, we simply move from item to item,
following the underlying sequential ordering until we either find what we are looking for or run out of items.
If we run out of items, we have discovered that the item we were searching for was not present.
'''

def sequentialSearch(alist, item):
    pos = 0
    found = False

    while pos < len(alist) and not found:
            if alist[pos] == item:
                found = True
            else:
                pos = pos+1

    return found

testlist = [1, 2, 32, 8, 17, 19, 42, 13, 0]
print(sequentialSearch(testlist, 3))
print(sequentialSearch(testlist, 13))


'''
                                    ===     5.3.1. Analysis of Sequential Search    ===

To analyze searching algorithms, we need to decide on a basic unit of computation. 
Recall that this is typically the common step that must be repeated in order to solve the problem. 
For searching, it makes sense to count the number of comparisons performed. 
Each comparison may or may not discover the item we are looking for. 
In addition, we make another assumption here. 
The list of items is not ordered in any way. 
The items have been placed randomly into the list. In other words, 
the probability that the item we are looking for is in any particular position is exactly the same for each position of the list.

If the item is not in the list, the only way to know it is to compare it against every item present. 
If there are n items, then the sequential search requires n comparisons to discover that the item is not there. 
In the case where the item is in the list, the analysis is not so straightforward. 
There are actually three different scenarios that can occur. 
In the best case we will find the item in the first place we look, at the beginning of the list. 
We will need only one comparison. In the worst case, we will not discover the item until the very last comparison, the nth comparison.

What about the average case? 
On average, we will find the item about halfway into the list; that is, we will compare against n2 items. 
Recall, however, that as n gets large, the coefficients, no matter what they are, 
become insignificant in our approximation, so the complexity of the sequential search, is O(n). 
Table 1 summarizes these results.
    
'''
print('---------------------------------------------------------------')


def orderedSequentialSearch(alist, item):
    pos = 0
    found = False
    stop = False
    while pos < len(alist) and not found and not stop:
        if alist[pos] == item:
            found = True
        else:
            if alist[pos] > item:
                stop = True
            else:
                pos = pos+1

    return found

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(orderedSequentialSearch(testlist, 3))
print(orderedSequentialSearch(testlist, 13))