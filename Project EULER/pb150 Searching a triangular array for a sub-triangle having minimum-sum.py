#!/usr/bin/python
# Solved by Bogdan Trif @   Completed on Fri, 1 Sep 2017, 15:41
#The  Euler Project  https://projecteuler.net
'''
Searching a triangular array for a sub-triangle having minimum-sum      -       Problem 150

In a triangular array of positive and negative integers, we wish to find a sub-triangle
such that the sum of the numbers it contains is the smallest possible.

In the example below, it can be easily verified that the marked triangle satisfies this condition having a sum of −42.


We wish to make such a triangular array with one thousand rows, so we generate 500500
pseudo-random numbers sk in the range ±2**19, using a type of random number generator
(known as a Linear Congruential Generator) as follows:

t := 0
for k = 1 up to k = 500500:
    t := (615949*t + 797807) modulo 2**20
    sk := t−2**19

Thus: s_1 = 273519, s_2 = −153582, s_3 = 450905 etc

Our triangular array is then formed using the pseudo-random numbers thus:

                                                        s1
                                                     s2  s3
                                                   s4  s5  s6
                                                s7  s8  s9  s10
...
Sub-triangles can start at any element of the array and extend down as far as we like
(taking-in the two elements directly below it from the next row,
the three elements directly below from the row after that, and so on).
The "sum of a sub-triangle" is defined as the sum of all the elements it contains.
Find the smallest possible sub-triangle sum.


'''
import time


def Linear_Congruential_Generator():           # EFFICIENT GENERATOR
    '''      t := 0
            for k = 1 up to k = 500500:
                t := (615949*t + 797807) modulo 2**20
                sk := t−2**19
        Thus: s_1 = 273519, s_2 = −153582, s_3 = 450905 etc                 '''
    t=0
    while True :
        t = (615949*t + 797807)% (2**20)
        s = t - 2**19
        yield s


print('\n--------------------------TESTS------------------------------')

LCG = Linear_Congruential_Generator()

for i in range( 10):
    print(str(i)+'.   ', next(LCG), end='    ')

print('\n-------------------------------------')

def build_triangle(up_lim):
    LCG = Linear_Congruential_Generator()
    T=[]
    rows = int( -(1/2)+ ( (1+4*2*up_lim)**(1/2) )/2 )
    for i in range(0, rows):
        tmp=[]
        for j in range(0, i+1):
            tmp.append(next(LCG))
        T.append(tmp)
        # print(str(i)+'.   '  , tmp)
    return T

T = build_triangle(5050)

def find_triangle_up_sum(triangle , row,  i, j ) :
    ''' Function to calculate the sum of a triangle of given size found at a position i,j
    :param triangle: triangle array, nested list
    :param i: int, row number
    :param j: int, column number
    :param size: size of the triangle
    :return: the sum of the triangle    '''
    S, T = 0, triangle
    S+= sum( T[row][i:j] )
    for k in range(1,  j-i ) :
        S+= sum( T[row-k][ i : j-k]  )
        # print(k, )
    return S



def find_triangle_sum_down(triangle , i, j, min_size ) :
    ''' Function to calculate the sum of a triangle of given size found at a position i,j
    :param triangle: triangle array, nested list
    :param i: int, row number
    :param j: int, column number
    :param size: size of the triangle
    :return: the sum of the triangle    '''
    S, T = 0, triangle
    for k in range(0, min_size) :
        S+= sum( T[i+k][ j : j+k+1] )
        # print(i, j, k ,T[i+k][j:j+k+1]  )
    return S



print('\n------------- Test Kadane Minimum -sum -----------\n')

def Kadane_minimum(arr):        # !!!!!!!!!!!! NOT YET WORKING PROPERLY  !!!!!!!!!!!
    ''' KADANE's Algorithm
    https://en.wikipedia.org/wiki/Maximum_subarray_problem    '''
    S=[0, 1]
    min_current = min_global = arr[0]
    start, end = 0, 1
    for i in range(1, len(arr)):
        min_current = min (arr[i], min_current+arr[i] )

        if arr[i] < min_current+arr[i]  :
            start = i+1
            S.append(start)
            # print('new start index:' ,start, '  ', arr[i],min_current ,min_current+arr[i], min_global)

        if min_current < min_global :
            min_global = min_current
            # print(min_current, min_global, start, end)
            end = i+1

#     print('start indexes :', S)
    for w in S : # What a shame Code Here ! Oh my God !!!@2017-02-18
        if sum(arr[w:end]) == min_global:
            start = w
            break
    # print('\nStart end indexes : ', start, end ,  '  ', sum(arr[start:end]), '  \n' , arr[start:end]  )

    return min_global, start, end

Test_arr = [ -3, -45, 9, 34, -87, 23, 1, -3, 99, 456, -89, 34, -45, 90, -123, 300, 9, -12, -67, 200 ]
# Test_arr = [-209363, -159048, -397369, 369546, -493967, 276012, 292011, 342814, -253707, -493856, 488911, 303602, 53689, 493780, 431923, -316410, -144195, 516104, -148265, -299686, -223743, -184196, 330427, 473582, -200315, -233936, 320735, 239042, -466103, -13020, -397501, -195370, -479411, -343720, -455193, -333014, 448913, -131380, 222411, 273598, 271893, -296576, -370705, 187794, -288551, -367244, 232275, -503386, 423389, -313688, -204041, 72954, 16673, -286436, 33499, -453746, -344411, -354096, -471297, -46750, 127593, -241212, 289635, -388490, 8301, -114696, -377849, -326966, 117937, -321684, -170773, 192094, -410827, -78816, 84495, 387378, 323577, -355820, -159885, -47290, -86275, -467640, 137495, 367770, 293953, 90556, -324869, -82642, -386107, -191632, 313631, 244994, -159351, -383388, -2173, 323606, -319091, 3736, 358951, -136598]
print('\n Kadane_algo : \t', Kadane_minimum(Test_arr))

print(sum(Test_arr[10:15]), '     ',Test_arr[10:15])


print('\n------------------  BRUTE FORCE CHECK SOLUTION  ----------------------\n')
t1  = time.time()

def brute_force(start_row) :
    smin = 10**8
    i2, j2, what_row = 0, 0, 0
    for row in range(start_row, 0, -1) :
        print('we are at the row number :\t ', row )
        for i in range(len(T[row])):
            print(i)
            for j in range( len(T[row]), i, -1  ):
                if j-i < 750 : break
                UK = sum( T[row][i:j] )
                J = find_triangle_up_sum(T , row, i, j )
                if smin > J :
                    smin = J
                    i2, j2  = i, j
                    what_row = row
                    print(row, i, j, '    base_span =',j-i  ,UK, '         MIN =', J,'       first, last=' , T[row][i], ',',T[row][j-1]  ,  '        row_sum=' ,sum(T[row][i:j]) )

    return print('\nFinal : \t',' indeces ' , i2, j2, '    row :', what_row ,  '    '  ,smin )

# brute_force(start_row =978 )

# T_test = [[1],[2,3],[4,5,6],[7,8,9,10],[11,12,13,14,15], [16,17,18,19,20,21],[22,23,24,25,26,27,28],[29,30,31,32,33,34,35,36] ]
# K_tst = [-209363, -159048, -397369, 369546, -493967, 276012, 292011, 342814, -253707, -493856, 488911, 303602, 53689, 493780, 431923, -316410, -144195, 516104, -148265, -299686, -223743, -184196, 330427, 473582, -200315, -233936, 320735, 239042, -466103, -13020, -397501, -195370, -479411, -343720, -455193, -333014, 448913, -131380, 222411, 273598, 271893, -296576, -370705, 187794, -288551, -367244, 232275, -503386, 423389, -313688, -204041, 72954, 16673, -286436, 33499, -453746, -344411, -354096, -471297, -46750, 127593, -241212, 289635, -388490, 8301, -114696, -377849, -326966, 117937, -321684, -170773, 192094, -410827, -78816, 84495, 387378, 323577, -355820, -159885, -47290, -86275, -467640, 137495, 367770, 293953, 90556, -324869, -82642, -386107, -191632, 313631, 244994, -159351, -383388, -2173, 323606, -319091, 3736, 358951, -136598]
K_tst = [-480269, -345658, 163709, -166968, 310679, 194330, 70849, -516036, -411781]

i2, j2, smin = 0,0, 10**8   # BRUTE FORCE SINGLE CHECK #
for i in range(len(K_tst)):
    for j in range(i+1, len( K_tst )+1):
        UK = sum( K_tst[i:j] )
        # J = find_triangle_up_sum(T , row, i, j )
        if smin > UK :
            i2, j2 = i, j
            smin = UK
            print(  i2, j2, '    base_span =', j2-i2  , '    BF=' , smin   )

print()



t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n================  My FIRST SOLUTION,   ===============\n')
t1  = time.time()

# for k in range(len(T)) :
#     i2, j2, smin = 0,0, 10**8
#     for i in range(len(T[k])):        # BRUTE FORCE CHECK #
#         for j in range(i+1, len( T[k] )+1):
#             UK = sum( T[k][i:j] )
#             # J = find_triangle_up_sum(T , row, i, j )
#             if smin > UK :
#                 i2, j2 = i, j
#                 smin = UK
#     # if i2 != Kadane_minimum(T[k])[1] :
#     print('row=', k , '   Kadane_algo:', Kadane_minimum(T[k]), '     ',i2, j2, '    BF=' , smin, '    base_span =', j2-i2   )

def smart_brute_force(size_start , T) :       # SMART BRUTE FORCE TRY

    ii, jj, row_k, J_min = 0, 0, 0, 10**8

    for size in range(size_start, len(T)+1 ):
        print('we are at the size : ', size )
        for row in range( len(T)-size+1 ):
            for col in range(len(T[row])) :
                J = find_triangle_sum_down(T ,  row, col, size )
                if J < J_min  :
                    J_min = J
                    ii, jj,  size_m = row, col , size

                    print(str(size)+'.     ', J, '    row, col:', row, col )

    return print('\nAnswer : \t', J_min,'  ;   size=',size_m, ' ;   start row :' ,ii , ' ,  start col :', jj )


# 2017-02-19, 11:52 --- IT REMAINS FOR A JAVA BRUTE FORCE APPROACH !!!!

# smart_brute_force(1 , T)



t2  = time.time()
print('\nCompleted in :', round((t2-t1),6), 's\n\n')



print('\n================  My SECOND SOLUTION,  2 sec if we limit to 10 rows ===============\n')
t1  = time.time()

T =  build_triangle(500500)
# ss = 0
# for i in range(len(T)) :
#     ss += sum(T[i])
#     print(T[i] , '           ',sum(T[i]))
# print('total sum = ', ss )

def find_triangle_position_going_down(triangle , i, j   ) :
    ''' Find the sum of all possible triangles at a position i,j
    :param triangle: triangle array, nested list
    :param i: int, row number
    :param j: int, column number
    :return: smallest  sum of the  triangle    '''
    S, T, s_temp, dim = 1e8, triangle, 0, 0
    for k in range(0, len(T)- i ) :
        s_temp += sum( T[i+k][ j : j+k+1] )
        if s_temp < S :
            S = s_temp
            dim = k+1
            # print('row, col =',i, j, '     ; len_row = ',k+1 , '    s_temp = ', s_temp        )
    return S, dim

Ts = find_triangle_position_going_down( T, 0, 0 )
print('\n find_triangle_position_going_down : \t', Ts )

def an_interesting_brute_force_approach(T, min_dim):
    SUM, temp_sum = 1e8, 0
    for row in range( len(T)-min_dim ) :
        print("we are at the row :  " , row)
        # if row == 10 : break
        for col in range( row+1 ) :
            temp_sum, dim = find_triangle_position_going_down(T, row, col )
            if temp_sum < SUM :
                SUM = temp_sum
                print( ' ----   row, col , dim = ', row, col, dim ,'-----------------------', SUM   )
    return print('\n Smallest possible minimum-sum : \t', SUM )

an_interesting_brute_force_approach(T, 1 )


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


# print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
# print('\n--------------------------SOLUTION 1,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
# print('\n--------------------------SOLUTION 2,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
# print('\n--------------------------SOLUTION 3,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
# print('\n--------------------------SOLUTION 4,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
# print('\n--------------------------SOLUTION 5,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 6,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
