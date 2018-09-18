#  Created by Bogdan Trif on 16-03-2018 , 1:47 PM.

def extendList(val, list=[] ):
    list.append(val)
    return list

list1 = extendList(10)
list2 = extendList(123, [])
list3 = extendList('a')


print( "list1 = %s" % list1)
print( "list2 = %s" % list2)
print( "list3 = %s" % list3)

''' EXPLANATION : The behaviour may look strange but actually Let's take it step by step :
1. on line 7 : list1 object is created with the value 10. As there is no 2nd argument the default is taken from the 
already filled function argument list=[]
2. On line 8 : list2 is created . There is a second argument as an empty list [] which means that list2 = [123].
We created a new list2 object from scratch.
3. On line 9 : list3 is created and it appends a value of 'a' . There is no second argument so the def is taking what it already has
 and we already have a list = [10] and we add an 'a'. Therefore list3 = [10, 'a'] . But as they reference the same list object =>
 also the list1 = [10, 'a']
 
 Many will mistakenly expect list1 to be equal to [10] and list3 to be equal to ['a'], 
 thinking that the list argument will be set to its default value of [] each time extendList is called.

However, what actually happens is that the new default list is created only once when the function is defined, 
and that same list is then used subsequently whenever extendList is invoked without a list argument being specified. 
This is because expressions in default arguments are calculated when the function is defined, not when it’s called.

list1 and list3 are therefore operating on the same default list, 
whereas list2 is operating on a separate list that it created (by passing its own empty list as the value for the list parameter).

The definition of the extendList function could be modified as follows, though, 
to always begin a new list when no list argument is specified, which is more likely to have been the desired behavior:

def extendList(val, list=None):
  if list is None:
    list = []
  list.append(val)
  return list
 
 
'''