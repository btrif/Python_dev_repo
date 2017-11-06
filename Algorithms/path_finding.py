# dynamic programming.
print(' ---------------DYNAMIC PROGRAMMING, Backwards Induction------------------ ')

triangle=[[75],
              [95, 64],
              [17, 47, 82],
              [18, 35, 87, 10],
              [20, 4, 82, 47, 65],
              [19, 1, 23, 75, 3, 34],
              [88, 2, 77, 73, 7, 63, 67],
              [99, 65, 4, 28, 6, 16, 70, 92],
              [41, 41, 26, 56, 83, 40, 80, 70, 33],
              [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
              [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
              [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
              [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
              [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
              [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]]

for i in range(len(triangle)-2,-1,-1):
    for j in range(0,i+1):
        triangle[i][j]+=max(triangle[i+1][j],triangle[i+1][j+1])


print ('And the solution is :   ',triangle[0][0])

for i in triangle:    print(i)

'''

print('\n with testing prints keeping track ...')
a=[[75], [95, 64], [17, 47, 82], [18, 35, 87, 10], [20, 4, 82, 47, 65], [19, 1, 23, 75, 3, 34], [88, 2, 77, 73, 7, 63, 67], [99, 65, 4, 28, 6, 16, 70, 92], [41, 41, 26, 56, 83, 40, 80, 70, 33], [41, 48, 72, 33, 47, 32, 37, 16, 94, 29], [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14], [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57], [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48], [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31], [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]]

for i in range(len(a)-2,-1,-1):
        for j in range(0,i+1):
                print('\nPrevious-----',a[i+1])
                print('Next-----',a[i])
                print(a[i+1][j], ', ',a[i+1][j+1] ,' ;  Max:', max(a[i+1][j] , a[i+1][j+1]), end = '  -next->   ')
                a[i][j] += max(a[i+1][j] , a[i+1][j+1])
                print(a[i][j],  end = '     ### \n')
                print('Next----',a[i])
        #print('Chosen: ')
        print('=='*20)

print ('\nThe SOLUTION  :',a[0][0])
for j in a:    print(j)
#for i in a:    print(i)
'''

############################################
print('\n\n-------------------  BACKWARDS INDUCTION  -----------------')

filePath = r'pb018.txt'
data = [(line.rstrip('\n')).split(' ') for line in open(filePath)]

for i,line in enumerate(data):
    data[i] = [int(num) for num in line]

numRows = len(data)
for rowIndex in range(numRows-2,-1,-1): #start at second to last row
    for node,entry in enumerate(data[rowIndex]):
        data[rowIndex][node] = (entry
                                + max (data[rowIndex+1][node],data[rowIndex+1][node+1]))

print ('max path length='+ str(data[0][0]))


print('------'*20)


# read from file the triangle of values

'''
Similar to many others on this thread, I concluded that the most effective algorithm was to start on the second
to the lowest row and add that value to the maximum of the two values below it as the new value of that square.
Deleting the bottom row after all of the useful information has been extracted from it allows for linear time in dealing with this problem.
'''





