
#Very simple and quick way of finding dupes with one iteration in Python is:
testList = ['red', 'blue', 'red', 'green', 'blue', 'blue']

testListDict = {}

for item in testList:
  try:
    testListDict[item] += 1
  except:
    testListDict[item] = 1

print (testListDict)

#A bit late, but maybe helpful for some. For a largish list, I found this worked for me.
l=[1,2,3,5,4,1,3,1]
s=set(l)
d=[]
for x in l:
    if x in s:
        s.remove(x)
    else:
        d.append(x)
print(d)

#
list_a = [1,2,3,2,19,5,6,5,5,19,5,17,19]
import collections
print ([x for x, y in collections.Counter(list_a).items() if y > 1])
print('----'*20)

#In an earlier version you can use a conventional dict instead: !!!!!!!!!!!!!!!!!!!!!!!!!!
dictionary = {}
for elem in list_a:
    if elem in dictionary:
        dictionary[elem] += 1
    else:
        dictionary[elem] = 1

print ([x for x, y in dictionary.items() if y > 1])
print(dictionary)

print('----'*20)
#You don't need the count, just whether or not the item was seen before. Adapted that answer to this problem:
def list_duplicates(seq):
  seen = set()
  seen_add = seen.add
  # adds all elements it doesn't know yet to seen and all other to seen_twice
  seen_twice = set( x for x in seq if x in seen or seen_add(x) )
  # turn the set into a list (as requested)
  return list( seen_twice )

a = [1,2,3,2,1,5,6,8,8,8]
print(list_duplicates(a))