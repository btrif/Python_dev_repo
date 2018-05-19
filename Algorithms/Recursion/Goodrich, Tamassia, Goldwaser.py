#  Created by Bogdan Trif on 19-04-2018 , 5:15 PM.


print('----------------- Recursion sum of a list ------------')
### Recursion Sum of a list

L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def list_sum_rec(S, n):
    if n ==0 :
        return 0
    else :
        return list_sum_rec(S, n-1) + S[n-1]

list_sum_rec(L, len(L))
print(L, '         ',list_sum_rec(L, len(L) ) , '         ' )

print('\n----------------- Reversion sum of a list ------------')

def reverse_list(S, start, stop) :
    if start < stop-1 :
        S[start], S[stop-1] = S[stop-1], S[start]
        reverse_list(S, start+1, stop -1)

reverse_list(L, 0, 10)
print(L)

print('\n---------------------   Raise to power   ----------------------  ')

### Compute the value x n for integer n.

def power(x, n):

    if n == 0:         return 1

    else:
        partial = power(x, n // 2)     # rely on truncated division
        result = partial * partial

        if n % 2 == 1:         # if n odd, include extra factor of x
            result *= x

        return result

print(' power =      ', power(3,5))

print('\n---------------------   Binary Recusion   ----------------------  ')


'''     When a function makes two recursive calls, we say that it uses binary recursion.
We have already seen several examples of binary recursion, most notably when
drawing the English ruler (Section 4.1.2), or in the bad fibonacci function of Section
4.3. As another application of binary recursion, let us revisit the problem of
summing the n elements of a sequence, S, of numbers. Computing the sum of one
or zero elements is trivial. With two or more elements, we can recursively compute
the sum of the first half, and the sum of the second half, and add these sums
together. Our implementation of such an algorithm, in Code Fragment 4.13, is
initially invoked as binary sum(A, 0, len(A)).          '''


### Binary Recursion

def binary_sum(S, start, stop):
    '''Return the sum of the numbers in implicit slice S[start:stop].”””'''
    if start >= stop:      # zero elements in slice
        return 0
    elif start == stop-1:   # one element in slice
        return S[start]
    else: # two or more elements in slice
        mid = (start + stop) // 2
        return binary_sum(S, start, mid) + binary_sum(S, mid, stop)

print(' Binary Recurion : ', binary_sum(L, 0, 10))