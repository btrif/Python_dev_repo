#!/usr/bin/python
# Solved by Bogdan Trif @   Completed on Sat, 12 Nov 2016, 13:30
#The  Euler Project  https://projecteuler.net
'''
                                    Cyclical figurate numbers       -       Problem 61
Triangle, square, pentagonal, hexagonal, heptagonal, and octagonal numbers are all figurate (polygonal) numbers
and are generated by the following formulae:

                                    Triangle     P[3,n]=n(n+1)/2    1, 3, 6, 10, 15, ...
                                    Square       P[4,n]=n^2         1, 4, 9, 16, 25, ...
                                    Pentagonal   P[5,n]=n(3n-1)/2   1, 5, 12, 22, 35, ...
                                    Hexagonal    P[6,n]=n(2n-1)     1, 6, 15, 28, 45, ...
                                    Heptagonal   P[7,n]=n(5n-3)/2   1, 7, 18, 34, 55, ...
                                    Octagonal    P[8,n]=n(3n-2)     1, 8, 21, 40, 65, ...

The ordered set of three 4-digit numbers: 8128, 2882, 8281, has three interesting properties.
 1. The set is cyclic, in that the last two digits of each number is the first two digits of the next number
            (including the last number with the first).
 2. Each polygonal type: triangle (P[3,127]=8128), square (P[4,91]=8281), and pentagonal (P[5,44]=2882),
            is represented by a different number in the set.
 3. This is the only set of 4-digit numbers with this property.

Find the sum of the only ordered set of six cyclic 4-digit numbers for which each polygonal type:
triangle, square, pentagonal, hexagonal, heptagonal, and octagonal, is represented
'''
import time
from itertools import combinations, permutations

def isTriangular(n):
    x = ((((8 * n) + 1) ** 0.5) - 1) / 2
    if x % 1 == 0 :  return True
    else:  return False

def isSquare(n):
    x = n**(0.5)
    if x % 1 == 0 :  return True
    else:  return False

def isPentagonal(n):
    x = ((((24 * n) + 1) ** 0.5) + 1) / 6
    if x % 1 == 0 :  return True
    else:  return False

def isHexagonal(n):
    x = ((((8 * n) + 1) ** 0.5) + 1) / 4
    if x % 1 == 0 :  return True
    else:  return False

def isHeptagonal(n):
    x = ((((40 * n) + 9) ** 0.5) + 3) / 10
    if x % 1 == 0 :  return True
    else:  return False

def isOctagonal(n):
    x = ((((12 * n) + 4) ** 0.5) + 2) / 6
    if x % 1 == 0 :  return True
    else:  return False

def gen_Triangular(n):
    '''  Computes the triangular number of n '''
    return int(n*(n+1)/2)

def gen_Square(n):
    return int(n*n)

def gen_Pentagonal(n):
    penta = int((n * ((3 * n) - 1)) // 2)
    return penta

def gen_Hexagonal(n):
    return int(n*((2*n) - 1))

def gen_Heptagonal(n):
    return int((n * ((5 * n) - 3))/2)

def gen_Octagonal(n):
    return int(n*(3*n-2))


# print('\n-------------------- TESTS ------------------------')

TRIANG=[]
SQUARE=[]
PENTA=[]
HEXA=[]
HEPTA=[]
OCTA=[]

#print('\n--------OCTAGONAL-------------')
for i in range(19,59):         # Octagonal Lower end for 4-digit nr is 19, and 59 is the  Upper Range
    a = gen_Octagonal(i)
    # print(a,   end='  ')
    if str(a)[-2] != '0' : OCTA.append(str(a))

#print('\n--------HEPTAGONAL-------------')
for i in range(21,64):         # Heptagonal Lower end for 4-digit nr is 21, and 64 is the  Upper Range
    a = gen_Heptagonal(i)
    # print(a,   end='  ')
    if str(a)[-2] != '0' : HEPTA.append(str(a))

#print('\n--------HEXAGONAL-------------')
for i in range(23,71):         # Hexagonal Lower end for 4-digit nr is 23, and 71 is the  Upper Range
    a = gen_Hexagonal(i)
    # print(a,   end='  ')
    if str(a)[-2] != '0' : HEXA.append(str(a))

#print('\n-------- PENTAGONAL-------------')
for i in range(26,82):         # Pentagonal Lower end for 4-digit nr is 26, and 82 is the  Upper Range
    a = gen_Pentagonal(i)
    # print(a,   end='  ')
    if str(a)[-2] != '0' : PENTA.append(str(a))

#print('\n-------- SQUARE-------------')
for i in range(32,99):         # Square Lower end for 4-digit nr is 32, and 99 is the  Upper Range
    a = gen_Square(i)
    # print(a,   end='  ')
    if str(a)[-2] != '0' : SQUARE.append(str(a))

#print('\n-------- TRIANGULAR-------------')
for i in range(45,141):         # Triangular Lower end for 4-digit nr is 45, and 141 is the  Upper Range
    a = gen_Triangular(i)
    # print(a,  str(a)[-2::]  ,end=' ;  ')
    if str(a)[-2] != '0' and isHexagonal(a) == False :  # Add only the numbers which are NOT HEXAGONAL
        TRIANG.append(str(a))

print('OCTA: ' , len(OCTA), OCTA)
print('HEPTA: ' , len(HEPTA), HEPTA)
print('HEXA: ' , len(HEXA), HEXA)
print('PENTA: ' , len(PENTA), PENTA)
print('SQUARE: ' , len(SQUARE), SQUARE)
print('TRIANG: ' , len(TRIANG), TRIANG)

# print([val for val in HEXA if str(val[0:2]) in TRIANG])
# test='1045'
# for nr in TRIANG:
#     print(re.findall('\d\d45', str(nr)), end = ' ')

# print([str(i) for i in OCTA if  1035 in str(j) for j in TRIANG  ] )
# print( [x for x in OCTA if  '45' in  TRIANG] )

print('----------------------')
print('1035'[2:], '1035'[:2] )
lst1=['1035', '1046', '3000', '7639', '1225', '1275', '1326']
lst2=['3510', '1081', '3528', '1176', '2512', '1275', '1376']
matchers = [i[2:] for i in lst1]
print(matchers)
print('Last two digits from lst1 with first two digits of lst2',[s for s in lst2 if any(y in s[:2] for y in matchers)])

def try_match(first, second) :
    if first[-2::] == second[:2] :
        return True
    else : return False

print('\n',try_match( '1081', '8177'   ))

print('----------------------')

matchers = [i[2:] for i in OCTA]
print(matchers)
print([s for s in TRIANG if any(y in s[:2] for y in matchers)])

print('\n---------TESTS-------------')

COLECTION = { 'TRIANG' : TRIANG, 'SQUARE' : SQUARE, 'PENTA' : PENTA, 'HEXA': HEXA, 'HEPTA': HEPTA, 'OCTA': OCTA}
C_O_L = {  'SQUARE' : SQUARE, 'PENTA' : PENTA, 'HEXA': HEXA, 'HEPTA': HEPTA, 'OCTA': OCTA}
print(COLECTION.keys())
# del(COLECTION['TRIANG'])
# print(COLECTION.keys())
C = list(combinations(COLECTION , 2))
print(len(C) ,  C)

B = list(permutations(COLECTION))
print(len(B) , B)

P = list(permutations(C_O_L))
print(len(P) , P)

# m1 = [s for s in COLECTION['PENTA'] if any(y in s[:2] for y in [i[-2::]]) ]       # List Variant
for i in range(len(TRIANG)) :
    # print(TRIANG[i])
    m1 = [s for s in COLECTION['PENTA'] if  s[:2] == TRIANG[i][-2::] ]                      # String Variant
    print(m1, end='  ')

print('\n','75' in P[0][0] )



print('\n\n------------------------ MY SOLUTION ------------------------------\n')
t1  = time.time()

SIX_4_DIGIT_SET = []
cnt1, cnt2 = 0, 0
for w in range(len(P)):
    # print(P[w] , P[w][0], P[w][1], P[w][2], P[w][3], P[w][4])
    for i in range(len(TRIANG)) :
    # print(TRIANG[i])
        m0 = [s for s in C_O_L[P[w][0]] if  s[:2] == TRIANG[i][-2::] ]     # This is the FIRST Step, meaning first 2 numbers
        if len(m0) >0 :
            cnt1+=1
            m0 = m0[0]
            # print(m0, end='  ')              # This is the First Step, meaning first 2 pairs : TRIANG + other1
            # print(str(cnt1)+'.   ',TRIANG[i] , m0, m0[-2::] , P[w][0] )
            m1 = [s for s in C_O_L[P[w][1]] if  s[:2] == m0[-2::] ]             # This is the SECOND Step, 3 nr's  : 3 numbers
            if len(m1) >0 :
                m1 = m1[0]
                # print(TRIANG[i] , '  '  ,P[w][0] ,m0, '  '  ,P[w][1], m1  )
                m2 = [s for s in C_O_L[P[w][2]] if  s[:2] == m1[-2::] ]             # This is the THIRD Step,   : 4 numbers
                if len(m2) > 0:
                    m2 = m2[0]
                    # print(TRIANG[i] , '  '  ,P[w][0] ,m0, '  '  ,P[w][1], m1 , '  '  ,P[w][2], m2  )
                    m3 = [s for s in C_O_L[P[w][3]] if  s[:2] == m2[-2::] ]             # This is the FOURTH Step,   : 5 numbers
                    if len(m3) > 0:
                        cnt2+=1
                        m3 = m3[0]
                        # print(str(cnt2)+'.   ',TRIANG[i] , '  '  ,P[w][0] ,m0, '  '  ,P[w][1], m1 , '  '  ,P[w][2], m2 , '  '  ,P[w][3], m3  )
                        m4 = [s for s in C_O_L[P[w][4]] if  s[:2] == m3[-2::] ]             # This is the FIFTH Step,   : 6 numbers
                        if len(m4) > 0:
                            m4 = m4[0]
                            if m4[-2::] == TRIANG[i][:2] :
                                SIX_4_DIGIT_SET=[  int(TRIANG[i]) , int(m0), int(m1), int(m2), int(m3), int(m4) ]
                                print(str(cnt2)+'.     TRIANG',TRIANG[i] , '  '  ,P[w][0] ,m0, '  '  ,P[w][1], m1 , '  '  ,P[w][2], m2 , '  '  ,P[w][3], m3 , '  '  ,P[w][4], m4 )

print('\nAnswer:', sum(SIX_4_DIGIT_SET), SIX_4_DIGIT_SET  )     # 28684

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')



print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1,  Sandamnit, USA --------------------------')
t1  = time.time()

# I determined the lower and upper bounds of n so that each type of number would generate a 4-digit number.
# Not really necessary, but didn't think filtering out < 1000 and >=10000 was very elegant.

triangle = lambda n: n*(n+1)//2
square = lambda n: n*n
pentagonal = lambda n: n*(3*n-1)//2
hexagonal = lambda n: n*(2*n-1)
heptagonal = lambda n: n*(5*n-3)//2
octagonal = lambda n: n*(3*n-2)

def recurse(levels, cycle):
   # base case to check the desired cycle condition
   if len(levels) == 6 and cycle[0] == cycle[-1]:
      print(sum(cycle[:6]) * 101)
      #exit()

   # only check those levels not already listed in `levels'
   for level in [ x for x in range(6) if not x in levels ]:
      for n in nums[level]:
         # skip those numbers which invalidate the required condition
         if int(str(n)[:2]) != cycle[-1]: continue

         # condition satisfied, add level and append cycle
         recurse(levels+[level], cycle+[int(str(n)[2:])])

# build lists of 4-digit numbers of each type
nums = [
   [ triangle(n) for n in range(44,140) ],
   [ square(n) for n in range(31,99) ],
   [ pentagonal(n) for n in range(25,81) ],
   [ hexagonal(n) for n in range(22,70) ],
   [ heptagonal(n) for n in range(20,63) ],
   [ octagonal(n) for n in range(18,58) ] ]

# loop over all valid triangle numbers / initialize the recursion
for n in nums[0]:
   recurse([0], [int(str(n)[:2]), int(str(n)[2:])])

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('--------------- WHAT THE FUCK !!!!!!!! doest print anything after here ? ---------- ')
print('--------------- Oh yeah ! it was an exit() on the function def recurse  ---------- ')

print('\n--------------------------SOLUTION 2,  VERY ELEGANT SOLUTION, bienj, Philipine  --------------------------')
t1  = time.time()

figNumbers = [
    [(n*(n+1))/2 for n in range(46,141)],
    [n*n for n in range(32,100)],
    [(n*(3*n-1))/2 for n in range(26,82)],
    [n*(2*n-1) for n in range(23,71)],
    [(n*(5*n-3))/2 for n in range(21,64)],
    [n*(3*n-2) for n in range(19,59)]
    ]

def getNextNumbers(origin,degreesToExclude):
    adj = [(d,[n for n in figNumbers[d] if n//100==origin%100]) for d in range(0,6) if d not in degreesToExclude]
    return adj

def findCyclesWithLength(targetLength,orderedSet=[],degreesToExclude=[],initDegree=0):

    DEGREE,VALUES = 0,1

    if orderedSet==[] and degreesToExclude==[]:
        for num in figNumbers[initDegree]:
            findCyclesWithLength(targetLength,[num],[initDegree])

    elif len(orderedSet)==targetLength:
        for nextNumbers in getNextNumbers(orderedSet[-1],[n for n in range(0,6) if n!=initDegree]):
            for number in nextNumbers[VALUES]:
                if orderedSet[0]==number:
                    print (orderedSet, sum(orderedSet))
    else:
        for nextNumbers in getNextNumbers(orderedSet[-1],degreesToExclude):
            for number in nextNumbers[VALUES]:
                findCyclesWithLength(targetLength,orderedSet+[number],degreesToExclude+[nextNumbers[DEGREE]])

findCyclesWithLength(6)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 3,  FAST, VERY GOOD SOLUTION, imanuel.sygal, Israel  --------------------------')
t1  = time.time()
# Finishes instantly.
# remember all 4-digit numbers of each type, and recursively look at what numbers can be added from types that were not used yet.

triangles = [(n * (n + 1)) // 2 for n in range(40, 150) if
             2000 <= (n * (n + 1)) < 20000]
squares = [n * n for n in range(32, 100)]
pents = [(n * (3 * n - 1)) // 2 for n in range(20, 100) if
         2000 <= (n * (3 * n - 1)) < 20000]
hex = [n * (2 * n - 1) for n in range(20, 76) if
       1000 <= (n * (2 * n - 1)) < 10000]
hept = [(n * (5 * n - 3)) // 2 for n in range(20, 61) if
        2000 <= (n * (5 * n - 3)) < 20000]
oct = [n * (3 * n - 2) for n in range(31) if
       1000 <= (n * (3 * n - 2)) < 10000]

types_values = [triangles, squares, pents, hex, hept, oct]


def search_cyclic_candidates(numbers_used_so_far, types_used_so_far):
    """ This function receives the numbers we took so far in their cyclic order,
    and the types used so far in the same order.
    This function checks whether there exists a syclic series continuing this given sequence.
    """

    if len(numbers_used_so_far) == 6:
        return numbers_used_so_far[5] % 100 == numbers_used_so_far[0] // 100

    # we represent the types used so far as the indices in types_values.
    # find all possible next-candidates together with their type:
    possible_nexts = [(val, i) for i, num_type in enumerate(types_values) for val in num_type if
                      i not in types_used_so_far and val // 100 == numbers_used_so_far[-1] % 100]

    for (current_candid, current_candid_type) in possible_nexts:
        if search_cyclic_candidates(numbers_used_so_far + (current_candid,),
                                    types_used_so_far + (current_candid_type,)):
            print(sum(numbers_used_so_far) + current_candid)


for oct_n in oct:
    search_cyclic_candidates((oct_n,), (5,))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 4,  RECURSIVE SOLUTION, Brian.Mellendorf, USA --------------------------')
t1  = time.time()
# Python 3 recursion

def find_next(avail,path,long_string):
	if avail == []:
		if long_string[0:2] == long_string[-2:]:
			sum=0
			for z in range(6):
				sum += int(long_string[z*5:z*5+4])
			print(long_string,";  path ->",path,";  sum =",sum)
		return
	for i in avail:
		for j in p[i]:
			if long_string[-2:] == j[0:2]:
				newlist = avail[:]
				newlist.remove(i)
				find_next(newlist,path+" "+str(i),long_string+" "+j)
	return

newlist=[]
p=[[] for _ in range(9)]
f=[[] for _ in range(9)]
n=0
while True:
	n += 1
	f[3] = n * (n+1) // 2
	if f[3] > 9999: break
	f[4] =  n ** 2
	f[5] = n * (3 * n - 1) // 2
	f[6] = n * (2 * n - 1)
	f[7] = n * (5 * n - 3) // 2
	f[8] = n * (3 * n - 2)
	for r in range(3,9):
		if f[r] > 999 and f[r] <= 9999 and str(f[r])[2] != "0":
			p[r].append(str(f[r]))

for x in p[8]:
	find_next([3,4,5,6,7],"8",x)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 5, FJ_Sevilla, Spain  --------------------------')
t1  = time.time()
# Python 3 brute force in 39 milliseconds:

from math import sqrt

def triangle_numbers(l,L):
    n = (sqrt(8*l+1)-1)/2
    if not n.is_integer(): n = int(n)+1
    else: n = int(n)
    N = int((sqrt(8*L+1)-1)/2)+1
    return['3'+str(int(i*(i+1)/2)) for i in range(n, N)]

def square_numbers(l,L):
    n = sqrt(l)
    if not n.is_integer(): n = int(n)+1
    else: n = int(n)
    N = int(sqrt(L))+1
    return['4'+str(i*i) for i in range(n, N)]

def pentagonal_numbers(l,L):
    n = (sqrt(24*l+1)+1)/6
    if not n.is_integer(): n = int(n)+1
    else: n = int(n)
    N = int((sqrt(24*L+1)+1)/6)+1
    return['5'+str(int(i*(3*i-1)/2)) for i in range(n, N)]

def hexagonal_numbers(l,L):
    n = (sqrt(8*l+1)+1)/4
    if not n.is_integer(): n = int(n)+1
    else: n = int(n)
    N = int((sqrt(8*L+1)+1)/4)+1
    return['6'+str(i*(2*i-1)) for i in range(n, N)]

def heptagonal_numbers(l,L):
    n = (sqrt(9+40*l)+3)/10
    if not n.is_integer(): n = int(n)+1
    else: n = int(n)
    N = int((sqrt(9+40*L)+3)/10)+1
    return['7'+str(int(i*(5*i-3)/2)) for i in range(n, N)]

def octagonal_numbers(l,L):
    n = (2+sqrt(4+12*l))/6
    if not n.is_integer(): n = int(n)+1
    else: n = int(n)
    N = int((2+sqrt(4+12*L))/6)+1
    return['8'+str(i*(3*i-2)) for i in range(n, N)]

def solve(dic):
    for k in dic:
        for a in dic[k]:
            for b in dic[a]:
                for c in dic[b]:
                    for d in dic[c]:
                        for e in dic[d]:
                            if e[3:]==k[1:3] and len(set((k[0],a[0],b[0],c[0],d[0],e[0])))==6:
                                return sum([int(n) for n in [k[1:],a[1:],b[1:],c[1:],d[1:],e[1:]]])

def main():
    n3=triangle_numbers(1000,9999)
    n4=square_numbers(1000,9999)
    n5=pentagonal_numbers(1000,9999)
    n6=hexagonal_numbers(1000,9999)
    n7=heptagonal_numbers(1000,9999)
    n8=octagonal_numbers(1000,9999)
    dic=dict()

    for lis in (n3,n4,n5,n6,n7,n8):
        for i in lis:
            dic[i]=[j for lis2 in [n3,n4,n5,n6,n7,n8] for j in lis2 if lis != lis2 and i[3:]==j[1:3]]
    print(solve(dic))


if __name__ == '__main__':
        main()
        # input('Press "Enter" to out...')

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 6,   --------------------------')
t1  = time.time()



t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')











# for i in range(len(TRIANG)) :
#     m1 = [s for s in COLECTION['PENTA'] if  s[:2] == TRIANG[i][-2::] ]                      # String Variant
#     print(m1, end='  ')






# COL1 = COLECTION.copy()
# COL2 = COL1.copy()
# i = '1081'
# CHAIN = {} #{'TRIANG' :'1081',  }
# CHAIN2 = CHAIN.copy()
# del(COL1['TRIANG'])
# del(COL2['TRIANG'])
# print(COL1.keys())
#
# for i in TRIANG:
#     CHAIN = {}
#     COL1 = COLECTION.copy()
#     COL2 = COL1.copy()
#     del(COL1['TRIANG'])
#     del(COL2['TRIANG'])
#     for j in COL1 :
#         m1 =  [s for s in COL1[str(j)] if  s[:2] == i[-2::] ]
#         if len(m1) >0 :
#             CHAIN[str(j)] = m1
#             del(COL2[str(j)])
#             # print( j , m1)
#         COL1 = COL2.copy()
#         CHAIN2 = CHAIN.copy()
#     print('\n', i ,CHAIN, '       ',COL1.keys(),' <------1---- Dictionaries')
#     if len(CHAIN) > 0:
#         print('\n', i ,CHAIN, '       ',COL1.keys(),' <-----1.2----- Dictionaries')
#         for k in CHAIN:
#             for l in COL1 :
#                 m2 = [s for s in COL1[str(l)] if  s[:2] == CHAIN[k][0][-2::] ]
#                 if len(m2) >0 :
#                     CHAIN2[str(l)] = m2
#                     del(COL2[str(l)])
#                 COL1 = COL2.copy()
#                 CHAIN = CHAIN2.copy()
#                 print( k  ,CHAIN[k]  ,COL1.keys() ,m2 ,' <-----2----- Dictionaries' )
#

