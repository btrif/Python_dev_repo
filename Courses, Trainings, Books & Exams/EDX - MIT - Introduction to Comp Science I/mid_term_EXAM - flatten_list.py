'''
Problem 9    (15 points possible)
Write a function to flatten a list. The list contains other lists, strings, or ints.
For example, [[1,'a',['cat'],2],[[[3]],'dog'],4,5] is flattened into [1,'a','cat',2,3,'dog',4,5]
Hint: How to think about this problem

Recursion is extremely useful for this question.
You will have to try to flatten every element of the original list.
To check whether an element can be flattened, the element must be another object of type list.
'''

def flatten(aList):
	return sum( ([x] if not isinstance(x, list) else flatten(x)
		     for x in aList), [] )

aList = [[180.0, 1, 2, 3], [173.8], [164.2], [156.5,[45,12,[81,41,[2,3,8],4,11]]], [147.2], [138.2]]

flatten(aList)
print(flatten(aList))
