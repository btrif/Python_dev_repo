#  Created by Bogdan Trif on 17-03-2018 , 5:12 PM.
from sys import stdin

# x = stdin.read(1)
# userinput = stdin.readline()
# betAmount = int(userinput)
# print ("x=",x)
# print ("userinput=",userinput)
# print ("betAmount=",betAmount)



'''
PROBLEM 1

Consider an array of n decimal integers named elements. We want to rearrange elements according to the following rules:

= Sort the integers in ascending order by the number of 1's in their binary representations. 
For example, (7)10 → (111)2 and (8)10 → (1000)2, so 8 (which has one 1 in binary) would be 
ordered before 7 (which has three 1's in binary).

= Two or more integers having the same number of 1's in their binary representations are ordered by increasing decimal value. 
For example, (5)10 → (101)2 and (6)10 → (110)2 both contain two 1's in their binary representation, 
so 5 would be ordered before 6 because it has the smaller decimal value.

Complete the rearrange function in the editor below. It has one parameter: an array of n integers, elements. 
The function must sort the elements array according to the rules above and return the sorted array.

Input Format

The internal test cases read the following input from stdin and passes it to the function:

The first line contains an integer, n, denoting the number of integers in elements.

Each line i of the n subsequent lines (where 0 ≤ i < n) contains an integer describing elementsi.

Constraints

1 ≤ n ≤ 10^5

1 ≤ elementsi ≤ 10^9

Output Format

Return an array of n integers denoting the sorted elements.

Sample Input 0

3
1
2
3


Sample Output 0

1
2
3


Explanation 0

Given elements = [1, 2, 3]:

(1)10 → (1)2

(2)10 → (10)2

(3)10 → (11)2

The decimal integers 1 and 2 both have one 1 in their binary representation, 
so we order them by increasing decimal value (i.e., 1 < 2). 
The decimal integer 3 has two 1's in its binary representation, so we order it after 1 and 2. 
We then return elements = [1, 2, 3] as our sorted array.

Sample Input 1

5
5
3
7
10
14


Sample Output 1

3
5
10
7
14


Explanation 1

Given elements = [1, 2, 3]:

(5)10 → (101)2

(3)10 → (11)2

(7)10 → (111)2

(10)10 → (1010)2

(14)10 → (1110)2

The decimal integers 5, 3, and 10 have two 1's in their binary representations, 
so we order them by increasing decimal value (i.e., 3 < 5 < 10). 
The decimal integers 7 and 14 have three 1's in their binary representations, 
so we place them after 3, 5, and 10 in increasing decimal order (i.e., 7 < 14). 
We then return elements = [3, 5, 10, 7, 14] as our sorted array.
For example:


Input	Result
    3       1
    2       3
    1       2
    3

'''


import sys

"""
* Complete the function below.
* DO NOT MODIFY CODE OUTSIDE THIS FUNCTION!
"""

def rearrange( L ):
    ''' IMPORTANT NOTICE : Normally an assertion should be placed in main
     to assert that the first element of  sys.stdin.readlines()[0] == nr_of_lines -1.
     As I am not allowed to edit outside this function I must work only with what arrives
     as argument within the function which is my list . The correct approach would be to
     check this in the main()  before it passes to the function    '''

    assert( 1 <= len(L) <= 10**5 ), " Please make sure that the list has at least one element and maximum of 10^5 elements "

    from collections import OrderedDict
    arrangedL = []
    D = OrderedDict()

    for i in L :
        if  1 <= i <= 10** 9 :
            ones = str(bin(i)).count('1')
    #         print('elem = ',i, '      bin = ', str(bin(i)). split('b')[1], '    ones = ', ones  )
            if not ones in D :
                D[ones] = [i]

            else : D[ones].append(i)

    for k, v in sorted( D.items()) :
        print(k, sorted(v) )
        arrangedL.extend(sorted(v) )

    return arrangedL




"""
* DO NOT MODIFY CODE BELOW THIS POINT!
"""
def main():
    data = sys.stdin.readlines()

    elements = []

    for i in range(1, int(data[0]) + 1):
        elements.append(int(data[i]))

    result = rearrange(elements)

    for val in result:
        print(val)

main()