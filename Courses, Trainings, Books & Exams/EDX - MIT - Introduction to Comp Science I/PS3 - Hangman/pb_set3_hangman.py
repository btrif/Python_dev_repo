# Made by bogdan Trif @ 2016-10-08
# Hangman game
#
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words_hangman.txt"

global wordlist
wordlist =''

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()

    print("  ", len(wordlist),  "words loaded.")
    return wordlist


#print( wordlist )

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    # secretWord: string, the word the user is guessing
    # lettersGuessed: list, what letters have been guessed so far
    # returns: boolean, True if all the letters of secretWord are in lettersGuessed;
    # False otherwise
    word=''
    for i in secretWord:
        if i in lettersGuessed:
            word+=i
    if secretWord == word : return True
    else : return False


def getGuessedWord(secretWord, lettersGuessed):
    # secretWord: string, the word the user is guessing
    # lettersGuessed: list, what letters have been guessed so far
    # returns: string, comprised of letters and underscores that represents
    # what letters in secretWord have been guessed so far.

    unguessed = list(len(secretWord)*'_')
    sW=list(secretWord)
    for k in lettersGuessed:
        if k in sW:
            ss = list(secretWord.replace(k,'1'))
            #print(ss)
            for j in range(len(ss)) :
                if ss[j] == '1' :
                    unguessed[j] = k
    ung = ' '.join(unguessed)
    return ung


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    global letters_available
    letters_available = letters[:]
    for i in lettersGuessed :
        letters_available.remove(i)

    return ''.join(letters_available)


def guesses_left():
    return 8-mistakes

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    global letters
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    global lettersGuessed
    lettersGuessed = []
    global mistakes
    mistakes = 0
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is', len(secretWord) ,'letters long.')

    while True:
            if guesses_left() > 0:
                    print('-----------')
                    print('You have', guesses_left() ,'guesses left.')
                    print('Available letters: ', getAvailableLetters(lettersGuessed))
                    while True:
                        try:
                            guess = input("Please guess a letter: ")
                            if guess in letters or guess.lower() in letters :
                                guessLower = guess.lower()
                                break

                        except TypeError:
                            print('Please enter a letter.')

                    if guessLower in lettersGuessed:
                        print("Oops! You've already guessed that letter:", getGuessedWord(secretWord, lettersGuessed))


                    elif guessLower in secretWord:
                        lettersGuessed.append(guessLower)
                        print('Good guess:', getGuessedWord(secretWord, lettersGuessed))


                        if  isWordGuessed(secretWord, lettersGuessed) :
                            print('-----------')
                            print('Congratulations, you won!')
                            break

                    elif guessLower not in secretWord:
                            print('Oops! That letter is not in my word:', getGuessedWord(secretWord, lettersGuessed))
                            lettersGuessed.append(guessLower)
                            mistakes += 1

            else:
                print('-----------')
                print('Sorry, you ran out of guesses. The word was', secretWord)
                break

# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)


secretWord = chooseWord(wordlist).lower()
#print(secretWord)
hangman(secretWord)

'''
# This is for test :
hangman('c')


secretWord = 'hipopotam'
lettersGuessed = 'abcdefoip'

print('1 -->',getGuessedWord(secretWord, lettersGuessed))
print('2-->', lettersGuessed)
print(isWordGuessed('ai',['a','i']))
'''