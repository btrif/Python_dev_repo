__author__ = 'trifb'

# List the values from a Dictionary
d = {'one': 1, 'two':2, 'three':3, 'four':4, 'five':5}
for k in d:
    print(k, d[k], end = ' ;  ')

print('\nPrint (Reference) only a value from the dictionary :  ',d['three'])

#	DICTIONARY 	(MUTABLE)       , KEYS are Immutable because are based on hashes and to be able to keep track of the values

# Define an empty dictionary
girls = {}

#### If Clause Check if an element in the dictionary has values :
print('\n-------------  If Clause Check if an element in the dictionary has values :   ------------------ ')
D={ 3:[], 5:[5] }
if D[5] : print('yes')
else : print('no')
if D[3] : print('yes')
else : print('no')


#  Make a CLONE to a dictionary :
print('\n--------------------Make a CLONE to a dictionary :-----------------------------')
d_clone = d.copy()
for k, v in d_clone.items() : print(k,v, end=' ;  ')

print('\n----------------------Listing & Printing--------------------------')
#Add a couple of names to the dictionary
girls['Gianina'] = 23
girls['Rebeca'] = 19
girls['Pamela'] = 78
girls['Denise'] = 45

#   Get the type of the the girls object
print('Print the type of the object: ', type(girls))
print('Print only Keys: ', girls.keys())
print('Print only Values: ', girls.values())
print('Print the entire Dictionary: \n', girls.items())
print('---'*15)

#	Modify a key:
print('\nModify a key:')
girls['Denise'] = 10
print('The new dictionary is now: \n' ,girls)

# Delete, Remove a key from Dictionary without generating Error:
my_dict = {'13': [5], '76': [4], '77': [9]}
if 'Denise' in my_dict:    del girls['88']

# This will return my_dict[key] if key exists in the dictionary, and None otherwise.
# If the second parameter is not specified (ie. my_dict.pop('key')) and key does not exist, a KeyError is raised.

my_dict.pop('key', None)        # The MOST EFFICIENT WAY

# You should consider, though, that this way of deleting an object from a dict is not atomic—
# it is possible that 'key' may be in myDict during the if statement, but may be deleted before del is executed,
# in which case del will fail with a KeyError.
# Given this, it would be safest to either use  dict.pop or something along the lines of
try:    del my_dict['key']
except KeyError:   pass



# List Only the keys
print('\n------------# List Only the keys -------------------')
print(list(girls.keys()))
print('\n------------# List Only the keys -------------------')
for k in  list(girls.keys()): print(k,type(k) ,end=' ')

print('\n----------------- Interogate about an item or a value---------------------')
# Interogate about an item:  This is the "safe" way to access a value if we are not sure the key is in the dictionary.
print('\nInterogate about an item:')
print(girls.get('Bogdan', 0), ', the item is not on the list')
print(girls.get('Denise', 0))
print(girls.get('Pamela') == None)

# To avoid this, we can use the call hand.get('a',0). This is the "safe" way to access a value if we are not sure the key is in the dictionary.

# Interogate about a value :
print('\n Interogate about a value :' , list(girls.keys())[list(girls.values()).index(78)] )



# Reverse the Dictionary , keys become values :
print('\n-------------  Reverse the Dictionary , keys become values : ----------------------')
new_girls = dict(zip(girls.values(),girls.keys()))
print(new_girls)
print(new_girls[19])

# Length, Count the number of elements
print('\nLength (size, count elements) of the dictionary: ', len(girls))
print('Print the list with ordered (sorted ) names: ', sorted(girls))

print('\nGet elements using a for loop:')
for k, v in girls.items():
    print(k, v)

print('---'*10,'   Define a second dictionary','---'*10)
boys = {'Andrei' : 33, 'Marius' : 12, 'Bogdan' : 2, 'Viorel' : 13, 'Ionut' : 4, 'Dan' : 18}
print('the boys dictionary is: ', boys)
print('---'*15)

#Update the first dictionary with the second one, this joins  the girls dictionary with the boys dictionary:
girls.update(boys)
print('The new dictionary containing GIRLS & BOYS is :     ',girls)



print('---'*15,'  Dictionary Comprehension  ','---'*15)

#Python 2.7+ introduces Dictionary Comprehension. Building the dictionary from the list will get you the count as well as get rid of duplicates.
a = [1,1,1,1,2,2,2,2,3,3,4,5,5]
d = {x : a.count(x) for x in a}
print(d)
a, b = d.keys(), d.values()
print(a , b)

print('\n------------------Return the Key with the Largest / Smallest Value--------------------------')

stats = {'a':1000, 'b':3000, 'c': 100}
# There are two ways
print(max(stats, key=stats.get))
print(min(d, key=lambda k: d[k]))

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.
    returns: The key with the largest number of values associated with it
    '''
    big=0
    for k, v in aDict.items() :
        if big <  len(v):
            big, key = len(v), k
            #print(big, len(v), key, k)
    return (key, len(v))
animals = {'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati'], 'd': ['donkey', 'dog', 'dingo']}
print(biggest(animals))

print('\n------------------Return the largest (max) Key --------------------------')
Tracker = { 2 : 4, 3 : 2 , 5: 2 }
print('Maximum value of the key in a dict :', max(Tracker, key=int) )


print('\n--------------Pb060 Euler, Nice function to store sorted nrs as key with lists as values ------------------------------')

def cubic_permutations():
        '''Uses a dictionary to store sorted numbers as keys and lists as values '''
        from itertools import count
        d = {}
        for i in count():
            cube = i**3
            signature = ''.join(sorted(str(cube)))
            if signature in d:
                d[signature].append(cube)
                #print(d[signature])
                if len(d[signature]) == 3:
                    print(d[signature][0])
                    break
            else :
                d[signature] = [cube]       # Here we add a list value to each key of the dictionary, Nice idea !

cubic_permutations()

print('\n--------------PB155 - Counting Capacitors circuits - Dictionary Flatten ------------------------------------')
print('-----This procedure it shows how to flatten a dictionary containing lists : ----------------')

D = {1: [60], 2: [30.0, 120], 3: [20.0, 40.0, 90.0, 180], 4: [15.0, 24.0, 36.0, 45.0, 60.0, 80.0, 100.0, 150.0, 240]}

# Method I
print(sorted({x for v in D.values() for x in v}))

# Method II
from itertools import chain
print(sorted(set(chain.from_iterable(D.values()))))

 # Method III
from functools import reduce
print( list(reduce(lambda a, b: a.union(set(b)), D.values(), set())) )


print('\n--------Convert , map, zip two lists into a dictionary -------------')
keys = ['a', 'b', 'c']
values = [1, 2, 3]
# Method II - Using dict
dictionary = dict(zip(keys, values))
print (dictionary)
# Method II - Using List Comprehension
print({k: v for k, v in zip(keys, values)})
# Method III - Using itertools
import itertools
print(dict(itertools.zip_longest(keys,values)))

print('\n--------dictionary setdefault() Method, equivalent to get Method -------------')
# This method returns the key value available in the dictionary and if given key is not available then it will return provided default value.
#!/usr/bin/python
dict = {'Name': 'Zara', 'Age': 7}
print ("Value : %s" %  dict.setdefault('Age', None))
print ("Value : %s" %  dict.setdefault('Sex', None))
# It is equivalent to the get Metod :
print('Value :', dict.get('Sex'))

print('\n-------------- Sort, Arrange a Dictionary after the keys / values ---------------')
print('-------------- Sort, after values ---------------')
# METHOD I
import operator
x = {1: 1, 2: 2, 3: 3, 4: 2, 5: 5, 6: 6, 7: 7, 8: 2, 9: 3, 10: 10}
sorted_x = sorted( x.items(), key=operator.itemgetter(1) )
print('Method I - Sort after the VALUES :' ,sorted_x)

# METHOD II -   not what I want at this moment
print('Method II - Sort after the VALUES :' ,sorted(x, key=x.get))

print('-------------- Sort, after keys ---------------')

# METHOD I -
x = {1: 1, 42: 2, 13: 3, 14: 2, 117: 5, 16: 6, 27: 7, 17: 2, 39: 3, 11: 10}
sorted_y = sorted(x.items(), key=operator.itemgetter(0))
print('Method I - Sort after the KEYS :' ,sorted_y)

print('\n-------------- Check if a key is in dictionary ---------------')
dd = {}
for i in range(100):
    key = i % 10
    if key in dd:
        dd[key] += 1
    else:
        dd[key] = 1
print(dd)

print('\n ----------------- Dictionary comprehensions -------------------')

m = {x: x ** 2 for x in range(5)}
print( m )

print('-------- VERY USEFUL to use to GENERATE VARIABLES DYNAMICALLY ------------- ')
m = {x: 'A' + str(x) for x in range(10)}
print( m )

print('\n ----------------- Inverting a dictionary using a dictionary comprehension -------------------')
m = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(m)
print( {v: k for k, v in m.items()} )

print('\n---------- Build Dictionary within dictionary -------------------')
D = { x : { y: 0 for y in range(10)}  for x in range(10)}

print('\n----------  Print only a range of values from a Dictionary -------------- ')
SQD = {x*x: x for x in range(1000) }
print('This prints only the k,v fro the dictionary if the values are < 100 :')
print( 'Length : ',len(SQD) , '\n', { k:v for k,v in SQD.items() if v<100 } )
