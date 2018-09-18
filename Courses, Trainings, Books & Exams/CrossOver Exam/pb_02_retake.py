#  Created by Bogdan Trif on 05-07-2018 , 3:37 PM.

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
An array of n integers, maxReplacements, where max Replacementsi denotes the maximum number of replacements
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

# We use the following STACK
class Stack:
    def __init__(self):
        self.L = []

    def push(self, var):
        self.L.append(var)

    def size(self):
        return len(self.L)

    def isEmpty(self):
        return self.L == []

    def peek(self):
        return self.L[-1]

    def pop(self):
        self.L.pop()

    def get_elements(self):
        return self.L



def isBalanced( symbolString ) :
    print( set(symbolString) )

    if len(set(symbolString)) != 2 : return False

    s1, s2 = set(symbolString)
    if ord(s1) > ord(s2) :
        s1, s2 = s2, s1

    print('s1 : ', s1, ord(s1), '   s2 :', s2, ord(s2)  )

    S = Stack()

    bal = True

    i=0
    while i < len(symbolString) and bal == True :

        if symbolString[i] == s1 :
            S.push( s1 )
        if symbolString[i] == s2 :
            if S.size() == 0:
                return False
            else :
                S.pop()

        print(i,'    s=', symbolString[i] ,'    Stack :' , S.get_elements() )


        i+=1
    if S.size() == 0 :
        return True
    else :
        return False



print('\nisBalanced : \t', isBalanced('[][[[][]]]]]')  )

print('\n--------------------------------------------')

'''
3.7. Balanced Symbols (A General Case)
The balanced parentheses problem shown above is a specific case of a more general situation that arises in many programming languages. 
The general problem of balancing and nesting different kinds of opening and closing symbols occurs frequently. 
For example, in Python square brackets, [ and ], are used for lists; curly braces, { and }, are used for dictionaries; 
and parentheses, ( and ), are used for tuples and arithmetic expressions. 
It is possible to mix symbols as long as each maintains its own open and close relationship. 

Strings of symbols such as :

{ { ( [ ] [ ] ) } ( ) }

[ [ { { ( ( ) ) } } ] ]

[ ] [ ] [ ] ( ) { }
are properly balanced in that not only does each opening symbol have a corresponding closing symbol, 
but the types of symbols match as well.

Compare those with the following strings that are not balanced:

( [ ) ]

( ( ( ) ] ) )

[ { ( ) ]
The simple parentheses checker from the previous section can easily be extended to handle these new types of symbols. 
Recall that each opening symbol is simply pushed on the stack to wait for the matching closing symbol to appear later in the sequence. 
When a closing symbol does appear, the only difference is that we must check to be sure that it correctly matches 
the type of the opening symbol on top of the stack. If the two symbols do not match, the string is not balanced. 

Once again, if the entire string is processed and nothing is left on the stack, the string is correctly balanced.

The Python program to implement this is shown in ActiveCode 1. 
The only change appears in line 16 where we call a helper function, matches,
to assist with symbol-matching. Each symbol that is removed from the stack must be checked to see
 that it matches the current closing symbol. 
 If a mismatch occurs, the boolean variable balanced is set to False.

'''

def matches( open, close ) :
    opens = '{[('
    closers = '}])'
    if opens.index(open) == closers.index(close) :
        return True
    return False



def isBalanced2( symbolString ) :
    print('symbolString : \t' , symbolString )


    S = Stack()
    bal = True

    i=0
    while i < len(symbolString) and bal == True :

        if symbolString[i] in '{[(' :
            S.push( symbolString[i] )
        if symbolString[i] in '}])' :
            if S.size() == 0:
                return False
            else :
                top = S.get_elements()[-1]
                # print('Statck S : ', S.get_elements() )
                if matches( top , symbolString[i]  ) :
                    S.pop()

        print(i,'    s=', symbolString[i] ,'    Stack :', S.get_elements() )

        i+=1

    if S.size() == 0 :
        return True
    else :
        return False


print('\nisBalanced2 : \t', isBalanced2( '{{((()))[()]}{}}' )  )