#  Created by Bogdan Trif on 05-07-2018 , 1:55 PM.

'''
http://interactivepython.org/runestone/static/pythonds/BasicDS/ImplementingaStackinPython.html

                            ===     3.5. Implementing a Stack in Python     ===

Now that we have clearly defined the stack as an abstract data type we will turn our attention to using Python to implement the stack.
Recall that when we give an abstract data type a physical implementation we refer to the implementation as a data structure.

As we described in Chapter 1, in Python, as in any object-oriented programming language, the implementation of choice
for an abstract data type such as a stack is the creation of a new class.
The stack operations are implemented as methods.
Further, to implement a stack, which is a collection of elements,
it makes sense to utilize the power and simplicity of the primitive collections provided by Python.
We will use a list.

Recall that the list class in Python provides an ordered collection mechanism and a set of methods.
For example, if we have the list [2,5,3,6,7,4], we need only to decide which end of the list will be considered
the top of the stack and which will be the base.
Once that decision is made, the operations can be implemented using the list methods such as append and pop.

The following stack implementation (ActiveCode 1) assumes that the end of the list will hold the top element of the stack.
As the stack grows (as push operations occur),
new items will be added on the end of the list. pop operations will manipulate that same end.

'''

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
        return self.L.pop()

    def get_elements(self):
        return self.L





print('\n------------------------------     Applications    -----------------------------------')

def isBalanced(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()

        index = index + 1

    if balanced and s.isEmpty():
        return True
    else:
        return False


s= '(()((()(())'
print( str(s) + '  isBalanced : \t', isBalanced(s)  )


print('\n----------------------        Converting Decimal Numbers to Binary Numbers        --------------------')

### 3.8. Converting Decimal Numbers to Binary Numbers

def divideBy2(decNumber):
    remstack = Stack()

    ### Here we add elements to the stack
    while decNumber > 0:
        rem = decNumber % 2
        remstack.push(rem)
        decNumber = decNumber // 2

    print(remstack.get_elements())

    # But as we have all the elements in the stack, but in reversed order, we must take them one by one
    # from the  top (end) to bottom (start)
    binString = ""
    while not remstack.isEmpty():
        binString += str(remstack.pop())
        print(binString)

    return binString

n=42
print('divideBy2 : \t',divideBy2(42)  )

print('\n----------------------------   Base Conversion ----------------------------')
'''
The algorithm for binary conversion can easily be extended to perform the conversion for any base. 
In computer science it is common to use a number of different encodings. 
The most common of these are binary, octal (base 8), and hexadecimal (base 16).

The decimal number 233 and its corresponding octal and hexadecimal equivalents 351_8 and E9_16 are interpreted as

3×8^2+5×8^1+1×8^0
and
14×16^1+9×16^0

The function divideBy2 can be modified to accept not only a decimal value but also a base for the intended conversion. 
The “Divide by 2” idea is simply replaced with a more general “Divide by base.” A new function called baseConverter, 
shown in ActiveCode 2, takes a decimal number and any base between 2 and 16 as parameters. 

The remainders are still pushed onto the stack until the value being converted becomes 0. 
The same left-to-right string construction technique can be used with one slight change. 
Base 2 through base 10 numbers need a maximum of 10 digits, so the typical digit characters 0, 1, 2, 3, 4, 5, 6, 7, 8, and 9 work fine. 
The problem comes when we go beyond base 10. 
We can no longer simply use the remainders, as they are themselves represented as two-digit decimal numbers. 
Instead we need to create a set of digits that can be used to represent those remainders beyond 9.

A solution to this problem is to extend the digit set to include some alphabet characters. 
For example, hexadecimal uses the ten decimal digits along with the first six alphabet characters for the 16 digits. 
To implement this, a digit string is created (line 4 in Listing 6) that stores the digits in their corresponding positions. 
0 is at position 0, 1 is at position 1, A is at position 10, B is at position 11, and so on. 
When a remainder is removed from the stack, 
it can be used to index into the digit string and the correct resulting digit can be appended to the answer. 

For example, if the remainder 13 is removed from the stack, the digit D is appended to the resulting string.

'''

def baseConverter(decNumber,base):
    digits = "0123456789ABCDEF"

    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % base
        remstack.push(rem)
        decNumber = decNumber // base

    newString = ""
    while not remstack.isEmpty():
        newString = newString + digits[remstack.pop()]

    return newString

print('baseConverter :  ', baseConverter(25,2) )
print('baseConverter :  ', baseConverter(25,16) )


print('\n-------------          3.9. Infix, Prefix and Postfix Expressions    -----------------------------')

'''
3.9.2. General Infix-to-Postfix Conversion
We need to develop an algorithm to convert any infix expression to a postfix expression. 
To do this we will look closer at the conversion process.

Consider once again the expression A + B * C. As shown above, A B C * + is the postfix equivalent. 
We have already noted that the operands A, B, and C stay in their relative positions. 
It is only the operators that change position. Let’s look again at the operators in the infix expression. 
The first operator that appears from left to right is +. 
However, in the postfix expression, + is at the end since the next operator, *, has precedence over addition. 
The order of the operators in the original expression is reversed in the resulting postfix expression.

As we process the expression, the operators have to be saved somewhere since their corresponding right operands are not seen yet. 
Also, the order of these saved operators may need to be reversed due to their precedence. 
This is the case with the addition and the multiplication in this example. 
Since the addition operator comes before the multiplication operator and has lower precedence, 
it needs to appear after the multiplication operator is used. 
Because of this reversal of order, it makes sense to consider using a stack to keep the operators until they are needed.

What about (A + B) * C? Recall that A B + C * is the postfix equivalent. 
Again, processing this infix expression from left to right, we see + first. 
In this case, when we see *, + has already been placed in the result expression because 
it has precedence over * by virtue of the parentheses. We can now start to see how the conversion algorithm will work. 
When we see a left parenthesis, we will save it to denote that another operator of high precedence will be coming. 
That operator will need to wait until the corresponding right parenthesis appears to denote 
its position (recall the fully parenthesized technique). When that right parenthesis does appear, 
the operator can be popped from the stack.

As we scan the infix expression from left to right, we will use a stack to keep the operators. 
This will provide the reversal that we noted in the first example. 
The top of the stack will always be the most recently saved operator. 
Whenever we read a new operator, we will need to consider how that operator compares in precedence with the operators, 
if any, already on the stack.

Assume the infix expression is a string of tokens delimited by spaces. 
The operator tokens are *, /, +, and -, along with the left and right parentheses, ( and ). 
The operand tokens are the single-character identifiers A, B, C, and so on. 

=The following steps will produce a string of tokens in postfix order.

1.  Create an empty stack called opstack for keeping operators. Create an empty list for output.
2.  Convert the input infix string to a list by using the string method split.
3.  Scan the token list from left to right.
        -   If the token is an operand, append it to the end of the output list.
        -   If the token is a left parenthesis, push it on the opstack.
        -   If the token is a right parenthesis, pop the opstack until the corresponding left parenthesis is removed. 
            Append each operator to the end of the output list.
        -   If the token is an operator, *, /, +, or -, push it on the opstack. 
            However, first remove any operators already on the opstack that have higher or equal 
            precedence and append them to the output list.
4.  When the input expression has been completely processed, check the opstack. 
    Any operators still on the stack can be removed and appended to the end of the output list.

Figure 9 shows the conversion algorithm working on the expression A * B + C * D. 
Note that the first * operator is removed upon seeing the + operator. 
Also, + stays on the stack when the second * occurs, since multiplication has precedence over addition. 
At the end of the infix expression the stack is popped twice, removing both operators and 
placing + as the last operator in the postfix expression.
'''

def infixToPostfix(infixexpr):
    prec = {}
    prec["^"] = 4
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = Stack()       # The stack which will hold the operators
    postfixList = []            # Postfix list which hold ithe operands and operators
    tokenList = infixexpr.split()       # the arranged expression which  will evaluate

    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while not opStack.isEmpty() and prec[opStack.peek()] >= prec[token] :
                postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return " ".join(postfixList)

print(infixToPostfix("A * B + C * D"))
print(infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))


'''
3.9.3. Postfix Evaluation
As a final stack example, we will consider the evaluation of an expression that is already in postfix notation. 
In this case, a stack is again the data structure of choice. 
However, as you scan the postfix expression, it is the operands that must wait, not the operators as in the conversion algorithm above. 
Another way to think about the solution is that whenever an operator is seen on the input, 
the two most recent operands will be used in the evaluation.

To see this in more detail, consider the postfix expression 4 5 6 * +. 
As you scan the expression from left to right, you first encounter the operands 4 and 5. 
At this point, you are still unsure what to do with them until you see the next symbol. 
Placing each on the stack ensures that they are available if an operator comes next.

In this case, the next symbol is another operand. So, as before, push it and check the next symbol. 
Now we see an operator, *. 
This means that the two most recent operands need to be used in a multiplication operation. 
By popping the stack twice, we can get the proper operands and then perform the multiplication (in this case getting the result 30).

We can now handle this result by placing it back on the stack so that it can 
be used as an operand for the later operators in the expression. 
When the final operator is processed, there will be only one value left on the stack.
Pop and return it as the result of the expression. 
Figure 10 shows the stack contents as this entire example expression is being processed.

Assume the postfix expression is a string of tokens delimited by spaces. 
The operators are *, /, +, and - and the operands are assumed to be single-digit integer values. 

The output will be an integer result.

1.  Create an empty stack called operandStack.
2.  Convert the string to a list by using the string method split.
3.  Scan the token list from left to right.
        -   If the token is an operand, convert it from a string to an integer and push the value onto the operandStack.
        -   If the token is an operator, *, /, +, or -, it will need two operands. Pop the operandStack twice. 
            The first pop is the second operand and the second pop is the first operand. Perform the arithmetic operation. 
            Push the result back on the operandStack.
4.  When the input expression has been completely processed, the result is on the stack. 
    Pop the operandStack and return the value.
    
The complete function for the evaluation of postfix expressions is shown in ActiveCode 2. 
To assist with the arithmetic, a helper function doMath is defined that will take two operands and 
an operator and then perform the proper arithmetic operation.

'''

def postfixEval(postfixExpr):
    operandStack = Stack()
    tokenList = postfixExpr.split()

    for token in tokenList:
        if token in "0123456789":
            operandStack.push(int(token))
        else:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = doMath(token,operand1,operand2)
            operandStack.push(result)
    return operandStack.pop()

def doMath(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    elif op == "-":
        return op1 - op2
    elif op == "^":
        return op1 ** op2


print(postfixEval('7 8 + 3 2 + /') )
print(postfixEval('5 3 4 2 - ^ *') )