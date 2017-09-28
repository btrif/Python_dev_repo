

for x in range(1, 11):

    print(repr(x).rjust(2), repr(x*x).rjust(3), end=" ")

# Note trailing comma on previous line

    print(repr(x*x*x).rjust(4))
    
print('something', end=' ... ')
print('else')

#####################Python 2 way ########################

'''
for x in range(1, 11):
    print ('{0:2d} {1:3d} {2:4d}'.format(x, x * x, x * x * x))
'''