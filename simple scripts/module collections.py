import collections

# Counter
# A Counter is a container that keeps track of how many times equivalent values are added.
# It can be used to implement the same algorithms for which bag or multiset data structures
# are commonly used in other languages.

print('\n------------------ Initializing ---------------------')

# Counter supports three forms of initialization.
# Its constructor can be called with a sequence of items, a dictionary containing keys and counts,
# or using keyword arguments mapping string names to counts.

print (collections.Counter(['a', 'b', 'c', 'a', 'b', 'b']))
print (collections.Counter({'a':2, 'b':3, 'c':1}))
print (collections.Counter(a=2, b=3, c=1))

# The results of all three forms of initialization are the same.
print()
# An empty Counter can be constructed with no arguments and populated via the update() method.
c = collections.Counter()
print ('Initial :', c)

c.update('abcdaab')
print ('Sequence:', c)

c.update({'a':1, 'd':5})
print ('Dict    :', c)
# The count values are increased based on the new data, rather than replaced.
# In this example, the count for a goes from 3 to 4.

print('\n-------------------   Accessing Counts ---------------------------')
# Once a Counter is populated, its values can be retrieved using the dictionary API.

c = collections.Counter('abcdaab')

for letter in 'abcde':
    print ('%s : %d' % (letter, c[letter]), end='   ')
print()
# Counter does not raise KeyError for unknown items.
# If a value has not been seen in the input (as with e in this example), its count is 0.

# The elements() method returns an iterator that produces all of the items known to the Counter.

c = collections.Counter('extremely')
c['z'] = 0
print ('\n',c)
print ('Elements : \t',list(c.elements()))

# The order of elements is not guaranteed, and items with counts less than zero are not included.

# Use most_common() to produce a sequence of the n most frequently encountered input values and their respective counts.
c = collections.Counter()
with open('test.file', 'rt') as f:
    for line in f:
        c.update(line.rstrip().lower())

print ('Most common:')
for letter, count in c.most_common(3):
    print ('%s: %7d' % (letter, count))

# This example counts the letters appearing in all of the words in the system dictionary to produce
# a frequency distribution, then prints the three most common letters.
# Leaving out the argument to most_common() produces a list of all the items, in order of frequency.

print('\n------------------ Arithmetic -----------------------------')
# Counter instances support arithmetic and set operations for aggregating results.

import collections

c1 = collections.Counter(['a', 'b', 'c', 'a', 'b', 'b'])
c2 = collections.Counter('alphabet')

print( 'C1:', c1)
print ('C2:', c2)

print ('\nCombined counts:')
print (c1 + c2)

print ('\nSubtraction:')
print (c1 - c2)

print ('\nIntersection (taking positive minimums):')
print (c1 & c2)

print ('\nUnion (taking maximums):')
print (c1 | c2)

# Each time a new Counter is produced through an operation, any items with zero or negative counts are discarded.
# The count for a is the same in c1 and c2, so subtraction leaves it at zero.


print('\n ===========   defaultdict ================= ')
# The standard dictionary includes the method setdefault() for retrieving a value and establishing
# a default if the value does not exist.
# By contrast, defaultdict lets the caller specify the default up front when the container is initialized.

def default_factory():
    return 'default value'

d = collections.defaultdict(default_factory, foo='bar')
print ('d:', d)
print ('foo =>', d['foo'])
print ('bar =>', d['bar'])

# his works well as long as it is appropriate for all keys to have the same default.
# It can be especially useful if the default is a type used for aggregating or accumulating values,
# such as a list, set, or even int.
# The standard library documentation includes several examples of using defaultdict this way.

######## Method 1
dict_set = {}

# if key not in dict_set:
#     dict_set[key] = set()
# dict_set[key].add(item)

##### Method 2

dict_set = {}
# dict_set.setdefault(key, set()).add(item)

#######Method 3

from collections import defaultdict
# dict_set = defaultdict(set)
# dict_set[key].add(item)


print('\n ===========   Deque =================' )
#A double-ended queue, or deque, supports adding and removing elements from either end.
# The more commonly used stacks and queues are degenerate forms of deques,
# where the inputs and outputs are restricted to a single end.



d = collections.deque('abcdefg')
print( 'Deque:', d)
print( 'Length:', len(d))
print( 'Left end:', d[0])
print( 'Right end:', d[-1])

d.remove('c')
print( 'remove(c):', d)

# Since deques are a type of sequence container, they support some of the same operations that lists support,
# such as examining the contents with __getitem__(), determining length,
# and removing elements from the middle by matching identity.

######## Populating
print('\n----- Populating : ---------')
# A deque can be populated from either end, termed “left” and “right” in the Python implementation.
# Add to the right
d = collections.deque()
d.extend('abcdefg')
print( 'extend    :', d)
d.append('h')
print( 'append    :', d)

# Add to the left
d.extendleft('abcdefg')
print( 'extendleft:', d)
d.appendleft('h')
print( 'appendleft:', d)

# Notice that extendleft() iterates over its input and performs the equivalent of an appendleft() for each item.
#  The end result is the deque contains the input sequence in reverse orde
print('\n----- Consuming  :-------')
# Consuming
# Similarly, the elements of the deque can be consumed from both or either end, depending on the algorithm being applied.

print( 'From the right:')
d = collections.deque('abcdefg')
while True:
    try:
        print( d.pop(), end='  ')
    except IndexError:
        break

print('\n',d)

print( '\nFrom the left:')
d = collections.deque('abcdefg')
while True:
    try:
        print( d.popleft(), end='  ')
    except IndexError:
        break


# Use pop() to remove an item from the “right” end of the deque and popleft() to take from the “left” end.
# Since deques are thread-safe, the contents can even be consumed
# from both ends at the same time from separate threads.

import threading
import time

candle = collections.deque(range(11))

def burn(direction, nextSource):
    while True:
        try:
            next = nextSource()
        except IndexError:
            break
        else:
            print ('%8s: %s' % (direction, next) , end='   ')
            time.sleep(0.1)
    print( '%8s done' % direction, end='   ')
    return

left = threading.Thread(target=burn, args=('Left', candle.popleft))
right = threading.Thread(target=burn, args=('Right', candle.pop))

left.start()
right.start()

left.join()
right.join()

print('\n--------------------- Rotating :--------------------')
# Another useful capability of the deque is to rotate it in either direction, to skip over some items.
d = collections.deque(range(10))
print ('Normal        :', d)

d = collections.deque(range(10))
d.rotate(2)
print ('Right rotation:', d)

d = collections.deque(range(10))
d.rotate(-2)
print ('Left rotation :', d)

# Rotating the deque to the right (using a positive rotation) takes items from the right end and moves them to the left end.
# Rotating to the left (with a negative value) takes items from the left end and moves them to the right end.
# It may help to visualize the items in the deque as being engraved along the edge of a dial.