import random
import string
from ps4b import *


VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print("  ", len(wordList), "words loaded.")
    return wordList


def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    S = 0
    for i in str(word) :
        S += SCRABBLE_LETTER_VALUES[str(i)]
    if len(word) == n :
        return S*len(word)+50
    else : return S*len(word)


def dealHand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand={}
    numVowels = n // 3

    for i in range(numVowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1

    for i in range(numVowels, n):
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1

    return hand


def displayHand(hand):
    """
    Displays the letters currently in the hand.

    For example:
    #>>> displayHand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter,end=" ")       # print all on the same line
    print()                             # print an empty line


def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it.

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)
    returns: dictionary (string -> int)
    """
    hnd = hand.copy()
    for i in word :
        if hnd.get(str(i)) != None :
            #print(i,  handd.get(str(i)), end=' ->   ')
            hnd[str(i)] = hnd.get(str(i)) -1
        #hand = hnd.copy()
    return hnd


def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.

    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    w_l=  [[x, word.count(x)] for x in set(word)]
    #print(w_l)
    val =[]
    for i in w_l:
        if hand.get(str(i[0])) != None :
            val.append(hand.get(str(i[0])) - i[1])
        else : val.append(-1)
    #print(val)
    if len(val) > 0 :
        if min(val) >= 0 and word in wordList :
            return True
        else :
            return False
    else :
        return False


def calculateHandlen(hand):
    """
    Returns the length (number of letters) in the current hand.

    hand: dictionary (string-> int)
    returns: integer
    """
    S=0
    for k,v in hand.items() :
        S += v
    return S  #print(S)


wordList = loadWords()


def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".")
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)

    """
    # BEGIN PSEUDOCODE <-- Remove this comment when you code this function; do your coding within the pseudocode (leaving those comments in-place!)
    # Keep track of the total score
    # As long as there are still letters left in the hand:
            # Display the hand
            # Ask user for input
            # If the input is a single period:
                    # End the game (break out of the loop)

        # Otherwise (the input is not a single period):
                # If the word is not valid:
                        # Reject invalid word (print a message followed by a blank line)

            # Otherwise (the word is valid):
                    # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
                    # Update the hand

    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    Total = 0
    #hand= {'w':1, 's':1, 't':2, 'a':1, 'o':1, 'f':1}
    hnd = hand.copy()
    hnd_lst = [x for x in hnd.values() if x >0]
    while True:
            if len(hnd_lst) > 0 :
                    print('Current Hand:   ',end=''),displayHand(hnd)
                    word = input('Enter word, or a "." to indicate that you are finished: ')
                    if word == '.' :
                        print('Goodbye! Total score:', Total ,'points.\n')
                        break
                    elif isValidWord(word, hnd, wordList) == True :
                        hnd = updateHand(hnd, word)
                        score = getWordScore(word, n)
                        #print('Score',score)
                        #print(len(word),calculateHandlen(hnd))
                        Total += score
                        print(word, 'earned', getWordScore(word, n) , ' points. Total: ' , Total )
                        hnd_lst = [x for x in hnd.values() if x >0]
                    else :
                        print('Invalid word, please try again.')
            else:
                    print('\nRun out of letters. Total score: ',Total,' points.')
                    break


def playGame_user_only(wordList):
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.

    2) When done playing the hand, repeat from step 1
    """
    n = HAND_SIZE
    while True:
        choice = input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        if choice == 'n' :
            hand = dealHand(n)
            #print(hand)
            playHand(hand, wordList, n)
        elif choice == 'r' :
            try:
                hand
            except NameError:
                print ('You have not played a hand yet. Please play a new hand first!')
            else:
                playHand(hand, wordList, n)
        elif choice == 'e' :
            break
        else :
            print('Invalid command.')



def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.

        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    n = HAND_SIZE
    while True:
            choice = input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
            while choice == 'n' :
                choice_player =input('Enter u to have yourself play, c to have the computer play:')
                if choice_player == 'u' :
                    hand = dealHand(n)
                    #print(hand)
                    playHand(hand, wordList, n)
                    break

                elif choice_player == 'c':
                    hand = dealHand(n)
                    #print('Current Hand:  ', hand)
                    compPlayHand(hand, wordList, n)
                    break
                else :
                    print('Invalid command.\n')

            if choice == 'r' :
                try:
                    hand
                except NameError:
                    print ('You have not played a hand yet. Please play a new hand first!')
                else:
                    choice_player =input('Enter u to have yourself play, c to have the computer play:')
                    if choice_player == 'u' :
                        playHand(hand, wordList, n)
                    elif choice_player == 'c':
                        compPlayHand(hand, wordList, n)
                    else :
                        print('Invalid command..\n')

            elif choice == 'e' :
                break
            elif choice not in ['n' , 'r' , 'e' ] :
                print('Invalid command.\n')



playGame(wordList)