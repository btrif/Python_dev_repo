import operator

# My answer is a little late, but I hope that maybe it will be helpful for the future.
# Yes, you are right. The problem with the translation from Python 2 --> Python 3
# is the fact that lambdas in Python 3 do not accept tuples as arguments.
# However, there is a solution and this is done by having the expected sequence
# argument bound to a single parameter and then indexing on that parameter :

# lambda (i,x):i-x
# will become :

# lambda x: x[1]-x[0]
# Therefore, the code which works in Python 3 will be :

from operator import itemgetter
import itertools
# Find runs of consecutive numbers using groupby.  The key to the solution
# is differencing with a range so that consecutive numbers all appear in
# same group.
L = [ 1,  4,5,6, 10, 15,16,17,18, 22, 25,26,27,28]
for k, g in itertools.groupby( enumerate(L), lambda x: x[1]-x[0] ) :
  print (list(map(itemgetter(1), g)))


print('\n',help(operator))
print('-----------------------------------')

print(dir(operator))


import os


print(help(os))
print('-----------------------------------')

print(dir(os))

