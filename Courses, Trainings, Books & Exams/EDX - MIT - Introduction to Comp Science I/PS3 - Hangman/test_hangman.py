import random

WORDLIST_FILENAME = "words_hangman.txt"

global wordlist
wordlist =''

def loadWords():
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()

    print("  ", len(wordlist),  "words loaded.")
    return wordlist


def chooseWord(wordlist):
    return random.choice(wordlist)


wordlist = loadWords()

#secretWord=chooseWord(wordlist)
print('\n-----------------------------------------------')


#secretWord='mangosteen'
#print('secret Word :',secretWord)

#lettersGuessed = ['a', 'e', 't', 'b', 'g', 'o', 'c', 'm', 'n', 's']
#print('letters Guessed : ',lettersGuessed)

'''
unguessed = list(len(secretWord)*'_')

ung =len(secretWord)*'_'
print(ung, len(ung))

print(unguessed, len(unguessed))

lG = list(lettersGuessed)
sW=list(secretWord)

for k in lettersGuessed:
    if k in sW:
        ss = list(secretWord.replace(k,'1'))
        print(ss)
        for j in range(len(ss)) :
            if ss[j] == '1' :
                unguessed[j] = k

print(unguessed, len(unguessed))

print(' '.join(unguessed))

#for i in range(0, len(unguessed)):
#    unguessed.insert(i*2,' ')
#print(unguessed, len(unguessed))

    #secretWord.replace(x, ''_)
    #sW = secretWord.replace(x, ''_)


#print('\n'*2,secretWord.replace('i','_ '))


letters=''
for i in secretWord:
    if i in lettersGuessed:
        letters+=i
print('-->  ',letters)


a = getGuessedWord('mangosteen', ['i', 'p', 't', 'b', 'q', 'z', 'c', 'm', 'n', 's']).replace(' ','')
#print(a)
b = a.replace('_','')
#print(b, type(b))
#print( 'm _ n _ _ s t _ _ n' == getGuessedWord('mangosteen', ['i', 'p', 't', 'b', 'q', 'z', 'c', 'm', 'n', 's']))
bb = getGuessedWord(secretWord, lettersGuessed)
#print(type(bb))

#print(isWordGuessed(secretWord, lettersGuessed))

'''

def getGuessedWord(secretWord, lettersGuessed):
    # secretWord: string, the word the user is guessing
    # lettersGuessed: list, what letters have been guessed so far
    # returns: string, comprised of letters and underscores that represents
    # what letters in secretWord have been guessed so far.

    unguessed = list(len(secretWord)*'_')
    #lG = list(lettersGuessed)
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

print(getGuessedWord('mangosteen', ['i', 'p', 't', 'b', 'q', 'z', 'c', 'm', 'n', 's']),'\n')

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




print(isWordGuessed('apple', ['a', 'e', 'i', 'k', 'p', 'r', 's']))








def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    letters_available = letters[:]
    for i in lettersGuessed:
        letters_available.remove(i)

    return ''.join(letters_available)


# print(getAvailableLetters(lettersGuessed))