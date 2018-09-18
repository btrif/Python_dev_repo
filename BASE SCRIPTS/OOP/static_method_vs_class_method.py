#  Created by Bogdan Trif on 19-07-2018 , 4:36 PM.
'''

@staticmethod function is nothing more than a function defined inside a class.
It is callable without instantiating the class first.
It’s definition is immutable via inheritance.

@classmethod function also callable without instantiating the class,
but its definition follows Sub class, not Parent class, via inheritance.
That’s because the first argument for @classmethod function must always be cls (class).

To decide whether to use @staticmethod or @classmethod you have to look inside your method.
-   If your method accesses other variables/methods in your class then use @classmethod.
-   On the other hand, if your method does not touches any other parts of the class then use @staticmethod.


Basically :
@staticmethod does not have any implicit arguments.
@classmethod makes a method whose first argument is the class it's called from (rather than the class instance),


@   A staticmethod is a method that knows nothing about the class or instance it was called on.
It just gets the arguments that were passed, no implicit first argument.
It is basically useless in Python -- you can just use a module function instead of a staticmethod.

@   A classmethod, on the other hand, is a method that gets passed the class it was called on,
or the class of the instance it was called on, as first argument.
This is useful when you want the method to be a factory for the class:
since it gets the actual class it was called on as first argument, you can always instantiate the right class,
even when subclasses are involved.

Observe for instance how dict.fromkeys(), a classmethod, returns an instance of the subclass when called on a subclass:

>>> class DictSubclass(dict):
...     def __repr__(self):
...         return "DictSubclass"
...
>>> dict.fromkeys("abc")
{'a': None, 'c': None, 'b': None}
>>> DictSubclass.fromkeys("abc")
DictSubclass
>>>
'''

print('-------------------  Example 1   ------------------------')

print('\n-------------------  Example 2   ------------------------')

class Apple:

    _counter = 0

    @staticmethod
    def about_apple():
        print('Apple is good for you.')

        # note you can still access other member of the class
        # but you have to use the class instance
        # which is not very nice, because you have repeat yourself
        #
        # For example:
        # @staticmethod
        #    print('Number of apples have been juiced: %s' % Apple._counter)
        #
        # @classmethod
        #    print('Number of apples have been juiced: %s' % cls._counter)
        #
        #    @classmethod is especially useful when you move your function to other class,
        #       you don't have to rename the class reference

    @classmethod
    def make_apple_juice(cls, number_of_apples):
        print('Make juice:')
        for i in range(number_of_apples):
            cls._juice_this(i)

    @classmethod
    def _juice_this(cls, apple):
        print('Juicing %d...' % apple)
        cls._counter += 1
        return cls._counter

print('classmethod --> Apple.make_apple_juice(4) : ', )
Apple.make_apple_juice(4)
print('\nstatic method --> Apple.about_apple() : ',  )
Apple.about_apple()


print('\n-------------------  Example 3   ------------------------')

# Maybe a bit of example code will help: Notice the difference in the call signatures of foo, class_foo and static_foo:

class A(object):
    def foo(self,x):
        print( "executing foo(%s,%s)"%(self,x))

    @classmethod
    def class_foo(cls, x ):
        print( "executing class_foo(%s,%s)"%( cls, x) )

    @staticmethod
    def static_foo(x):
        print ("executing static_foo(%s)"%x )

a = A()
a.foo(1)
print(a.class_foo)
print(a.static_foo)
print(A.static_foo)

'''
Below is the usual way an object instance calls a method. 
The object instance, a, is implicitly passed as the first argument.

a.foo(1)
# executing foo(<__main__.A object at 0xb7dbef0c>,1)
With classmethods, the class of the object instance is implicitly passed as the first argument instead of self.

a.class_foo(1)
# executing class_foo(<class '__main__.A'>,1)
You can also call class_foo using the class. In fact, if you define something to be a classmethod, 
it is probably because you intend to call it from the class rather than from a class instance. 
A.foo(1) would have raised a TypeError, but A.class_foo(1) works just fine:

A.class_foo(1)
# executing class_foo(<class '__main__.A'>,1)
One use people have found for class methods is to create inheritable alternative constructors.

With staticmethods, neither self (the object instance) nor  cls (the class) is implicitly passed as the first argument. 
They behave like plain functions except that you can call them from an instance or the class:

a.static_foo(1)
# executing static_foo(1)

A.static_foo('hi')
# executing static_foo(hi)
Staticmethods are used to group functions which have some logical connection with a class to the class.

foo is just a function, but when you call a.foo you don't just get the function, 
you get a "partially applied" version of the function with the object instance a bound as the first argument to the function. 
foo expects 2 arguments, while a.foo only expects 1 argument.

a is bound to foo. That is what is meant by the term "bound" below:

print(a.foo)
# <bound method A.foo of <__main__.A object at 0xb7d52f0c>>
With a.class_foo, a is not bound to class_foo, rather the class A is bound to class_foo.

print(a.class_foo)
# <bound method type.class_foo of <class '__main__.A'>>

Here, with a staticmethod, even though it is a method, a.static_foo just returns a good 'ole function 
with no arguments bound. 
static_foo expects 1 argument, and a.static_foo expects 1 argument too.

print(a.static_foo)
# <function static_foo at 0xb7d479cc>

And of course the same thing happens when you call static_foo with the class A instead.

print(A.static_foo)
# <function static_foo at 0xb7d479cc>
'''

'''
You might want to move a function into a class because it logically belongs with the class. 
In the Python source code (e.g. multiprocessing,turtle,dist-packages), 
it is used to "hide" single-underscore "private" functions from the module namespace. 
Its use, though, is highly concentrated in just a few modules -- perhaps an indication that it is mainly a stylistic thing. 
Though I could not find any example of this, @staticmethod might help organize your code by being overridable by subclasses. 
Without it you'd have variants of the function floating around in the module namespace.


 static methods are an organization/stylistic feature. 
 Sometimes a module have many classes, and some helper functions are logically tied to a a given class and not to the others, 
 so it makes sense not to "pollute" the module with many "free functions", 
 and it is better to use a static method than relying on the poor style of mixing classes and function defs 
 together in code just to show they are "related"

'''