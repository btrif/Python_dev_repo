x=100
h=100
l=0
y=0
print ("Please think of a number between 0 and 100!")
while True:
   if y!='c':
       print ("Is your secret number " + str(int((h+l)/2)) +"?")
       y=input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
       if y not in ('h', 'l', 'c'):
            print("Sorry. I did not understand your input.")
            continue
       elif y=='h':
         h=(h+l)//2
         int(h)
       elif y=='l':
        l=(h+l)//2
        int(l)
   else:
    break
print ("Game Over. Your secret number was: " + str(int((l+h)/2)) )

#########################################################

ans= 0
neg_flag= False
x = int(input("Enter an integer: "))
if x < 0:
    neg_flag= True
while ans**2 < x:
    ans = ans+ 1
if ans**2 == x:
    print("Square root of", x, "is", ans)
else:
    print(x, 'is not a perfect square')
    if neg_flag:
        print('Just checking... did you mean', -x, '?')

##############################################


print('\n\n-------------- User Input Validation Check : ---------------------------')

while True:
    try:
        n = input("Please enter an integer: ")
        n = int(n)
        break
    except ValueError:
        print("Input not an integer; try again")
print("Correct input of an integer!")

##############################################

print('\n\n-------------- User Input String Letter Validation Check : ---------------------------')

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
while True:
    try:
        guess = input("Please guess a letter: ")
        if guess in letters:
            guessLower = guess.lower()
            break

    except TypeError:
        print('Please enter a letter.')

#######################################
print('\n\n-------------- File Input CONTROL : ---------------------------')

data = []
file_name= input("Provide a name of a file of data ")
try:
    fh= open(file_name, 'r')
except IOError:
    print('cannot open', file_name)
else:
    for new in fh:
        if new != '\n':
            addIt = new[:-1].split(',') #remove trailing \n
            data.append(addIt)
finally:
    fh.close() # close file even if fail