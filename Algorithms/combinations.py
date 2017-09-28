def combinations_by_subset(seq, r):         # GENERATOR
    # https://codereview.stackexchange.com/questions/1419/python-generator-function-that-yields-combinations-of-elements-in-a-sequence-sor

    if r:
        for i in range(r - 1, len(seq)):
            for cl in combinations_by_subset(seq[:i], r - 1):
                yield cl + (seq[i],)
    else:
        yield tuple()

print(list(combinations_by_subset([1,2,3,4,5], 3)   ))


print('\n-----------'*10)

def combinations(n, list, combos=[]):           # ITERATOR
    # initialize combos during the first pass through
    if combos is None:
        combos = []

    if len(list) == n:
        # when list has been dwindeled down to size n
        # check to see if the combo has already been found
        # if not, add it to our list
        if combos.count(list) == 0:
            combos.append(list)
            combos.sort()
        return combos
    else:
        # for each item in our list, make a recursive
        # call to find all possible combos of it and
        # the remaining items
        for i in range(len(list)):
            refined_list = list[:i] + list[i+1:]
            combos = combinations(n, refined_list, combos)
        return combos

C= combinations(3, [1,2,3,4,5], [])
print(C)