#!/usr/bin/python3
# Solved by Bogdan Trif @ Completed on Tue, 20 Sep 2016, 00:08
#The  Euler Project  https://projecteuler.net
        '''Largest product in a grid        -       Problem 11

In the 20×20 grid below, four numbers along a diagonal line have been marked in red.

08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48

The product of these numbers is 26 × 63 × 78 × 14 = 1788696.
What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20×20 grid?
'''
import numpy as np

my_string='\
08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08\
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00\
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65\
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91\
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80\
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50\
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70\
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21\
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72\
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95\
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92\
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57\
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58\
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40\
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66\
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69\
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36\
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16\
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54\
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48'

import time

print('----------------MY FIRST METHOD, PRIMITIVE  :) -------------------------')
grid=[]
super_grid=[]
print('------------   String manipulation : ---------------')

print(len(my_string),' ;  First Line of the my string :',my_string[0:59])
#new=my_string.replace(" ", " ")
new = my_string[0:59]
print('Verifying   list :  ',new)

print('------------    Check to Convert a single of the string into ints : -------------- ')
for x in range(0, len(new),3):
    f = new[x:x+3]
    print(int(f), end = ' ')

print('\n','---------'*20)

for c in range(0, len(my_string),59):
    tmp = my_string[c:c+59]
    arr=[]
    #print(my_string[c:c+59],type(my_string[c:c+59]))
    for x in range(0, len(tmp),3):
        f = tmp[x:x+3]
        #print(int(f), end = ' ')
        arr.append(int(f))
    grid.append(arr)
    tmp=[]

print('\nGRID:   ','Length  : ',len(grid) ,' \n','Last element : ' , grid[-1],'\n'*2)

for b in range(len(grid)):
    print(grid[b])#, '   -->       Length:  ',len(grid[b]))


#print(type(grid),grid)
print('\n The first column of the grid : ',[row[0] for row in grid])

print('#########     START HERE    #############')
t1 = time.time()

print('\n---------HORIZONTAL-----------')

# HORIZONTAL, it works
HORIZ=[]
counter=0
for i in range(len(grid)):
    H=[]
    #print('----'*15)
    for j in range(len(grid[i])-3):
        counter +=1
        H=grid[i][j:j+4]
        #print(str(counter)+'.   ',H, '  ; Prod : ',np.prod(H))
        HORIZ.append(np.prod(H))

print('\nOnly as a test :   ',len(HORIZ), '   ;  ',H , '  ;  Product :', np.prod(H), '  ;  Max number : ', max(H))
print('\nMaximum number in HORIZ : ', max(HORIZ),'-------------This works fine !  --------------------\n')
super_grid.append(max(HORIZ))


print('\n---------VERTICAL-----------')
# VERTICAL MATRIX,  it works
VERT=[]
counter=0
for i in range(len(grid)):
    V=[]
    #print('----'*15)
    for j in range(len(grid[i])-3):
        counter +=1
        V=[row[i] for row in grid[j:j+4]]
        #print(str(counter)+'.   ',V, '  ; Prod : ',np.prod(V))
        VERT.append(np.prod(V))


print('\nOnly as a test :   ',len(VERT), '   ;  ',V , '  ;  Product :', np.prod(V), '  ;  Max number : ', max(V))
print('\nMaximum number in VERT : ', max(VERT),'-------------This works fine !  --------------------\n')
super_grid.append(max(VERT))

print('------------------  RIGHT DIAGONAL COMPUTATION : --------------------')

def get_diagP(m, i0, j0, d):     #m - matrix ;  i0 - start row  ; j0 - start column ;   d - directions
    return [m[(i0 + i - 20)%len(m)][(j0 + d*i - 20)%len(m[0])] for i in range(4)]

diagD=[]
counter=0
for x in range(len(grid)-3):
    for y in range(len(grid)-3):
        counter +=1
        D =  get_diagP(grid, x, y, 1)
        #print (str(counter)+'.   ',D, '  ; Prod : ',np.prod(D))
        diagD.append(np.prod(D))

print('\nOnly as a test :   ',len(diagD), '   ;  ',D , '  ;  Product :', np.prod(D), '  ;  Max number : ', max(D))
print('\nMaximum number in DiagD : ',max(diagD),'-------------This works fine !  --------------------\n')
super_grid.append(max(diagD))

print('------------------  LEFT DIAGONAL COMPUTATION : --------------------')

def get_diagS(m, i0, j0, d):     #m - matrix ;  i0 - start row  ; j0 - start column ;   d - directions
    return [m[(i0 + i - 20)%len(m)][(j0 + d*i - 20)%len(m[0])] for i in range(4)]

diagR=[]
counter=0
for x in range(len(grid)-3):
    #print('----'*15)
    for y in range(len(grid)-1,2,-1):
        counter +=1
        E =  get_diagS(grid, x, y, -1)
        #print (str(counter)+'.   ',E, '  ; Prod : ',np.prod(E))
        diagR.append(np.prod(E))

print('\nOnly as a test :   ',len(diagR), '   ;  ',E , '  ;  Product :', np.prod(E), '  ;  Max number : ', max(E))
print('\nMaximum number in diagR : ',max(diagR),np.max(diagR), '   ;   Index :',np.argmax(diagR),'-------------This works fine !  --------------------\n')
super_grid.append(max(diagR))

print(super_grid, '   ;    Maximum is :', max(super_grid),' <-----  This is the number you were looking for  !!!!!!!!!!\n')
#print('          !!!!         I NEED A BETTER TECHNIQUE FOR MANIPULATING MATRICES     !!!       \n'*100)

t2  = time.time()
print('\nCompleted in :', round((t2-t1),3), 's')

print('\n=============FORUM SOLUTIONS ==================')
print('\n-----------------SOLUTION 1, VERY ELEGANT SOLUTION--------------')
t1  = time.time()

d={}
m=grid
for i in m:
    for j in range (17):
        pro=i[j]*i[j+1]*i[j+2]*i[j+3]
        terms=str(i[j])+"X"+str(i[j+1])+"X"+str(i[j+2])+"X"+str(i[j+3])
        d[pro]=terms
for i in range (17):
    for j in range (20):
        pro=m[j][i]*m[j][i+1]*m[j][i+2]*m[j][i+3]
        terms=str(m[j][i])+"X"+str(m[j][i+1])+"X"+str(m[j][i+2])+"X"+str(m[j][3])
        d[pro]=terms
for i in range (17):
    for j in range (17):
        pro=m[i][j]*m[i+1][j+1]*m[i+2][j+2]*m[i+3][j+3]
        terms=str(m[i][j])+"X"+str(m[i+1][j+1])+"X"+str(m[i+2][j+2])+"X"+str(m[i+3][j+3])
        d[pro]=terms
for i in range (17):
    for j in range (19,3,-1):
        pro=m[i][j]*m[i+1][j-1]*m[i+2][j-2]*m[i+3][j-3]
        terms=str(m[i][j])+"X"+str(m[i+1][j-1])+"X"+str(m[i+2][j-2])+"X"+str(m[i+3][j-3])
        d[pro]=terms
key=d.keys()
maximum=max(key)
print (d[maximum],":",maximum)
print(d)

t2  = time.time()
print('\nCompleted in :', round((t2-t1),3), 's')

print('\n----------------SOLUTION 2,  ELEGANT BUT STILL MANY LINES OF CODE ---------------------')

grid = []
with open("pb011.txt") as file:
    for line in file:
        numbers_line = list(map(int, (line.strip()).split(" ")))
        grid.append(numbers_line)
grid_size = len(grid)
print(grid)

def greatest_product_vertically(grid):
    max = 0
    for column in range(0, grid_size):
        for row in range(0, grid_size - 3):
            four_numbers = [grid[row + i][column] for i in range(0, 4)]
            four_numbers_product = 1
            for num in four_numbers:
                four_numbers_product *= num
            if four_numbers_product > max:
                max = four_numbers_product
    return max

def greatest_product_horizontally(grid):
    max = 0
    for row in range(0, grid_size):
        for column in range(0, grid_size - 3):
            four_numbers = grid[row][column:(column+4)]
            four_numbers_product = 1
            for num in four_numbers:
                four_numbers_product *= num
            if four_numbers_product > max:
                max = four_numbers_product
    return max

def greatest_product_diagonally(grid):
    def calculate(numbers_grid):
        grid_size = len(numbers_grid)
        max = 0
        for row in range(0, grid_size- 3):
            for column in range(0, grid_size - 3):
                four_numbers = list([numbers_grid[row + i][column + i] for i in range(0, 4)])
                four_numbers_product = 1
                for num in four_numbers:
                    four_numbers_product *= num
                if four_numbers_product > max:
                    max = four_numbers_product
        return max
    grid_mirror_vertical = []
    for row in range(0, grid_size):
        grid_mirror_vertical.append(list(reversed(grid[row])))
    grid_mirror_horisontal = []
    for row in range(0, grid_size):
        grid_mirror_horisontal.append(grid[grid_size - 1 - row])
    grid_mirror_horisontal_vertical = []
    for row in range(0, grid_size):
        new_row = list(reversed(grid[grid_size - 1 - row]))
        grid_mirror_horisontal_vertical.append(new_row)
    max1 = calculate(grid_mirror_vertical)
    max2 = calculate(grid_mirror_horisontal)
    max3 = calculate(grid_mirror_horisontal_vertical)
    return max(max1, max2, max3)

result = max(greatest_product_vertically(grid),
             greatest_product_horizontally(grid),
             greatest_product_diagonally(grid))

print(result)
######################################
print('\n----------------SOLUTION 3,  USING NUMPY  ---------------------')

import numpy

def horizontal_max(grid):
    results = []
    for i in range(grid.shape[1]):
        start = 0
        end = 4
        for n in range(grid.shape[0] - 4):
            adj = 1
            for k in grid[i, :][start:end]:
                adj *= k
            start += 1
            end += 1
            results.append(adj)
    return max(results)


def vertical_max(grid):
    results = []
    for i in range(grid.shape[0]):
        start = 0
        end = 4
        for n in range(grid.shape[1] - 4):
            adj = 1
            for k in grid[:, i][start:end]:
                adj *= k
            start += 1
            end += 1
            results.append(adj)
    return max(results)


def diagonal_left_max(grid):
    results = []
    for i in range(-16, grid.shape[0] + grid.shape[1] - 7):
        start = 0
        end = 4
        diag = grid.diagonal(i)
        for n in range(len(diag) - 3):
            adj = 1
            for k in diag[start:end]:
                adj *= k
            start += 1
            end += 1
            results.append(adj)
    return max(results)


def diagonal_right_max(grid):
    grid = numpy.fliplr(grid)
    results = []
    limit = grid.shape[0] + grid.shape[1] - 7
    for i in range(-16, limit):
        start = 0
        end = 4
        diag = grid.diagonal(i)
        for n in range(len(diag) - 3):
            adj = 1
            for k in diag[start:end]:
                adj *= k
            start += 1
            end += 1
            results.append(adj)
    return max(results)


def grid_max(grid):
    horizontal = horizontal_max(grid)
    vertical = vertical_max(grid)
    diagonal_left = diagonal_left_max(grid)
    diagonal_right = diagonal_right_max(grid)
    results = [horizontal, vertical, diagonal_left, diagonal_right]
    return max(results)


matrix = numpy.loadtxt('pb011.txt')
print(grid_max(matrix))

print('\n----------------SOLUTION 4,  THE MOST  ELEGANT & EFFICIENT , from  Vietnam ---------------------')
t1  = time.time()

f = open('pb011.txt')
gid =[]
while True:
	line = f.readline()
	if len(line)==0:
		break
	row= line.replace('\n','').split(' ')
#	print (row)
	gid.append(row)
#print(gid[2][2])

p =0
for x in range(20):
    for y in range(20):
    #print(x,y)
    #check diagonally line right
        try:
            #print('Ok')
            a, b, c, d =int(gid[x][y]), int(gid[x+1][y+1]), int(gid[x+2][y+2]), int(gid[x+3][y+3])
        except :
            a, b, c, d = 1, 1 ,1 ,1
        tmp=a*b*c*d
        if tmp >p:
            p=tmp
    #check diagonally line left
        try:
            #print("2ok")
            a , b, c, d = int(gid[x][y]), int(gid[x+1][y-1]), int(gid[x+2][y-2]), int(gid[x+3][y-3])
        except:
            a, b, c, d = 1, 1, 1, 1
        tmp = a*b*c*d
        if tmp>p:
            p=tmp
        #check wasd
        try:
            #print("3ok")
            a, b, c, d = int(gid[x][y-1]), int(gid[x][y+1]), int(gid[x-1][y]), int(gid[x+1][y])
        except:
            a, b, c ,d =1, 1, 1, 1
        tmp =a*b*c*d
        if tmp>p:
            p = tmp
f.close()
print(p)

t2  = time.time()
print('\nCompleted in :', round((t2-t1),3), 's')

print('\n---------------- SOLUTION 5, THE BEST SOLUTION :  ELEGANT & EFFICIENT , drtunio  from  Pakistan ---------------------')

# My Python solution  ;   Note: I kept the given number array in a text file named 'grid.txt'
t1  = time.time()

# Open and read the file
f = open('pb011.txt', 'r')
text = f.read()

# Initialize and populate grid
grid = []

for row in text.split('\n'):
    grid.append(list(map(int, row.split(' '))))

maxprod = 0

# Find highest product in rows
for i in range(20):
    for j in range(17):
        prod = grid[i][j]*grid[i][j+1]*grid[i][j+2]*grid[i][j+3]
        if prod > maxprod:
            maxprod = prod

# Find highest product in columns
for j in range(20):
    for i in range(17):
        prod = grid[i][j]*grid[i+1][j]*grid[i+2][j]*grid[i+3][j]
        if prod > maxprod:
            maxprod = prod

# Find highest product in downward-right diagonal
for i in range(17):
    for j in range(17):
        prod = grid[i][j]*grid[i+1][j+1]*grid[i+2][j+2]*grid[i+3][j+3]
        if prod > maxprod:
            maxprod = prod

# Find highest product in upward-right diagonal
for i in range(3,20):
    for j in range(17):
        prod = grid[i][j]*grid[i-1][j+1]*grid[i-2][j+2]*grid[i-3][j+3]
        if prod > maxprod:
            maxprod = prod

print(maxprod)
t2  = time.time()
print('\nCompleted in :', round((t2-t1),3), 's')

print('\n---------------- SOLUTION 6 :  ELEGANT & EFFICIENT   ---------------------')

grid = '08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08\
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00\
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65\
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91\
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80\
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50\
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70\
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21\
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72\
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95\
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92\
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57\
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58\
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40\
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66\
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69\
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36\
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16\
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54\
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48'

T1 = map(lambda x: x.split(' '), grid.split('\n'))
# Split grid by '\n' to make new list, split them by ' ' and map them.
print(T1)

T2 = [[int(colmun) for colmun in row] for row in T1]
# convert each string into integer
print(T2)

def down(x, y):
	return T2[x][y] + T2[x+1][y] + T2[x+2][y] + T2[x+3][y]

def right(x, y):
	return T2[x][y] + T2[x][y+1] + T2[x][y+2] + T2[x][y+3]

def rightdown(x, y):
	return T2[x][y] * T2[x+1][y+1] * T2[x+2][y+2] * T2[x+3][y+3]

def leftdown(x, y):
	return T2[x][y] * T2[x-1][y+1] * T2[x-2][y+2] * T2[x-3][y+3]

sum = -1
for i in range(20):
	for j in range(20):
		if i <= 16 and j <= 16:
			sum = max(sum, down(i, j), rightdown(i, j), right(i, j))
		elif i <= 16:
			# i <= 16 and j > 17
			sum = max(sum, down(i,j))
		elif j <= 16:
			# i > 17 and j <= 16
			sum = max(sum, right(i,j))
		if i >= 3 and j <= 16:
			sum = max(sum, leftdown(i, j))

print(sum)
print('\n---------------- END SOLUTION    ---------------------')

print('\n---------------- SOLUTION 7    ---------------------')

#Simple solution using a transformation to logarithms, and applying a 2D convolution.


import numpy as np
from scipy import signal

#--- Load data
grid = np.loadtxt(open("grid.csv","rb"),delimiter=",")
# log(xy) = log(x) + log(y) -> This transformation is necessary for the convolution
grid = np.log(grid)

#--- Define kernels
v = np.zeros((4,4))
v[:,0] = 1
h = np.zeros((4,4))
h[0,:] = 1
dlr = np.eye(4)
drl = np.fliplr(dlr)


#--- Convolve grid with each kernel and check que maximum, then convert back by
#    doing the exp(max)
grad_v = signal.convolve2d(grid, v, mode='full')
grad_h = signal.convolve2d(grid, h, mode='full')
grad_dlr = signal.convolve2d(grid, dlr, mode='full')
grad_drl = signal.convolve2d(grid, drl, mode='full')

all_grad = np.concatenate((grad_v[:],grad_h[:], grad_dlr[:], grad_drl[:]))

print('Final answer: ' + str(np.exp(np.nanmax(all_grad))))
