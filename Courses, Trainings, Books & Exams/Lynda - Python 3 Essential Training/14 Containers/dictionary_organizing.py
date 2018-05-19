# Dictionaries are hashed arrays, associative Array s
# Dictionaries have the advantage that indexes are data, text, words ...
# Allowing you to create your own workspace

d= {'one' : 1, 'two' :2, 'three' : 3}
print (d)

# Making a dictionary Using constructor method of python
d2 = dict(eleven =11, twelve = 12, thirteen = 13)
print(d2)
print(type(d2))

d3 = dict(twenty = 20, thirty = 30, forty = 40)
print(d3)

d = dict(eighteen = 18 , **d2)
print(d)

# Testing for a value in dictionary:
print('four' in d2, 'forty' in d3)

#Printing items:
print(d.items())

for k,v in d.items():
    print(k, v)
   # Getting the values :  
print(d.get('twelve'))
print(d.get('three'), 'Not fount in here!')

# Remove items:
d.pop('eleven')
print(d)
