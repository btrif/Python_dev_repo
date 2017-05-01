
print('\n--------- How to create a set? -------------')

# A set is created by placing all the items (elements) inside curly braces {}, separated by comma or by using the built-in function set().
# It can have any number of items and they may be of different types (integer, float, tuple, string etc.).
# But a set cannot have a mutable element, like list, set or dictionary, as its element.

# set of integers
my_set = {1, 2, 3}
print(my_set)

# set of mixed datatypes
my_set = {1.0, "Hello", (1, 2, 3)}
print(my_set)

# set do not have duplicates
# Output: {1, 2, 3, 4}
my_set = {1,2,3,4,3,2}
print(my_set)

# set cannot have mutable items
# here [3, 4] is a mutable list
# If you uncomment line #25,
# this will cause an error.
# TypeError: unhashable type: 'list'

# my_set = {1, 2, [3, 4]}

# we can make set from a list
# Output: {1, 2, 3}
my_set = set([1,2,3,2])
print(my_set)



# Creating an empty set is a bit tricky.
# Empty curly braces {} will make an empty dictionary in Python.
# To make a set without any elements we use the set() function without any argument.
# initialize a with set()
a = set()
# check data type of a
# Output: <class 'set'>
print(type(a))

print('\n--------- How to change a set in Python? -------------')

# How to change a set in Python?
# Sets are mutable. But since they are unordered, indexing have no meaning.
#
# We cannot access or change an element of set using indexing or slicing. Set does not support it.
#
# We can add single element using the add() method and multiple elements using the update() method.
# The update() method can take tuples, lists, strings or other sets as its argument. In all cases, duplicates are avoided.

# initialize my_set
my_set = {1,3}
print(my_set)

# if you uncomment line 9,
# you will get an error
# TypeError: 'set' object does not support indexing

#my_set[0]

# add an element
# Output: {1, 2, 3}
my_set.add(2)
print(my_set)

# add multiple elements
# Output: {1, 2, 3, 4}
my_set.update([2,3,4])
print(my_set)

# add list and set
# Output: {1, 2, 3, 4, 5, 6, 8}
my_set.update([4,5], {1,6,8})
print(my_set)

print('\n--------- How to remove elements from a set? -------------')

# How to remove elements from a set?
# A particular item can be removed from set using methods, discard() and remove().
#
# The only difference between the two is that, while using discard() if the item does not exist in the set,
# it remains unchanged. But remove() will raise an error in such condition.
#
# The following example will illustrate this.

# initialize my_set
my_set = {1, 3, 4, 5, 6}
print(my_set)

# discard an element
# Output: {1, 3, 5, 6}
my_set.discard(4)
print(my_set)

# remove an element
# Output: {1, 3, 5}
my_set.remove(6)
print(my_set)

# discard an element  not present in my_set
# Output: {1, 3, 5}
my_set.discard(2)
print(my_set)

# remove an element  not present in my_set
# If you uncomment line bellow,  you will get an error.
# Output: KeyError: 2

# my_set.remove(2)

# Similarly, we can remove and return an item using the pop() method.
#
# Set being unordered, there is no way of determining which item will be popped. It is completely arbitrary.
#
# We can also remove all items from a set using clear().
# initialize my_set
# Output: set of unique elements
my_set = set("HelloWorld")
print(my_set)

# pop an element
# Output: random element
print(my_set.pop())

# pop another element
# Output: random element
my_set.pop()
print(my_set)

# clear my_set
#Output: set()
my_set.clear()
print(my_set)

print('\n--------- Python Set Operations -------------')
# Sets can be used to carry out mathematical set operations like union, intersection, difference and symmetric difference.
# We can do this with operators or methods.
# Let us consider the following two sets for the following operations.
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
print(A,'\n',B)

print('\n--------- Set Union -------------')

# Union of A and B is a set of all elements from both sets.
# Union is performed using | operator. Same can be accomplished using the method union().
# use | operator
# Output: {1, 2, 3, 4, 5, 6, 7, 8}
print('Union of A and B :\t',A | B)

# use union function
print('Union of A and B :\t',A.union(B))

# use union function on B
print('Union of A and B :\t',B.union(A))

print('\n--------- Set Intersection -------------')

# Set Intersection
# Intersection of A and B is a set of elements that are common in both sets.
# Intersection is performed using & operator. Same can be accomplished using the method intersection().
# initialize A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
# use & operator
# Output: {4, 5}
print('Intersection of A and B :\t',A & B)

# use intersection function on A
print('Intersection of A and B :\t',A.intersection(B))

# use intersection function on B
print('Intersection of A and B :\t',B.intersection(A))

print('\n--------- Set Difference -------------')
 # Set Difference
# Difference of A and B (A - B) is a set of elements that are only in A but not in B. Similarly, B - A is a set of element in B but not in A.
# Difference is performed using - operator. Same can be accomplished using the method difference().
# initialize A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# use - operator on A
# Output: {1, 2, 3}
print('Set Difference of A and B :\t',A - B)

# use difference function on A
print('Set Difference of A and B :\t',A.difference(B))

# use - operator on B
print('Set Difference of B and A :\t',B - A)

# use difference function on B
print('Set Difference of B and A :\t',B.difference(A))

print('\n--------- Set Symmetric Difference -------------')

# Set Symmetric Difference
# Symmetric Difference of A and B is a set of elements in both A and B except those that are common in both.
# Symmetric difference is performed using ^ operator. Same can be accomplished using the method symmetric_difference().
# initialize A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# use ^ operator
# Output: {1, 2, 3, 6, 7, 8}
print('Set Symmetric Difference of A and B :\t',A ^ B)

# use symmetric_difference function on A
print('Set Symmetric Difference of A and B :\t',A.symmetric_difference(B))

# use symmetric_difference function on B
print('Set Symmetric Difference of A and B :\t',B.symmetric_difference(A))


print('\n--------- Other Set Operations -------------')
print('\n--------- Set Membership Test -------------')

# We can test if an item exists in a set or not, using the keyword in.
# initialize my_set
my_set = set("apple")

# check if 'a' is present
# Output: True
print('a' in my_set)

# check if 'p' is present
# Output: False
print('p' not in my_set)

# Built-in Functions with Set
# Built-in functions like
# all(),      Return True if all elements of the set are true (or if the set is empty).
# any(),      Return True if any element of the set is true. If the set is empty, return False.
# enumerate(),    Return an enumerate object. It contains the index and value of all the items of set as a pair.
# len(), max(),
# min(),
# sorted(),
# sum() etc. are commonly used with set to perform different tasks.

print('\n--------- Python Frozenset-------------')

# Frozenset is a new class that has the characteristics of a set, but its elements cannot be changed once assigned.
# While tuples are immutable lists, frozensets are immutable sets.
#
# Sets being mutable are unhashable, so they can't be used as dictionary keys.
# On the other hand, frozensets are hashable and can be used as keys to a dictionary.
#
# Frozensets can be created using the function frozenset().
#
# This datatype supports methods like copy(), difference(), intersection(), isdisjoint(), issubset(), issuperset(),
# symmetric_difference() and union(). Being immutable it does not have method that add or remove elements.

# initialize A and B
A = frozenset([1, 2, 3, 4])
B = frozenset([3, 4, 5, 6])
print(A,'\n',B)
A.isdisjoint(B)
print('A-B Difference: \t',A.difference(B))
print('Union :\t ',A | B)
# print('Adding an element fails because it is immutable : \t', A.add(3) )




print('\n----------- Multisets and multiset operations (collections.Counter) --------------')
import collections

A = collections.Counter([1, 2, 2])
B = collections.Counter([2, 2, 3])
print(A)
print(B)
print( A | B )
print(A & B)
print( A + B )
print(A - B)
print( B - A )



print('\n-------------- Named tuples (collections.namedtuple)----------------------')
Point = collections.namedtuple('Point', ['x', 'y'])
p = Point(x=1.0, y=2.0)
print(p)
print( p.x, p.y)



print('\n------------ SET INTERSECTION of a list of numbers -------------------------')
# We have a list of numbers and we have a test number.
# We want to make the intersection of the test number with every number from the list
# and return only the numbers which have no common digits with the test number
lst = {257, 641, 643, 769, 389, 263, 647, 137, 521, 139, 523, 269, 397, 271, 653, 659, 149}
print('The initial list to of elements :\t',lst)
test_nr = 324
set_nr = set([int(i) for i in str(test_nr)])
print('Test number :\t', test_nr, set_nr)
INTERSECTION = [ s for s in lst if len(set_nr& set([int(i) for i in str(s)]) )==0 ]
print(' Intersection of the test_nr with every element of the list yields :\n', INTERSECTION )


print('\n--------------- Create set of tuples ---------------------------')

import itertools
mySet = set(itertools.product(range(1,5), repeat=2))
print(mySet)
mySet = set((x,y) for x in range(1,5) for y in range(1,5))
print(mySet)


