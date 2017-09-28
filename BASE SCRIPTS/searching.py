# ### Python: Searching for a string within a list – List comprehension
# The simple way to search for a string in a list is just to use ‘if string in list’. eg:


list=['a cat','a dog','a yacht']
string='a cat'
if string in list:
    print ('found a cat!')

# But what if you need to search for just ‘cat’ or some other regular expression and return a list of the list
# items that match, or a list of selected parts of list items that match.
# Then you need list comprehension.


import re
list=['a cat','a dog','a yacht','cats']
regex=re.compile(".*(cat).*")
print([m.group(0) for l in list for m in [regex.search(l)] if m])




print([m.group(1) for l in list for m in [regex.search(l)] if m])

# Lets work through that. Firstly we’re going to use the regular expression library so we import that. re.compile
# lets us create a regular expression that we can later use for search and matching.
#
# Now lets look at a simpler comprehension line:


print([m for l in list for m in [regex.search(l)]])

# This is creating a list of the results of running regex.search() on each item in l.
# Next we want to exclude the None values. So we use an if statement to only include the not None values:


print([m for l in list for m in [regex.search(l)] if m ])

# Lastly rather than returning just a list of the m’s, which are RE match objects, we get the information we want from them.


print([m.group(0) for l in list for m in [regex.search(l)] if m])


print([m.group(1) for l in list for m in [regex.search(l)] if m])