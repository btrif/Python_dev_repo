'''
he initial expression in a list comprehension can be any arbitrary expression, 
including another list comprehension.
Consider the following example of a 3x4 matrix implemented as a list of 3 lists of length 4:
'''
matrix = [
[1, 2, 3, 4],
[5, 6, 7, 8],
[9, 10, 11, 12],
]
print('The Starting matrix : \n',matrix)

''' The following list comprehension will transpose rows and columns: '''
transpose = [[row[i] for row in matrix] for i in range(4)]
print('Transpose matrix with List comprehension method(single line): \n',transpose)

''' As we saw in the previous section, the nested listcomp is evaluated
 in the context of the for that follows it, so this example is equivalent to: '''

transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
print('Transposed matrix with For loop with append method: \n',transposed)

''' which, in turn, is the same as: '''

transposed = []
for i in range(4):
# the following 3 lines implement the nested listcomp
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)
print('Transposed matrix with Double for loop in transposed: \n',transposed)

'''In the real world, you should prefer built-in functions to complex flow statements.
 The zip() function would do a great job for this use case: '''

a = list(zip(*matrix))
print('Transposed matrix with The list zip method:\n',a) 

 