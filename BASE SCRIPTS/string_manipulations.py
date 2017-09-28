# Remove left & right whitespaces :

J = '      Jena is beautiful         '
print('           original string J :', J, '\n  without white spaces :', J.rstrip().lstrip() )

#String going backwards. Reverse String
print('\n-------------  String going backwards. Reverse String ---------------')
a = '0123456789'
print(a[::2])               # Returns only the odd index elements, from 2 by 2
print(a[1::2])               # Returns only the even index elements, from 2 by 2
print(a[::-1])              #Reverses the string : becomes 54321
print(a[::-2])              #becomes 531
print(a[4::])              #from a fixed character to the end

print('\n------------ Palindrome Construction ------------------')
i=12345
print('the string is :', i)
print( 'Returns only the the characters until the last(not included) and Reversed :', str(i)+str(i)[ len(str(i))-2::-1] )


print( 'Completely Reverse the entire String :', str(i)+str(i)[::-1 ] )

print('----------------------')

L=[9,6,16,0,54,11,3, 11, 0, 6, 11]
print("Join a list of numbers in a string :",  ''.join( str(i) for i in  L ) )

#Last few elements
print(a[-3:])              # Last 3 elements in the string or list

#  If you want to remove leading and ending spaces, use str.strip():

sentence = ' hello  apple '
new = sentence.strip()
print(new)

# If you want to remove all spaces, use str.replace():

sentence = ' hello  apple'
new = sentence.replace(" ", "")
print(new)

#If you want to remove duplicated spaces, use str.split():

sentence = ' hello  apple'
new = " ".join(sentence.split())
print(new)

# Return Boolean if a character, or another string is in a string:
print('9' in '548139')
print('93' in '548139')

# String Fill with padding zeros, to have a proper length
print('1'.zfill(3))

print('----------------------String SPLIT --------------------')
# Input string.
s = "topeka,kansas city,wichita,olathe"
# Separate on comma.
cities = s.split(",")
# Loop and print each city name.
for city in cities:    print(city, end='  ')
# No arguments. Split() can be called with no argument. In this case, split() uses spaces as the delimiter.
# Please notice that one or more spaces are treated the same.
print('\n-------------------------')

# Input string.
s = "One two   three                four"       # ... Irregular number of spaces between words.
# Call split with no arguments.
words = s.split()
# Display results.
for word in words:    print(word, end ='   ')
print('\n----------------CSV file ---------')
# CSV file. This kind of file contains lines of text. It has values separated by commas. These files can be parsed with the split method.
# Methods:
# We combine the open(), readlines(), and strip() methods. The path passed passed to open should be corrected.
# Read Files
# Info: This CSV parser splits each line of text at the commas. It loops and displays the original data and the extracted values.
# Open this file.
f = open("perls.txt", "r")

# Loop over each line in the file.
for line in f.readlines():
    line = line.strip()         # Strip the line to remove whitespace.
    print(line)
    parts = line.split(",")             #     Split the line.
    # Display each part of the line, indented.
    for part in parts:
        print("   ", part)

print('\n------------rsplit-------------')
# Python program that uses rsplit
# CSV module. We do not need to use split() to manually parse CSV files. The csv module is available.
# It offers the csvfile type. We use dialects to detect how to parse files.
# Rsplit. Usually rsplit() is the same as split. The only difference occurs when the second argument is specified.
# This limits the number of times a string is separated.
# So:  When we specify 3, we split off only three times from the right. This is the maximum number of splits that occur.
# Tip: The first element in the result list contains all the remaining, non-separated string values. This is unprocessed data.
# Data :
s = "Buffalo;Rochester;Yonkers;Syracuse;Albany;Schenectady"
# Separate on semicolon.
cities = s.rsplit(";", 3)           # ... Split from the right, only split three.
# Loop and print.
for city in cities:   print(city)

print('\n------------Splitlines-------------')
# Python program that calls splitlines
# Lines of text can be separated with Windows, or UNIX, newline sequences.
# This makes splitting on lines complex. The splitlines() method helps here.
# And: We split the three-line string literal into three separate strings with splitlines(). We print them in a for-loop
# Data.
s = """This string
has many
lines."""
# Split on line breaks.
lines = s.splitlines()
# Loop and display each line.
for line in lines:    print("[" + line + "]")

print('\n------------Partition-------------')
# Python program that uses partition
# This method is similar to split(). It separates a string only on the first (leftmost) delimiter. It then returns a tuple containing its result data.
# Tuple: This has three parts. It has the left part, the delimiter character, and the remaining string data.
# Also: The rpartition() method is available. It acts from the right of the string, rather than the left. Partition is "lpartition."
# Input data.
s = "123 Oak Street, New York"
# Partition on first space.
t = s.partition(" ")
# Print tuple contents.
print(t)
# Print first element.
print("First element:", t[0])

print('\n------------Partition loop - While-------------')
# Python that uses partition, while-loop
# Partition loop. The result tuple of partition() makes it easy to use in a loop.
# We can continually partition a string, shortening the source data as we go along.
# Here: In this example, we continue to consume each word in a source string. We read in each word at a time.
# While:  We use the while-loop to continue as long as further data exists in the input string.
# The input string.
s = "Dot Net Perls website"
# Continue while the string has data.
while len(s) > 0:
    t = s.partition(" ")        # Partition on first space.
    print(t[0])                 # Display the partitioned part.
    print("    ", t)
    # Set string variable to non-partitioned part.
    s = t[2]

print('\n-------------------------------- slice ------------------------')
s = "ABCDEFGHIJKL"
sl = slice(0,4)
print (s[sl])

print('\n ----------------------- range of letters --------------------------')
for c in range(ord('a'), ord('z')+1):
    print (chr(c), end=' ' )

print('\n--------- Generator strings of three letters--------------------------')
cnt=0
for i in range(ord('a'), ord('z')+1):
    for j in range(ord('a'), ord('z')+1):
        for k in range(ord('a'), ord('z')+1):
            print (chr(i)+chr(j)+chr(k),  end='  ' )
            cnt+=1
    if cnt > 50 : break


print('\n\n--------------- Monotonic increase / decrease number -------------------')
def monotonic_number(n) :
    listN = list(str(n))
    flag1 = False
    flag2 = False
    for i in range(1, len(listN)):
        if listN[i] > listN[i-1]:
            flag1 = True
        if listN[i] < listN[i-1]:
            flag2 = True
    if flag1 == True and flag2 == True:
        return print('False . NOT monotonic ! ')
    else : return print('True. IS monotonic !')

monotonic_number(145665)

print('\n------------------- String, Integer Padding of a number -------------------')
#### Method I
print(  str(31).zfill(4), str(3).zfill(4), list(str(31).zfill(4)) )

#### Method II
add_nulls = lambda number, zero_count : "{0:0{1}d}".format(number, zero_count)
print(add_nulls(2,3) , list(add_nulls(2,3)))

#### Method III
print(  '%0*d' % (3, 4)  )

print('\n------------------- String,  fill out of a string with spaces  -------------------')
print( 'hi'.ljust(10) )
print('{0: <16}'.format('Hi'))
print("'%-10s'" % 'hi')
print( format(14, '#010b'))          #python convert to binary and keep leading zeros
print( '{:08b}'.format(1))          #python convert to binary and keep leading zeros


print('\n======== FIND & REPLACE n-th OCCURENCE ===================')
print('-------------------  FIND the n-th occurence of a string  -------------------')

def findnth(source, target, n):
    num = 0
    start = -1
    while num < n:
        start = source.find(target, start+1)
        if start == -1: return -1
        num += 1
    return start

Test_string = "abc=abc=abc=abc=abc"
print('Test_string : ' , Test_string.title() )

print('findnth , returns the index of the 2-nd occurence :\t',findnth(Test_string, 'abc', 2) )

print('\n------------------- ,  REPLACE  the n-th occurence of a string  -------------------')

def replacenth(source, old, new, n):
    p = findnth(source, old, n)
    if n == -1: return source
    return source[:p] + new + source[p+len(old):]

print('replacenth, replaces the 3-rd occurence :\t', replacenth(Test_string, "abc", "WXYZ", 3) )


print('\n-----------------------String Rotation --------------------')
def rotate(l, n):
    return l[-n:] + l[:-n]

A = '123456'
print('Initial string: \t', A, '          Right rotation :' , rotate(A,-1)  )
print('Initial string: \t', A, '          Left rotation with 2 units :' , rotate(A, 2)  )