#!/usr/bin/python3
# Solved by Bogdan Trif @
#The  Euler Project  https://projecteuler.net
'''
                            Su Doku     -   Problem 96
Su Doku (Japanese meaning number place) is the name given to a popular puzzle concept.
Its origin is unclear, but credit must be attributed to Leonhard Euler who invented a similar,
and much more difficult, puzzle idea called Latin Squares. The objective of Su Doku puzzles, however,
is to replace the blanks (or zeros) in a 9 by 9 grid in such that each row, column,
and 3 by 3 box contains each of the digits 1 to 9.
Below is an example of a typical starting puzzle grid and its solution grid.

                +-----------------------+         +-----------------------+
                   | 0 0 3 | 0 2 0 | 6 0 0 |         | 4 8 3 | 9 2 1 | 6 5 7 |
                   | 9 0 0 | 3 0 5 | 0 0 1 |         | 9 6 7 | 3 4 5 | 8 2 1 |
                   | 0 0 1 | 8 0 6 | 4 0 0 |         | 2 5 1 | 8 7 6 | 4 9 3 |
                   |-------+-------+-------|         |-------+-------+-------|
                   | 0 0 8 | 1 0 2 | 9 0 0 |         | 5 4 8 | 1 3 2 | 9 7 6 |
                   | 7 0 0 | 0 0 0 | 0 0 8 |         | 7 2 9 | 5 6 4 | 1 3 8 |
                   | 0 0 6 | 7 0 8 | 2 0 0 |         | 1 3 6 | 7 9 8 | 2 4 5 |
                   |-------+-------+-------|         |-------+-------+-------|
                   | 0 0 2 | 6 0 9 | 5 0 0 |         | 3 7 2 | 6 8 9 | 5 1 4 |
                   | 8 0 0 | 2 0 3 | 0 0 9 |         | 8 1 4 | 2 5 3 | 7 6 9 |
                   | 0 0 5 | 0 1 0 | 3 0 0 |         | 6 9 5 | 4 1 7 | 3 8 2 |
                   +-----------------------+         +-----------------------+

A well constructed Su Doku puzzle has a unique solution and can be solved by logic,
although it may be necessary to employ "guess and test" methods in order to eliminate options
(there is much contested opinion over this). The complexity of the search determines the difficulty of the puzzle;
the example above is considered easy because it can be solved by straight forward direct deduction.

The 6K text file, sudoku.txt (right click and 'Save Link/Target As...'), contains fifty different Su Doku puzzles
ranging in difficulty, but all with unique solutions (the first puzzle in the file is the example above).

By solving all fifty puzzles find the sum of the 3-digit numbers found in the top left corner of each solution grid;
for example, 483 is the 3-digit number found in the top left corner of the solution grid above.
'''
# Generate a 9x9 Matrix
from macpath import split
from copy import copy, deepcopy
from itertools import count
from numpy import transpose
import hashlib, time

#  ::::::::::::::::::::::::::::::         DIFFERENT METHODS TO LOAD A FILE          ::::::::::::::::::::::::::::::  #

# filename = "pb096_test_matrix.txt"
filename = "pb096_sudoku.txt"

def load_file_1(filename):
    M=[]
    with open(filename) as f:
        M = [list(map(int, line.rstrip('\n') )) for line in f.readlines()]
    return M

def load_file_2(filename):
    M=[]
    with open(filename, 'r') as f :
        for line in f :
            # print(line, type(line))
            M.append([ int(i) for i in line.rstrip('\n') ])
    return M

def load_file_3(filename) :

    f = open(filename, 'r')
    text = f.read()
    for row in text.split('\n'):
        if row[0] == 'G' :
            matrix = []
            Mall[row] = matrix
        else :
            matrix.append(list(map(int, row)))
    return matrix

Mall = {}
M = load_file_3(filename)
cnt= 0
for k,v in Mall.items() :
    cnt+=1
    print(str(cnt)+'.    ' , k,'    ' ,v)



def status(M):
    digits = {}
    for i in range(len(M)):
        for j in range(1,10):
            #print(M[i],'  ', j ,M[i].count(j))
            if j in M[i] :
                if j not in digits: digits[j] = 1
                else : digits[j] = digits[j]+1
    return digits

print('Status: ',status(M))

digits = {}
for i in range(len(M)):
    for j in range(1,10):
        #print(M[i],'  ', j ,M[i].count(j))
        if j in M[i] :
            if j not in digits: digits[j] = 1
            else : digits[j] = digits[j]+1


def SubMatrix_3x3(x, y, M ):
    '''Function which cuts a given matrix  in 3x3 SubMatrices. In a 9x9 matrix there will be 9 3x3 matrices called Ninants
     Based on the position coordinate (x,y) returns the corresponding Ninant.
     Note: x, y values go from 1 up. 0 is excluded. Don't confuse with referencing matrix like M[0]
    :returns
    Returns the Ninant where the coordinate (x,y) lies in.    '''
    N =  M[((x-1)//3)*3 : ((x-1)//3)*3+3 ]      # This complicated expression do the work of slicing the list into sub pieces
    return [row[((y-1)//3)*3 : ((y-1)//3)*3+3] for row in N]

def intersection(nr, x, y, M):
    ''':Description:    It checks if a number is on the row, column or 3x3 subMatrix of the indexes x,y. The
        function has been made specifically for Sudoku Matrices.
    :param nr:  is the number to test : 1...9
    :param x:   row index   1...9
    :param y:   column index    1...9
    :param M:   the matrix which is tested, Must be a 9x9 matrix
    :return:    Returns boolean : True if the number already exists, False otherwise
    '''
    if ( nr in M[x-1]  or  nr in  transpose(M)[y-1] ) or \
             ( True  if  True in [ nr in row for row in SubMatrix_3x3(x, y, M) ]  else False )    :
        return True
    else : return False

# print('\n SubMatrix :   ',SubMatrix_3x3(5, 6,M),'\n')
# print( [ 8 in row for row in SubMatrix_3x3(5,6)])
print( True  if  True in [ 7 in row for row in SubMatrix_3x3(1,1,M) ]  else False)        # Nice List Comprehension Construction, @Bogdan Trif


# print(((x-1)//3)*3, ((x-1)//3)*3+3)
# print('Get last 3 columns of a matrix : ',  [row[-3:] for row in M])
print('------------ Intersection Test ----------')

print('\nIntersection Test :      ',intersection(1, 3, 7, M),'\n')
for i in range(1,10):
    print(i ,intersection(i, 3 , 5, M), end='  ')


print('\n---------------------------')

def get_to_fill_status(M):
    ''':Description: Important function which get the *FILL STATUS* of the matrix.
    :param M:   the matrix to be tested
    :return:    a **dictionary** in the following format:
        :key: as the *xy* position in the matrix
        :value: as a list of 9 boolean corresponding to each number.
        E.g. :  '93': [True, True, True, True, True, True, True, False, True] --> 8-th value is *False*
         which means that the number *8* at position *x=9, y=3* CAN BE FILLED
         '98': [False, True, False, True, True, True, False, True, True] => 1,3,7 CAN BE FILLED
     :NOTE:     It depends on the **intersection function** which returns the boolean    '''
    sudoku={}
    for x in range(1,10):
        for y in range(1,10):
            if M[x-1][y-1] == 0 :
                # print('------ Position  ',x, y,'  --------------')
                answer=[]
                sudoku[str(x)+str(y)]=[]
                for n in range(1,10):
                    # print('Nr: ',n , '     x=',x,'  y=',y ,'    ' ,intersection(n, x , y, M) )
                    answer.append(intersection(n, x , y, M))
                    sudoku[str(x)+str(y)].append(intersection(n, x , y, M))
                # print(answer.count(False))
    return sudoku

print('get_to_fill_status Function : ' ,get_to_fill_status(M) ,'\n')


def quench(M):
    SDK = get_to_fill_status(M)
    for k,v in SDK.items() :
        if v.count(True) ==9 :
            return True
    return False

def one_available_spot(M):
    ''':Description:    check if there are positions in the matrix which can be filled **only** with **1**  number
    :return: boolean:   *True* if there are fields with only one possibility to fill a number, otherwise *False*
    :NOTE:  Depends on the function get_to_fill_status    '''
    return 1 in [ h.count(False) for h in  [i for i in get_to_fill_status(M).values()]   ]

def two_available_spots(M):
    ''':Description:    check if there are positions in the matrix which can be filled **only** with **2** numbers
    :return: boolean:   True if there are fields with only one possibility to fill a number, otherwise false
    :NOTE:  Depends on the function get_to_fill_status    '''
    return 2 in [ h.count(False) for h in  [i for i in get_to_fill_status(M).values() ] ]


def no_more_zeros(M):
    '''Returns True if the Matrix is still containing zeros , otherwise False
    '''
    # print('Get 0  non-filled positions : ', [ h.count(0) for h in  [i for i in M]   ]  )
    val = sum([ h.count(0) for h in  [i for i in M] ])
    # val = False in [ i for i in [ val for sublist in get_to_fill_status(M).values() for val in sublist ]  ]
    if val >0 : return False
    else : return True

def get_status(M):
    ''':Description:    Count how many times the  numbers 1-9 have been used.
        If all the numbers have been used returns True, otherwise False.
    :param M:   matrix M
    :return: boolean: True or False
    :NOTE:  Depends on the status function
    '''
    s = status(M).values()
    if  ([i for i in s ].count(9) == 9) == True :
        return True
    else : return False

def validate_final(M):
    ''':Description:    Check if the Matrix has been completed. Check if for every number 1-9
        at every position from (1,1) to (9,9) is a valid choice. The function gives boolean True
        if all the numbers have been filled correctly and thus the sudoku has been solved.
    :param M:   the matrix to test
    :return:    boolean: True or False
    :NOTE:      It depends on the intersection function
    '''
    def All_Positions_Intersection(M):
        V = []
        for x in range(1,10):
            for i in range(1,10):
                for j in range(1,10):
                    V.append( intersection(x, i , j, M) )
        if V.count(True) == 9**3 :  return True
        else : return False
    s = status(M).values()
    if  ([i for i in s ].count(9) == 9) == True and All_Positions_Intersection(M) == True:
        return True
    else : return False

def check_duplicates(M):
    ''':Description:    check if the matrix was filled with the same value twice:
        same row, same column, same 3x3 subMatrix
    :param M:   the matrix to test
    :return:    boolean:    True if there are duplicates, False if all are unique    '''
    r, c = 0, 0
    for x in range(1,10):
        for i in range(1,10):
            row = M[i-1]
            col = transpose(M)[i-1].tolist()
            r, c = row.count(x), col.count(x)
            # print('nr = ', x,'   row=' ,i, '    ' ,r ,  row)
            # print('nr = ', x,  '   col=', i, '   ', c ,   col )
            if r > 1 == True or c >1 == True :      # True if there are duplicates
               return True

        for i in range(2,10,3):
            for j in range(2,10,3):
                submatrix = [val for sublist in SubMatrix_3x3(i,j,M) for val in sublist]
                # print(submatrix, x,  i, j)
                s =  submatrix.count(x)
                if s > 1 == True  :
                    # print('True', x,i,j)
                    return True

    return False
# def check_doubles(M):
#     ''':Description:    check if there are values 2 times or more at a position. Checks if
#         there are >1 numbers on a row, a column or a 3x3 subMatrix. If there are duplicate
#         numbers return True, returns False if all the numbers are Unique.
#     :param M:   the matrix to test
#     :return:    boolean:    True if there are duplicates, False if all are unique    '''
#     for x in range(1,10):
#         for i in range(1,10):
#             row = M[i-1]
#             col = transpose(M)[i-1].tolist()
#             if row.count(x) > 1 == True or col.count(x) >1 == True :
#                 res1 = True
#             else: return False
#             print(row.count(x) > 1 ,row.count(x) , type(row),x,i )
#             print( col.count(x) >1 , col.count(x) ,type(col),x,i )
#         for i in range(2,10,3):
#             for j in range(2,10,3):
#                 submatrix = [val for sublist in SubMatrix_3x3(i,j,M) for val in sublist]
#                 print(submatrix, x,  i, j)
#                 if submatrix.count(x) > 1 == True  :
#                     print('True', x,i,j)
#                     res2 = True
#                 else: return False
#         if res1 == True and res2 == True:
#             return True

def get_1_choice_position(M):
    ''':Description:    Prints out the positions which have **ONLY  1 CHOICE**     '''
    one_var={}
    sudoku = get_to_fill_status(M)
    for k, v in sudoku.items() :
        # print(k, v , v.count(False)     ,end=' ')
        if v.count(False) ==1 :
            number = v.index(False)+1
            position = [int(i) for i in list(k)]
            one_var[k] = number
            # print('position: ',position , v, '  choice: ',number )
        # else : print('\nNo more 1 Choice')
    if len(one_var) != 0 : return one_var
    else: return []

def get_2_choices_positions(M):     # Not working properly
    ''':Description:    Return out the positions which have **2 CHOICES**     '''
    two_vars = []
    sudoku = get_to_fill_status(M)
    for k, v in sudoku.items() :
        # print(k, v , v.count(False)     ,end=' ')
        if v.count(False) == 2 :
            position = [int(i) for i in list(k)]
            # print(position)
            z = [i+1 for i, x in enumerate(v) if x == False ]
            # print(z)
            two_vars.append( [ str(k)+str(z[0]), str(k)+str(z[1]) ] )
            # del(two_vars[k][1])
            # print( 'position: ', position , v,'  choices: ', z )
        # else : print('No more 2 Choices')
    if len(two_vars) != 0 : return two_vars
    else: return []

def rotate(l, n):
    return l[-n:] + l[:-n]

def binary_counter( digits):
    # Binary counter
    x=0
    while True :
        yield (bin(x)[2:].zfill(digits))
        x+=1

F = [ ['815', '819'], ['976', '979'], ['734', '738'] ]
def create_tracker(F) :
    '''Creates the INITIAL tracker list which will be used to explore
    all possibilties. The tracker list becomes larger by exp(2)
    Therefore a liss of 10 pairs will yield 2**10 possibilities
    '''
    tracker=[]
    elem_nr = 2**len(F)
    B = binary_counter(len(F))
    for i in range(elem_nr) :
        b = [ int(k) for k in next(B)]
        tmp = []
        for j in range(len(F)) :
#             print(b, F[j][b[j]] , end='  ' )
            tmp.append(F[j][b[j]] )
        tracker.append(tmp)

    return tracker

def update_tracker(G, tracker) :
    '''Creates the INITIAL tracker list which will be used to explore
    all possibilties. The tracker list becomes larger by exp(2)
    Therefore a liss of 10 pairs will yield 2**10 possibilities
    '''
#     print(tracker,'\n\n')
    trackerU  = deepcopy(tracker)
    tmp = deepcopy(trackerU)
    tracker=[]
    elem_nr = 2**len(G)
    B = binary_counter(len(G))

    for i in range(elem_nr) :
        b = [ int(k) for k in next(B)]
        for j in range(len(trackerU)) :
            for l in range(len(b)) :
                tmp[j].append(G[l][b[l]])
            tracker.append(tmp[j])
#         print(tmp)
        tmp = deepcopy(trackerU)
    return tracker


def tracker_fill( M, tracker, glide):
    N = deepcopy(M)
    tracker2 = deepcopy(tracker)
    while glide < len(tracker) :
        for I in tracker[glide] :
            M[int(I[0])-1] [int(I[1])-1] = int(I[2])
        # print(check_duplicates(M), len (tracker), M)
        if check_duplicates(M) == True :
            M = deepcopy(N) # revert back matrix to initial state
            tracker.pop(glide)
        elif check_duplicates(M) == False :
            return M


def show_complete(M, grid) :
        print('=='*6+'   '+str(grid)+'   '+'=='*6)
        # print('=='*15 )
        for i in range(len(M)):
            print('  +++++   ', M[i] ,'   +++++  ')
        print('=='*15 )
        # print('\nCONGRATULATIONS !! SUDOKU Magic Puzzle has been Correctly Solved ! \n ')

print( '\n---------------------------- Test for spots ---------------------')
print('Test one_available_spot Function : ', one_available_spot(M))
print('Test two_available_spots Function : ', two_available_spots(M),'\n\n')

print('Prints out the positions which have ONLY  1 CHOICE : \n' , get_1_choice_position(M) )
print('Prints out the positions which have 2 CHOICES : \n', get_2_choices_positions(M) )

print('----------------------------------------------------------- \n')


#############        END    DEFINITIONS        ####################
t1  = time.time()

M = [[6, 3, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 5, 0, 0, 0, 0, 8], [0, 0, 5, 6, 7, 4, 0, 0, 0], [0, 0, 0, 0, 2, 0, 0, 0, 0], [0, 0, 3, 4, 0, 1, 0, 2, 0], [0, 0, 0, 0, 0, 0, 3, 4, 5], [0, 0, 0, 0, 0, 7, 0, 0, 4], [0, 8, 0, 3, 0, 0, 9, 0, 2], [9, 4, 7, 1, 0, 0, 0, 8, 0]]
# M = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 7, 9, 0, 5, 0, 1, 8, 0], [8, 0, 0, 0, 0, 0, 0, 0, 7], [1, 9, 7, 3, 4, 6, 8, 5, 2], [4, 5, 2, 7, 1, 8, 3, 9, 6], [6, 8, 3, 5, 9, 2, 7, 0, 0], [7, 0, 0, 0, 0, 0, 0, 0, 5], [0, 1, 6, 0, 3, 0, 4, 2, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]

   ##########         CASE 1          #########
def fill_1_available_position(M):
    sudoku = get_to_fill_status(M)
    if one_available_spot(M) == True :
        for k, v in sudoku.items() :
            # print(k, v , v.count(False)     ,end=' ')
            if v.count(False) == 1 :        #  if only 1 False it can be completed with the number
                number = v.index(False)+1
                position = [ int(i) for i in list(k) ]
                print(position , ' completed with  value: ',number, '   ', v    ,'           <--   CASE  1 ')
                M[position[0]-1 ] [position[1]-1 ] = number
                return M    # only one at a time !!!!!!!!!!!!
    if one_available_spot(M) == False :
        return False

       ###########          CASE 2          ############

A, tracker, within_tracker , glide  = [], [], [], 0

def get_2_fill_available_positions(M ):
    global A, tracker, within_tracker, glide
    if len(tracker) == 0 :
        A = deepcopy(M)
        print('\n\n      ################    matrix A was created (tracker is empty)   ############:\n',A)


        tmp = get_2_choices_positions(M)
        tracker = create_tracker(tmp)
        print('\nTracker was created, length =', len(tracker) , tmp,'\n', tracker[:3])

    if len(tracker) != 0 :
        M = tracker_fill( M, tracker, 0)
        print('tracker_length : ', len(tracker), tracker[:3])
        return M




def solve_sudoku( grid ):
    global M, tracker
    tracker_change, len_tracker = 3, 0      # Tracker Flag
    while True :

        if one_available_spot(M) == True :
            fill_1_available_position(M)
            print('\nCASE 1', M)

        if two_available_spots(M) == True :
            get_2_fill_available_positions(M)
            M = tracker_fill( M, tracker, 0)
            print('\nCASE 2', M )

            if len_tracker != len(tracker) :        # Update len_tracker & Flag
                len_tracker = len(tracker)
                tracker_change = True
            elif len_tracker == len(tracker) and one_available_spot(M) ==False :
                tracker_change = False
            print( 'tracker length : ',len(tracker), '          tracker_change :', tracker_change, '     ', len_tracker )


        print(' ONE_spot =' ,one_available_spot(M), '      TWO_spots =' ,two_available_spots(M), '    Quench : ', quench(M))
        print('get_2_choices_positions : ', len(get_2_choices_positions(M)), get_2_choices_positions(M),'\n' )

        if quench(M) == True :
            M = deepcopy(A)
            tracker.pop(glide)


        if  tracker_change == False and one_available_spot(M) == False and two_available_spots(M)==True :
            print(' ++++++++++++++         TRACKER WIL BE UDATED    +++++++++++++++')
            M = deepcopy(A)
            G = get_2_choices_positions(M)
            if len(G) > 8 :
                G = G[ :3 ]
            tracker = update_tracker(G, tracker)
            print('\nTracker was UPDATED, length =', len(tracker), G, '\n', tracker[:3])



        if validate_final(M) == True :
            show_complete(M, grid )
            break


solve_sudoku(grid=14)



# cnt= 0
# for k, v in Mall.items() :
#     cnt+=1
#     M, grid = v, k
#     solve_sudoku( grid )
#     Mall[k] = M
#     print(str(cnt)+'.    ' , k,'    ' , M)



# print('\n===================Mecanic ==============   \n', M)
# memo, A,  SIGN, SuperFlag = {}, [], [] , False
# print('STEP 1  '),fill_available_position(M)
# print('STEP 2  '),fill_available_position(M)
# print('STEP 3  '),fill_available_position(M)
# print('STEP 4  '),fill_available_position(M)
# print('STEP 5  '),fill_available_position(M)
# print('STEP 6  '),fill_available_position(M)
# print('Intermediary:  ',M)
# print('STEP 7  '),fill_available_position(M)
# # # print(M)
# print('STEP 8  '),fill_available_position(M)
# print('STEP 9  '),fill_available_position(M)
# print('CHECK Doubles Test : ',check_doubles(M))
# print('STEP 10  '),fill_available_position(M)
# print('STEP 11  '),fill_available_position(M)
# print('STEP 12  '),fill_available_position(M)
# print('STEP 13  '),fill_available_position(M)
# print('CHECK Doubles Test : ',check_doubles(M), memo)
# print('Intermediary:  ',M)
# print('STEP 14  '),fill_available_position(M)
# print('STEP 15  '),fill_available_position(M)
# print('STEP 16  '),fill_available_position(M)
# print('CHECK Doubles Test : ',check_doubles(M), memo)
# print('STEP 17  '),fill_available_position(M)
# print('STEP 18  '),fill_available_position(M)
# # print('Intermediary:  ',M)
# print('STEP 19  '),fill_available_position(M)
# print('CHECK Doubles Test : ',check_doubles(M), memo)
# print('STEP 20  '),fill_available_position(M)
# print('STEP 21  '),fill_available_position(M)
# print('STEP 22  '),fill_available_position(M)
# print('STEP 24  '),fill_available_position(M)
# print('STEP 25  '),fill_available_position(M)
# print('STEP 26  '),fill_available_position(M)




t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n-----------------------------------------------')
