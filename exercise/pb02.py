#  Created by Bogdan Trif on 17-03-2018 , 6:42 PM.
'''
Consider a string, expression consisting of the characters < and > only.
We consider the string to be balanced if each < always appears before (i.e., to the left of)
a corresponding > character (they do not need to be adjacent).
Moreover, each < and > act as a unique pair of symbols and neither symbol can be considered as part of
any other pair of symbols. For example, the strings <<>>, <>, and <><> are all balanced,
but the strings >>, <<>, and ><>< are unbalanced.

To balance a string, we can replace only > character with <> at most maxReplacement times.
Given an expression and the value of maxReplacement, can you turn an unbalanced string into a balanced one?

Complete the balancedOrNot function in the editor below. It has the following parameters:

An array of n strings, expressions, denoting the list of expressions to check.
An array of n integers, maxReplacements, where maxReplacementsi denotes the maximum number of replacements
allowed when attempting to balance expressionsi.
The function must return an array of integers where each index i (0 ≤ i < n)
contains a 1 if expressionsi is balanced or a 0 if it is not.

Input Format

A set of internal unit tests will be on the code with input in the following format.

The first line contains an integer, n, denoting the size of expressions.

Each line i of the n subsequent lines (where 0 ≤ i < n) contains a string describing expressionsi.

The next line contains an integer, m, denoting the size of maxReplacements.

Each line i of the n subsequent lines (where 0 ≤ i < n) contains a string describing maxReplacementsi.

Constraints :

1 ≤ n ≤ 10^2
1 ≤ length of expressionsi ≤ 10^5
0 ≤ maxReplacementsi ≤ 10^5
Output Format

The function must return an array of integers where each index i (0 ≤ i < n) contains a 1 if expressionsi is balanced or a 0 if it is not.

Observations

Check that your code runs before submitting it!
Sample Input 0

2
<>>>
<>>>>
2
2
2
Sample Output 0

1
0
Explanation 0

We process expressions = ["<>>>", "<>>>>"] and maxReplacements = [2, 2] like so:

For string <>>> with maxReplacements0 = 2, it becomes balanced after two replacements: <>>> → <><>> → <><><>.
Because the string was converted in ≤ maxReplacements0 replacements, we store a 1 in index 0 of our return array.
For string <>>>> with maxReplacements1 = 2,
becomes balanced after three replacements: <>>>> → <><>>> → <><><>> → <><><><>.
Because the string was converted in > maxReplacements1replacements, we store a 0 in index 1 of our return array.
We then return the array [1, 0] as our answer.

Sample Input 1

2
<>
<>><
2
1
0
Sample Output 1

1
0
Explanation 1

We process expressions = ["<>", "<>><"] and maxReplacements = [1, 0] like so:

For string <> with maxReplacements0 = 1, it is already balanced and needs no replacements.
Because the string is balanced in ≤ maxReplacements0 replacements, we store a 1 in index 0 of our return array.
For string <>>< with maxReplacements1 = 0, the string is not balanced.
It's impossible to balance the string because it ends in < (and we're also restricted to performing 0 replacements),
so we store a 0 in index 1 of our return array.
We then return the array [1, 0] as our answer.

For example:

Input	Result
2               1
<>>>        0
<>>>>
2
2
2

'''

import sys

"""
* Complete the function below.
* DO NOT MODIFY CODE OUTSIDE THIS FUNCTION!
"""


def balancedOrNot(expressions, maxReplacements):
    ''' Remark : Nice problem !
    :param expressions: lst, list of strings
    :param maxReplacements: , int, corresponding to each element in expressions
    :return: list of ints of 0, 1    '''


    assert ( len(expressions) == len(maxReplacements) ),  "The two lists must be of equal length"
    assert (   1<=  len(expressions) <= 10**2    ), " Please make sure that  the expressions length is greater than 1 & not greater than 10.000 "


    def tryToBalance( S, maxR):
        S = S.strip()       # I had some nasty bugs when copy paste and I put this condition !
        assert (   1<=  len(S) <= 10**5    ), " Please put not null strings arguments & not greater than 10.000 "
        assert (   0 <=  maxR <= 10**5    ), " Please put not negative strings arguments & not greater than 10.000 "

        a, b = '<', '>'
        cnta, cntb = S.count(a), S.count(b)


        if S.endswith(a) :  # CASE 0 : No need for further analysis
            return 0

        if cnta > cntb :    # CASE 1 : No need for further analysis as we cannot replace the '<' to balance
            return 0

        if cnta == cntb :               ### CASE 2 : Equal number of '<' and ' >'
            if S.startswith(a) and S.endswith(b) :
                return 1
            else :
                return 0

        if cnta < cntb :    ### CASE 3 : Detailed Analysis
            if maxR >= cntb-cnta :
                bal, replacements =  0, 0
                for cnt, s in enumerate(S) :
                    if s == b :
                        bal+=1
                        if bal > 0 :
                            bal -= 1
                            replacements +=1

                    if s == a :
                        bal -= 1

                if bal == 0 and replacements <= maxR:
                    return 1
                else : return 0

            else :
                return 0

        return None     # I used this as a test case to make sure that I do not miss some cases. My tests worked fine !!!



    RES=[]      # To fill list

    for i in range(len(expressions)) :
        t = tryToBalance( expressions[i], maxReplacements[i]  )
        RES.append(t)

    return RES



"""
* DO NOT MODIFY CODE BELOW THIS POINT!
"""
def main():
    data = sys.stdin.readlines()


    expressionsCount = int(data[0])
    expressions = []

    for i in range(1, expressionsCount + 1):
        expressions.append(data[i])

    maxReplacementsCount = int(data[expressionsCount + 1])
    maxReplacements = []

    for i in range(expressionsCount + 2, len(data)):
        maxReplacements.append(int(data[i]))

    result = balancedOrNot(expressions, maxReplacements)

    for val in result:
        print(val)

main()