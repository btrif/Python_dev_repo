#  Created by Bogdan Trif on 25-09-2017 , 2:52 PM.
# © o(^_^)o  Solved by Bogdan Trif  @       Completed on Fri, 3 Nov 2017, 23:41
#The  Euler Project  https://projecteuler.net
'''
               Under The Rainbow       -       Problem 493

70 colored balls are placed in an urn, 10 for each of the seven rainbow colors.

What is the expected number of distinct colors in 20 randomly picked balls ?

Give your answer with nine digits after the decimal point (a.bcdefghij).


'''
import time, zzz, random
from gmpy2 import comb

C = 'ROYGBIV'
Colors = list(C)
print(Colors)


print('\n--------------------------TESTS------------------------------')
t1  = time.time()
# Here we use Monte Carlo only to estimate the Expected number with 1,2 decimals

def Monte_Carlo_simulation( runs) :
    S = 0
    for run in range(runs) :
        Urn = Colors *10
        Picked = []
        for i in range(20) :
            L = len(Urn)
            # print( L ,'   '  ,Urn)
            r = random.randint(0, L-1 )
            # print( r )
            Picked.append(Urn[r] )
            Urn.pop(r)
            # print( len(Urn) , '        len(Picked) = ', len(Picked) , '    set = ' ,set(Picked) ,'       Picked = ', Picked )
        S+= len(set(Picked))

    return print('\nExpected number of colors : \t', S /runs)

# Monte_Carlo_simulation(10**5)       # Expected number of colors : 	 6.81874


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')

print('\n===========   My FIRST SOLUTION,  Probability Theory  ===============\n')
t1  = time.time()

# We start in reverse :
# the probability that from the 20 chosen balls we do not pick a single color.
# We eliminate that color which is represented by 10 balls => 70-10 = 60 .
# And from this we must choose 20 balls
# Practically we must choose 20 from 60 --> C(60, 20) and we must multiply with
# C(70, 20) --->  the probability that we choose 20 from 70 (all the balls)


p1 = comb(60, 20)       # probability that a color is not picked from the total combinations
p2 = comb(70, 20)
prob = p1/ p2
print(' C(60, 20) = ' ,p1, ' C(70, 20) = ' , p2 )
print('\nProbability that a single color IS NOT picked : ' , prob )


# The for a single color, the probability that a color is picked is 1-prob
print('\nProbability that a single color IS picked : ' , 1- prob )

print('\nProbability that all seven colors ARE picked which is ≡ \n ≡ '
      'is the expected number of distinct colors in 20 randomly picked balls: ' )

P = 7*(1-prob)

print('\nANSWER : Expected number of distinct colors in 20 randomly picked balls : \n' ,  P )

#   ANSWER :    6.818741802




t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')

# ===== GENERAL IDEA ===========
# Interesting learning this probability stuff.  E=7⋅(1− C(60, 20)/ C(70,20))

# === Fri, 20 Nov 2015, 20:53, zookham, Sweden
# Calculating 6 + (C(70,20) − 7 * C(60,20)) / C(70,20) gives the correct answer


# ====Wed, 25 Feb 2015, 00:44, CUViper, USA
# Can anyone explain to me why this and the thing Tepsi did are equivalent?
#
# I didn't come up with Tepsi's approach either, but I think I get it now.  I'll try to rephrase how others have already explained it.
# Expected values are linear, so E(X+Y) = E(X)+E(Y), even if X and Y are not independent.
# You can think of E(#colors) = E(#reds + #oranges +...) = E(#reds) + E(#oranges) + ...
# The number of reds only has two possibilities, 0 or 1.
# Then E(#reds) = 0*p(red wasn't chosen) + 1*p(red was chosen) = p(red was chosen).
# All 7 colors have the same individual probabilities, so adding them up gives 7p.

# ==== Sat, 13 Dec 2014, 18:06, Tepsi. Hungary
# Yay! College paid off!
#
# For any given colour, the probability of it being present in the draw is :
# p=1− (C(60,20)/C(70, 20)) . The expected value of the number of colours present is just the sum
# of the expected values of the number of occurrences of the individual colours,
# which are all equal to pp (0 with probability 1−p, 1 with probability p), so the total expectation value is 7p.

# =====Sat, 13 Dec 2014, 18:53, Jonathan Paulson, USA
# Since expectation is linear, the expected number of colors is the probability that red gets picked plus the probability
# that orange gets picked ... plus the probability that violet gets picked.
# By symmetry, all these probabilities are the same, so the answer is just 7 times the probability that red gets picked.
#
# There are sixty non-red balls out of 70. So if we label all the balls, there areC (60,20) ways to pick all non-red balls,
# out of C(70,20) ways to pick 20 balls. So the probability that red is picked is
#
# 1−C(60,20)/C(70,20)
# , and the final answer is 7 times that.
#
# http://www.wolframalpha.com/input/?i=%281-+%2860+choose+20%29+%2F+%2870+choose+20%29%29+*+7


print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1,  breadth-first search, BFS , 30 sec --------------------------')
t1  = time.time()


# ==== Fri, 27 May 2016, 03:08, azax1, USA
# A reminder to myself that we don't always see the elegant way to do something...
#
# My code is essentially breadth-first search through the tree of possibilities,
# using a dictionary to keep track of elements on the frontier.
#
# Simple probability theory is, of course, a better solution. And I call myself a math major?

def BFS() :
    dic = { (0,0,0,0,0,0,0) : 1 }
    for dummy in range(20):
        newDic = { }
        for x in dic:
            arr = [ [] ] * 7
            for i in range(len(arr)):
                if x[i] < 10:
                    app = list(x)
                    app[i] += 1
                    arr[i] = tuple(app)

            for i in range(len(arr)):
                if arr[i] == []:
                    continue
                if arr[i] in newDic:
                    newDic[arr[i]] += (11 - (arr[i])[i]) * dic[x]
                else:
                    newDic[arr[i]] = (11 - (arr[i])[i]) * dic[x]

        dic = newDic

    s = 0
    a = dic.keys()
    for x in a:
        count = 0
        for i in range(len(x)):
            if x[i] != 0:
                count += 1
        s += count * dic[x]

    n = 70
    m = n
    prod = 1
    while m > n - 20:
        prod *= m
        m -= 1


    return print ((s + 0.0) / prod)


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')


print('\n--------------------------SOLUTION 2, Probability Theory  --------------------------')
t1  = time.time()

# ==== Sun, 25 Sep 2016, 13:13, Arvind Ganesh, USA
# 5 lines in python, not sure why people did crazy solutions :P

from math import factorial

def nCr(n,r):
    f = factorial
    return float(f(n) / f(r) / f(n-r))

print (str(float(7 * (1 - (nCr(60,20)) / (nCr(70,20)))))[:11])

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')


print('\n--------------------------SOLUTION 3,  RECURSION  --------------------------')
t1  = time.time()

# ====  Wed, 1 Feb 2017, 22:08, bad_dude , Australia
# Simulated all of the possible results with a recursive function.
# Each step branches off in 2 directions depending on whether a new colour is picked.

def urn(colours, picks):
  if picks == 20:
    return(colours)
  else:
    return(  (urn( colours+1,picks+1)*(70-10*colours) + urn(colours , picks+1) * (10*colours-picks)) / (70-picks))

print(urn(0, 0))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')


print('\n--------------------------SOLUTION 4,   --------------------------')
t1  = time.time()

# ===Mon, 20 Apr 2015, 02:49, joncoop1972, USA
# I just figured the probablity that an individual color appears.
# The expected value for each color is the same, so then I multiplied by 7.
# I'll spare everyone the pages of code and scratchwork that led up to this obvious (now) solution.
#  On the other hand, I think I learned quite a bit investigating all my dead ends.


p_no_red = 1.0

for i in range(41, 61):
    p_no_red *= i

for i in range(51, 71):
    p_no_red /= i

print(p_no_red)

p_some_red = 1 - p_no_red
print(p_some_red)


expected_number_of_colors = 7 * p_some_red
print(round(expected_number_of_colors, 9))

'''
Note:

p_no_red is calculated as follows:

60   59   58         41    60! * 50!
-- x -- x -- x ... x -- =  ---------
70   69   68         51    70! * 40!

I figure an iterative approach should be faster than using factorials,
since most terms cancel.
'''


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')


print('\n--------------------------SOLUTION 5,   --------------------------')
t1  = time.time()

# ==== Tue, 16 Jun 2015, 17:01, Nicolas Patrois, France
# Main code taken here:
# http://phillipmfeldman.org/Python/combinatorics.html

from sympy.functions.combinatorial.factorials import binomial

def solution5():
    def prod(liste):
      p=1
      for i in liste:
        p*=i
      return p

    def unlabeled_balls_in_labeled_boxes(balls, box_sizes):
      if not isinstance(balls, int):
        raise TypeError("balls must be a non-negative integer.")
      if balls < 0:
        raise ValueError("balls must be a non-negative integer.")
      if not isinstance(box_sizes, (list, tuple)):
        raise ValueError("box_sizes must be a non-empty list or tuple.")
      capacity= 0
      for size in box_sizes:
        if not isinstance(size, int):
          raise TypeError("box_sizes must contain only positive integers.")
        if size < 1:
          raise ValueError("box_sizes must contain only positive integers.")
        capacity+= size
      if capacity < balls:
        raise ValueError("The total capacity of the boxes is less than the number of balls to be distributed.")
      return _unlabeled_balls_in_labeled_boxes(balls, box_sizes)

    def _unlabeled_balls_in_labeled_boxes(balls, box_sizes):
      if not balls:
        yield len(box_sizes) * (0,)
      elif len(box_sizes) == 1:
        if box_sizes[0] >= balls:
          yield (balls,)
      else:
        for balls_in_first_box in range( min(balls, box_sizes[0]), -1, -1 ):
          balls_in_other_boxes= balls - balls_in_first_box
          for distribution_other in _unlabeled_balls_in_labeled_boxes(balls_in_other_boxes, box_sizes[1:]):
            yield (balls_in_first_box,) + distribution_other

    compte=0
    nbcouleurs=0

    for b in unlabeled_balls_in_labeled_boxes(20,[10]*7):
      nb=prod([binomial(10,bi) for bi in b])
      compte+=nb
      nbcouleurs+=(7-b.count(0))*nb

    return print(float(nbcouleurs/compte))


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')


print('\n--------------------------SOLUTION 6,  Dynamic Programming  --------------------------')
t1  = time.time()

# ==== Sat, 13 Dec 2014, 18:38, devjoe, USA
# Simple dynamic program.
# There are only C(26,6)=230230 ways* that 20 balls can be distributed among the 7 colors,
# so let the vector of number-of-balls-of-each-color be a state.
# For each of 20 steps, for each possible case after the previous step,
# calculate the probability of the next ball being each possible color,
# and sum of the probabilities for each state after this draw as a new case.
#
# * This figure comes from the following analogy which is useful in this sort of problem:
# The number of ways 20 balls can be distributed among 7 colors is the number of ways of inserting 6 dividers
# into the row of 20 balls (the balls in each section being one color).
# If we consider dividers and balls together, the number of ways of inserting the dividers is the number of ways
# of choosing 6 elements out of 26 to be the dividers.
#
# Since the colors are all equivalent, we can consolidate the cases further by sorting the distribution.
# If we replace the line where we calculate newcas with:
#         newcas=list(cas)
#         newcas[color]+=1
#         newcas.sort()
#         newcas=tuple(newcas)

def solution6():
    cases={}
    cases[(0,0,0,0,0,0,0)]=1.0
    for j in range(20):
      newcases={}
      remain=70-j
      for cas in cases:
        for color in range(7):
          if cas[color]<10:
            chance=cases[cas]*(10.0-cas[color])/remain
            newcas=cas[:color]+(cas[color]+1,)+cas[(color+1):]
            if newcas in newcases:
              newcases[newcas]+=chance
            else:
              newcases[newcas]=chance
      cases=newcases
    #Sum up results
    e=0.0
    for cas in cases:
      numcolors=7-cas.count(0)
      e+=numcolors*cases[cas]
    return print (e)

solution6()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')


print('\n--------------------------SOLUTION 7,   --------------------------')
t1  = time.time()

# === Mon, 15 Dec 2014, 07:06, ChopinPlover, Taiwan
# Shame to share my code due to wonderful Tepsi's method.
# Select colors first, then brute force on every possible distribution of color balls.

import itertools
import sys

class Problem():
    def solve(self):
        total_value_count = 0
        for color in range(2, 7 + 1):
            color_selection_count = self.__get_binomial_coefficient(7, color)
            for settings in itertools.product(range(1, 10 + 1), repeat=color):
                if sum(settings) == 20:
                    value_count = 1
                    for i in settings:
                        value_count *= self.__get_binomial_coefficient(10, i)
                    total_value_count += value_count * color_selection_count * color
        sample_count = self.__get_binomial_coefficient(70, 20)
        print(total_value_count / sample_count, total_value_count, sample_count)

    def __get_binomial_coefficient(self, n, k):
        if k < 0 or n < 0 or n < k:
            return 0
        if k > n - k:
            return self.__get_binomial_coefficient(n, n - k)
        result = 1
        for i in range(k):
            result = result * (n - i) // (i + 1)
        return result


problem = Problem()
problem.solve()




t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')


print('\n--------------------------SOLUTION 8,  RECURSION --------------------------')
t1  = time.time()

# ==== Mon, 15 Dec 2014, 15:21, gjermv, Norway
# I made a list with 70 balls, and then I recursively picked out one ball with a color that I had drawn
# before and one ball with a new color.
# The recursion stopped either when I had drawn 7 different balls or 20 balls in total.
# I was expecting the code to take forever or not have good enough accuracy,
# but happy when I saw this approach worked…

def nice_recursion() :
    urn = [10,10,10,10,10,10,10]

    pPos = dict()
    for i in range(0,8):
        pPos[i] = 0

    def drawBall( urn , pBall):

        ballsLeft = sum( urn )
        colorsDrawn = 0
        ballsDrawn = 0

        for i in range(0,7):
            if urn[i] == 10:
                pass
            else:
                colorsDrawn = colorsDrawn + 1
                ballsDrawn = ballsDrawn + urn[i]

        if ballsLeft < 51 or colorsDrawn == 7:
            pPos[colorsDrawn] = pPos[colorsDrawn] + pBall
            return 0


        pBall_Diff = pBall * ((70-colorsDrawn * 10)/ballsLeft)
        pBall_Same = pBall * ballsDrawn/ballsLeft


        # Draw ball with same Color
        for i in range(0,7):
            if urn[i] == 0 or urn[i] == 10:
                pass
            else:
                urn[i] = urn[i] -1
                drawBall(urn[:],pBall_Same)
                urn[i] = urn[i] +1
                break

        # Draw ball with different Color
        for i in range(0,7):
            if urn[i] == 10:
                urn[i] = urn[i] -1
                drawBall(urn[:] , pBall_Diff)
                break
            else:
                pass

    drawBall(urn[:],1)

    expectedVal = 0
    for i in iter(pPos.items()):
        expectedVal = expectedVal+i[0]*i[1]

    return print(expectedVal)

nice_recursion()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')


print('\n--------------------------SOLUTION 9, MEmoization  --------------------------')
t1  = time.time()

# ===Mon, 15 Dec 2014, 22:57, Esco, USA
# Simple memoization in Python, no combinatorics.

ememo = {}

def countdistinct(d):
    count = 0.0
    for i in d:
        if d[i] != 10:
            count += 1
    return count

def expect(d):
    f = frozenset((i, d[i]) for i in d)
    try:
        return ememo[f]
    except KeyError:
        s = sum(d[i] for i in d)
        if s == 50:
            ememo[f] = countdistinct(d)
        else:
            e = 0.0
            for i in d:
                if d[i] > 0:
                    d1 = d.copy()
                    d1[i] -= 1
                    e += d[i] * expect(d1)
            ememo[f] = e/s
        return ememo[f]

print( expect({i: 10 for i in range(7)}))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')


print('\n--------------------------SOLUTION 10,  simple Dynamic Programming --------------------------')
t1  = time.time()

# === Mon, 26 Jan 2015, 01:12, DanGoldbach, England
# Simple DP.

"""
E = 2*P(2 distinct colours) +
    3*P(3 distinct colours) + ... +
    7*P(7 distinct colours)

  = 2*(num ways to select 2 distinct colours)/(num ways to select colours) + ...

  Count number of picks of 20 from the box, then multiply by each way of
  choosing colours.
  +--+
  |RO|YGBIV
  |RO|YGBIV
  |RO|YGBIV
  |RO|YGBIV
  |RO|YGBIV
  |RO|YGBIV
  |RO|YGBIV
  |RO|YGBIV
  |RO|YGBIV
  |RO|YGBIV
  +--+
  Repeat for each width box from 2..7
"""

import euler

NUM_BALLS_PER_COLOUR = 10
NUM_COLOURS = 7
NUM_TO_PICK = 2*NUM_BALLS_PER_COLOUR

@euler.memoize
def count(n, k):
    if k == 0:
        return n == 0
    tot = 0
    for i in range(1, min(NUM_BALLS_PER_COLOUR+1, k+1)):
        tot += count(n-1, k-i)*euler.binom(NUM_BALLS_PER_COLOUR, i)
    return tot


vs = []
for num_uniq_colours in range(2, NUM_COLOURS+1):
    vs.append(count(num_uniq_colours, NUM_TO_PICK) *
              euler.binom(NUM_COLOURS, num_uniq_colours))
ans = sum((i+2)*vs[i]/float(sum(vs)) for i in range(len(vs)))
print('%.9f' % ans)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')


print('\n--------------------------SOLUTION 11, RECURSION  --------------------------')
t1  = time.time()

# ==== Wed, 25 Mar 2015, 03:46, vh311, Czeck Republic
# A recursive solution to the problem. I split the balls into two groups - fballs are the balls of new color,
# kballs are already revealed balls and bpc is the number of balls per color.

def take_ball(to_take, kballs, fballs, bpc):
    if to_take == 0:
        return 0

    if kballs < 0:
        return 0

    if fballs < 0:
        return 0

    balls = kballs + fballs
    p = float(fballs)/float(balls) # probability of choosing new color

    return p*(1+take_ball(to_take-1, kballs + bpc -1 , fballs-bpc, bpc)) + (1-p) * (take_ball(to_take-1, kballs -1 , fballs, bpc))

print(take_ball(20, 0, 70, 10))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')


# print('\n--------------------------SOLUTION 12,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')




