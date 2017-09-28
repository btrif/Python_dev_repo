#  Created by Bogdan Trif on 17-09-2017 , 9:57 PM.

#!/usr/bin/python                   o(^_^)o         ( ͡° ͜ʖ ͡°)
# © Solved by Bogdan Trif @     Completed on Mon, 18 Sep 2017, 01:02
#The  Euler Project  https://projecteuler.net
'''
                                Monopoly odds       -           Problem 84

In the game, Monopoly, the standard board is set up in the following way:

A player starts on the GO square and adds the scores on two 6-sided dice to determine the number of squares
they advance in a clockwise direction. Without any further rules we would expect to visit each square with equal probability: 2.5%.
However, landing on G2J (Go To Jail), CC (community chest), and CH (chance) changes this distribution.

In addition to G2J, and one card from each of CC and CH, that orders the player to go directly to jail,
if a player rolls three consecutive doubles, they do not advance the result of their 3rd roll. Instead they proceed directly to jail.

At the beginning of the game, the CC and CH cards are shuffled.
When a player lands on CC or CH they take a card from the top of the respective pile and, after following the instructions,
it is returned to the bottom of the pile.
There are sixteen cards in each pile, but for the purpose of this problem we are only concerned with cards that order a movement;
any instruction not concerned with movement will be ignored and the player will remain on the CC/CH square.

= Community Chest (2/16 cards):
Advance to GO
Go to JAIL

= Chance (10/16 cards):
Advance to GO
Go to JAIL
Go to C1
Go to E3
Go to H2
Go to R1
Go to next R (railway company)
Go to next R
Go to next U (utility company)
Go back 3 squares.

The heart of this problem concerns the likelihood of visiting a particular square.
That is, the probability of finishing at that square after a roll.
For this reason it should be clear that, with the exception of G2J for which the probability of finishing on it is zero,
the CH squares will have the lowest probabilities, as 5/8 request a movement to another square,
and it is the final square that the player finishes at on each roll that we are interested in.
We shall make no distinction between "Just Visiting" and being sent to JAIL,
and we shall also ignore the rule about requiring a double to "get out of jail",
assuming that they pay to get out on their next turn.

By starting at GO and numbering the squares sequentially from 00 to 39 we can concatenate these two-digit numbers
to produce strings that correspond with sets of squares.

Statistically it can be shown that the three most popular squares, in order, are JAIL (6.24%) = Square 10,
E3 (3.18%) = Square 24, and GO (3.09%) = Square 00.
So these three most popular squares can be listed with the six-digit modal string: 102400.

If, instead of using two 6-sided dice, two 4-sided dice are used, find the six-digit modal string.


'''
import time, zzz
import random


# print('\n--------------------------TESTS------------------------------')
# t1  = time.time()
#

#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')


# print(BOARD,'\n')

### CARDS   ###



#
# cc  = random.choice(CC + list(range(1, 15 )) )
# ch = random.choice(CH + list(range(1, 7 )) )
# print('Comunity Chest : \t',cc )
# print('Chance : \t ' ,ch  ,'\n' ,'---'*25)

print('\n================  My FIRST SOLUTION, Monte Carlo Simulation, 1 sec  ===============\n')
t1  = time.time()


class Monopoly_Odds() :
    def __init__(self):
        self.BOARD = { 0 : "GO"  , 1 : "A1"  , 2 : "CC1"  , 3 : "A2"  , 4 : "T1"  , 5 : "R1"  , 6 : "B1"  , 7 : "CH1"  , 8 : "B2"  , 9 : "B3"  ,
          10 : "JAIL"  , 11 : "C1"  , 12 : "U1"  , 13 : "C2"  , 14 : "C3"  , 15 : "R2"  , 16 : "D1"  , 17 : "CC2"  , 18 : "D2"  , 19 : "D3"  ,
          20 : "FP"  , 21 : "E1"  , 22 : "CH2"  , 23 : "E2"  , 24 : "E3"  , 25 : "R3"  , 26 : "F1"  , 27 : "F2"  , 28 : "U2"  , 29 : "F3"  ,
          30 : "G2J"  , 31 : "G1"  , 32 : "G2"  , 33 : "CC3"  , 34 : "G3"  , 35 : "R4"  , 36 : "CH3"  , 37 : "H1"  , 38 : "T2"  , 39 : "H2"  }

        self.BOARD2 = dict(zip( self.BOARD.values(), self.BOARD.keys() ) )

        self.Memo = { i:0 for i in range(40)  }

        self.CC = [ 'Advance to GO', 'Go to JAIL' ]
        self.CH = [ 'Advance to GO', 'Go to JAIL', 'Go to C1', 'Go to E3', 'Go to H2', 'Go to R1',
                                'Go to next R', 'Go to next R', 'Go to next U', 'Go back 3 squares' ]

        self.Distrib = dict()
        self.pos, self.consecutive_doubles = 0 , 0

    def throw_dices( self, nr_sided ) :
        a, b = random.randint(1, nr_sided), random.randint(1, nr_sided)
        return (a,b)

    def next_rail_pos(self, pos) :
    #     Rail = [ BOARD2.get('R4'), BOARD2.get('R3'), BOARD2.get('R2'), BOARD2.get('R1') ]
        Rail = [35, 25, 15, 5]
        for i in range(len(Rail)):
            if pos > Rail[i] :
                pos = Rail[i-1]
                return pos
            if pos < 5 : return 5


    def Monte_Carlo(self, throws, nr_sided  ) :

        for turn in range(throws) :
            dh = self.throw_dices(nr_sided)     # dh is a tuple so we must sum it
            # print( 'after throw : ', dh,'    ', sum(dh) )

            # CASE  of 3 Consecutive Doubles :
            if dh[0] == dh[1] :         # if we hit a double record it
                self.consecutive_doubles += 1
            if dh[0] != dh[1] :         # reset the double counter by setting it back to 0
                self.consecutive_doubles =0
            if self.consecutive_doubles == 3 :
                self.pos = 10
                self.Memo[self.pos] +=1
                self.consecutive_doubles = 0
                continue

            self.pos = ( self.pos + sum(dh) ) % 39

            if self.pos == 30 : self.pos = 10

            if self.pos in [2, 17, 33 ] :        # CC1 ,CC2 ,CC3 ,
                card = random.choice(self.CC + list(range(1, 15 )) )
                # print('card CC : \t', card )
                if card ==  'Advance to GO' : pos = 0
                if card == 'Go to JAIL' : pos = 10

            if self.pos in [ 7 , 22, 36  ] :              ## 'CH1' ,'CH2', 'CH3'
                card = random.choice(self.CH + list(range(1, 7 )) )
                # print('card CH : \t', card )
                if card ==  'Advance to GO' : self.pos = 0
                if card == 'Go to JAIL' : self.pos = 10
                if card == 'Go to C1' : self.pos = 11
                if card == 'Go to E3' : self.pos = 24
                if card == 'Go to H2' : self.pos = 39
                if card == 'Go to R1' : self.pos = 5
                if card == 'Go to next R' : self.pos = self.next_rail_pos(self.pos)
                if card == 'Go to next U' :
                    if self.pos < 12 or self.pos > 28 : self.pos = 12
                    if 12< self.pos < 28 : self.pos = 28
                if card == 'Go back 3 squares' : self.pos -= 3
            self.Memo[self.pos] +=1

            if turn % 1e6 == 0 : print('iter = ', turn)
        print('Memo :   pos with greatest val = ', max(self.Memo, key=self.Memo.get) ,'\n' , self.Memo ,'\n')

        # Constructing the Distribution :
        for k, v in self.Memo.items() :
            self.Distrib[k] = v/throws
        W = ''
        for v in list(reversed(sorted(self.Memo.values())))[:3] :
            p = list(self.Memo.keys())[list(self.Memo.values()).index(v)]
            print('value : ',v , '     pos = ' , p , '     Distribution = ' , self.Distrib[p] )
            W += str(p)
        print('\nDistribution : \n', self.Distrib )

        return print('\nModal string is : \t', W)


# Monte_Carlo( 10**5 , 4 ,  Memo )      # Answer  for 4-sides dices:     101524

solution = Monopoly_Odds()
solution.Monte_Carlo(10**5, 4  )



# Completed in : 612 sec  for 5*10**7 turns on for 4-sides dices :
# value :  3553396      pos =  10      Distribution =  0.07106792
# value :  1843979      pos =  15      Distribution =  0.03687958
# value :  1675621      pos =  24      Distribution =  0.03351242
# ====  Distribution :  =====
#  {0: 0.02994642, 1: 0.01907182, 2: 0.01621292, 3: 0.0201953, 4: 0.02251052, 5: 0.02981374, 6: 0.0218608, 7: 0.00808574, 8: 0.02161982,
#   9: 0.0212703, 10: 0.07106792, 11: 0.02510468, 12: 0.02465584, 13: 0.025726, 14: 0.02935044, 15: 0.03687958, 16: 0.03277208,
#   17: 0.02768844, 18: 0.030298, 19: 0.03125486, 20: 0.0305097, 21: 0.03103736, 22: 0.01148224, 23: 0.03051992, 24: 0.03351242,
#   25: 0.03171058, 26: 0.02694572, 27: 0.0260357, 28: 0.02910812, 29: 0.02806672, 30: 0.0, 31: 0.0286743, 32: 0.02634314,
#   33: 0.0224818, 34: 0.0224297, 35: 0.02022742, 36: 0.00805094, 37: 0.02164266, 38: 0.02123942, 39: 0.00459692}

#       For 6-dices :   10 24 00    JAIL (6.24%) = Square 10, E3 (3.18%) = Square 24, and GO (3.09%) = Square 00


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')


print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1,  Markov Chains , needs fixing --------------------------')
t1  = time.time()

# === Wed, 19 Jul 2017, 02:59, lpage, USA
# Fun problem, despite ambiguity around corner cases such as redrawing a card after landing on CH3 and drawing "Go Back Three."
#
# Here are two approaches to solving the problem:
# one that computes the stationary probability distribution explicitly using Markov chains,
# and one that approximates the stationary distribution via Monte Carlo.
# Both use a common MonopolyBoard class.
# The simulation based approach yields a result that's very close to the true stationary distribution, and with less code...but math FTW.

import random

# pylint: disable=invalid-name
class MonopolyBoard(object):

    squares = 'GO A1 CC1 A2 T1 R1 B1 CH1 B2 B3 JAIL ' \
              'C1 U1 C2 C3 R2 D1 CC2 D2 D3 FP ' \
              'E1 CH2 E2 E3 R3 F1 F2 U2 F3 G2J ' \
              'G1 G2 CC3 G3 R4 CH3 H1 T2 H2'.split(' ')

    n_squares = len(squares)
    indices = {value:idx for idx, value in enumerate(squares)}
    go = indices['GO']
    jail = indices['JAIL']
    g2j = indices['G2J']
    c1 = indices['C1']
    e3 = indices['E3']
    h2 = indices['H2']
    r1 = indices['R1']

    @staticmethod
    def index_of_card(card):
        return MonopolyBoard.indices[card]

    def __init__(self, dice_sides=6):
        self._index = MonopolyBoard.go
        self._doubles_counter = 0
        self._dice_sides = dice_sides
        nop = lambda: None
        self.community_chest = [nop for _ in range(14)] + \
                               [self._g2g, self._g2j]
        self.chance_chest = [nop for _ in range(6)] + \
                            [self._g2g, self._g2j, self._gc1, self._ge3,
                             self._gh2, self._gr1, self._gnr, self._gnr,
                             self._gnu, self._gb3]

        random.shuffle(self.community_chest)
        random.shuffle(self.chance_chest)

    def take_turn(self):
        d1 = random.randint(1, self._dice_sides)
        d2 = random.randint(1, self._dice_sides)

        if d1 == d2:
            self._doubles_counter += 1
        else:
            self._doubles_counter = 0

        if self._doubles_counter == 3:
            self._doubles_counter = 0
            self._g2j()
            return

        self._move_n(d1+d2)
        if self.index == MonopolyBoard.jail:
            pass
        elif self.index == MonopolyBoard.g2j:
            self._g2j()
        else:
            self._handle_draw()

    def current_square(self):
        return MonopolyBoard.squares[self._index]

    def _handle_draw(self):
        def _handle_card(deck):
            card = deck.pop()
            card()
            deck.insert(0, card)
            random.shuffle(deck)

        current_square = self.current_square()
        if current_square[:2] == 'CC':
            _handle_card(self.community_chest)
        elif current_square[:2] == 'CH':
            _handle_card(self.chance_chest)

    @property
    def index(self):
        return self._index

    def _move_n(self, n):
        self._index = (self._index+n) % MonopolyBoard.n_squares

    def _g2g(self):
        self._index = MonopolyBoard.go

    def _g2j(self):
        self._index = MonopolyBoard.jail

    def _gc1(self):
        self._index = MonopolyBoard.c1

    def _ge3(self):
        self._index = MonopolyBoard.e3

    def _gh2(self):
        self._index = MonopolyBoard.h2

    def _gr1(self):
        self._index = MonopolyBoard.r1

    def _gnr(self):
        while not self.current_square()[0] == 'R':
            self._move_n(1)

    def _gnu(self):
        while not self.current_square()[0] == 'U':
            self._move_n(1)

    def _gb3(self):
        self._move_n(-3)
        self._handle_draw()


print('\n----Markov Chains Implementation --------------')


import itertools
import numpy as np # pylint: disable=import-error
from scipy.linalg import eig # pylint: disable=import-error



def sol_markov():
    def _compute_roll_sum_pdf(dice_sides):
        outcomes = sorted([x+y for x, y in  itertools.product(range(1, dice_sides+1),  range(1, dice_sides+1))])
        counts = [(key, len([x for x in group])) for key, group in   itertools.groupby(outcomes)]
        probabilities = [(total, count/dice_sides**2) for total, count in counts ]

        return print('Probabilities : \t', probabilities)

    def _transition_matrix(dice_sides):
        """
        We need to track how many doubles we roll (up to three, when we
        go to jail and reset the doubles counter) so we'll need a state
        squares * max_doubles states
        """

        num_states = 3*MonopolyBoard.n_squares
        transition_matrix = np.zeros((num_states, num_states,))
        move_probs = _compute_roll_sum_pdf(dice_sides)
        double_prob = 1/dice_sides
        not_double_prob = 1-double_prob

        def _seek_next_square(idx, prefix):
            while not MonopolyBoard.squares[idx].startswith(prefix):
                idx = (idx+1)%MonopolyBoard.n_squares
            return idx

        def _transition_rules(cur_idx, next_idx, move_prob, roll):
            def _apply_transition(next_state, prob):
                """
                If we don't roll a double, the double counter resets and we
                return to a state offset of zero. If we do roll a double,
                we increment the double counter if doubles < 3, and go to
                jail otherwise
                """
                cur_state = roll*MonopolyBoard.n_squares+cur_idx

                transition_matrix[cur_state][next_state] += \
                    not_double_prob*move_prob*prob

                if roll < 2:
                    next_state += (roll+1)*MonopolyBoard.n_squares
                    transition_matrix[cur_state][next_state] += \
                        double_prob*move_prob*prob
                else:
                    transition_matrix[cur_state][MonopolyBoard.jail] += \
                        double_prob*move_prob*prob

            if next_idx == MonopolyBoard.g2j:
                _apply_transition(MonopolyBoard.jail, 1)
            elif MonopolyBoard.squares[next_idx].startswith('CC'):
                _apply_transition(next_idx, 14/16)
                _apply_transition(MonopolyBoard.go, 1/16)
                _apply_transition(MonopolyBoard.jail, 1/16)
            elif MonopolyBoard.squares[next_idx].startswith('CH'):
                _apply_transition(next_idx, 6/16)
                _apply_transition(MonopolyBoard.go, 1/16)
                _apply_transition(MonopolyBoard.jail, 1/16)
                _apply_transition(MonopolyBoard.c1, 1/16)
                _apply_transition(MonopolyBoard.e3, 1/16)
                _apply_transition(MonopolyBoard.h2, 1/16)
                _apply_transition(MonopolyBoard.r1, 1/16)
                _apply_transition(_seek_next_square(next_idx, 'R'), 2/16)
                _apply_transition(_seek_next_square(next_idx, 'U'), 1/16)
                _apply_transition((cur_idx-3)%MonopolyBoard.n_squares, 1/16)
            else:
                _apply_transition(next_idx, 1)

        for cur_idx in range(MonopolyBoard.n_squares):
            for move_distance, move_prob in move_probs :
                next_idx = (cur_idx+move_distance)%MonopolyBoard.n_squares
                for roll in range(3):
                    _transition_rules(cur_idx, next_idx, move_prob, roll)

        return transition_matrix

    def _find_stationary_distribution(transition_matrix):
        """
        Compute the eigenvectors and eigenvalues of our (transposed)
        transition matrix and return the eigenvector corresponding to the
        eigenvalue that's closest to one. Said eigenvalue is the stationary
        distribution of our Markov chain. Since we're only interested in the
        probability of being in a given board position, and not a
        board position/doubles count pair, we sum over the dice marginal.
        """
        S, U = eig(transition_matrix.T) # pylint: disable=invalid-name
        stationary = np.array(U[:, np.where(np.abs(S-1.) < 1e-6)[0][0]].flat)
        stationary = np.real(stationary/np.sum(stationary))
        return np.sum(stationary.reshape(3, MonopolyBoard.n_squares), axis=0)


    stationary_dist = _find_stationary_distribution(_transition_matrix(4))
    stationary_dist = sorted([(value, idx) for idx, value in \
                             enumerate(stationary_dist)], reverse=True)
    return ''.join(str(idx).zfill(2) for _, idx in stationary_dist[:3])

# sol_markov()


print('\n----Monte Carlo  Implementation --------------')

def solMC():
    simulations = 100000
    board = MonopolyBoard(dice_sides=4)
    position_counts = {idx:0 for idx in range(MonopolyBoard.n_squares)}

    for _ in range(simulations):
        board.take_turn()
        position_counts[board.index] += 1

    counts = sorted([(100.*count/simulations, idx) for idx, count in \
                      position_counts.items()], reverse=True)

    counts = ''.join([str(idx) for _, idx in counts][:3])
    return print('Probabilities :\t' ,counts )

# solMC()


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')


print('\n--------------------------SOLUTION 2,  MARKOV CHAINS, Beautiful --------------------------')
t1  = time.time()
# === Mon, 17 Aug 2015, 21:45 ,iLaurens
#
# I took the Markov Chain approach. As a statistician, I reckoned that there was no need to include for even triple throws
# due to insignificant chance. Moreover, if penalties for throwing doubles are excluded,
# why would there be any need to consider a double turn? This would just be the same as two turns.
# Hence, I constructed a Markov Transition matrix for just single turns with a single throw of two dice.
#
# Eventually got a code that is barely 30 lines and runs in under a millisecond in Python 3.
# I for once think I did a fairly good job at this problem, keeping the coding to a minimum and applying maximum theory.
# Euler would be proud.

import numpy as np

sides = 4
roll = np.zeros(2*sides-1)
for r1 in range(sides):
    for r2 in range(sides):
        roll[r1+r2] += 1/(sides**2)

P = np.zeros((40,40))

for old in range(40):
    for r in range(2,2*sides+1):
        new = (old+r)%40
        if new in [2,17,33]:
            P_ = np.zeros(40)
            P_[[0,10]] += 1/16
            P_[new] += 14/16
            P[old] += roll[r-2]*P_
        elif new in [7,22,36]:
            P_ = np.zeros(40)
            P_[[0,10,11,24,39,5]] += 1/16
            P_[(new < 12 or new > 28)*12 + (new > 12 and new < 28)*28] += 1/16
            P_[(40+new-3)%40] += 1/16
            P_[(5+10*((new+5)//10))%40] += 2/16
            P_[new] += 6/16
            P[old] += roll[r-2]*P_
        else:
            P[old][(new!=30)*(new-10)+10] += roll[r-2]

print('\nAnswer : \t' ,np.argsort((np.linalg.matrix_power(P,30))[0])[:-4:-1] )


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')


print('\n--------------------------SOLUTION 3,  MARKOV CHAINS, Perfect  --------------------------')
t1  = time.time()

# ==== Wed, 8 Apr 2015, 00:42, Varcho, USA
# I treated the problem as a Markov process. To get the probability of landing on a certain square I found the eigenvector
# of the boards state transition matrix (which produces a probability distribution function on the squares)
# to find which square were most likely.

import numpy as np

#treat the game as a markov process where the eigenvector of
#the transition matrix produces a probability distribution on
#the squares

def createBoard(diceSize):
	a = []
	for i in range(40):
		l = [0]*40
		tripDoubProb = 1/float(pow(6,3))
		for j in range(2,2*diceSize+1):
			l[(i+j)%40]+=(1-tripDoubProb)*(min(j-1,-j+2*diceSize+1)/float(diceSize**2))
		#triple doubles
		l[10]+=tripDoubProb
		a.append(l)

	#community chest
	for row in [2,17,33]:
		tripDoubProb = 1/float(pow(6,3))
		dontMoveProb = 14/float(16)
		l = [0]*40
		for j in range(2,2*diceSize+1):
			l[(row+j)%40]=(1-tripDoubProb)*dontMoveProb*(min(j-1,-j+2*diceSize+1)/float(diceSize**2))

		#advance to GO
		l[0]+=(1-tripDoubProb)*(1-dontMoveProb)*(.5)
		#go to Jail
		l[10]+=(1-tripDoubProb)*(1-dontMoveProb)*(.5)

		#rolled doubles
		l[10]+=tripDoubProb
		a[row] = l

	#chance
	for row in [7,22,36]:
		tripDoubProb = 1/float(pow(6,3))
		dontMoveProb = 6/float(16)
		l = [0]*40
		for j in range(2,2*diceSize+1):
			l[(row+j)%40]=(1-tripDoubProb)*dontMoveProb*(min(j-1,-j+2*diceSize+1)/float(diceSize**2))

		#advance to GO
		l[0]+=(1-tripDoubProb)*(1-dontMoveProb)*(.1)
		#go to Jail
		l[10]+=(1-tripDoubProb)*(1-dontMoveProb)*(.1)
		#go to C1
		l[11]+=(1-tripDoubProb)*(1-dontMoveProb)*(.1)
		#go to E3
		l[24]+=(1-tripDoubProb)*(1-dontMoveProb)*(.1)
		#go to H2
		l[39]+=(1-tripDoubProb)*(1-dontMoveProb)*(.1)
		#go to R1
		l[5]+=(1-tripDoubProb)*(1-dontMoveProb)*(.1)

		#Go to next R
		if row ==7:
			l[15]+=(1-tripDoubProb)*(1-dontMoveProb)*(.2)
		elif row ==22:
			l[25]+=(1-tripDoubProb)*(1-dontMoveProb)*(.2)
		else:
			l[5]+=(1-tripDoubProb)*(1-dontMoveProb)*(.2)


		#go to next utility
		if row ==7 or row==36:
			l[12]+=(1-tripDoubProb)*(1-dontMoveProb)*(.1)
		else:
			l[28]+=(1-tripDoubProb)*(1-dontMoveProb)*(.1)
		#go back 3 squares
		l[row-3]+=(1-tripDoubProb)*(1-dontMoveProb)*(.1)
		#rolled doubles
		l[10]+=tripDoubProb
		a[row] = l

	#go to jail
	a[30] = [0]*40
	a[30][10]=1.0

	return a

def modalMonopolyNumber(diceSize):
	board = createBoard(diceSize)
	guess = [[1.0] for i in range(40)]

	m = np.matrix(board)
	m = np.transpose(m)
	g = np.matrix(guess)
	#get eigenvector using power method
	for i in range(400):
		g = np.dot(m,g)

	#return sorted([float(x) for x in g])
	sortedList=[i[0] for i in sorted(enumerate([float(x) for x in g]),key=lambda x:x[1])]
	return 10000*sortedList[-1] + 100*sortedList[-2] + sortedList[-3]

print (modalMonopolyNumber(4))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')


print('\n--------------------------SOLUTION 4,  MARKOV CHAINS  --------------------------')
t1  = time.time()

# === Tue, 5 May 2015, 19:02, oneequalstwo,  USA
# I was really confused when I saw all the simulation solutions.
# I did a Markov thingy where I explicitly computed the probability distribution at the nth throw, and took the limit.
# This wasn't too hard to do recursively: we start off with a naive distribution assuming that you stay where you land,
# and then take the CC, CH, and G2J squares into account. My code is the farthest thing from robust,
# but nobody wants to generalize Monopoly anyways.

# Create transList:
# List of dicts that give
# P(land on Y | start at X)
# = transList[X][Y]

transList = []
for index in range(40):
    transList.append({})
# 16.0 is hard to type
s = 16.0

# Create naive dist.

for i in range(40):
    for j in range(40):
        transList[i][j] = 0
    transList[i][(i+2)%40]+=1/s
    transList[i][(i+3)%40]+=2/s
    transList[i][(i+4)%40]+=3/s
    transList[i][(i+5)%40]+=4/s
    transList[i][(i+6)%40]+=3/s
    transList[i][(i+7)%40]+=2/s
    transList[i][(i+8)%40]+=1/s

# Account for CC, CH, G2J

for i in range(40):
    #CC1
    if transList[i][2] != 0:
        totprob = transList[i][2]
        transList[i][2] = totprob * 14/s
        transList[i][0] += totprob * 1/s
        transList[i][10] += totprob * 1/s
    else:
        pass
    #CC2
    if transList[i][17] != 0:
        totprob = transList[i][17]
        transList[i][17] = totprob * 14/s
        transList[i][0] += totprob * 1/s
        transList[i][10] += totprob * 1/s
    else:
        pass
    #CC3
    if transList[i][33] != 0:
        totprob = transList[i][33]
        transList[i][33] = totprob * 14/s
        transList[i][0] += totprob * 1/s
        transList[i][10] += totprob * 1/s
    else:
        pass
    #CH1
    if transList[i][7] != 0:
        totprob = transList[i][7]
        transList[i][7] = totprob * 6/s
        transList[i][0] += totprob * 1/s
        transList[i][10] += totprob * 1/s
        transList[i][11] += totprob * 1/s
        transList[i][24] += totprob * 1/s
        transList[i][39] += totprob * 1/s
        transList[i][5] += totprob * 1/s
        transList[i][15] += totprob * 2/s
        transList[i][12] += totprob * 1/s
        transList[i][4] += totprob * 1/s
    else:
        pass
    #CH2
    if transList[i][22] != 0:
        totprob = transList[i][22]
        transList[i][22] = totprob * 6/s
        transList[i][0] += totprob * 1/s
        transList[i][10] += totprob * 1/s
        transList[i][11] += totprob * 1/s
        transList[i][24] += totprob * 1/s
        transList[i][39] += totprob * 1/s
        transList[i][5] += totprob * 1/s
        transList[i][25] += totprob * 2/s
        transList[i][28] += totprob * 1/s
        transList[i][19] += totprob * 1/s
    else:
        pass
    #CH3
    if transList[i][36] != 0:
        totprob = transList[i][36]
        transList[i][36] = totprob * 6/s
        transList[i][0] += totprob * 1/s
        transList[i][10] += totprob * 1/s
        transList[i][11] += totprob * 1/s
        transList[i][24] += totprob * 1/s
        transList[i][39] += totprob * 1/s
        transList[i][5] += totprob * 1/s
        transList[i][5] += totprob * 2/s
        transList[i][12] += totprob * 1/s
        transList[i][33] += totprob * (1/s) * (14/s)
        transList[i][0] += totprob * (1/s) * (1/s)
        transList[i][10] += totprob * (1/s) * (1/s)
    else:
        pass
    #G2J
    if transList[i][30] != 0:
        transList[i][10] += transList[i][30]
        transList[i][30] = 0
    else:
        pass

# Create transition function,
# takes prob. dist. at nth
# step, returns prob. dist.
# at n+1st step

def transition(probList):
    newProbs = [0]*40
    for oldSquare in range(40):
        for newSquare in transList[oldSquare]:
            newProbs[newSquare] += probList[oldSquare] * transList[oldSquare][newSquare]
    return newProbs

# Do it

distribution = [1.0] + [0]*39
for i in range(1000):
    distribution = transition(distribution)

# We have our desired prob. dist.

dummy = [0]*40
for i in range(40):
    dummy[i]=distribution[i]
a = str(distribution.index(max(dummy)))
dummy.remove(max(dummy))
b = str(distribution.index(max(dummy)))
dummy.remove(max(dummy))
c = str(distribution.index(max(dummy)))
print (a + b + c)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')


print('\n--------------------------SOLUTION 5,  MARKOV CHAINS --------------------------')
t1  = time.time()

# ==== Tue, 20 Nov 2012, 08:29, kalhartt, USA
# I used a Markov chain to solve the problem, and everyone seems to be having issue with the three doubles rule in markov chains.
# I just used the idea that the probability the last two rolls were doubles is 1/n^2 for an n-sided die.
#
# After that, setting up the transition matrix was straight forward and numpy makes eigenvectors a breeze.
# Although using numpy's eigenvecs automatically makes everything into complex floats,
# so I went with an alternate method to find the eigenvector in the end.

import numpy as np

# Constants
J = 10	# Jail
GJ = 30	# Go to Jail
RR = [ 5, 15, 25, 35 ]	# Rail roads
CC = [ 2, 17, 33 ]	# Community Chest
CH = [ 7, 22, 36 ]	# Chance

## Helpers
def nextRR(n):#{{{
    if n < 5:
        return 5
    elif n < 15:
        return 15
    elif n < 25:
        return 25
    elif n < 35:
        return 35
    return 5#}}}

def nextU(n):#{{{
    if n < 12:
        return 12
    if n < 28:
        return 28
    return 12#}}}

# Setup Transition Matrix
A = np.zeros((40,40))

## Add die roll probabilities
for n in range(40):
    A[(n+2) %40][n] = 1./16
    A[(n+3) %40][n] = 2./16
    A[(n+4) %40][n] = 3./16
    A[(n+5) %40][n] = 4./16
    A[(n+6) %40][n] = 3./16
    A[(n+7) %40][n] = 2./16
    A[(n+8) %40][n] = 1./16

## Fix Go to jail by 3 doubles
## and Go to jail
for n in range(40):
    A[J][n] += (1./4)**3
    A[(n+2) %40][n] *= 1 - (1./1)*(1./4)**2
    A[(n+4) %40][n] *= 1 - (1./3)*(1./4)**2
    A[(n+6) %40][n] *= 1 - (1./3)*(1./4)**2
    A[(n+8) %40][n] *= 1 - (1./1)*(1./4)**2
    A[J][n] += A[GJ][n]
    A[GJ][n] = 0

for n in range(40):
## Fix Chance
    for ch in CH:
        if A[ch][n] == 0: continue
        rr = nextRR(ch)
        u = nextU(ch)
        A[0 ][n] += A[ch][n] * (1./16)
        A[J ][n] += A[ch][n] * (1./16)
        A[11][n] += A[ch][n] * (1./16)
        A[24][n] += A[ch][n] * (1./16)
        A[39][n] += A[ch][n] * (1./16)
        A[5 ][n] += A[ch][n] * (1./16)
        A[rr][n] += A[ch][n] * (2./16)
        A[u ][n] += A[ch][n] * (1./16)
        A[ch-3][n]+= A[ch][n] * (1./16)
        A[ch][n] = A[ch][n] * (6./16)
## Fix Community Chest
for cc in CC:
    if A[cc][n] == 0: continue
    A[0 ][n] += A[cc][n] * (1./16)
    A[J ][n] += A[cc][n] * (1./16)
    A[cc][n] = A[cc][n] * (14./16)

## Print the Matrix
# for n, row in enumerate(A):
# print '%02d\t'%n, ' '.join('%0.2f'%x for x in row)


## These 4 lines find the eigenvector of A
## associated with eigenvalue 1
## Alt. Paramaterize Kernel of A-I
u, s, vh = np.linalg.svd(A-np.identity(40))
null_mask = (s <= 1e-3)
null_space = np.compress(null_mask, vh, axis=0)
eigenvec = null_space[0] / sum(null_space[0]) # normalize the result so probabilities sum to 1

# Print the list of probabilities
for x, y in sorted(enumerate(eigenvec), key=lambda x:-x[1]):
    print( '%02d'%x, '%0.4f'%y)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')


# print('\n--------------------------SOLUTION 6,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 7,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 8,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 9,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 10,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 11,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 12,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')

