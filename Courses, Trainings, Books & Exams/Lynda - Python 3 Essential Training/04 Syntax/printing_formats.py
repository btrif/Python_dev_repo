x = 10 * 3.25
y = 200 * 200
s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
print(s)
print('_____'*10)
'''There is another method, str.zfill(), 
which pads a numeric string on the left with zeros. 
It understands about plus and minus signs:'''
# The argument to repr() may be any Python object:
print(repr((x, y, ('spam', 'eggs'))))           # in python console:  repr((x, y, ('spam', 'eggs')))
print('_____'*10)

for x in range(1, 11):          # The Python 3. way
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
    # Note use of 'end' on previous line
    print(repr(x*x*x).rjust(4))
print('_____'*10)

for x in range(1, 11):          # The Python 2. OLD way
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

print('_____'*10)

'''There is another method, str.zfill(), which pads a numeric string on the left with zeros. 
It understands about plus and minus signs:'''
print('12'.zfill(5))                 # in python console :'12'.zfill(5)
print('-3.14'.zfill(7))              # '-3.14'.zfill(7)
print('3.14159265359'.zfill(5))        #'3.14159265359'.zfill(5)
print('_____'*10)

'''Basic usage of the str.format() method looks like this: '''
print('We are the {} who say "{}!"'.format('knights', 'Ni'))
print('_____'*10)

'''The brackets and characters within them (called format fields) 
are replaced with the objects passed into the str.format() method. 
A number in the brackets can be used to refer to the position 
of the object passed into the str.format() method.'''
print('{0} and {1}'.format('spam', 'eggs'))
print('{1} and {0}'.format('spam', 'eggs'))
print('_____'*10)

'''If keyword arguments are used in the str.format() method,
their values are referred to by using the name of the argument.'''
print('This {food} is {adjective}.'.format(
        food='spam', adjective='absolutely horrible'))
print('_____'*10)

'''Positional and keyword arguments can be arbitrarily combined:''' 
print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred',other='Georg'))
print('_____'*10)

''''!a' (apply ascii()), '!s' (apply str()) and '!r' (apply repr()) 
can be used to convert the value before it is formatted:'''
import math
print('The value of PI is approximately {}.'.format(math.pi))
print('The value of PI is approximately {!r}.'.format(math.pi))
print('_____'*10)

'''An optional ':' and format specifier can follow the field name. 
This allows greater control over how the value is formatted.
The following example rounds Pi to three places after the decimal.'''
print('The value of PI is approximately {0:.48f}.'.format(math.pi))
print('_____'*10)

'''Passing an integer after the ':' will cause that field to be a minimum number of characters wide. 
This is useful for making tables pretty.'''
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}        # it is a dictionary
for name, phone in table.items():
    print('{0:10} ==> {1:10d}'.format(name, phone))
print('_____'*10)    
    
'''If you have a really long format string that you don't want to split up, 
it would be nice if you could reference the variables to be formatted by name instead of by position. 
This can be done by simply passing the dict and using square brackets [] to access the keys'''

print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
            'Dcab: {0[Dcab]:d}'.format(table))

print('_____'*10) 
'''This could also be done by passing the table as keyword arguments with the '**' notation.'''
print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))
