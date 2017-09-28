
print('\n------------------- enumerate --------------------------')
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print(list(enumerate(seasons)))

print(list(enumerate(seasons, start=1)))

print('\n-----------------------  enumerate & lambda    ---------------------')
from pyprimes import  primes_below
N=100
primes = primes_below(N)
fact = [1]*(N+1)
for p in primes:
      for j in range(1,N//p+1):
         fact[p*j]*=p
         s,n = 0,0
F = sorted(enumerate(fact), key = lambda x:x[1])
C = sorted(enumerate(fact),key= lambda x:x[0]/x[1], reverse=True)
print(C)
print(F)


print('\n-----------------Binary, Decimal, Octodecimal,  Hexadecimal  Conversions ----------------')
print('Decimal to Binary : ',bin(14))
print('Binary to Decimal : ',int('10111', 2))

print('Decimal to Binary : ',bin(1411))
print('Binary to Decimal : ',int('10110111', 2))
print('------------------------')
print('Hexadecimal to Decimal : ',int('ffaa', 16))
print('Octodecimal to Decimal : ',int('7676', 8))

print('Decimal to Hexadecimal  : ', hex(65365) )
print('Decimal to Octodecimal  : ', oct(65) )

print('\n-----------------------   ord & chr    ---------------------')
print('ord(a) and chr(57) return (respectively) the integer representing the given char and the char represented by the given integer.')
print('Test ord  :   ', ord('a'))
print('Test chr  :   ', chr(97))




print('\n--------------------    zip    -------------------------')
print('zip(a, b) returns an iterator that aggregates elements from each of the two iterables. '
      'It stops on the shortest input sequence ')
a = [0,1,2,3,4,5,6]
b = ['a' , 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i','j' 'k', 'l','m']
z = zip(a,b)
for i in range(6):  print(next(z), end='  ')

print('\n\n--------------------       cycle & next    -------------------------')
from itertools import cycle
print("cycle(key) returns an iterator that produces an infinite concatenation of key's content ")
print('G.__next__() or next(G) where G is a generator gives next item in the sequence ')
print('cycle works well with zip and next \n')
key='abcd'
C = cycle(key)
print('Cycling the key : ' , C.__next__() , C.__next__(),  C.__next__() , C.__next__() )
for i in range(14) : print( next(C)  , end='  ' )

print('\n--------------------       map    -------------------------')
# The advantage of the lambda operator can be seen when it is used in combination with the map() function.
# map() is a function with two arguments:       r = map(func, seq)
# The first argument func is the name of a function and the second a sequence (e.g. a list) seq. map() applies
# the function func to all the elements of the sequence seq. It returns a new list with the elements changed by func

print('Here we make o conversion between Celsius and Fahrenheit using lambda and map: ' )
Celsius = [39.2, 36.5, 37.3, 37.8]
print(Celsius)
Fahrenheit = map(lambda x: (float(9)/5)*x + 32, Celsius)
print( list(Fahrenheit) ,'\n')

#   Example 2 :
# map() can be applied to more than one list. The lists have to have the same length. map() will apply its lambda
#         function to the elements of the argument lists, i.e. it first applies to the elements with the 0th index,
# then to the elements with the 1st index until the n-th index is reached:
print(' ---  map can be applied to more than one list : ----')
a = [1,2,3,4]
b = [17,12,11,10]
c = [-1,-4,5,9]
print('Using two lists with map: ', list( map(lambda x,y : x+y, a , b) ))
print('Using three lists with map: ', list(map(lambda x,y,z : x+y+z, a, b ,c)))
print('Using three lists with map: ', list(map(lambda x,y,z : x+y-z, a, b , c) ))


print("\n --------------------------- FILTERING, filter function --------------------------")
# The function filter(function, list) offers an elegant way to filter out all the elements of a list,
# for which the function function returns True.
# The function filter(f,l) needs a function f as its first argument. f returns a Boolean value, i.e. either True or False.
# This function will be applied to every element of the list l.
# Only if f returns True will the element of the list be included in the result list.

fib = [0,1,1,2,3,5,8,13,21,34,55]
even = filter(lambda x: x % 2, fib)
print ('Here we filter the even numbers of the Fibonacci sequence, we display only odd :  ', list(even))

odd = filter(lambda x: x % 2 == 0, fib)
print ('Here we filter the odd numbers of the Fibonacci sequence, we display only even :  ',list(odd))

# Lambda forms can also be used with the filter function;
# in fact, they can be used anywhere a function is expected in Python.
# In the fifth example, the list of squares is filtered according to whether the given entries are greater than 5 and less than 50.
# A lambda form that returns True when this condition is met is lambda x: x > 5 and x < 50.
# Thus, we can reproduce the fifth example as follows:

squares = map(lambda x: x**2, range(10))
special_squares = filter(lambda x: x > 5 and x < 50, squares)
print (special_squares)


A = [6, 7, 8, 9, 10, 11, 12]
subset_of_A = set([6, 9, 12]) # the subset of A
result = [a for a in A if a not in subset_of_A]
a = list(filter(lambda x: x not in subset_of_A, A))
print(a)


print('\n -------------------------------  Reducing a list, with reduce -----------------')
# The function reduce(func, seq) continually applies the function func() to the sequence seq. It returns a single value.
#
# If seq = [ s1, s2, s3, ... , sn ], calling reduce(func, seq) works like this:
# = At first the first two elements of seq will be applied to func, i.e. func(s1,s2)
#     The list on which reduce() works looks now like this: [ func(s1, s2), s3, ... , sn ]
# = In the next step func will be applied on the previous result and the third element of the list, i.e. func(func(s1, s2),s3)
#     The list looks like this now: [ func(func(s1, s2),s3), ... , sn ]
# = Continue like this until just one element is left and return this element as the result of reduce()
# We illustrate this process in the following example:
from functools import reduce
a = reduce(lambda x,y: x+y, [47,11,42,13])
print('Calculates the sum of the list :   ', a )
f = lambda a,b: a if (a > b) else b
print('Determining the maximum of a list of numerical values by using reduce:   ', reduce(f, [47,11,42,102,13]))
s = reduce(lambda x, y : x+y, range(1,101))
print('Calculating the sum of the numbers from 1 to 100:   ', s)
factorial = reduce(lambda x,y : x*y, range(1,6))
print('Calculating the factorial of 5 :   ', factorial)


print('\n------------------- Digital Sum of a number ----------------')
N = 467
print( N, '     and its digital sum : \t',sum(map(int, str(N))) )

def ds(n):
    ds = sum(map(int,str(n)))
    if ds < 10 : return ds
    else: return sum(map(int,str(ds)))


print('\n================ bytearray ================')
print('\n------------------- bytearray ----------------')
# With bytes, we have an addressable unit of memory. A byte is made of bits—but these are not as easily accessed.
# Back to Python. A byte can store 0 through 255 --- we use bytes and bytearray.



print('------------Python program that creates bytearray from list----------------')
# Bytearray example. This example creates a list. Each number in the list is between 0 and 255 (inclusive).
# We create a bytearray from the list.
# Modify:
# We modify the first two elements in the bytearray. This cannot be done with a bytes object.
# For:
# We use the for-loop to iterate over the bytearray's elements. This is the same as how we use a list.

elements = [0, 200, 50, 25, 10, 255]

# Create bytearray from list of integers.
values = bytearray(elements)

# Modify elements in the bytearray.
values[0] = 5
values[1] = 0

# Display bytes.
for value in values:  print(value, end='   ')
print()

print('\n--------------- Bytes example. --------------')
# Bytes example.
# We now consider "bytes." This is similar to bytearray. But the elements of a bytes object cannot be changed.
# It is an immutable array of bytes.
# Buffer protocol:
# Bytearray, bytes and memoryview act upon the buffer protocol. They all share similar syntax with small differences.
# Python program that creates bytes object

elements = [5, 10, 0, 0, 100]

# Create immutable bytes object.
data = bytes(elements)

# Loop over bytes.
for d in data:    print(d, end='  ')

print('\n--------------- Bytes error  --------------')

# Error. Now we get into some trouble—that is always fun. Here we try to modify the first element of a bytes object.
# Python complains—the "object does not support item assignment."
# Python program that causes error

data = bytes([10, 20, 30, 40])

# We can read values from a bytes object.
print(data[0])

# We cannot assign elements.
# data[0] = 1

print('\n--------------- Bytes Literals  --------------')

# Literals. Bytes and bytearray objects can be created with a special string literal syntax.
# We prefix the literals with a "b." This prefix is required.
# Tip:
# Buffer protocol methods require byte-prefix string literals, even for arguments to methods like replace().
# Python program that uses byte literals

# Create bytes object from byte literal.
data = bytes(b"abc")
for value in data:
    print(value, end='  ')

print()
# Create bytearray from byte literal.
arr = bytearray(b"abc")
for value in arr:    print(value, end='  ')

print('\n--------------- bytearray Slice  --------------')
# Slice, bytearray. We can slice bytearrays. And because bytearray is mutable,
# we can use slices to change its contents. Here we assign a slice to an integer list.
# Python program that uses slice, changes bytearray

values = [5, 10, 15, 20]
arr = bytearray(values)

# Assign first two elements to new list.
arr[0:2] = [100, 0, 0]

# The array is now modified.
for v in arr: print(v, end='  ')

print('\n--------------- Bytes Slice  --------------')
# Slice, bytes. A bytes object too supports slice syntax, but it is read-only.
# Here we get a slice of bytes (the first two elements) and loop over it.
# Often:
# We can loop over a slice directly in the for-loop condition. The variable is not needed.
# Python that uses slice, bytes

data = bytes(b"abc")

# Get a slice from the bytes object.
first_part = data[0:2]

# Display values from slice.
for element in first_part: print(element, end='  ')

print('\n--------------- Bytes Count  --------------')

# Count. Many methods are available on the buffer interface. Count is one.
# It loops through the bytes and counts instances matching our specified pattern.
# Note:
# Count must loop through all elements. If another loop is needed afterwards, often we can combine loops for speed.
# Argument:
# The argument to count() must be a byte object, like a "b" string literal or a number between 0 and 255.
# Python that uses count, buffer interface

# Create a bytes object and a bytearray.
data = bytes(b"aabbcccc")
arr = bytearray(b"aabbcccc")

# The count method (from the buffer interface) works on both.
print(data.count(b"c"))
print(arr.count(b"c"))

print('\n--------------- Combine two bytearrays.  --------------')
# Combine two bytearrays. As with lists and other sequences, we can combine two bytearrays (or bytes) with a plus.
# In my tests, I found it does not matter if we combine two different types.
# Python that uses plus on bytearrays

left = bytearray(b"hello ")
right = bytearray(b"world")

# Combine two bytearray objects with plus.
both = left + right
print(both)

print('\n--------------- Convert list. --------------')

# Convert list. A list of bytes (numbers between 0 and 256) can be converted into a bytearray with the constructor.
# To convert back into a list, please use the list built-in constructor.
# Tip:
# Lists display in a more friendly way with the print method. So we might use this code to display bytearrays and bytes.
# Python that uses list built-in

initial = [100, 255, 255, 0]
print(initial)

# Convert the list to a byte array.
b = bytearray(initial)
print(b)

# Convert back to a list.
result = list(b)
print(result)

print('\n--------------- Convert string. --------------')
# Convert string. A bytearray can be created from a string. The encoding (like "ascii") is specified as the second argument
# in the bytearray constructor.
# Decode:
# To convert from a bytearray back into a string, the decode method is needed.
# Python that converts string, bytearray

# Create a bytearray from a string with ASCII encoding.
arr = bytearray("abc", "ascii")
print(arr)

# Convert bytearray back into a string.
result = arr.decode("ascii")
print(result)

print('\n--------------- Append, del, insert --------------')

# Append, del, insert. A bytearray supports many of the same operations as a list.
# We can append values. We can delete a value or a range of values with del. And we can insert a value.
# Python that uses append, del, insert

# Create bytearray and append integers as bytes.
values = bytearray()
values.append(0)
values.append(1)
values.append(2)
print(values)

# Delete the first element.
del values[0:1]
print(values)

# Insert at index 1 the value 3.
values.insert(1, 3)
print(values)

print('\n--------------- ValueError--------------')
# ValueError. Numbers inserted into a bytearray or bytes object must be between 0 and 255 inclusive.
# If we try to insert an out-of-range number, we will receive a ValueError.
# Python that causes ValueError

# This does not work.
# values = bytes([3000, 4000, 5000])
# print("Not reached")

print('\n--------------- Replace--------------')

# Replace. The buffer protocol supports string-like methods. We can use replace() as on a string.
# The arguments must be bytes objects—here we use "b" literals.
# Python that uses replace on bytes

value = b"aaabbb"

# Use bytes replace method.
result = value.replace(b"bbb", b"ccc")
print(result)

print('\n--------------- Compare--------------')

# Compare. A "b" literal is a bytes object. We can compare a bytearray or a bytes object with this kind of constant.
# To compare bytes objects, we use two equals signs.
# Note:
# Two equals signs compares the individual byte contents, not the identity of the objects.
# Python that compares bytes

# Create a bytes object with no "bytes" keyword.
value1 = b"desktop"
print(value1)

# Use bytes keyword.
value2 = bytes(b"desktop")
print(value2)

# Compare two bytes objects.
if value1 == value2:
    print(True)

print('\n--------------- Start, end--------------')

# Start, end. We can handle bytes objects much like strings. Common methods like startswith and endswith are included.
# These check the beginning and end parts.
# Argument:
# The argument to startswith and endswith must be a bytes object. We can use the handy "b" prefix.
# Python that uses startswith, endswith

value = b"users"

# Compare bytes with startswith and endswith.
if value.startswith(b"use"):
    print(True)

if value.endswith(b"s"):
    print(True)

print('\n--------------- Split, join--------------')
# Split, join. The split and join methods are implemented on bytes objects. Here we handle a simple CSV string in bytes.
# We separate values based on a comma char.
# Python that uses split, join

# A bytes object with comma-separate values.
data = b"cat,dog,fish,bird,true"

# Split on comma-byte.
elements = data.split(b",")

# Print length and list contents.
print(len(elements))
print(elements)

# Combine bytes objects into a single bytes object.
result = b",".join(elements)
print(result)

print('\n--------------- Memory view--------------')

# Memoryview. This is an abstraction that provides buffer interface methods.
# We can create a memoryview from a bytes object, a bytearray or another type like an array.
# Array
# Tip:
# With memoryview we can separate our code that uses the buffer interface from the actual data type. It is an abstraction.
# Python that uses memoryview

view = memoryview(b"abc")

# Print the first element.
print(view[0])

# Print the element count.
print(len(view))

# Convert to a list.
print(view.tolist())

print('\n--------------- Performance, Actually does not work as advertised --------------')
# Performance. Suppose we want to append 256 values to a list. Bytearray here is faster.
# So we both improve memory size and reduce time required with bytearray over list.
# So:
# Bytearray is more complex to handle. It does not support non-ASCII characters or large numeric values.
# But:
# In many programs where these are not required, bytearray can be used to improve speed. This benchmark supports this idea.
# Python that times list, bytearray appends

import time
t1=time.time()


# Version 1: append to list.
for i in range(0, 100000):
    x = list()
    for v in range(0, 255):
        x.append(v)

print('Completed in : ',time.time() -t1)

# Version 2: append to bytearray.
t1=time.time()

for i in range(0, 1000 ):
    x = bytearray()
    for v in range(0, 255):
        x.append(v)

print('Completed in : ',time.time() -t1)









