

print('\n -----------------------First Method,  converts the strings to int : ----------------')
'''		FILE SAMPLE
08 02 22 97 38 15
49 49 99 40 17 81
'''
f = open('matrix_file.txt', 'r')
text = f.read()

# Initialize and populate grid
grid = []
print(text,type(text),'\n')

for row in text.split('\n'):
    grid.append(list(map(int, row.split(' '))))         # This maps the strings into ints on the run, SMART TECHNIQUE
    #print(row, type(row))

f.close()
print('Check : ',grid[2][2]*grid[3][3])

print('\n===================  BETTER METHODS =================')
'''	FILE SAMPLE
4445,2697,5115,718,2209
2212,654,4348,3079,6821
'''
filename = 'D:\Google Drive\Computing & PROGRAMMING\Python\WORK\simple scripts\matrix_file.txt'
def load_file(filename):
	with open(filename) as f:
		matrix = [list(map(int, line.split(","))) for line in f.readlines()]
	f.close()
	return matrix

# print(load_file(filename))


print('\n------------------------NICE METHODS ----------------------------')
filename = "D:\Google Drive\Computing & PROGRAMMING\Python\WORK\Project EULER\pb096_test_matrix.txt"

''' FILE SAMPLE
003020600
900305001
'''

def load_file_1(filename):
    M=[]
    with open(filename) as f:
        M = [list(map(int, line.rstrip('\n') )) for line in f.readlines()]
    return M

def load_file_2(filename):
    M=[]
    with open(filename, 'r') as f :
        for line in f :
            # print(line, type(line))
            M.append([ int(i) for i in line.rstrip('\n') ])
    return M

def load_file_3(filename) :
    matrix=[]
    f = open(filename, 'r')
    text = f.read()
    for row in text.split('\n'):
        matrix.append(list(map(int, row)))
    return matrix

print(load_file_1(filename))
print(load_file_2(filename))
print(load_file_3(filename))






print('\n-----------------------numpy genfromtxt-------------------------------------')

def load_genfromtxt(filename):
	from numpy import genfromtxt
	M = genfromtxt(filename, delimiter=',')
	rows = M.shape[0]
	cols = M.shape[1]
	return M

print(load_genfromtxt("D:\Google Drive\COMPUTING & PROGRAMMING\PYTHON\WORK\Project EULER\pb081_matrix.txt"))


##############################################
print('\n -----------------------Second Method,  uses strings : ----------------')

fl = open('matrix_file.txt')
grid =[]
while True:
	line = fl.readline()
	if len(line)==0:
		break
	row= line.replace('\n','').split(' ')
	print (row)
	grid.append(row)

fl.close()
print(grid[2][2])




###############################################

# Using pandas to manipulate files , IT WORKS BUT I MUST FIX THE NUMPY ERROR
print( ' ------------------   Using pandas to manipulate files  -----------')
import pandas as pd
df=pd.read_csv('pb099_base_exp.txt', sep=',',header=None)
print(df.values)

print('------'*20)
print('\n ---  Load the file line by line separated by new line and on each line separated by comma :---------')
# Load the file line by line separated by new line and on each line separated by comma :
filePath = r'pb099_base_exp.txt'
data = [(line.rstrip('\n')).split(',') for line in open(filePath)]

# Transform the data into INTEGERS :
for i,line in enumerate(data):
    data[i] = [int(num) for num in line]
print(type(data[0]), type(data[0][0]),data)

##############################################
print('------------------Create Empty File---------------------')
# Python program that creates new, empty file
# New, empty file. The second argument to open() is a string containing "mode" flag characters.
# The "w" specifies write-only mode—no appending or reading is done.
# Erased: If the file happens to exist, it is erased. So be careful when developing programs with this call.

# Create new empty file. ... If the file exists, it will be cleared of content.
f = open("test.file", "w")             # Absolute path C:\\programs\\test.file

print('------------------ Write Lines ---------------------')
# Python program that uses write
# Write lines. This program writes lines to a file. It first creates an empty file for writing.
# It specifies the "w" mode to create an empty file. Then it writes two lines.
# Tip: The line separators (newline chars) are needed. There is no "writeline" method available.
# Create an empty file for writing.
with open("test.file", "w") as f:
    # Write two lines to the file.
    f.write('cat\naaaa\nbbbbb\naaaa\nbbbbb\n\naaaa bbbbb\nCCcc\nxx\ny y y y y\n\nZ')
    f.write("bird\n")

print('------------------ Count character frequencies ---------------------')
# Python program that counts characters in file
# Count character frequencies. This program opens a file and counts each character using a frequency dictionary.
# It combines open(), readlines, and dictionary's get().
# Strip: The program strips each line because we do not want to bother with newline characters.
# Get: The code uses the two-argument form of get. If a value exists, it is returned—otherwise, 0 is returned.
# Open a file.
f = open(r"test.file", "r")
# Stores character counts.
chars = {}
# Loop over file and increment a key for each char.
for line in f.readlines():
    for c in line.strip():
    # Get existing value for this char or a default of zero.	# ... Add one and store that.
        chars[c] = chars.get(c, 0) + 1
for item in chars.items():    print(item)       # Print character counts.



