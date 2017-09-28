# list-version                   #  # generator-version
def makeRange_list(n):                #  def makeRange(n):
    """return [0,1,2,...,n-1]""" #~     """return 0,1,2,...,n-1"""
    TO_RETURN = []               #>
    i = 0                        #      i = 0
    while i < n:                 #      while i < n:
        TO_RETURN += [i]         #~         yield i
        i += 1                   #      i += 1
    return TO_RETURN             #>

makeRange_list(5)

print(makeRange_list(16))

  # generator-version
def makeRange_generator(n):           #return 0,1,2,...,n-1
    a = 0
    while a < n:
        yield a
        print(a)
        a += 1

makeRange_generator(10)
print(makeRange_generator(10))

print('\n-----------A very Basic GENERATOR, Works similarly to Range----------')
def small_gen(i):
    ''' :Usage:
        *   sg=small_gen(100)             followed by
        *   small_gen().__next__()             can be called as many times, giving each next iteration '
    Examples:
        Examples should be written in doctest format, and should illustrate how
        to use the function.

        #>>> sg=small_gen(1979)
        #>>>sg.__next__()
        1980     '''

    while True:
        next = i+1
        yield next
        i+=1

print('\n------------------ MORE GENERATORS ----------------------')

def countdown(num):
    ''' Countdown Generator'''
    print('Starting')
    while num > 0:
        yield num
        num -= 1
val = countdown(5)
print(next(val))
print(next(val))

print('-----------------Generator Expressions--------------------')
# Just like list comprehensions, generators can also be written in the same manner except they return a generator object rather than a list:
my_list = ['a', 'b', 'c', 'd']
gen_obj = (x for x in my_list)
for val in gen_obj:     print(val, end='  ')
print('\n------------------------')
# Take note of the parens on either side of the second line denoting a generator expression, which,
# for the most part, does the same thing that a list comprehension does, but does it lazily:
import sys
g = (i * 2 for i in range(10000) if i % 3 == 0 or i % 5 == 0)
print('Memory usage of the generator : ',sys.getsizeof(g) )
#72
l = [i * 2 for i in range(10000) if i % 3 == 0 or i % 5 == 0]
print('Memory usage of the list : ', sys.getsizeof(l), '    ;     Length: ',len(l))



