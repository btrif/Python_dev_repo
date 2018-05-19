#  Created by Bogdan Trif on 06-05-2018 , 12:20 AM.


'''
__foo__: this is just a convention, a way for the Python system to use names that won't conflict with user names.

_foo: this is just a convention, a way for the programmer to indicate that the variable is private (whatever that means in Python).

__foo: this has real meaning: the interpreter replaces this name with _classname__foo as a way to ensure that the name
will not overlap with a similar name in another class.

No other form of underscores have meaning in the Python world.

There's no difference between class, variable, global, etc in these conventions.

'''

class MyClass():
    def __init__(self):
        self.__superprivate = "Hello"
        self._semiprivate = ", world!"

mc = MyClass()

print(mc._semiprivate)

print(mc.__dict__)

# print(mc.__superprivate)

##  Special access to the superprive variable is done as follows :
print(mc._MyClass__superprivate)

#####
print('\n--------------------- Second Example ----------------------')

'''
._variable           is semiprivate and meant just for convention

.__variable          is often incorrectly considered superprivate, while it's actual meaning is just to namemangle to prevent accidental access[1]

.__variable__        is typically reserved for builtin methods or variables

You can still access .__mangled variables if you desperately want to. 
The double underscores just namemangles, or renames, the variable to something like instance._className__mangled

Example:
'''

class Test(object):
    def __init__(self):
        self.__a = 'a'
        self._b = 'b'

t = Test()

# 1.      t._b is accessible because it is only hidden by convention
print( t._b)

#  2.      t.__a isn't found because it no longer exists due to namemangling
# print(t.__a)

##  3.   By accessing instance._className__variable instead of just the double underscore name, you can access the hidden value

print(t._Test__a)
