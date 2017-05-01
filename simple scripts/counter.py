# Binary counter
for x in range(16):
    print (bin(x)[2:].zfill(4), end='  ')
print()

print('\n------------------- Binary counter Generator --------------------\n')

def binary_counter( digits):
    ''' Binary counter

    :param: digits: int, represents the padding, digits = 4 gives 0001
    :return: a binary number
    :Usage:     B = binary_counter(3), print(next(B)
    '''
    x=0
    while True :
        yield (bin(x)[2:].zfill(digits))
        x+=1

B = binary_counter(3)

for i in range(20):
    print(str(i)+'.', next(B), end='   ')


##################    ITERATORS   ##########################
print('\n\n----------- A nice constructed Counter and a way to avoid stop Generator Error ---------')
# Iterators
# Python iterator objects are required to support two methods while following the iterator protocol.
#
# __iter__ returns the iterator object itself. This is used in for and in statements.
#
# __next__ method returns the next value from the iterator.
# If there is no more items to return then it should raise StopIteration exception.

class Counter(object):
    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self):
        'Returns itself as an iterator object'
        return self

    def __next__(self):
        'Returns the next value till current is lower than high'
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1



c = Counter(5,10)
for i in c: print(i, end=' ')
print()
# Remember that an iterator object can be used only once.
# It means after it raises StopIteration once, it will keep raising the same exception.

# Using the iterator in for loop example we saw, the following example tries to show the code behind the scenes.
c = Counter(5,10)
iterator = iter(c)
while True:
    try:
        x = iterator.__next__()
        print(x, end=' ')
    except StopIteration as e:
        break



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