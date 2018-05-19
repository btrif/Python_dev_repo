
# The following Piece of Code returns correctly for rem(2,5) but doesn't return anything for
# rem(7,5)

def rem(x, a):
    """
    x: a non-negative integer argument
    a: a positive integer argument

    returns: integer, the remainder when x is divided by a.
    """
    if x == a:
        return 0
    elif x < a:
        return x
    else:
        rem(x-a, a)

print(rem(2,5))
print(rem(7, 5))

print('-----------------------FIX -------------------------')
#Remember what the professor said: always look at who's calling the function so you know who to return it to.
# In this case, the recursive rem(x-a,a) is calling the function, using (2, 5) as values.
# When it does the computation it returns the correct answer 2, but who does it return it to?
# It returns it to the line rem(x-a,a) in the original iteration of the function. So you have:
# else:
#        2
# As you can tell, that statement doesn't make much sense, and it won't give us the answer.
# So why does 'return' fix it?
# When you put that 'return' next to rem(x-a,a), the 2 that is returned by the second call of the function
# is then in turn returned out of the original, first call of the function. So it becomes:
# else:
#   return 2
# So you get the correct output out of the original function, and not just the output out of the recursive call which goes nowhere.
# Hope the explanation makes sense.

# My comment(Bogdan) Actually the Recursion Call doesn't return anything. So we need to add return in front

def rem(x, a):
    """
    x: a non-negative integer argument
    a: a positive integer argument

    returns: integer, the remainder when x is divided by a.
    """
    if x == a:
        return 0
    elif x < a:
        return x
    else:
        return rem(x-a, a)

print(rem(7, 5))

# FACTORIAL RECURSION :
print('\n--------------  FACTORIAL RECURSION : -------------------')
def f(n):
   """
   n: integer, n >= 0.
   """
   if n == 0:
      return n
   else:
      return n * f(n-1)

print(f(3), f(1), f(0), f(2), f(6))

'''
When we call f(3) we expect the result 6, but we get 0.
When we call f(1) we expect the result 1, but we get 0.
When we call f(0) we expect the result 1, but we get 0.
'''
print('----------------------FIX------------------------')
def f(n):
   """
   n: integer, n >= 0.
   """
   if n == 0:
      return 1
   else:
      return n * f(n-1)

print(f(3), f(1), f(0), f(2), f(6))
