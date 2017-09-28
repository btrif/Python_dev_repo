'''
List Comprehensions
List comprehensions are a much simpler way of creating lists. 
This is one feature, rather widely used, and I saw this in many examples and source 
of many libraries.
Imagine you have a function which returns a list of data.

 A good example of this is range(start, end) function,
which returns all numbers within the range [start, end). 
This is a generator, so it doesn't return all numbers at once,
 but you need to call this function many times, and each time it returns the next number.
'''
numbers = []
for i in range(1, 11):
    numbers.append(i)

print(numbers)

# If you want to get only the even numbers, then you can write:
numbers = []
for i in range(1, 11):
    if i % 2 == 0:
        numbers.append(i)
        
print(numbers)

'''
List comprehensions can make the code much simpler. The below expression evaluates to a list:
[ expression for item in list if conditional ]
The first example can be then written as:
'''
#   Doing it with List comprehensions
numbers = [i for i in range(1, 11)]
print(numbers)

# and the second becomes
numbers = [i for i in range(1, 11) if i%2 ==0]
print(numbers)
'''
Removing Duplicates
Another common usage of collections is to remove duplicates. And again there are plenty of ways to do it.
Consider a collection like this:
'''
numbers = [i for i in range(1,11)] + [i for i in range(1,6)]
#The most complicated way of removing duplicates I've ever seen was:
unique_numbers = []
for n in numbers:
    if n not in unique_numbers:
        unique_numbers.append(n)
print(numbers)
print(unique_numbers)

'''
Of course it works, but there a much easier way. You can use a standard type like set. 
Set cannot have duplicates, so when converting a list to a set, all duplicates are removed. 
However at the end there will be set, not list, if you want to have a list, then you should convert it again:
'''
unique_numbers2 = list(set(numbers))
print(unique_numbers2)

print('_____'*20,'\n')
########################################################################

#   this is a list
words = 'The quick brown fox jumps over the lazy dog'.split()
print(words)
print('the type of the words is: ', type(words))

#   this is a string because it has no split so it is automatically considered a string
words2 = 'The quick brown fox jumps over the lazy dog'
print(words2)
print('the type of the words2 is: ', type(words2))

print('_____'*10,'\n')

#   Make operations unto the list and then print it
stuff = [[w.upper(), w.lower(), len(w)] for w in words]
for i in stuff:
    print(i)

stuff = map(lambda w: [w.upper(), w.lower(), len(w)], words)

print('_____'*20,'\n')
########################################################################
#Comprehension LISTS

S = [x**2 for x in range(10)]
V = [2**i for i in range(13)]
M = [x for x in S if x % 2 == 0]

print ('S:  ',S); print('V:  ',V); print ('M:  ',M)

print('_____'*20,'\n')

'''
The following is yet another way to compute prime numbers.
The interesting thing is that we first build a list of non-prime numbers,
using a single list comprehension, then use another list comprehension
 to get the "inverse" of the list, which are prime numbers
'''
''' the idea behind the next list called no_primes is to put in a list all the multiples of the numbers 2-7
and then to create another list (primes) with the numbers not found in the no_primes list
'''
print('---'*20,'PRIME NUMBERS','---'*20,'\n')
a = [i for i in range(2,8)]
print(a)
no_primes = [j for i in range(2,8) for j in range(i*2, 50, i)]
print(no_primes)
primes = [x for x in range(2,50) if x not in no_primes]
print(primes)


print('----'*15,'   NICE LIST COMPREHENSIONS   ','----'*15)
import itertools
A = [x for x in list(itertools.permutations(['1','0','6','9']))]
B = ["".join(x) for x in A  ]   # = ''.join(x)
C = [int(x) for x in B  if int(x) >1000]
print(A)
print(B)
print(C)

print('====='*15)
test_list=[[8, 49, 31, 23],\
[2, 99, 73, 4],\
[22, 40, 55, 60],\
[97, 17, 79, 11],\
[38, 81, 14, 42],\
[15, 18, 29, 69],\
[0, 57, 93, 24],\
[40, 60, 71, 68],\
[0, 87, 40, 56]]

grid=[x for x in test_list]
print(grid)

print('\n---------------Build a matrix or table with zeroes in it of custom size----------------- ')
print( [[0 for x in range(4)] for x in range(10+1)])


print('\n ---------------------   break list comprehension, Stop an iteration if a condition is met ----------')


from itertools import count
def end_of_loop():
    raise StopIteration

print('This loop stops at 100 even if normally will go to Infinity :'  , list( end_of_loop() if i*i > 100 else  i*i for i in count(1) ))




print('\n ---------------------   List Comprehension, IF ELSE Statements Together, same proposition ----------')


l = [22, 13, 45, 50, 98, 69, 43, 44, 1]
print(' IF ELSE Statements Together : \t' , [x+1 if x >= 45 else x+5 for x in l] )

print('\n ---------------------   List Comprehension, Double if statement list comprehension----------')
print(' Double if statement list comprehension : \t ' , [i for i in range(100) if i > 10 if i < 30] )
print(' Double if statement list comprehension : \t ' , [i for i in range(100)  if ( i > 10 and  i < 30 ) ] )








