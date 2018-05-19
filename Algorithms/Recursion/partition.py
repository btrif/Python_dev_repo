#  Created by Bogdan Trif on 09-09-2017 , 9:34 PM.


def partition(number):
    answer = set()
    answer.add((number, ))
    for x in range(1, number):
        for y in partition(number - x):
            answer.add(tuple(sorted((x, ) + y)))
            #print(answer)
    return answer

print(partition(4))


S = [1, 4, 9, 16, 25, 36, 49]

def partition_nr_into_given_set_of_nrs(nr, S,  lim=10 ):
    ''' :Description: partition a number into a custom set of integers with a limit maximum number of terms
    :param n: number to partition
    :param S: integer set
    :return: list of partitions             '''
    nrs = sorted(S, reverse=True)
    def inner(n, i, lim ):
        if lim >= 0 :
            if n == 0:
                yield []
            for k in range(i, len(nrs)):
                if nrs[k] <= n:
                    for rest in inner(n - nrs[k], k , lim-1 ):

                        yield [nrs[k]] + rest
    return list(inner(nr, 0, lim))


print(partition_nr_into_given_set_of_nrs( 45, S ))