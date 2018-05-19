'''
Problem 7       (20 points possible)
Assume you are given two dictionaries d1 and d2, each with integer keys and integer values.
You are also given a function f, that takes in two integers, performs an unknown operation on them, and returns a value.

Write a function called dict_interdiff that takes in two dictionaries (d1 and d2).
The function will return a tuple of two dictionaries: a dictionary of the intersect of d1 and d2 and
a dictionary of the difference of d1 and d2, calculated as follows:

intersect: The keys to the intersect dictionary are keys that are common in both d1 and d2.
To get the values of the intersect dictionary, look at the common keys in d1 and d2
and apply the function f to these keys' values -- the value of the common key in d1 is the first parameter to the function
and the value of the common key in d2 is the second parameter to the function.
Do not implement f inside your dict_interdiff code -- assume it is defined outside.

difference: a key-value pair in the difference dictionary is (a) every key-value pair in d1 whose key appears only
in d1 and not in d2 or (b) every key-value pair in d2 whose key appears only in d2 and not in d1.
Here are two examples:

If f(a, b) returns a + b
d1 = {1:30, 2:20, 3:30, 5:80}
d2 = {1:40, 2:50, 3:60, 4:70, 6:90}
then dict_interdiff(d1, d2) returns ({1: 70, 2: 70, 3: 90}, {4: 70, 5: 80, 6: 90})

If f(a, b) returns a > b
d1 = {1:30, 2:20, 3:30}
d2 = {1:40, 2:50, 3:60}
then dict_interdiff(d1, d2) returns ({1: False, 2: False, 3: False}, {})

Paste your entire function, including the definition, in the box below.
The function f will be automatically added to your code, do not paste it in the box. Do not leave any debugging print statements.
Note that we ask you to write a function only -- you cannot rely on
any variables defined outside your function for your code to work correctly.
'''

def dict_interdiff2(d1, d2):

    d1_keys, d2_keys = set(d1.keys()) , set(d2.keys())
    x = d1_keys.intersection(d2_keys)
    d3, d4, d5, d6 = {}, {}, {}, {}
    for i in x:   d3[i] = d1[i]+d2[i]

    diff1, diff2 = d2_keys - d1_keys, d1_keys - d2_keys

    y = {i for j in (diff1,diff2) for i in j}
    for i in y:
        if d1.get(i) != None :    d4[i]  = d1[i]
        elif d2.get(i) != None :    d4[i]  = d2[i]

    tup=(d3,d4)

    for j in d1:
        if d1.get(j) != None and d2.get(j) != None:
            d5[j] = bool(d1[j] > d2[j])

    tup2=(d5, d6)


def dict_interdiff3(d1, d2):
    # symmetric difference, keys in either d1 or d2 but not both.
    sym_diff = d1.viewkeys() ^ d2
    # intersection, keys that are common to both d1 and d2.
    intersect = d1.viewkeys() & d2
    # apply f on values of the keys that common to both dicts.
    a = {k: f(d1[k], d2[k]) for k in intersect}
    b = {k: d1[k] for k in sym_diff & d1.viewkeys()}
    # add key/value pairings from d2 using keys that appear in sym_diff
    b.update({k: d2[k] for k in sym_diff & d2.viewkeys()})
    return a,b

def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    # Your code here
    orderedintersect={}
    ordereddiff={}
    done=d1.copy()
    dtwo=d2.copy()
    for key in done:
        if key in dtwo:
            orderedintersect[key]=f(done[key],dtwo[key])
            del d1[key]
            del d2[key]
    d1.update(d2)
    for i in sorted(d1.keys()):
        ordereddiff[i]=d1[i]

    return orderedintersect, ordereddiff

def f(a,b):
    return a+b



d1 = {1:30, 2:20, 3:30, 5:80}
d2 = {1:40, 2:50, 3:60, 4:70, 6:90}

dict_interdiff(d1,d2)

#######################################################
print('-----'*25)

print(d1)
print(d2)

d1_keys, d2_keys = set(d1.keys()) , set(d2.keys())
a=d1_keys.intersection(d2_keys) ; print(a)
d3={}
for i in a:   d3[i] = d1[i]+d2[i]
print(d3)
# d4={}
#      This Works too :     for i in a:  d4.update( {i:d1[i]+d2[i]})
# print(d4)

d4={}
diff1, diff2 = d2_keys - d1_keys, d1_keys - d2_keys

b = {i for j in (diff1,diff2) for i in j}       ;   print(b)
for i in b:
    if d1.get(i) != None :    d4[i]  = d1[i]
    elif d2.get(i) != None :    d4[i]  = d2[i]
print(d4)
#print(d1.get(1) != None)
tup=(d3,d4) ;   print(tup)

d5={}
for j in d1:
    #print(j)
    if d1.get(j) != None and d2.get(j) != None:
            d5[j] = bool(d1[j] > d2[j])

print(d5)
d6={}
tup2=(d5, d6)
print(tup2)
d1_keys.union(d2_keys)