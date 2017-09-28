#!/usr/bin/python
# Prime number GENERATOR :
i = 2                               #Set the starting Prime, First Prime in the list, MAIN VARIABLE
END = 10                               #Set the END Prime, First Prime in the list, MAIN VARIABLE

while(i < END):                 # Set the last Prime Number - the Upper Limit
    j = 2
    while(j <= (i/j)):              # This condition checks in the lower list  
        if not(i%j): break          # IF  it's TRUE it stops, if FALSE it continues    # VERY IMPORTANT This line checks if the number is PRIME
        j = j + 1                       #Returns FALSE and continues if is i%j = 0 ; Returns TRUE and stops if i%j = 1,2,....
    if (j > i/j) : print( i, " is prime")           # If j > i/j means that the number is not already in the list, therefore must be another prime
    i = i + 1

print ("Good bye!")

print('==='*20)
#############################################
# There are many ways to solve this problem! Here is one:
# Generate ascending numbers
print('----------   VERY BASIC  NUMBER GENERATORS  ---------------')
num = 2
while num < 11:
    print(num, end=' ')
    num += 2
print("Goodbye!")

# Here is another:
num = 2
while num <= 10:
    print(num, end=' ')
    num += 2
print("Goodbye!")

# And another:
num = 0
while True:
    num += 2
    print(num, end=' ')
    if num >= 10:
        print("Goodbye!")
        break

# And one more:
num = 1
while num <= 10:
    if num % 2 == 0:
        print(num, end=' ')
    num += 1
print("Goodbye!")

# There are always many, many different ways to solve a programming
# problem. Here are just four examples and surely there are quite
# a few more.

'''
Write a while loop that sums the values 1 through end, inclusive. end is a variable that we define for you.
So, for example, if we define end to be 6, your code should print out the result:
21 which is 1 + 2 + 3 + 4 + 5 + 6.
For problems such as these, do not include input statements or define variables we will provide for you.
Our automating testing will provide values so write your code in the following box assuming these variables are already defined.
'''
print(' ------------ While loop and String manipulation :   ------------')
end=10
num=1
mysum = 0
string=''
while num <= end:
    string1=str(num)
    string = string + string1
    #print(a,end=' ')
    if num < end:
       string = string+' + '
    mysum += num
    num += 1

print(mysum, 'which is', string)
#######################################################
print('----'*25)

# Iterative algorithm, find if an integer is a cube by GENERATING GUESSES:
#x = int(input('Enter an integer: '))
x= 44
ans = 0
while ans**3 < x:
    ans = ans + 1
if ans**3 != x:
    print(str(x) + ' is not a perfect cube')
else:
    print('Cuberoot of '+ str(x) + ' is ' + str(ans))

###############################################
print('-------'*20)
# Find the maximum in a list a retain it :
nr=12
test_arr=[2,4,6,23,34,23,56,67,91, 45, 2, 123, 45,45,5,3,23,12]
for i in test_arr:
    if i > nr:
        nr = i
print('Maximum number is : ',nr)

print('\n--------------------------- DOUBLE WHILE LOOP ------------------------------')
i,j = 0,0
while i < 5 :
    while j < 5 :
        print(i, j, end='  ')
        j = j+1
    i = i + 1
    j=0

print('\n--------------------------- TRIPLE WHILE LOOP ------------------------------')

i,j,k=0,0,0
count=0
while i < 3 :
    while j < 3 :
        while k < 3 :
            count+=1
            print(str(count)+'. ', i, j, k,  end='   ')
            k+=1
        j+=1
        k=0
    j , k = 0,0
    i+=1
print('\n',count,' iterations')