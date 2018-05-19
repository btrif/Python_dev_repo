'''
List comprehensions provide a concise way to create lists. 
Common applications are to make new lists where each element is the result 
of some operations applied to each member of another sequence or iterable,
 or to create a subsequence of those elements that satisfy a certain condition.

For example, assume we want to create a list of squares, like:
'''

squares = []
for x in range(10):
    squares.append(x**2)
print(squares)
print(x)

'''
Note that this creates (or overwrites) a variable named x that still exists after the loop completes.
 We can calculate the list of squares without any side effects using:
'''

squares = list(map(lambda x: x**2, range(10)))
print(squares)

''' or, equivalently: '''

squares = [x**2 for x in range(10)]
print(squares)
''' which is more concise and readable.

A list comprehension consists of brackets containing an expression followed by a for clause, 
then zero or more for or if clauses. The result will be a new list resulting from evaluating 
the expression in the context of the for and if clauses which follow it. For example,
 this listcomp combines the elements of two lists if they are not equal:
'''

list = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
print(list)

""" and it's equivalent to: """

combss = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combss.append((x, y))

print(combss)
#---------------------------------------------------
vec = [-4, -2, 0, 2, 4]
 # create a new list with the values doubled
a = [x*2 for x in vec]
print(a)

 # filter the list to exclude negative numbers
a= [x for x in vec if x >= 0]
print(a)

# apply a function to all the elements
a = [abs(x) for x in vec]
print(a)

# call a method on each element
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
a= [weapon.strip() for weapon in freshfruit]
print(a)

# create a list of 2-tuples like (number, square)
# the tuple must be parenthesized, otherwise an error is raised
a = [(x, x**2) for x in range(6)]
print(a)

#------------------------------------------------
# flatten a list using a listcomp with two 'for'
vec = [[1,2,3], [4,5,6], [7,8,9]]
a = [num for elem in vec for num in elem]
print(a)

'''List comprehensions can contain complex expressions and nested functions: '''
from math import pi
a = [str(round(pi, i)) for i in range(1, 16)]
print(a)

