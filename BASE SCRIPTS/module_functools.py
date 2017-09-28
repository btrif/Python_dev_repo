import functools, operator

print(' ----- functools.reduce with operator.mu ------------')


a = functools.reduce(operator.mul, [2, 3, 4 ,5] , 1 )
print('reduce and operator.mul, third argument is the multiplicative :', a)

b = functools.reduce(operator.mul, [2, 3, 4 ,5] , 2 )
print('reduce and operator.mul, third argument is 2x :', b)

# Third argument @ reduce makes sure that event empty lists are considered:
c = functools.reduce(operator.mul, [] , 1 )
print('reduce and operator.mul, on an empy list :', c)



print('\n-----------------------------------')

print(help(functools))
print('\n-----------------------------------')


print(dir(functools))

#################   fractiions ################

import fractions

print(help(fractions))
print('\n-----------------------------------')

print(dir(fractions))


