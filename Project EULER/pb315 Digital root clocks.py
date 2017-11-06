#  Created by Bogdan Trif on 02-11-2017 , 8:23 PM.
# © o(^_^)o  Solved by Bogdan Trif  @       Completed on Thu, 2 Nov 2017, 23:26
#The  Euler Project  https://projecteuler.net
'''
Digital root clocks         -           Problem 315

p315_clocks.gif
Sam and Max are asked to transform two digital clocks into two "digital root" clocks.
A digital root clock is a digital clock that calculates digital roots step by step.

When a clock is fed a number, it will show it and then it will start the calculation,
showing all the intermediate values until it gets to the result.
For example, if the clock is fed the number 137, it will show: "137" → "11" → "2"
and then it will go black, waiting for the next number.

Every digital number consists of some light segments: three horizontal (top, middle, bottom)
and four vertical (top-left, top-right, bottom-left, bottom-right).
Number "1" is made of vertical top-right and bottom-right,
number "4" is made by middle horizontal and vertical top-left,
top-right and bottom-right. Number "8" lights them all.

The clocks consume energy only when segments are turned on/off.
To turn on a "2" will cost 5 transitions, while a "7" will cost only 4 transitions.

Sam and Max built two different clocks.

Sam's clock is fed e.g. number 137: the clock shows "137", then the panel is turned off,
then the next number ("11") is turned on,
then the panel is turned off again and finally the last number ("2") is turned on and, after some time, off.
For the example, with number 137, Sam's clock requires:

"137"	:	(2 + 5 + 4) × 2 = 22 transitions ("137" on/off).
"11"	:	(2 + 2) × 2 = 8 transitions ("11" on/off).
"2"	:	(5) × 2 = 10 transitions ("2" on/off).

For a grand total of 40 transitions.
Max's clock works differently. Instead of turning off the whole panel,
it is smart enough to turn off only those segments that won't be needed for the next number.
For number 137, Max's clock requires:

"137"  :  2 + 5 + 4 = 11 transitions ("137" on)
            7 transitions (to turn off the segments that are not needed for number "11").
"11"  :  0 transitions (number "11" is already turned on correctly)
            3 transitions (to turn off the first "1" and the bottom part of the second "1";
            the top part is common with number "2").

"2"     :   4 transitions (to turn on the remaining segments in order to get a "2")
            5 transitions (to turn off number "2").
For a grand total of 30 transitions.

Of course, Max's clock consumes less power than Sam's one.
The two clocks are fed all the prime numbers between A = 10^7 and B = 2×10^7.
Find the difference between the total number of transitions needed by Sam's clock and that needed by Max's one.

'''

import time, zzz

def prime_sieve_generator(lower, upper):      #FIFTH FASTEST
    """  Sieve of Eratosthenes
    Create a candidate list within which non-primes will be marked as None.         """
    cand = [i for i in range(3, upper + 1, 2)]
    end = int(upper ** 0.5) // 2

    # Loop over candidates (cand), marking out each multiple.
    for i in range(end):
        if cand[i]:
            cand[cand[i] + i::cand[i]] = [None] * ( (upper // cand[i]) - (upper // (2 * cand[i])) - 1 )

    # Filter out non-primes and return the list.
    return  [ i for i in cand if i and i > lower ]


def digital_root_steps2(n) :   # Digital Root of a number
    '''':Description: It is performed step by step as it is requested by the problem

    https://en.wikipedia.org/wiki/Digital_root#Congruence_formula    '''
    N = [ n ]
    n = str(n)
    while len(str(n)) > 1 :
        dr = 0
        for i in n :
            dr += int(i)
        # print(dr)
        N.append(dr)
        n = str(dr)
    return N

def digital_root_steps(n) :   # Digital Root of a number   # Is a little faster than the string version
    '''':Description: It is performed step by step as it is requested by the problem

    https://en.wikipedia.org/wiki/Digital_root#Congruence_formula    '''
    N = [ n ]
    r = n
    while r > 9:
        root=0
        while n:
            root += n % 10
            n //= 10
            # print(n, root)
        N.append(root)
        r = n = root

    return N


print( digital_root_steps(137) )
print( digital_root_steps(19999963) )

Sam_clock = { 0 : 6,    1 : 2 ,     2 : 5,     3 : 5,    4 : 4,    5 : 5,     6: 6,     7 : 4 ,     8 : 7,    9 : 6  }

Max = { 0 : 2+4+8+32+64+128,    1: 8+64, 2: 2+8+16+32+128,    3 : 2+8+16+64+128,     4: 4+8+16+64 ,
           5: 2+4+16+64+128,   6: 2+4+16+32+64+128, 7: 2+4+8+64,   8: 2+4+8+16+32+64+128,     9: 2+4+8+16+64+128  }

# Another simple version could have been :

# Max = { 0 : 1110111,   }            # AND SO ON

def Max_enc(Max) :      # We use bitwise XOR to represent bits (line) conversions from one digit to another
    M = dict()

    for k, v in Max.items() :
        for l, u in Max.items() :
            res = bin(u ^ v)            #   bitwise XOR
            M[  str(k)+str(l)   ] = str(res).count('1')
            # print(' k , l  = ', k, l  ,'             v , u = ', v , u ,'         u^v = ' , res ,'       ', str(res).count('1') )

    return M

Max_clock = Max_enc(Max)
print('\nMax_enc : \n' , Max_clock )

def Sam_transition_cost(n, Sam_clock ) :
    L = digital_root_steps( n )
    cost = 0
    for i in L :
        for s in str(i) :
            cost += Sam_clock[int(s) ] *2

    return cost

print('\nSam_transition_cost : \t', Sam_transition_cost( 137, Sam_clock ),'\n' )

def Max_transition_cost(n, Sam_clock ,Max_clock ) :
    L = digital_root_steps( n )
    cost = sum( [ Sam_clock[ int(z)] for z in str(n)    ] )
    for i in range( len(L)-1 ) :
        l1, l2 = len(str(L[i])) ,  len(str(L[i+1]))
        if l1 > l2 :
            cost1 =  sum([ Sam_clock[ int(b) ] for b in  str( L[i])[: l1-l2 ] ])
            # print('cost 1 :   ', l1, l2 ,'         cost 1 =   ' ,cost1  ,     '   numbers = ' , str( L[i])[: l1-l2 ] )
            cost3 = sum( [ Max_clock[  str(L[i])[-l2::][j] + str(L[i+1])[-l2::][j]   ]  for j in range(l2) ] )
            # print('cost 3 :   ', l1, l2 ,'         cost 3 =   ' ,cost3  ,     '   numbers = ' , str( L[i])[-l2::]  , str( L[i+1])[-l2::]   )
            # print ( [  str(L[i])[-l2::][j] + str(L[i+1])[-l2::][j]   for j in range(l2) ]  )
            cost += cost1 + cost3

        if l1 == l2 :
            cost2 = sum( [ Max_clock[ str(L[i])[j] + str(L[i+1])[j] ]  for j in range(l1) ] )
            cost += cost2
            # print('cost 2 :   ', l1, l2 ,'         cost 2 =   ' ,cost2  ,     '   numbers = ' ,  L[i] ,  L[i+1]  )

    # print( Sam_clock[int(str(L[-1]) ) ] )

    cost += Sam_clock[int(str(L[-1]) ) ]

    return cost

print('\nMax_transition_cost : \t', Max_transition_cost( 137, Sam_clock, Max_clock ))
print('\nMax_transition_cost : \t', Max_transition_cost( 19999963, Sam_clock, Max_clock ))




print('\n--------------------------TESTS------------------------------')
t1  = time.time()




t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000 , 4), 'ms\n\n')

print('\n================  My FIRST SOLUTION,  50 sec  ===============\n')
t1  = time.time()



def pb315_Digital_root_clocks():
    primes = prime_sieve_generator(10**7, 2*10**7)
    # print(len(primes) , primes[:3] , primes[-3::])

    S, M = 0, 0
    for p in primes :
        feed_Sam = Sam_transition_cost(p, Sam_clock)
        feed_Max = Max_transition_cost(p, Sam_clock, Max_clock)
        S += feed_Sam
        M += feed_Max
        # print(str(p)+'.           Sam =   '  ,  feed_Sam ,'            Max =  ', feed_Max   )

    return print('\nANSWER :  Total diff between Sam and Max =  ' , S-M  )    #   ANSWER  =   13625242    Completed in : 61.1015 s

# pb315_Digital_root_clocks()


t2  = time.time()
print('\n# Completed in :', round((t2-t1), 4), 's\n\n')


print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1,   --------------------------')
t1  = time.time()

# === Mon, 1 Jun 2015, 06:27, wakkadojo, USA
# Lets call this one a "confidence booster" :)

def solution_1() :

    """
    Orientation of segments
               0
             1   2
               3
             4   5
               6
    """

    seg = [ [1, 1, 1, 0, 1, 1, 1],  # 0
                [0, 0, 1, 0, 0, 1, 0],  # 1
                [1, 0, 1, 1, 1, 0, 1],  # 2
                [1, 0, 1, 1, 0, 1, 1],  # 3
                [0, 1, 1, 1, 0, 1, 0],  # 4
                [1, 1, 0, 1, 0, 1, 1],  # 5
                [1, 1, 0, 1, 1, 1, 1],  # 6
                [1, 1, 1, 0, 0, 1, 0],  # 7
                [1, 1, 1, 1, 1, 1, 1],  # 8
                [1, 1, 1, 1, 0, 1, 1] ] # 9

    def intersection (a, b): # segment overlap between a and b
        return sum (seg[a][i]*seg[b][i] for i in range (len (seg[a])))

    def sieve (m, n):
        s = [ False if i % 2 == 0 else True for i in range (n) ]
        if 2 >= m:
            yield 2
        for i in range (3, n):
            if s[i]:
                if i >= m:
                    yield i
                for j in range (i*i, n, i):
                    s[j] = False

    def save (p): # amount saved for an input number p
        saved, s1 = 0, str (p)
        while p >= 10:
            p = sum (int (x) for x in s1) # step the digital root
            s1, s2 = str (p), s1
            # save 2x for turning off and turning on
            saved += 2*sum (intersection (int(s1[-i-1]), int(s2[-i-1])) \
                for i in range (len (s1)))
        return saved

    return print (sum (save (p) for p in sieve (10**7, 2*10**7)))

t2  = time.time()
print('\n# Completed in :', round((t2-t1) , 2), 's\n\n')


print('\n--------------------------SOLUTION 2,   --------------------------')
t1  = time.time()


t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')


# print('\n--------------------------SOLUTION 3,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 4,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 5,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 6,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 7,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 8,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 9,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 10,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 11,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 12,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')




