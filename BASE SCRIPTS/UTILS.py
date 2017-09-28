print('\n---------------------- Counter Generator List   -----------------')

def counter_generator( up_nr, elem_nr ):    # o(^_^)o   ©Bogdan Trif @ 2017 -02-19, 14:00   ( ͡° ͜ʖ ͡°)
    ''':Generates a counter of a given elem_nr up to the up_nr
        Useful in finding common multiples of a list of primes numbers
    :param up_nr: int, up_power of the list
    :param elem_nr: int, nr of elements in the list
    :return: tuples, representing the   possible combinations                                             '''
    import itertools
    # G=[]
    for k in itertools.product(*[range(1, up_nr+1)]*elem_nr):
        # print( k )
        # G.append(k)
        yield k

print( list(counter_generator( 7 , 2 )) )
print( list(counter_generator( 2 , 4 )) )

print('\n-------------- Non Increasing counter ---------------------')
# Note : the sequences generated are in decreasing order !

def non_increasing_counter(values, length):
    ''':Description: generates from a list of values all the combinations up to to the maximum value
        in the values list. length is the length of the sequences generated
        https://www.reddit.com/r/learnpython/comments/3dnzap/need_to_generate_all_possible_permutations/
    :param values:   list
    :param length: the length of list
    :return:
    '''
    if length == 1:
        for value in values:
            yield value,
    else:
        for index, value in enumerate(values, 1):
            for rest in non_increasing_counter(values[:index], length - 1):
                yield (value,) + rest

print( list(non_increasing_counter([1,2, 3],4)) )