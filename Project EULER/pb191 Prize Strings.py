#!/usr/bin/python
# Solved by Bogdan Trif @   Completed on Fri, 3 Feb 2017, 15:19
#The  Euler Project  https://projecteuler.net           ( ͡° ͜ʖ ͡°)
'''
            Prize Strings       -       Problem 191

A particular school offers cash rewards to children with good attendance and punctuality.

If they are absent for three consecutive days or late on more than one occasion then they forfeit their prize.

During an n-day period a trinary string is formed for each child consisting of :
            L's (late),             O's (on time),          and A's (absent).

Although there are 81 trinary strings for a 4-day period that can be formed, exactly 43 strings would lead to a prize:

OOOO OOOA OOOL OOAO OOAA OOAL OOLO OOLA OAOO OAOA
OAOL OAAO OAAL OALO OALA OLOO OLOA OLAO OLAA AOOO
AOOA AOOL AOAO AOAA AOAL AOLO AOLA AAOO AAOA AAOL
AALO AALA ALOO ALOA ALAO ALAA LOOO LOOA LOAO LOAA
LAOO LAOA LAAO

How many "prize" strings exist over a 30-day period?

'''
import time, gmpy2
import itertools


def comb_L( k ) :       # Counts how many LL'are. Works well !!!
    S = 0
    for i in range(2, k+1):
        c = gmpy2.comb(k, i)
        # print(c, S)
        S+=c * 2**(k - i)
    return S

def comb_A_deactivated(n) : # Counts how many AAA's without L's !!!! NEEDS FIXING !!
    k  = n-2
    return k * 2**(k-1) #   - (k-1)*2**(k-2) - (k-4)*2**(k-5)

def comb_AO(n) : # Counts how many AAA's & O's without L's
    if n < 3: return 0
    if n < 7 :
        return (n-2) * 2**(n-3) - (n-3) * 2**(n-4)

    if n >= 7:
        S=(n-2) * 2**(n-3)
        for i in range(n-1, 2, -1):
            if n-i <= 3 :
                S-=comb_A(i)
            else :
#                 print(i, n-i, comb_A(i) ,comb_A(i)*2**(i-2) )
                S-=comb_A(i)*2**(n-i-3)
        return S


def comb_A1L(n) :       # Counts how many AAA and 1L are. Doesn't work as expected !!!!
    L = [1, 2]
    k  = n-2
    x =  k * 3**(k-1) - (k-1)*3**(k-2)
    for i in range(n-4) :
        L.append(L[-1]+ 2**i)
        L.append(L[-2]+L[-1])
    L.reverse()
    # print(L)
    S, k = 0,  0
    for j in range(n-2, 1, -1):
        ab = 2*L[k] + (j-2)*L[k+1]
        # print(j , 2*L[k] , (j-2)*L[k+1] )
        S+=ab
        k+=2
    return S+1




print('\n--------------------------TESTS------------------------------')
t1  = time.time()

print('Total available possibilities : \t',3**30)

def brute_force_check( days ) :

    marks = [ 'O', 'L' , 'A' ]
    C = [p for p in itertools.product( marks, repeat=days) ]
    print( len(C), C[0:100] ,'\n--------------')

    cnt, itr = 0, 0
    for i in range(len(C)):
        s = ''.join(C[i])
        a = s.find('AAA')
        l = s.count('L')
        # print(a, l, s)
        if a != -1 or l>=2 :
            cnt+=1
        # if l<= 1 and ( s.find('O') == 0 or s.find('L') == 0 ) and s.find('A') != 1  :
        # if l <= 1 and s.find('A') != 0 :
            if l == 1 :
                itr +=1

                print(str(cnt)+'.       ' , a, l, '      ',s,'        ', itr)

    return print('\nPrize string WINS = ' , len(C)-cnt, '           Losses :   ', cnt , '            Total comb=', len(C) )


nr = 5

brute_force_check(nr)

print('\ncomb_L : \t', comb_L(nr))

print('\ncomb_A : \t', comb_AO(nr))

print('\ncomb_A1L : \t', comb_A1L(nr))

# 3             27 : 8 /  19
# 4             81 : 43 / 38
# 5             243 :94 /149
#  6                729 : 200 529
#   7               2187 : 418 /1769
# 8                 6561 : 861 /5700
# 9               19683 : 1753 17930
# 10             59049 : 3536 55513
# 11            177147 : 7077 170070
# 12           531441 : 14071 517370
# 15      Total comb= 14348907    WINS =  107236     Losses :    14241671



# I’d proceed in three steps:           #v Did not succeed
#
# First, count the strings of length 30 with two or more Ls in them.
# The non-L spots in these strings can filled any whichway.
# They can even have runs of three or more As in a row—it doesn’t matter.
#
# Second, count all of the strings with runs of As in them that also don’t have any Ls.
# So we’re just considering the length-30 strings with some mix of Os and As,
# and counting only the ones that include three or more As in a row.
#
# Finally, count all of the strings with three or more As in a row
# that also have exactly one L in them.


############## GENERAL IDEAS ################
'''
===== Tue, 29 Apr 2008, 23:57, rayfil, Assembly  , Canada
There are only 6 states in which strings can exist, divided into two groups.

Three of those states are those where the strings don't contain any LATE occurence.
The other three are those where the strings already contain one LATE occurence.

Within each group, one state is when the string does not end with an absence,
another when the string ends with only one absence, and the third when the string
ends with two absences. Let's denote them as O, Oa, Oaa, L, La and Laa.
Let's denote the sums of these two groups as SO and SL.
I.   On time O combined with absences
    === STRING ENDINGS ===
O - On time & no absence
Oa - On time & one abscence
Oaa - On time &  string ending with two abscences
II.  Late occurences combined with absences
    === STRING ENDINGS ===
L - Late occurence
La - Late occurence & 1 absence
Laa - Late occurence & 2 absences

The initial states after the first day would be O=1, Oa=1 and L=1(all other states =0).
The initial sums would be SO=2 and SL=1.
a) If ABSENT on the following day :
    -   all strings in state Oa would become Oaa strings
    -    all strings in state O would become Oa strings.
    Similarly, 
    -   all strings in state La would become Laa strings and
    -   all strings in state L would become La strings.

b) If LATE on the following day, all strings in group O would become L strings.

c) If neither late nor absent on the following day, all strings in group O would become O strings (O=SO),
and all strings in group L would become L strings in addition to (b) above such that L=SL+SO.

The following algo should produce the answer within 1 ms with most (if not all) programming languages.
zeycus and logopetria have already posted similar algos in their own programming language.

'''


# =====Fri, 2 May 2008, 21:48, easyway
# This is just a variation of problem 164.  I simply modified my Ruby code for that one.

# ===Wed, 4 Jun 2008, 05:45, CRGreathouse, USA
# There are only six cases (absent 0, 1, or 2 times in preceding days; has been/has never been late),
# so I just did it in a spreadsheet.  It took about 2 minutes to write; runtime: < 10 ms.

# === Thu, 4 Sep 2008, 15:13, TheRequiem, Canada
# I also used the 6-state machine, counting the number of strings starting with 0, 1 or 2 A's, and with or without an L in them.


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n==========  My FIRST SOLUTION, DYNAMIC PROGRAMMING, Cheating ,Stolen Internet  ===============\n')
t1  = time.time()

# 2017-02-03 - After a whole week trying desperately to find the solution I ceased the temptation
# and looked for solutions on the internet. First idea I came across, similar to mine was too complicated !
# Second idea was this magnificent solution which is NOT MINE ! Dynamic Programming

#################     Approach -  Finite State  Machine Automata   ##############

                # _________  |             0A              |           1A             |            2A            |
                #     1L       |              A               |            B              |               C            |
                #     0L       |              C               |            D              |               F            |

                #                                 First day :       STATES   # Remark : Only 3 possibilities : O, A, L
                # _________  |             0A              |           1A             |            2A            |
                #     1L       |              1               |            0              |               0            |
                #     0L       |              1               |            1              |               0            |
                #
                #                                           Next day :  STATES
                # __________|               0A             |           1A             |            2A            |
                #     1L       |  A+B+C+D+E+F     |            A              |               B            |
                #     0L       |         D+E+F           |            D              |               E            |

### The ABOVE IMPLEMENTATION
def pb191_finite_state_automata_machine(days):

    A , B, C , D, E, F = 1, 0, 0, 1, 1, 0
    for i in range(2, days+1 ):
        tA = A+B+C+D+E+F
        tB = A
        tC = B
        tD = D + E + F
        tE = D
        tF = E
        A, B, C, D, E, F = tA, tB, tC, tD, tE, tF
        S = A+B+C+D+E+F
        print('day: '+str(i)+'   ', A, B, C, D, E, F , S)

    return print('\nAnswer : \t', S)

pb191_finite_state_automata_machine( 30 )             #   Answer : 	 1918080160


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n-------------          My SECOND SOLUTION ----------------')

'''
===== Tue, 29 Apr 2008, 23:57, rayfil, Assembly  , Canada
There are only 6 states in which strings can exist, divided into two groups.

Three of those states are those where the strings don't contain any LATE occurence.
The other three are those where the strings already contain one LATE occurence.

Within each group, one state is when the string does not end with an absence,
another when the string ends with only one absence, and the third when the string
ends with two absences. 
Let's denote them as O, Oa, Oaa, L, La and Laa.
Let's denote the sums of these two groups as SO = O + Oa + Oaa and SL = L + La + Laa
I.   On time O combined with absences
    === STRING ENDINGS ===
O - On time & no absence
Oa - On time & one abscence
Oaa - On time &  string ending with two abscences
II.  Late occurences combined with absences
    === STRING ENDINGS ===
L - Late occurence
La - Late occurence & 1 absence
Laa - Late occurence & 2 absences

The initial states after the first day would be O=1, Oa=1 and L=1(all other states =0).
The initial sums would be SO=2 and SL=1.
a) If ABSENT on the following day :
    -   all strings in state Oa would become Oaa strings
    -   all strings in state O would become Oa strings.
    Similarly, 
    -   all strings in state La would become Laa strings and
    -   all strings in state L would become La strings.

b) If LATE on the following day, all strings in group O would become L strings.

c) If neither late nor absent on the following day :
 -  all strings in group O would become O strings (O=SO), AND
-  all strings in group L would become L strings in addition to (b) above such that L=SL+SO.


#################     Approach -  Finite State  Machine Automata   ##############
                # _________  |             0A              |           1A             |            2A            |
                #     0L       |              A               |            B              |               C            |
                #     1L       |              C               |            D              |               F            |

                #                                 First day :   STATES      # Remark : Only 3 possibilities : O, A, L
                # _________  |             0A              |           1A             |            2A            |
                #     0L       |              1               |            1              |               0            |
                #     1L       |              1               |            0              |               0            |
                #
                #                                           Next day :  STATES
                # __________|              0A             |           1A             |            2A            |
                #     0L       |          A+B+C          |            A              |              B            |
                #     1L       |   A+B+C+D+E+F   |            D              |               E            |

'''

def finite_state_automata_machine_2(days):

    A , B, C , D, E, F = 1, 1, 0, 1, 0, 0
    for i in range(2, days+1 ):
        tD = A+B+C+D+E+F
        tB = A
        tC = B
        tA = A + B + C
        tE = D
        tF = E
        A, B, C, D, E, F = tA, tB, tC, tD, tE, tF
        S = A+B+C+D+E+F
        print('day: '+str(i)+'   ', A, B, C, D, E, F ,'  ', S)

    return print('\nAnswer : \t', S)

pb191_finite_state_automata_machine( 30 )             #   Answer : 	 1918080160


print('\n--------------------------Recursion, without MEmoization  --------------------------')

def school( r, a, l ) :
# > option remember;
    if a==3 : return 0
    if l==2 : return 0
    if r==0 : return 1

    return school( r-1, 0, l ) + school( r-1, 0, l+1 ) + school( r-1, a+1, l )

# school(10,0,0)

print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1, Dynamic Programming  --------------------------')
t1  = time.time()

# ==== Sat, 26 Apr 2008, 08:34, zeycus, Spain
# I thought of an automata with 6 states, representing how many consecutive As are
# in the end of the string (0, 1 or 2), and whether or not the L has already appeared.
# It seems exactly the same as brock_lee did. That leads to the straightforward algorithm below.

n = 30
(v_0, v_1, v_2, v_L0, v_L1, v_L2) = (1, 1, 0, 1, 0, 0)
for _ in range(1, n):
    (v_0, v_1, v_2, v_L0, v_L1, v_L2) = (
        v_0 + v_1 + v_2,
        v_0,
        v_1,
        v_0 + v_1 + v_2 + v_L0 + v_L1 + v_L2,
        v_L0,
        v_L1)

print (sum([v_0, v_1, v_2, v_L0, v_L1, v_L2]))


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 2, RECURSION with Memoization,  Super Interesting  --------------------------')
t1  = time.time()

# ====Sat, 26 Apr 2008, 03:49, quilan, USA
# Borderline trivial memoized function.

f_db={}
def func(left,nl,na):
    if(nl>=3): return 0
    if(na>1): return 0
    if(left<=0): return 1

    key= "%d %d %d" % (left,nl,na)
    if(key in f_db): return f_db[key]

    total=0;
    total+=func(left-1, 0, na)
    total+=func(left-1,nl+1, na)
    total+=func(left-1, 0, na+1)

    f_db[key]=total
    return total

#===================

total=func(30,0,0);
print ("Total: %d"%total)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 3, Dynamic Programming  --------------------------')
t1  = time.time()

# =====Sat, 26 Apr 2008, 13:38, anceps, Switzerland
#
# As we're allowed only one L, I counted first possibilities with only O's and A's: that lead me to the formula for n days
# (*) R(n) = R(n-1) + R(n-2) + R(n-3)
# R(0)=1, R(1)=2 ('A', 'O'), R(2)=4, R(3)=7
#
# If S(n) is the number of possibilities with one 'L', you have
# (**) S(n) = R(0)*R(n-1) + R(1)*R(n-2) + ... + R(n-1)*R(0)
#
# And, of course, the solution T(n) = R(n) + S(n).
#
# Details:
# (*) R(n) = possibilities with only A and O, which is the sum of:
#     - possibilities starting with 0 = R(n-1)
#     - possibilites starting with AO = R(n-2)
#     - possibilites starting with AA0 = R(n-3)
#
# (**) S(n) = possibilities with one L, which is the sum of possibilities for each position of L in [0,n].
#     - possibilities with L at position k = R(k-1)*R(n-k)

N=30

f = (N+1) * [0]
f[0]=1
f[1]=2
f[2]=4

for i in range(3,N+1):
    f[i] = f[i-1] + f[i-2] + f[i-3]

print (f[N] + sum([ f[i] * f[N-1-i] for i in range(N) ]))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 4,   --------------------------')
t1  = time.time()

# === Sat, 26 Apr 2008, 15:47, logopetria, England

# After a bit of pen-and-paper work, this turns out to be nice and simple.
# Let f(n,L,A) be the number of strings of length n with L 'L's and ending in exactly A 'A's.
#
# We build up valid strings by starting with the empty string and appending either an 'A','O' or 'L' at each step.
# The prize-winning strings are those with L=0 or 1 and A=0,1, or 2.
# In moving from length-n strings to length-(n-1) strings, there are 3 cases to consider:
#
# (i) a string ending in exactly 1 'A' or 2 'A's can be made in just one way,
# by appending an 'A' to a string ending in exactly 0 or 1 'A's respectively.
#        f(n,L,1) = f(n-1,L,0) ;   f(n,L,2) = f(n-1,L,1)
#
# (ii) a string with no 'L's ending in no 'A's must end in 'O'; its prefix must contain no 'L's and can end in 0, 1 or 2 'A's.
#        f(n,0,0) = sum_{A=0..2} f(n-1,0,A)
#
# (iii) a string with 1 'L' ending in no 'A's must either end in 'O' or 'L'.
# In either case, its prefix can end with 0,1 or 2 'A's, as above.  If the string ends in 'L',
# its prefix must contain no 'L'; whereas if the string ends in 'O', its prefix must contain exactly 1 'L'.
#        f(n,1,0) = sum_{L=0..1} sum_{A=0..2) f(n-1,L,A)
# (So every prize-winning string of length n-1 can be extended to another prize-winning string in exactly 1 way.)
#
# Thus, denoting the 6 values of f(n,L,A) by:
#        [p,q,r,s,t,u] = [f(n,0,0), f(n,0,1), f(n,0,2), f(n,1,0), f(n,1,1), f(n,1,2)]
# we get the 6 values of f(n+1,L,A) by:
#        [(p+q+r), p, q, (p+q+r+s+t+u), s, t]
#
# The initial case at 0 days is clearly:
#     f(0,0,0)=1; f(0,L,A)=0 otherwise
#
# The total number of prize-winning strings of length n+1 is the sum of these 6 values;
# but the above formula shows that we can work this out just by iterating for one more day
# and returning the value of f(n,1,0).
# So the program itself is very simple and pretty quick:

def f(days):
    [p,q,r,s,t,u] = [1,0,0,0,0,0]
    for n in range(days+1):
        [p,q,r,s,t,u] = [(p+q+r), p, q, (p+q+r+s+t+u), s, t]
    return s

print (f(30))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 5,   --------------------------')
t1  = time.time()

# ===Sat, 26 Apr 2008, 16:22, Taifu, Italy
#
# I used a different approach.
# I calculated probability not having 3 "A" in a row using tribonacci numbers.
# Then I cycled "L" in each position multiplying probability not having 3 "A" before
# and after it and first cycle calculate probability not have any "L".
# It runs in no time :-)

def p191(days):
    cache_tribonacci = {0:0, 1:0, 2:1}
    def tribonacci(n):
        try:
            return cache_tribonacci[n]
        except:
            t = tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3)
            cache_tribonacci[n] = t
            return t

    def not_three_or_more(n):
        return tribonacci(n+3)

    def winnings(days):
        wins = 0
        for late in range(0, days + 1):
            if late == 0:
                wins += not_three_or_more(days - late)
            else:
                wins += not_three_or_more(late - 1) * not_three_or_more(days - late)
        return wins

    return winnings(30)

print (p191(30))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 6, recursive state-machine  --------------------------')
t1  = time.time()

# === Mon, 28 Apr 2008, 12:26, nestorpb85, Cuba
# Bottom-up memoization in Python using a recursive state-machine sort of approach, instant answer:

# prize string parameters
max_con_as = 2
max_num_ls = 1
n = 30

""" 3-dimensional table to memoize results of the number of
prize strings given how much into the string is already fixed,
the number of consecutive As and the total number of Ls
table[p][A][L] is the number of different prize strings that start
at p given A and L so far"""
table = [[[-1 for k in range(0, max_num_ls + 1)]
			for j in range(0, max_con_as + 1)]
				for i in range(0, n)]

def count_strings(n):
    """ Counts all the possible prize strings in an n-day period.
	There are a total of 3^n possible strings.
	A prize string satisfies:
	- has less than 2 (L)ates and
	- doesn't have 3 or more consecutive (A)bsences anywhere and
	- The rest are (O)n-times.
	P.S: As a counting problem it gets a bit tricky after n goes past
	n = 7 or 8 because of the consecutive As. """

    return aux_count(n, 0, 0, 0)

def aux_count(n, i, num_con_as, num_ls):
	""" Recursively count the prize strings and memoize the results.
	Assumes the string is valid when called (i.e. num_con_as and num_ls
	are in range). """

	global table

	if table[i][num_con_as][num_ls] != -1:
		return table[i][num_con_as][num_ls]

	if i == n - 1:		# last position

		# can always fill with 'O' and make it a prize string
		total = 1

		if num_ls < max_num_ls:     # can fill with 'L'
			total = total + 1

		if num_con_as < max_con_as: # can fill with 'A'
			total = total + 1

	else:
		# add O, consecutive A chain broken
		total = aux_count(n, i + 1, 0, num_ls)

		if num_ls < max_num_ls:
			# add L, consecutive A chain broken
			total = total + aux_count(n, i + 1, 0, num_ls + 1)

		if num_con_as < max_con_as:
			# add A, consecutive A chain now longer
			total = total + aux_count(n, i + 1, num_con_as + 1, num_ls)

	table[i][num_con_as][num_ls] = total
	return total


print ("The number of prize strings of length", n, "is", count_strings(n))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 7,   --------------------------')
t1  = time.time()

# ===Fri, 18 Jul 2008, 22:21, paradox, Bulgaria
# #http://mathworld.wolfram.com/Run.html
# hmmm, don't even know what is DP, but i knew (math sense tingling) there is a a simple recursion on n
# (i was even hopping for closed form).
# From there on it was a matter of good google searches, to hit the Tribonaci numbers.
# Whose recursion gave me idea how to thing about the problem right (erasing the last A sequence)
# and how to expand it for that annoying L (admittedly if the Ls are more this method would not work well).


#http://mathworld.wolfram.com/Run.html
Trib=[1,2,4]
TribL=[0,1,4]
N=30
for i in range(4,N+2):
    Trib.append(Trib[-1]+Trib[-2]+Trib[-3])
    TribL.append(Trib[-1]+TribL[-1]+TribL[-2]+TribL[-3])
print (Trib[N]+TribL[N])

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 8,   --------------------------')
t1  = time.time()

# ==== Sun, 5 Oct 2008, 11:15, elpres, Germany
# Trivial solution with linear runtime. 'sums' contains the number of possibilities to build a string of n characters
# from 'O' and 'A' with at most 2 'A's in a row.
# The 'possib' array keeps track of the last two characters for this purpose.
# Strings ending with 'AA' may only be extended with 'O'.
# Then just add 'sums[30]' (strings with no 'L') and (sums[n] * sums[29 - n] for n in [0, 29]) (strings with one 'L')

sums = {0: 1, 1: 2}

# possib contains numbers of strings ending with the 4 possible 2-char combinations.
# to get the number of combinations for n + 1, append '0' and 'a' and skip 'aa' + 'a'
# ['00', '0a', 'a0', 'aa']
possib = [1, 1, 1, 1] # initialized for n = 2

top = 30
for i in range(2, top + 1):
    sums[i] = sum(possib)
    possib = [possib[0] + possib[2], possib[0] + possib[2], possib[1] + possib[3], possib[1]]

for i in range(top):
    total += sums[i] * sums[top - 1 - i]
print (total)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 9, Recursion  --------------------------')
t1  = time.time()

# === Fri, 28 Jun 2013, 06:27, forretrio, Switzerland
# Recursion by first finding the combinations of O/A, then add the variation of L.

def p271(N):
    prize = [[1,0],[0,1],[0,0]]
    while len(prize[0]) < N+1:
        (a,b,c) = prize
        d = []
        for i in range(len(a)):
            d.append(a[i]+b[i]+c[i])
        d = d + [0]
        e = [0] + a
        f = [0] + b
        prize = [d,e,f]
    s = 0
    for i in range(N+1):
        s += (N+1-i)*(prize[0][i]+prize[1][i]+prize[2][i])
    return s

print (p271(30))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 10, AUTOMATA with 6 states  --------------------------')
t1  = time.time()

# === Mon, 3 Nov 2008, 07:03, MrDrake, Australia
# Automata time!

state = [1, 1, 0, 1, 0, 0, 0]

for i in range(29):
    temp = [0, 0, 0, 0, 0, 0, 0]

    temp[0] = state[0] + state[1] + state[2]
    temp[1] = state[0]
    temp[2] = state[1]
    temp[3] = state[0] + state[1] + state[2]
    temp[4] = state[3] + state[4] + state[5] + state[6]
    temp[5] = state[3] + state[4]
    temp[6] = state[5]

    state = temp

print (sum(state))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 11, STATE AUTOMATA  --------------------------')
t1  = time.time()

# === Sat, 21 Sep 2013, 02:04, Josay, France
# One of my shortest solutions. DP just like everyone else.

    # 0 consecutive a.,1 conse.,2 consecutive absences
nb =     [[1,               0,       0],        # 0 late
          [0,               0,       0]]        # 1 late
for _ in range(30):
    nb = [[sum(nb[0]),      nb[0][0],nb[0][1]], # 0 late
          [sum(nb[0]+nb[1]),nb[1][0],nb[1][1]]] # 1 late
print(sum(nb[0]+nb[1]))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 12,   --------------------------')
t1  = time.time()

# === Thu, 17 Oct 2013, 12:10, Zweedeend, Netherlands
# I used two recursive functions in Python. One counting the number of ways never to be late,
# and another counting the number of ways to be late at most once:

from functools import lru_cache as memoize

@memoize(maxsize=None)
def nl(n):  #Never Late
    """Return the number of ways to never be late
    e.g. for n = 4, the possibilities are:
    O       * nl(3)
    AO      * nl(2)
    AAO     * nl(1)
    """
    if n < 3:
        return 2**n
    return nl(n-1) + nl(n-2) + nl(n-3)

@memoize(maxsize=None)
def amlo(n):  # At Most Late Once
    """Return the number of ways to be late at most once
    e.g. for n = 4, the possibilities are:
    O       * amlo(3)
    L       * nl(3)
    AO      * amlo(2)
    AL      * nl(2)
    AAO     * amlo(1)
    AAL     * nl(1)
    """
    if n < 2:
        return 3**n
    if n == 2:
        return 8
    return nl(n-1) + amlo(n-1) + nl(n-2) + amlo(n-2) + nl(n-3) + amlo(n-3)

print(amlo(4))
print(amlo(30))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 13, Tranzition Matrix, Neeed to study it --------------------------')
t1  = time.time()

# === Sun, 18 May 2014, 18:52, Paul Crowley, England

transition_matrix = [
    [1, 1, 1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 1, 1, 2, 3],
]

count = [1, 0, 0, 0, 0, 0, 0]

for i in range(30):
    count = [sum(a*b for a, b in zip(r, count)) for r in transition_matrix]
    print (count, sum(count[:-1]))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 14, Recurstion with Memoization  --------------------------')
t1  = time.time()

# === Tue, 7 Jul 2015, 20:32, Panphobia, Croatia
# dynamic programming, recursion with memoization to be exact

cache={}
possible = ["O","L","A"]
def rec(N,lates,lastTwo):
    sums=0
    if N==0:
        return 1
    key = (N,lates,lastTwo)
    if key in cache:
        return cache[key]
    for i in possible:
        if i=="L" and lates < 1:
            sums+=rec(N-1,lates+1,lastTwo[1::]+i)
        elif i=="A" and lastTwo != "AA":
            sums+=rec(N-1,lates,lastTwo[1::]+i)
        elif i=="O":
            sums+=rec(N-1,lates,lastTwo[1::]+i)
    cache[key]=sums
    return sums
print (rec(30,0,"FF"))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 15, lru_cache Recursion with memoization  --------------------------')
t1  = time.time()

# === Thu, 7 Apr 2016, 04:10,ivan.orlov

D = 30

from functools import lru_cache as memoize
@memoize(maxsize=None)

def f(n, a, l):
    if n == 0:
        return 1
    ans = f(n - 1, 0, l)  # O
    if l == 0:
        ans += f(n - 1, 0, 1) # L
    if a < 2:
        ans += f(n - 1, a + 1, l) # A
    return ans

print( f(D, 0, 0) )

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 16,   --------------------------')
t1  = time.time()

# ==== Sun, 4 Dec 2016, 20:11. Andratx
# Among the posts I read I didn't see any answer that counted the sequences with no prize
# and then subtracted those from the total number of strings.
# Since this was my approach I thought it would be worth sharing it.
# The code is very likely not to be as efficient as it could be.
# I also included many comments so that the code is self-explanatory:

#---------------------------------------------------#
# How many strings with no L have at least one AAA? #
#---------------------------------------------------#
def f(n):
    if n<=2:
        return 0
    if n==3:
        return 1

    #O followed by strings of length n-1 containing AAA: f(n-1)
    #A followed by strings of length n-1 containing AAA: f(n-1)
    #A followed by strings of length n-1 starting with AAO and not containing AAA: 2**(n-4)-f(n-4)

    return 2*f(n-1)+2**(n-4)-f(n-4)

#----------------------------------------------------#
# How many strings with one L have at least one AAA? #
#----------------------------------------------------#
def g(n):
    total=0
    for j in range(n):
        #Strings with AAA before position j: 2**(n-j-1)*f(j)
        #Strings with AAA after position j: 2**j*f(n-j-1)
        #Strings with AAA before and after position j: f(j)*f(n-j-1)

        total+=2**(n-j-1)*f(j)+2**j*f(n-j-1)-f(j)*f(n-j-1)

    return total

#-------------------------------#
# How many prizes are in total? #
#-------------------------------#
def prizes(n):
    #Strings with no L: 2**n
    #Strings with one L: n*2**(n-1)
    return 2**n-f(n)+n*2**(n-1)-g(n)

#-----------------------------------------------#
# How many prizes are there in 30 days strings? #
#-----------------------------------------------#
print (prizes(30))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


