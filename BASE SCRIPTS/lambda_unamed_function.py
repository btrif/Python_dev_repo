'''
Unnamed functions (lambda function)
In Python we can also create unnamed functions, using the lambda keyword:

'''

f1 = lambda x: x**2

# is equivalent to

def f2(x):
    return x**2

print(f1(4), f2(3))
#This technique is useful for example when we want to pass a simple function
# as an argument to another function, like this:
# map is a built-in python function
map1 = map(lambda x: x**2, range(-3,4))
print(map1)
# in python 3 we can use `list(...)` to convert the iterator to an explicit list
list1 = list(map(lambda x: x**2, range(-3,4)))
print(list1)