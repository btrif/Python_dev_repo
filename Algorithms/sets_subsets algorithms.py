
# What is the recursive solution for finding all subsets of a given array?
def subsets( nums ):      # Returns all the subsets of the main set
    if nums is None: return None
    subsets_ = [[]]
    next = []
    for n in nums:
        for s in subsets_ :
            next.append(s + [n])
        subsets_ += next
        next = []
    return subsets_

print(subsets( [ 2, 3, 5, 7, 11, 13 ] ) )


###########################

print('\nAlgorithm to find which number in a list sum up to a certain number')

'''
http://stackoverflow.com/questions/3420937/algorithm-to-find-which-number-in-a-list-sum-up-to-a-certain-number
'''

def stackoverflow(x_list, target):
    memo = dict()
    result, _ = g(x_list, x_list, target, memo)
    return (sum(result), result)


def g(v, w, S, memo):
    subset = []
    id_subset = []
    for i, (x, y) in enumerate(zip(v, w)):
        # Check if there is still a solution if we include v[i]
        if f(v, i + 1, S - x, memo) > 0:
            subset.append(x)
            id_subset.append(y)
            S -= x
    return subset, id_subset


def f(v, i, S, memo):
    if i >= len(v):
        return 1 if S == 0 else 0
    if (i, S) not in memo:    # <-- Check if value has not been calculated.
        count = f(v, i + 1, S, memo)
        count += f(v, i + 1, S - v[i], memo)
        memo[(i, S)] = count  # <-- Memoize calculated result.
    return memo[(i, S)]       # <-- Return memoized value.


def main():
    # x_list = [100, 75, 15, 495, 995, 995, 995, 995, 510, 110]
    # target = 635
    x_list = [1150, 495, 995, 995, 995, 995, 100, 750, 3305, 75, 510, 3265, 2145, 1935, 140, 140, 15, 1330, 2800, 1250, 350, 850, 110]
    target = 8270
    P = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181]

    target = sum(P)//3
    so = stackoverflow(P, target)
    print(so)


main()