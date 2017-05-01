

print('\n------------------ ONE ARGUMENT ----------------------')

def memoize(f):
    memo = {}
    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]
    return helper

@memoize
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print(fib(40))

class Memoize:
    def __init__(self, fn):
        self.fn = fn
        self.memo = {}
    def __call__(self, *args):
        if args not in self.memo:
	        self.memo[args] = self.fn(*args)
        return self.memo[args]

#########################################

# With apologies to a certain European brand of beer, this is probably the fastest memoization decorator in the world.
# Implemented using the __missing__ method in a dict subclass.

def memodict(f):
    """ Memoization decorator for a function taking a single argument """
    class memodict(dict):
        def __missing__(self, key):
            ret = self[key] = f(key)
            return ret
    return memodict().__getitem__


# Memoization is the canonical example for Python decorators.
# For a single argument function this is probably the fastest possible implementation - a cache hit case does not introduce
# any extra python function call overhead on top of the dictionary lookup.
# If you need access to the underlying dictionary for any reason use f.__self__


print('\n------------------ TWO ARGUMENTS ----------------------')

# This can made [a lot] more useful by generalizing it to handle functions taking one or more arguments without taking a big performance hit.
# I've also made the decorator function's name something clearer as well as less implementation revealing.

def memoize(f):
    """ Memoization decorator for functions taking one or more arguments. """
    class memodict(dict):
        def __init__(self, f):
            self.f = f
        def __call__(self, *args):
            return self[args]
        def __missing__(self, key):
            ret = self[key] = self.f(*key)
            return ret
    return memodict(f)

@memoize
def foo(a, b):
    return a * b

print (foo(4, 2) )
print (foo)
print (foo('xo', 3) )
print (foo)

# The whole point of my recipe is to avoid the overhead of an additional python function call (the __call__ wrapper).
# Time it. Your version is probably not much faster than the "classic" memo decorator
#
# The trick to writing high performance python code is to do the critical part with no python function calls in the inner loop.
# They are expensive.
# This memozation decorator can help optimize such inner loops - a cache hit is as fast as a simple dictionary lookup.
# If you really need a multiple argument function call it with a tuple.


# Here's a slightly shorter version of a multi-argument function memoizing decorator:

def memoize(f):
    """ Memoization decorator for a function taking one or more arguments. """
    class memodict(dict):
        def __getitem__(self, *key):
            return dict.__getitem__(self, key)

        def __missing__(self, key):
            ret = self[key] = f(*key)
            return ret

    return memodict().__getitem__

# It still incurs the overhead of an additional function call and, for a single argument function, is slower than the original recipe.
# To quantify the cost of this additional overhead I compared applying each decorator to the following highly recursive
# Fibonacci number function:

def fib(n):
    return n if n < 2 else fib0(n-1) + fib0(n-2)

# The results for a very large number of repetitions were that the original decorator made calling the function
# almost 136,000 times faster verses only 93,000 times faster for my modified version, meaning the latter was about 1.5 times slower.
# In some other test cases I ran with a smaller number of repetitions, it was about 2.3 times slower.
#
# I couldn't do a comparison for decorating a function with more than one argument because the original decorator
# doesn't support it. Also, the results for a single-argument function would likely be different had it been done using
# a test function that was compute-bound rather than function-call bound.


# These type of micro-optimizations are silly.
# But since you're making claims ... your decorator does two unnecessary dict lookups on cache misses,
# costs of which vary by python version..

def memoize(f):
  class memodict(dict):
      __slots__ = ()
      def __missing__(self, key):
          self[key] = ret = f(key)
          return ret
  return memodict().__getitem__