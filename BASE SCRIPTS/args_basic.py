
import sys

print('Number of arguments:', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv))

print('\nThe list of arguments is:\n')

print('Argument No 0   is:', str(sys.argv[0]))
# print('Argument No 1   is:', str(sys.argv[1]))
# print('Argument No 2   is:', str(sys.argv[2]))
# print('Argument No 3   is:', str(sys.argv[3]))
# print('Argument No 4   is:', str(sys.argv[4]))


a = 0
for i in sys.argv[0:]:	
		print('Argument No', a, 'is:', i)
		a = a + 1


print('\n----------------https://stackoverflow.com/questions/3394835/args-and-kwargs ----------------------')

# The syntax is the * and **. The names *args and **kwargs are only by convention but there's no hard requirement to use them.

# You would use *args when you're not sure how many arguments might be passed to your function,
# i.e. it allows you pass an arbitrary number of arguments to your function. For example:

def print_everything(*args):
	for count, thing in enumerate(args):
		print( '{0}. {1}'.format(count, thing))
		# print( str(count)+  '.    ' , thing )

print_everything('apple', 'banana', 'cabbage')

print ( "\n ----  Similarly, **kwargs allows you to handle named arguments that you have not defined in advance: ")

def table_things(**kwargs):
	for name, value in kwargs.items():
		print( '{0} = {1}'.format(name, value))

table_things(apple = 'fruit', cabbage = 'vegetable')


# You can use these along with named arguments too.
# The explicit arguments get values first and then everything else is passed to *args and **kwargs.
# The named arguments come first in the list. For example:

print('\nYou can also use the * and ** syntax when calling a function. For example: ')

# You can also use both in the same function definition but *args must occur before **kwargs.
# You can also use the * and ** syntax when calling a function. For example:


def print_three_things(a, b, c):
	print( 'a = {0}, b = {1}, c = {2}'.format(a,b,c))

mylist = ['aardvark', 'baboon', 'cat']
print_three_things(*mylist)


print('\n ------------------------------ Subclassing with *args and **kwargs---------------------')

# One place where the use of *args and **kwargs is quite useful is for subclassing.

class Foo(object):
    def __init__(self, value1, value2):
        # do something with the values
        print (value1, value2)

class MyFoo(Foo):
    def __init__(self, *args, **kwargs):
        # do something else, don't care about the args
        print ('myfoo')
        super(MyFoo, self).__init__(*args, **kwargs)

# This way you can extend the behaviour of the Foo class, without having to know too much about Foo.
# This can be quite convenient if you are programming to an API which might change.
# MyFoo just passes all arguments to the Foo class.

Lst = [ 'Alpha' , 'Beta', 'Gamma', 'Delta' ]
print(Foo(Lst, 0))
print(MyFoo(Lst, 100))


print('\n--------------- some Custom Function --------------')

# *args and **kwargs are special-magic features of Python.
# Think of a function that could have an unknown number of arguments.
# For example, for whatever reasons, you want to have function that sums an unknown number of numbers
# (and you don't want to use the built-in sum function). So you write this function:

def sumFunction(*args):
  result = 0
  for x in args:
    result += x
  return result

print('This function sums all the arguments : \t', sumFunction( 3,4,6,3,6,8,9) )

# **kwargs has a diffrent function.
# With **kwargs you can give arbitrary keyword arguments to a function and you can access them as a dictonary.

def someFunction(**kwargs):
  if 'text' in kwargs:
    print (kwargs['text'])

someFunction(text="Dincolo de nori !")

