import heapq

print(help(heapq))
print('-----------------------------------')

print(dir(heapq))

#########################

print('\n-------------- Maximum Heapq -----------------')
# Here we maintain a heapq list ( binary list) with MAXIMUM elements :
# Note the elements are put such that   elem 2*i+1 is always BIGGER than 2*i, odd > even
listForTree = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
heapq.heapify(listForTree)             # for a min heap
heapq._heapify_max(listForTree)        # for a maxheap!!
print('MAximum element is always first :\t',listForTree)
print('Here we get the 6-th element : \t', heapq.nlargest(6, listForTree) )
print('Here we pop the maximum element : \t', listForTree)

print('\n-------------- Minimum Heapq -----------------')
# Here we maintain a heapq list ( binary list) with MINIMUM elements :
# Note the elements are put such that   elem 2*i+1 is always SMALLER than 2*i, odd < even
listForTree = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
heapq.heapify(listForTree)             # for a min heap

print('Minimum element is always first :\t',listForTree)
heapq.heappop(listForTree)
print('Here we pop the minimum element : \t', listForTree)  # Observe that the list is re-ordered

print('Here we get the 6-th element : \t', heapq.nlargest(6, listForTree)[-1] )

