#!/usr/bin/python
# Solved by Bogdan Trif @   Completed on Sat, 19 Nov 2016, 01:52
#The  Euler Project  https://projecteuler.net
'''
                            Poker hands     -       Problem 54
In the card game poker, a hand consists of five cards and are ranked, from
lowest to highest, in the following way:

  * High Card: Highest value card.
  * One Pair: Two cards of the same value.
  * Two Pairs: Two different pairs.
  * Three of a Kind: Three cards of the same value.
  * Straight: All cards are consecutive values.
  * Flush: All cards of the same suit.
  * Full House: Three of a kind and a pair.
  * Four of a Kind: Four cards of the same value.
  * Straight Flush: All cards are consecutive values of same suit.
  * Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the
highest value wins; for example, a pair of eights beats a pair of fives
(see example 1 below). But if two ranks tie, for example, both players
have a pair of queens, then highest cards in each hand are compared (see
example 4 below); if the highest cards tie then the next highest cards are
compared, and so on.

Consider the following five hands dealt to two players:

        Hand   Player 1            Player 2              Winner
        1      5H 5C 6S 7S KD      2C 3S 8S 8D TD        Player 2
               Pair of Fives       Pair of Eights
        2      5D 8C 9S JS AC      2C 5C 7D 8S QH        Player 1
               Highest card Ace    Highest card Queen
        3      2D 9C AS AH AC      3D 6D 7D TD QD        Player 2
               Three Aces          Flush with Diamonds
               4D 6S 9H QH QC      3D 6D 7H QD QS
        4      Pair of Queens      Pair of Queens        Player 1
               Highest card Nine   Highest card Seven
               2H 2D 4C 4D 4S      3C 3D 3S 9S 9D
        5      Full House          Full House            Player 1
               With Three Fours    with Three Threes

The file poker.txt contains one-thousand random hands dealt to two players.
Each line of the file contains ten cards (separated by a single space): the
first five are Player 1's cards and the last five are Player 2's cards. You
can assume that all hands are valid (no invalid characters or repeated
cards), each player's hand is in no specific order, and in each hand there
is a clear winner.

            How many hands does Player 1 win?
'''
import time
from collections import Counter

filename= 'pb054_poker.txt'
f = open(filename, 'r')
text = f.read()
f.close()
# print(text,'        ',type(text),'\n')

player1, player2 = [], []
cnt=0
for line in text.split('\n') :
    # print(line)
    pl1, pl2 = [], []
    for i in line.split() :
        if (cnt // 5) % 2 == 0 :
            pl1.append(i)
        else :
            pl2.append(i)
        cnt+=1
    player1.append(pl1)
    player2.append(pl2)

print('-------------------')

# ♠ Spades - S ,   ♥ Hearts - H   ,  ♦  Diamonds - D , ♣ Clubs - C

CARD = { '2':2, '3':3 , '4':4 , '5':5, '6':6 , '7':7, '8': 8 , '9': 9, 'T':10, 'J':12, 'Q':13, 'K':14, 'A' :15 }
print(CARD)
HAND = { 'High Card': 1 , 'One Pair':2, 'Two Pairs':3 , 'Three of a Kind':4 , 'Straight':5 , 'Flush':6, 'Full House':7 , 'Four of a Kind':8, 'Straight Flush': 9 , 'Royal Flush': 10,   }
print(HAND)

print(len(player1) ,player1)
print(len(player2) ,player2)

# test_hand=['8C', 'TS', 'KC', '9H', '4S']  # High Card
# test_hand = ['9C', 'KC', 'AS', '8D', 'AD']    # One Pair
# test_hand = ['5C', 'AD', '5D', 'AC', '9C']    # Two Pairs
# test_hand = ['AS', 'AD', '5D', 'AC', '9C']    # Three of a Kind
# test_hand = ['3S', '4D', '5D', '2C', '6C']    # Straight
# test_hand = ['KS', 'QD', 'TD', 'JC', '9C']    # Straight
# test_hand = ['3D', '9D', '6D', 'KD', 'QD']    # Flush
# test_hand =  ['5H', '9H', '7H', '6HS', '8H']   # Straight Flush
# test_hand = ['JS', 'AS', 'TS', 'KS', 'QS']     # Royal Flush
# test_hand = ['8S', 'JS', '8H', 'JD', '8C']     # Full House
# test_hand = ['8S', '8D', '8H', 'JD', '8C']     # Four of a Kind
# test_hand =  ['AD', '6C', '6S', '7D', 'TH']
# test_hand =  ['6H', '2H', '8H', 'KH', '4H']
test_hand =  ['5H', '5C', '6S', '7S', 'KD']
# test_hand =  ['2C', '3S', '8S', '8D', 'TD']
# test_hand =  ['5D', '8C', '9S', 'JS', 'AC']
# test_hand =  ['2C', '5C', '7D', '8S', 'QH']
# test_hand =  ['2D', '9C', 'AS', 'AH', 'AC']
# test_hand =  ['3D', '6D', '7D', 'TD', 'QD']
# test_hand = [ '4D', '6S',  '9H', 'QH',  'QC' ]
# test_hand = [ '3D', '6D',  '7H', 'QD',  'QS' ]
# test_hand = [ '2H', '2D',  '4C', '4D',  '4S' ]
# test_hand = [ '3C', '3D',  '3S', '9S',  '9D' ]


def is_straight(hand):
    val = sorted([  CARD[i[0]] for i in hand ])
    S = (max(val)*(max(val)+1))/2 - ( min(val)*(min(val)-1))/2
    if S == sum(val) or val ==[7,8,9,10,12] or val ==[8,9,10,12,13] \
            or val ==[9,10,12,13,14] or val==[2,3,4,5,15] :
        return True
    else : return False

print('\nTest evaluate straight Function :  ', is_straight(test_hand))

def evaluate_hand(hand) :
    card=[i[0] for i in hand]    # better, list comprehension, shorter
    colors = [i[1] for i in hand]
    val = [  CARD[i[0]] for i in hand ]
    royal_flush = [10, 12, 13, 14, 15]
    # print('\ncard :     ', card , '\ncolors :  ',colors, '\nval :       ', val)
    M = [item for item, count in Counter(card).items() if count == 2]
    N = [item for item, count in Counter(card).items() if count == 3]
    O = [item for item, count in Counter(card).items() if count == 4]
    # print(M,N,O)

    if len(set(card)) == 5 :                # == 5 different ==
        if len(set(colors)) > 1 :
            if is_straight(hand) == True :        # Straight
                return HAND['Straight'], 0
            elif is_straight(hand) == False :        # High Card - many colors
                maxv = max(val)
                s = sorted(val)[-2]
                return HAND['High Card'], maxv, s
        elif len(set(colors)) == 1 :
            if sorted(val) == royal_flush :         # Royal Flush
                return HAND['Royal Flush'], 0
            elif is_straight(hand) == False :           # Flush
                return HAND['Flush'], 0
            elif is_straight(hand) == True :           # Straight Flush
                return HAND['Straight Flush'], 0
    if len(set(card)) == 4 :        # One Pair      # == 4 different ==
        o = ''.join(M)
        s = max([i for i in val if i != CARD[o] ] )
        return HAND['One Pair'], CARD[o], s
    if len(set(card)) == 3 :                    # == 3 different ==
        if  len(M) == 2 :                               # Two Pairs
            s = sorted([ CARD[i] for i in M ])[::-1]
            s.insert(0, HAND['Two Pairs'] )
            return tuple(s)
        if  len(N) == 1 :                           # Three of a Kind
            s = ''.join(N)
            return HAND['Three of a Kind'], CARD[s]
    if len(set(card)) == 2 :                    # == 2 different ==
        if len(M) == 1 and len(N) == 1 :     # Full  House
            s = ''.join(N)
            return HAND['Full House'], CARD[s]
        if  len(O) == 1 :                        # Four of a Kind
            s = ''.join(O)
            return HAND['Four of a Kind'], CARD[s]


print('\nTest evaluate hand Function :  ', evaluate_hand(test_hand))            # Answer : 376


print('\n================  My FIRST SOLUTION,   ===============\n')

t1  = time.time()

error_investigations=[]
def play_poker_guys() :
    cnt1 , cnt2 = 0, 0
    for i in range(1000) :
        p1 = evaluate_hand(player1[i])
        p2 = evaluate_hand(player2[i])
        # print(player1[i] ,p1, '\n' ,  player2[i] ,p2,'\n')
        if p1 > p2 :        # !!!! IMPORTANT ! WE CAN COMPARE Tuples     (3,6,1) > (2,13)  !!!
            cnt1 +=1
            # print(p1, p2,' ==  ===  Player 1 wins =====   A  ====', cnt1)
        elif p1 < p2 :
            cnt2 +=1
            # print(p1, p2,' ==  ===  Player 2 wins =====   A  ====', cnt2)
        else :
            print(' ERROR ')
            investigations.append([player1[i], player2[i], p1, p2 ])
        # print('player 1 : ' ,p1 , '  ' ,player1[i] , [  CARD[i[0]] for i in player1[i] ] ,'\nplayer 2 : ' ,p2, '  ',player2[i], [  CARD[i[0]] for i in player2[i] ],'\n' )

    return print('\n\nPlayer 1 : ', cnt1 ,'\nPlayer 2 : ', cnt2)

play_poker_guys()
print('\n',error_investigations)


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')



print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1, VERY VERY GOOD & ELEGANT,  SafassThin, France  --------------------------')
t1  = time.time()
#
# Because of the fact that only the first 100 posts or so are permanent, some really cool python solutions
# in this forum are gone... so I repost a kind of medley I did of some of the best ideas.
#
# The main idea is that python can compare tuples - for ex: (3,2) > (3,1,1).
# So to evaluate a hand, you need to sort cards by their occurences first, and by their values next.
# Also keep track of color, to account for Flushes.
# J123's code (page 5 of this thread, for now) uses a similar strategy.
#
# The code is short, compact, a bit terse, but cool to look at!

hands = [line.split() for line in open(filename)]
def euler54():
    """
    Medley of Kutta, eske and Paul Crowley's code.
    KW. Diederich added a few corrections for 'real world' poker
    (but unrequired in the problem, it seems):
        - Straight (3,1,2) and Flush (3,1,3) have to be ranked :
                - above three of a kind (3,1,1)
                - below full house (3,2)
        - Ace,2,3,4,5 is also straight according to the rules.
    """
    values = {c: v for v, c in enumerate('23456789TJQKA', start=2)}
    def rank(hand):
        """
        Reduce the hand to a compact form that can be directly compared to another.
        The score (or ranking) of a hand is essentially the count of same cards, in
        descending order - for example three of a kind scores (3,1,1), a double pair
        scores (2,2,1). Full House will score (3,2).
        We attribute (3,1,3) to a Flush, and (3,1,2) to a Straight.
        The next ranking value are the cards values themselves.
        """
        cards, colors = zip(*hand)
        cards = [values[c] for c in cards]
        score, cards = zip(*sorted([(cards.count(c), c) for c in set(cards)], reverse=True))

        # Handle some special cases (flush, straight...)
        if len(cards) == 5:
            flush = (len(set(colors)) == 1)
            if cards == (14,5,4,3,2):  # this is the 'Ace' type of straight
                straight = 1; cards = (5,4,3,2,1)
            else:
                straight = (cards[0]-cards[4] == 4)
            score = (((1,), (3,1,3)), ((3,1,2), (5,)))[straight][flush]
        return (score, cards)

    player1, player2 = slice(0, 5), slice(5, 10)
    return sum((rank(hand[player1]) > rank(hand[player2])) for hand in hands)

print(euler54())

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 2, markus.obi, Germany  --------------------------')
t1  = time.time()

# Python's feature of sorting tuples really comes in handy.
# I believe I created a quite elegant and short solution, which is still readable(!).
# (-[<some booleans>].index(True)) is a pretty funny concept to generate a rank.


import itertools
from collections import Counter
from operator import itemgetter

def rank(cards):
    sorted_cards = sorted(card.value for card in cards)
    histogram = Counter(sorted_cards)
    highcards = list(map(itemgetter(1), sorted(((v, k) for k, v in histogram.items()), reverse=True)))
    is_flush = len(set(card.color for card in cards)) == 1
    is_straight = list(histogram.values()).count(1) == 5 and sorted_cards[-1] - sorted_cards[0] == 4
    n_pairs = sum(1 for k, v in histogram.items() if v == 2)
    return (-[
        is_straight and is_flush,
        4 in histogram.values(),
        3 in histogram.values() and n_pairs == 1,
        is_flush,
        is_straight,
        3 in histogram.values(),
        n_pairs == 2,
        n_pairs == 1,
        True
    ].index(True),) + tuple(highcards)

lookup = list(map(str, range(10))) + list("TJQKA")
class Card(object):
    def __init__(self, s):
        self.value = lookup.index(s[0])
        self.color = s[1] # one char of "CDHS"

def solve():
    hands = []
    with open(filename) as f:
        for line in f.readlines():
            cards = [Card(s) for s in line.split()]
            hands.append([cards[:5], cards[5:]])
    print(sum(rank(player1_hand) > rank(player2_hand) for player1_hand, player2_hand in hands))

def main():
    import time
    start = time.time()
    solve()
    end = time.time()
    elapsed = end - start
    print("elapsed: {:.1f} ms".format(elapsed * 1000))

main()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 3, Towzeur, France  --------------------------')
t1  = time.time()


suits = {'S': 'spades',
         'H': 'hearts',
         'D': 'diamonds',
         'C': 'clubs'}

cardsValues = {'2': 2,
               '3': 3,
               '4': 4,
               '5': 5,
               '6': 6,
               '7': 7,
               '8': 8,
               '9': 9,
               'T': 10,
               'J': 11,
               'Q': 12,
               'K': 13,
               'A': 14}


def Winner(r1, r2):
    if max(r1,r2) == r1:
        return 1
    return 2

def convertHandToValueAndSuit(hand):
    h = []
    for card in hand:
        value = cardsValues[card[0]]
        suit = suits[card[1]]
        h.append((value, suit))
    return h


def convertCardToValueandSuit(playerX):
    r = []
    for hand in playerX:
        h = convertHandToValueAndSuit(hand)
        r.append(h)
    return (r)


def convertFile(filename):  # converti le fichier poker
    with open(filename, 'r') as data:  # ouvre le fichier puis le ferme
        lignes = data.readlines()  # liste des lignes
        player1, player2 = [], []  # init des mains des 2 joueurs
        for ligne in lignes:  # parcour les lignes
            l = ligne.replace('\n', '').split(' ')  # enleve les \n et
            player1.append(l[:5])  # les 5 première cartes de la ligne au joueur 1
            player2.append(l[5:])  # les 5 dernière cartes de la ligne au joueur 2
    return player1, player2


def evaluateHand(hand):
    def Tri(hand):
        cardsValues = []
        cardsSuits = []
        for card in hand:
            cardsValues.append(card[0])
            cardsSuits.append(card[1])
        cardsValues.sort(reverse=True)
        return cardsValues, cardsSuits

    def HighCard(hand):
        ''' Highest value card. '''
        cardsValues, cardsSuits = Tri(hand)
        return [0] + cardsValues

    def OnePair(hand):
        '''Two cards of the same value.'''
        cardsValues, cardsSuits = Tri(hand)
        for value in cardsValues:
            if (cardsValues.count(value)) == 2:
                return [1] + [value] + [i for i in cardsValues if i != value]
        return False

    def TwoPairs(hand):
        '''Two different pairs.'''
        cardsValues, cardsSuits = Tri(hand)
        pairs = []

        for value in cardsValues:
            if (cardsValues.count(value)) == 2:

                l = [i for i in cardsValues if i != value]
                pairs.append(value)

                for value2 in l:
                    if (cardsValues.count(value2)) == 2:
                        pairs.append(value2)
                        l2 = [i for i in l if i != value2]
                        return [2] + pairs + [l2[0]]
        return False

    def ThreeOfaKind(hand):
        '''Three cards of the same value.'''
        cardsValues, cardsSuits = Tri(hand)
        for value in cardsValues:
            if (cardsValues.count(value)) == 3:
                l = [i for i in cardsValues if i != value]
                return [3] + [value] + l
        return False

    def Straight(hand):
        '''All cards are consecutive values.'''
        cardsValues, cardsSuits = Tri(hand)
        for i in range(5):
            if cardsValues[i] != cardsValues[0] - i:
                return False
        return [4] + cardsValues

    def Flush(hand):
        '''All cards of the same suit.'''
        cardsValues, cardsSuits = Tri(hand)
        if cardsSuits.count(cardsSuits[0]) == 5:
            return [5] + cardsValues
        return False

    def FullHouse(hand):
        '''Three of a kind and a pair.'''
        cardsValues, cardsSuits = Tri(hand)
        for value in cardsValues:
            if (cardsValues.count(value)) == 2:
                a = value
                l = [i for i in cardsValues if i != value]
                if l.count(l[0]) == 3:
                    return [6] + [l[0]] + [a]
        return False

    def FourOfaKind(hand):
        '''Four cards of the same value.'''
        cardsValues, cardsSuits = Tri(hand)

        for value in cardsValues:
            if cardsValues.count(value) == 4:
                l = [i for i in cardsValues if i != value]
                return [7] + [value] + [l[0]]
        return False

    def StraightFlush(hand):
        ''' All cards are consecutive values of same suit. '''
        if Straight(hand) != False and Flush(hand) != False:
            cardsValues, cardsSuits = Tri(hand)
            return [8] + cardsValues
        return False

    def RoyalFlush(hand):
        '''Ten, Jack, Queen, King, Ace, in same suit.'''
        cardsValues, cardsSuits = Tri(hand)
        if cardsValues == [14, 13, 12, 11, 10] and Flush(hand) != False:
            return [9]
        return False

    rank = {0: (HighCard, 'HighCard'),
            1: (OnePair, 'OnePair'),
            2: (TwoPairs, 'TwoPairs'),
            3: (ThreeOfaKind, 'ThreeOfaKind'),
            4: (Straight, 'Straight'),
            5: (Flush, 'Flush'),
            6: (FullHouse, 'FullHouse'),
            7: (FourOfaKind, 'FourOfaKind'),
            8: (StraightFlush, 'StraightFlush'),
            9: (RoyalFlush, 'RoyalFlush')}

    evalutation = HighCard(hand)

    for i in range(9, 0, -1):
        r = rank[i][0](hand)
        if r != False:
            evalutation = r
            break

    # print(evalutation)
    return evalutation


def problem54():
    player1, player2 = convertFile(filename)

    p1r = convertCardToValueandSuit(player1)
    p2r = convertCardToValueandSuit(player2)

    maReponse = []
    for i in range(1000):
        hand1 = evaluateHand(p1r[i])
        hand2 = evaluateHand(p2r[i])

        winner = Winner(hand1, hand2)
        # if i in erreurs:
        # print(player1[i], player2[i])
        # print(p1r[i], p2r[i])
        # print(hand1, hand2)
        # print(winner)

        if winner == 1:
            maReponse.append(1)
        else:
            maReponse.append(0)
    return (maReponse.count(1))


answer = problem54()


print('Answer : ', answer)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 4, windkingg, Turkey  --------------------------')
t1  = time.time()

f= open(filename, "r")
hands=[]

for line in f:
    p1=line[:14].split(" ")
    p2=line[15:].rstrip().split(" ")
    hands.append([p1,p2])

f.close()

def rank_hand(hand):
    pair=[0,0]
    trio=False
    foro=False
    flush=False
    straight=False
    royal=False
    high_card=[]
    values={}
    suits={"S":0,"D":0, "H":0, "C":0}

    for card in hand:
        val=card[0]
        suit=card[1]
        suits[suit]+=1
        if val=="T":
            val=10
        elif val=="J":
            val=11
        elif val=="Q":
            val=12
        elif val=="K":
            val=13
        elif val=="A":
            val=14
        else:
            val=int(val)
        if val in values:
            values[val]+=1
        else:
            values[val]=1

    for key in values:
        if values[key]==2:
            pair[0]+=1
            if key>pair[1]:
                pair[1]=key
        elif values[key]==3:
            trio=key
        elif values[key]==4:
            foro=key
        else:
            high_card.append(key)

    high_card=sorted(high_card)
    high_card=high_card[::-1]

    if len(high_card)==5:
        if sum(high_card)==60:
            royal=True
            straight=True
        elif high_card[0]-high_card[4]==4:
            straight=True

    for key in suits:
        if suits[key]==5:
            flush=True

    if flush and royal:
        return (10,high_card)
    elif straight and flush:
        return (9,high_card)
    elif foro:
        return (8,foro,high_card)
    elif pair[0]==1 and trio:
        return (7,trio,pair[1],high_card)
    elif flush:
        return (6,high_card)
    elif straight:
        return (5,high_card)
    elif trio:
        return (4,trio,high_card)
    elif pair[0]==2:
        return (3,pair[1],high_card)
    elif pair[0]==1:
        return (2,pair[1],high_card)
    else:
        return (1,high_card)

def compare_hands(games):
    p1_won=0
    p2_won=0
    for hands in games:
        p1=hands[0]
        p2=hands[1]
        if rank_hand(p1)>rank_hand(p2):
            p1_won+=1
        else:
            p2_won+=1
    return p1_won,p2_won

print (compare_hands(hands))


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 5,  jtp_10, France --------------------------')
t1  = time.time()

from collections import Counter

INPUT, LINES = filename, 1000
# translate the special cards to values
T = { 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14 }
TOP = 100;


def line(f):
    return f.readline().strip()


def format_hand(hand):
    return sorted([(T[h[0]] if h[0] in T else int(h[0]), h[1]) for h in hand])


def score(hand):
    res = [0, 0, 0, 0] # score vector
    values = tuple([x[0] for x in hand])
    max_v, min_v = max(values), min(values)
    straight = tuple([x - min_v for x in values]) == tuple(range(5))
    cnt = Counter(values).most_common()
    suits = tuple([x[1] for x in hand])
    same_suit = all(suits[0] == suit for suit in suits)

    if same_suit and straight and min_v == 10: # Royal flush
        res[0] = TOP
    elif same_suit and straight: # Straight flush
        res[0] = TOP - 1
        res[1] = max_v
    elif cnt[0][1] == 4: # Four of a kind
        res[0] = TOP - 2
        res[1] = cnt[0][0]
        res[2] = max_v
    elif cnt[0][1] == 3 and cnt[1][1] == 2: # Full House
        res[0] = TOP - 3
        res[1] = cnt[0][0]
        res[2] = cnt[1][0]
    elif same_suit: # Flush
        res[0] = TOP - 4
        res[1] = max_v
    elif straight: # Straight
        res[0] = TOP - 5
        res[1] = max_v
    elif cnt[0][1] == 3: # Three of a kind
        res[0] = TOP - 6
        res[1] = cnt[0][0]
        res[2] = max_v
    elif cnt[0][1] == 2 and cnt[1][1] == 2: # Two Pairs
        res[0] = TOP - 7
        res[1] = max(cnt[0][0], cnt[1][0])
        res[2] = min(cnt[0][0], cnt[1][0])
        res[3] = cnt[2][0]
    elif cnt[0][1] == 2: # One Pair
        res[0] = TOP - 8
        res[1] = cnt[0][0]
        res[2] = max_v
    else: # High Card
        res[0] = TOP - 9
        res[1] = max_v

    return tuple(res)

def solve():
    f = open(INPUT, 'r')
    ans = 0
    for _ in range(LINES):
        data = line(f).split()
        p1, p2 = format_hand(data[:5]), format_hand(data[5:])
        if score(p1) >= score(p2):
            ans += 1
    print(ans)
    f.close()

solve()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 6, Avi Levy, USA  --------------------------')
t1  = time.time()

cards = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
suits = ['S','D','C','H']
def val(card):
  return (cards.index(card[0]),card[1])

def flush(hand):
  return len(set(suit for card, suit in hand)) == 1

def straight(hand):
  s = set(card for card, suit in hand)
  return len(s) == 5 and max(s) - min(s) == 4, max(s)

def royal(hand):
  return min(card for card, suit in hand) >= cards.index('T')

def worth(hand):
  # [high card, one pair, two pair, three of a kind, straight, flush, full house, four of a kind, straight flush, royal flush]
  if straight(hand)[0] and flush(hand):
    if royal(hand):
      return 9, None
    print(hand)
    input()
    return 8, None
  d = {}
  for card, suit in hand:
    if card in d:
      d[card] += 1
    else:
      d[card] = 1
  e = sorted(d.values())
  if e[-1] == 4:
    return 7, max(card for card, freq in d.items() if freq == 4)
  if e[-1] == 3 and e[-2] == 2:
    return 6, max(card for card, freq in d.items() if freq == 3)
  if flush(hand):
    return 5, None
  if straight(hand)[0]:
    return 4, straight(hand)[1]
  if e[-1] == 3:
    return 3, max(card for card, freq in d.items() if freq == 3)
  if e[-1] == 2:
    if e[-2] == 2:
      return 2, max(card for card, freq in d.items() if freq == 2)
    return 1, max(card for card, freq in d.items() if freq == 2)
  return 0, None

def tiebreak(one, two):
  x = [card for card, suit in one]
  y = [card for card, suit in two]

  while x:
    a = max(x)
    b = max(y)

    if a > b:
      return True
    if a < b:
      return False
    x.remove(a)
    y.remove(b)

hands = []
for line in open(filename):
  line = line.strip().split(' ')
  if len(line) == 10:
    one = list(map(val, line[:5]))
    two = list(map(val, line[5:]))
    hands.append((one, two))

count = 0
for one, two in hands:
  a,b = worth(one)
  c,d = worth(two)

  if a > c:
    count += 1
    continue
  if a < c:
    continue


  if b is not None:
    if b > d:
      count += 1
      continue
    if b < d:
      continue
  if tiebreak(one, two):
    count += 1
print(count)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')





print('\n--------------------------SOLUTION 7,  philiplu, USA --------------------------')
t1  = time.time()
# Not a mathy problem, but I'm using Project Euler to learn Python,
# and this one was great for getting into some other areas.
# Not sure how pythonic this code is, but I like the way this came out.
# About 65 lines, including a few comments.
# Really pleased how an appropriate data structure made the ranking and comparisons trivial.


from enum import IntEnum


CardVals = { '2':2, '3':3, '4':4, '5':5, '6':6, '7':7,'8':8,
             '9':9, 'T':10, 'J':11, 'Q':12, 'K':13, 'A':14 }

class Rank(IntEnum):
    HighCard      = 1
    OnePair       = 2
    TwoPair       = 3
    ThreeOfAKind  = 4
    Straight      = 5
    Flush         = 6
    FullHouse     = 7
    FourOfAKind   = 8
    StraightFlush = 9
    RoyalFlush    = 10

class Hand:
    """
    A hand is encoded as a rank and a list of 5 tuples, each tuple recording
    the count of cards having the same value, then the value from 1 (ace low)
    to 14 (ace high).  The list is sorted in reverse order, by card count then
    card value.  This allows for easy comparisons.  The suit is thrown away,
    after detecting a flush.
    """
    def __init__(self, cards):
        flush = len(set(card[1] for card in cards)) == 1
        vals = [CardVals[card[0]] for card in cards]
        self.cards = sorted([(vals.count(val), val) for val in vals], reverse=True)
        if self.cards[0][0] == 4:            self.rank = Rank.FourOfAKind
        elif self.cards[0][0] == 3:
            if self.cards[3][0] == 2:        self.rank = Rank.FullHouse
            else:                            self.rank = Rank.ThreeOfAKind
        elif self.cards[0][0] == 2:
            if self.cards[2][0] == 2:        self.rank = Rank.TwoPair
            else:                            self.rank = Rank.OnePair
        else:   # nothing paired up, all counts will be 1
            if self.cards[0][1] == 14 and \
                    self.cards[1][1] == 5 and \
                    self.cards[4][1] == 2:
                # special case - straight with ace low
                self.cards[0] = (1, 1)
                self.cards.sort(reverse=True)
            if self.cards[0][1] == self.cards[4][1] + 4:
                if not flush:                self.rank = Rank.Straight
                elif self.cards[0][1] == 14: self.rank = Rank.RoyalFlush
                else:                        self.rank = Rank.StraightFlush
            elif flush:                      self.rank = Rank.Flush
            else:                            self.rank = Rank.HighCard

    def __lt__(self, other):
        if self.rank == other.rank:
            return self.cards < other.cards
        return self.rank < other.rank

def p54():
    count = 0
    with open(filename) as f:
        for line in f:
            cards = line.split()
            if Hand(cards[:5]) > Hand(cards[5:]):
                count += 1
    return count

print(p54())

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
















