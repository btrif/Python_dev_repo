
print('--------------the SIMPLEST POSSIBLE GENERATOR ------------------------')

s = 'abc'
IT = s.__iter__()       # or   IT = iter(s)
 #   function returns an iterator object that defines the method __next__()
print('IT, function returns an iterator object that defines the method __next__() :\t\t ', IT )
print('next item : ',  IT.__next__() )          #   which accesses elements in the container one at a time.
print('next item : ',  next(IT) )           #  IT.__next__() and next(IT) are equivalent




print('\n--------------------------------------')


def Blum_Blum_Shub_gen():           # EFFICIENT GENERATOR
    '''     s_0 = 290797
            s_(n+1) = s_n×s_n (modulo 50515093)
            t_n = s_n (modulo 500)                  '''
    s = 290797
    while True :
        s = pow(s, 2 , 50515093 )
        t = s % 500
        yield t

B = Blum_Blum_Shub_gen()
for i in range(12):    print( next(B),end=' ;  ')
print(next(B), next(B), next(B), next(B) )


print('\n---------------- Same Generator in a simpler way ---------------------')

SMOD = 50515093
TMOD = 500
def blum(pmod=TMOD):
    s = 290797
    while True:
        s = pow(s, 2, SMOD)
        yield s % pmod
B2 = blum()

for i in range(16) : print(next(B2), end=' ;  ')


def bbs_prng(s=290797, m_s=50515093, m_t=500):
    while 1:
        s = (s * s) % m_s
        yield s % m_t


print('\n\n------------------ RECURSIVE GENERATOR ------------------')

# RECURSIVE GENERATOR

def orduples(size, start, stop, step=1):
    if size == 0:
        yield ()
    elif size == 1:
        for x in range(start, stop, step):
            yield (x,)
    else:
        for u in orduples(size - 1, start, stop, step):
            for x in range(u[-1], stop, step):
                yield u + (x,)

if __name__ == "__main__":
    print(list(orduples(3, 0, 5)))


print('\n\n------------------    RECURSIVE GENERATOR  - MULTIRANGE    ------------------')











print('\n\n------------------    RECURSIVE GENERATOR  - Number Partition    ------------------')


def partition_nr_into_given_set_of_nrs_limit(nr, S, m=10):
    '''Recursive function to partition a number into a given set of numbers
    and also having an upper limit lim of the  partition length.
    :param nr: int, nr to partition, example : 109
    :param S: set of numbers used for partitioning
    :param m: int, limit, example m=10 represents the maximum partition length
    :return: list of partitions , list of lists
    '''
    nrs = sorted(S, reverse=True)
    def inner(n, i, m):
        if m >= 0:
            if n == 0:
                yield []
            for k in range(i, len(nrs)):
                if nrs[k] <= n:
                    for rest in inner(n - nrs[k], k, m - 1):
                        yield [nrs[k]] + rest
    return list(inner(nr, 0, m))


P = partition_nr_into_given_set_of_nrs_limit( 810, [ 1, 4, 9, 16, 25, 36 ,49, 64, 81 ], 11 )
print(P)



print('\n--------------------------- Unique Permutations ------------------------ ')

X = [49, 36, 25, 16, 4, 4, 4, 4, 4, 4, 4, 4, 4, 1, 1, 1, 1, 1, 1, 1]

def unique_permutations(lst):       # VERY EFFECTIVE
    ''':Description: Takes a list and makes ONLY Unique Permutations of a list with repeated elements.
        If one tries itertools.permutations on a list with 14 elements ==> BANG, computer freezes
    :param lst: type list
    :return:    a list of lists containing all the permutations
    '''
    if len(lst) == 1:
        yield (lst[0],)
    else:
        unique_lst = set(lst)
        for first_element in unique_lst:
            remaining_lst = list(lst)
            remaining_lst.remove(first_element)
            for sub_permutation in unique_permutations(remaining_lst):
                yield (first_element,) + sub_permutation

K = unique_permutations(X)
print(K)
# for  cnt, i in enumerate(K):     print(str(cnt) +'.    ',  next(K)  )