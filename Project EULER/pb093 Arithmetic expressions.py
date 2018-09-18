#!/usr/bin/python
# Solved by Bogdan Trif @   Completed on Thu, 1 Dec 2016, 17:04
#The  Euler Project  https://projecteuler.net
'''
                                                        Arithmetic expressions      -       Problem 93
By using each of the digits from the set, {1, 2, 3, 4}, exactly once, and making use of the
four arithmetic operations (+, −, *, /) and brackets/parentheses, it is possible to form different positive INTEGER targets.

For example,

                                                                        8 = (4 * (1 + 3)) / 2
                                                                        14 = 4 * (3 + 1 / 2)
                                                                        19 = 4 * (2 + 3) − 1
                                                                        36 = 3 * 4 * (2 + 1)

Note that concatenations of the digits, like 12 + 34, are not allowed.

Using the set, {1, 2, 3, 4}, it is possible to obtain thirty-one different target numbers of which 36 is the maximum,
and each of the numbers 1 to 28 can be obtained before encountering the first non-expressible number.

Find the set of four distinct digits, a < b < c < d, for which the longest set of consecutive positive integers, 1 to n,
can be obtained, giving your answer as a string: abcd.
'''
import time
from itertools import permutations, combinations, combinations_with_replacement
print('--------------------------TESTS------------------------------')

oper = { 1:  '+', 2:  '-', 3:  '*', 4:  '/' }
digits = [ str(i) for i in range(1,10) ]
print(digits)

D = list(combinations(digits,4))

print('Digits combinations: \n',len(D), D)

O=[]
cnt=0
for i in range(1,5):
    for j in range(1,5) :
        for k in range(1,5) :
            O.append([ oper[i], oper[j], oper[k]])
            cnt+=1
            # print(str(cnt)+'.    ',oper[i], oper[j], oper[k] )

print('Operator all combinations :\n',len(O) ,O)

def cut_consecutive_integers(lst):
    ''':Description: Takes any list and returns slices of consecutive integers.
        In this context it is customized to return the longest list of integers.
    '''
    C, D = [], []
    for i in range(1,len(lst)):
        if lst[i]== lst[i-1]+1:
            C.append(lst[i-1])
        else :
            C.append(lst[i-1])
            if len(C) > len(D): D=C[:]
            # print(C)
            C =[]
    return D


test_exp = '2/1+3-4'
print('\nThe test_exp used for testing : ',test_exp)

def add_parantheses(exp):
    E, R = [], []
    p1, p2 ='(', ')'
    for i in range(0, 6, 2 ):
        if i == 0 :
            a = p1+ exp[i:i+3] + p2 + exp[i+3:]
            b = p1+ a[0:7] + p2 + a[7:]
            c = p1+ exp[0:3] + p2 + exp[3:4]+ p1 +exp[4:] + p2
            d = p1+ exp[i:i+5] + p2 + exp[i+5:]
            E.append(b), E.append(c), E.append(d)
        else :
            a = exp[0:i] + p1+ exp[i:i+3] + p2 + exp[i+3:]
            b = a[0:2] + p1 + a[2:] + p2
            d = exp[0:2] + p1 + exp[2:] + p2
            E.append(b), E.append(d)
        E.append(a)
    # print(E)
    for k in E :
        try :
            eval(k)
            R.append(eval(k))
        except: ZeroDivisionError
    return R

print('\nFunction test add_parantheses :  ',add_parantheses(test_exp))


print('eval Builtin Function Testing:  ',eval( ' 1*(2+(3-4)) ' ))
print('eval Builtin Function Testing:  ',eval( ' 1+((2*3)-4) ' ))

print('\n======  My FIRST SOLUTION,  VERY SLOW, 2min, Must remake it using Reverse Polish Notation =========\n')
t1  = time.time()
# Must improve it using https://en.wikipedia.org/wiki/Reverse_Polish_notation
# Must renounce to the eval expression which is SLOW

def solve_pb093():
    scnt, counter , maxv, X = 0, 0, 0, []
    for i in range(len(D)):
        # if i== 1 : break
        P = list(permutations(D[i]))        # We want all the permutations of  ('1', '2', '3', '4')
        INT =[]
        counter+=1
        # print('\n',str(counter)+'.       Perm nr : ', len(P) ,'    ',P[0])
        for k in range(len(P)):
            for j in range(len(O)):
                scnt +=1
                exp = P[k][0]+ O[j][0] + P[k][1]+ O[j][1] + P[k][2]+ O[j][2] + P[k][3]
                # print(str(scnt)+'.   ',exp)
                E = add_parantheses(exp)
                # print([ int(i)  for i in E if i %1==0 and i >=0 ])
                tmp = list(set([  int(i)  for i in E if i %1==0 and i >0 ] ))
                # print( tmp )
                INT = INT+tmp
                # print('INT :   ',INT)
        INT = sorted( list(set(INT) ))
        # print( len( INT ) , INT )
        C = cut_consecutive_integers(INT)      # Select only Monotonic Consecutive numbers
        if len(C) > maxv :
            print(D[i], len(C))
            print(C ,'\n')
            maxv = len(C)
            X = ''.join(D[i])

    return print('\nAnswer : ',maxv, X)


solve_pb093()       #   Answer :  51 1258



t2  = time.time()
print('\nCompleted in :', round((t2-t1),6), 's\n\n')      # Completed in : 123318.053246 ms



#   jfreiberg
# As others have done, I implemented reverse polish evaluation.
# The nice part is that there is no need to figure out where the parentheses go, because there aren't any!
# In reverse polish, the order of the operands are always the same as in  the infix expression.
# Also, the last item must be an operator, and in this case, the first two must be operands
# ( because all of the operators require two operands).
# Finally, going left to right, the number operands to the left of any point must be greater than the number of operators.
# This leaves just 5 possible formulae.  In the following, the capital letters A,B,C,D are operands,
# and the lowercase letters x,y, and z are operations.
# The 5 formulae are : ABCDxyz,ABCxDyz,ABCxyDz,ABxCDyz,ABxCyDz.
# Now just iterate of all permutations of the digits 1 thru 9 , and the 4 operations, and keep track of the results.
# I implemented in Python, and kept the interpreted reverse polish evaluation function, so it took a few seconds to complete.


print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1, VERY FAST, kgorlen, USA  --------------------------')
t1  = time.time()

from itertools import combinations, permutations, product
from operator import add, sub, mul, truediv
from math import trunc

maxN = 0
maxGroup = []
maxResults = set()

for group in combinations((1,2,3,4,5,6,7,8,9,0), 4):
    results = set()
    for digits in permutations(group, 4):
        for ops in product((add,sub,mul,truediv), repeat=3):
            stack = list(digits)
            try:
                for op in ops:
                    stack.append(op(stack.pop(),stack.pop()))
            except ZeroDivisionError: continue
            if stack[0] != 0 and stack[0] == trunc(stack[0]):
                results.add(abs(trunc(stack[0])))    # abs() to handle unary minus case
        i = 0
        while i+1 in results: i += 1
        if i > maxN:
            maxN = i
            maxGroup = group
            maxResults = results

maxGroup = sorted(maxGroup)
print(maxN, sorted(maxResults))
print("p093 answer:", maxGroup)
assert [1,2,5,8] == maxGroup, "Expected [1,2,5,8]"

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 2,  DFHD, England --------------------------')
t1  = time.time()

# Well, Reverse Polish Notation is just brilliant - pity I never heard of it before solving this problem!
# Thank you Project Euler for enlightening me!
#
# My Python code is very many nested loops:
# combinations of 4 digits -> permutations of those -> options for op1, op2, op3 -> 5 ways of putting brackets into A op1 B op2 C op3 D
#
# I wish I'd thought of using functions like this:
# sO3SrLCr4Rqb00Zr4nIYCVBPZ_oFimST said
# In python, functions themselves can be passed as objects (or rather, they *are* objects),
# and you can even assign them to a variable and then call that variable as though it were a function.
#
# e.g.
# def somefunc(a, b):
#     return a+b
#
# newname = somefunc
# newname(1, 2)
#
# I used this to my advantage to make an (in my opinion) elegant solution:
# By the way, to those expressing a wish that their choice of language supported "eval":
# I was always taught that "eval is evil".
# It's never necessary, and it's a huge vector for failure.
# It's better to go the Euler route and relish the challenge of finding another way!

import itertools

def sub(a, b):
    return a - b

def divide(a, b):
    if b != 0:
        return 1.0 * a / b
    else:
        return float("inf")  # Easiest way, even if it's cheating.

def mult(a, b):
    return a * b

def add(a, b):
    return a + b


def clean(n):  # Use this to turn all those pesky approx. integer floating points into integers,
                        # and we only care about positive integers and approx. integer floating points.
    if n < 0:
        return 0
    if ((n - 0.5) % 1)-0.5 <= 1e-6:
        return int(round(n))
    else:
        return 0


def chainlen(nums):
    nums.add(0)
    nums = list(nums)
    nums.sort()
    for i in range(len(nums)):
        if i != nums[i]:
            break
    return i-1


def main():
    maxlen = 0
    for a, b, c, d in itertools.combinations(range(0, 10), 4):
        nums = set()
        for newa, newb, newc, newd in itertools.permutations((a, b, c, d), 4):
            for o1, o2, o3 in itertools.product(
                (sub, divide, mult, add), repeat=3):
    # Here we pass the functions sub, divide, etc. themselves into itertools.product, which can then be called with o1(a, b), o2(a, b), and o3(a, b)!
                nums.add(clean(o1(newa, o2(newb, o3(newc, newd)))))
                nums.add(clean(o1(newa, o3(o2(newb, newc), newd))))
                nums.add(clean(o3(o1(newa, o2(newb, newc)), newd)))
                nums.add(clean(o3(o2(o1(newa, newb), newc), newd)))
                nums.add(clean(o2(o1(newa, newb), o3(newc, newd))))
        if chainlen(nums) >= maxlen:
            maxlen = chainlen(nums)
            print (a, b, c, d, chainlen(nums))

main()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 3,  ELEGANT & VERY FAST, ,Antti Haapala, Finland --------------------------')
t1  = time.time()

# My Python 3 solution was surprisingly similar to many other Python solutions here.
# Basically I am abusing lambda capturing global variables, I took the parenthesisation
# from the Catalan numbers article because I was lazy; 1 second

from itertools import combinations, permutations, product, count
from operator import add, sub, truediv as div, mul

digits = range(1, 10)
ops = list(product([add, sub, div, mul], repeat=3))
exprs = [
    lambda: o3(o2(o1(a, b), c), d),
    lambda: o3(o1(a, o2(b, c)), d),
    lambda: o2(o1(a, b), o3(c, d)),
    lambda: o1(a, o3(o2(b, c), d)),
    lambda: o1(a, o2(b, o3(c, d)))
]
current_max = 1
for i in combinations(digits, 4):
    s = set()
    for a, b, c, d in permutations(i):
        for o1, o2, o3 in ops:
            for e in exprs:
                try:
                    v = e()
                except ZeroDivisionError:
                   continue

                if v == int(v):
                    s.add(v)

    # shortcut the worst cases
    if len(s) > current_max and current_max in s:
        for j in count(1):
            if not j in s:
                break

        if max(j - 1, current_max) > current_max:
            win = ''.join(map(str, i))
            current_max = j - 1

print(win)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 4, INTERESTING, The Fastest ,eltong, Albania  --------------------------')
t1  = time.time()

# I wanted to generate the code first, but I thought I could try to make it easier (right: "easier" :p) using Python's list comprehensions.
# The result, you ask? Well, see for yourself. Does its "magic" within 0.11700654029846191 seconds.

def calculate_all(a,b,c,d):
    ap = [ [], [a + b, a * b, a - b, a / b], [a + c, a - c, a * c, a / c], [a + d, a - d, a * d, a / d] ]

    bp = [ [b / a, b - a], [], [b + c, b - c, b * c, b / c], [b + d, b - d, b * d, b / d] ]

    cp = [ [c / a, c - a], [c / b, c - b], [], [c + d, c - d, c * d, c / d] ]

    dp = [ [d / a, d - a], [d / b, d - b], [d / c, d - c], [] ]

    ab = ap[1]+bp[0]
    ac = ap[2]+cp[0]
    ad = ap[3]+dp[0]
    bc = bp[2]+cp[1]
    bd = bp[3]+dp[1]
    cd = cp[3]+dp[2]

    abc = [x + a for x in bc] + [x + b for x in ac] + [x + c for x in ab] + [x - a for x in bc] + [x - b for x in ac] + [x - c for x in ab] + [x / a for x in bc] + [x / b for x in ac] + [x / c for x in ab] +    [x * a for x in bc] + [x * b for x in ac] + [x * c for x in ab] +    [a / x for x in bc] + [b / x for x in ac] + [c / x for x in ab] +    [a - x for x in bc] + [b - x for x in ac] + [c - x for x in ab]

    abd = [x + a for x in bd] + [x + b for x in ad] + [x + d for x in ab] + [x - a for x in bd] + [x - b for x in ad] + [x - d for x in ab] + [x / a for x in bd] + [x / b for x in ad] + [x / d for x in ab] +    [x * a for x in bd] + [x * b for x in ad] + [x * d for x in ab] +    [a / x for x in bd] + [b / x for x in ad] + [d / x for x in ab] +    [a - x for x in bd] + [b - x for x in ad] + [d - x for x in ab]

    acd = [x + a for x in cd] + [x + d for x in ac] + [x + c for x in ad] + [x - a for x in cd] + [x - d for x in ac] + [x - c for x in ad] + [x / a for x in cd] + [x / d for x in ac] + [x / c for x in ad] + [x * a for x in cd] + [x * d for x in ac] + [x * c for x in ad] + [a / x for x in cd]+[d/x for x in ac] + [c / x for x in ad] + [a - x for x in cd] + [d- x for x in ac] + [c - x for x in ad]

    bcd = [x + b for x in cd] + [x + d for x in bc] + [x + c for x in bd] + [x - b for x in cd] + [x - d for x in bc] + [x - c for x in bd] + [x / b for x in cd] + [x / d for x in bc] + [x / c for x in bd] +    [x * b for x in cd] + [x * d for x in bc] + [x * c for x in bd] +    [b / x for x in cd] + [d / x for x in bc] + [c / x for x in bd] +    [b - x for x in cd] + [d - x for x in bc] + [c - x for x in bd]

    sbcd = set(bcd)

    bcd_a = [x + a for x in sbcd] + [x * a for x in sbcd] + [x / a for x in sbcd] + [x - a for x in sbcd] + [a - x for x in sbcd] + [a / x for x in sbcd if x != 0]

    sabc = set(abc)

    abc_d = [x + d for x in sabc] + [x * d for x in sabc] + [x / d for x in sabc] + [x - d for x in sabc] + [d - x for x in sabc] + [d / x for x in sabc if x != 0]

    sabd = set(abd)

    abd_c = [x + c for x in sabd] + [x * c for x in sabd] + [x / c for x in sabd] + [x - c for x in sabd] + [c - x for x in sabd] + [c / x for x in sabd if x != 0]

    sacd = set(acd)

    acd_b = [x + b for x in sacd] + [x * b for x in sacd] + [x / b for x in sacd] + [x - b for x in sacd] + [b - x for x in sacd] + [b / x for x in sacd if x != 0]

    return sorted([a for a in set(bcd_a).union(set(abc_d), set(acd_b), set(abd_c)) if a > 0 and int(a) == a])

def max_sequence(a,b,c,d):
    r = set(calculate_all(a,b,c,d))
    diff = set(range(1,max(r))) - r
    if len(diff) == 0:
        return max(r)
    return min(diff) - 1

def main():
    longest = 0
    seq = (0,0,0,0)
    for i in range(1,7):
        for j in range(i + 1, 8):
            for k in range(j + 1, 9):
                for l in range(k + 1, 10):
                    m = max_sequence(i,j,k,l)
                    if m > longest:
                        longest = m
                        seq = (i,j,k,l)
    print (seq, '-->', longest)


if __name__ == '__main__':
    main()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')



print('\n--------------------------SOLUTION 5,  Mihailo_Keda, Ukraine --------------------------')
t1  = time.time()

# Reverse Polish notation and brute force - https://en.wikipedia.org/wiki/Reverse_Polish_notation

from timeit import timeit
from itertools  import combinations, product, permutations

def parse_rpn(expression):
    """ Evaluate a reverse polish notation """

    stack = []

    for val in expression:
        if val in ['-', '+', '*', '/']:
            op1 = stack.pop()
            op2 = stack.pop()

            if val=='/' and op1 == 0: return 0

            if val=='-': result = op2 - op1
            if val=='+': result = op2 + op1
            if val=='*': result = op2 * op1
            if val=='/': result = op2 / op1
            stack.append(result)
        else:
            stack.append(float(val))

    return stack.pop()

def solve():
    max_index = 0
    max_chain = 0
    digits_set = (i for i in range(1, 10))
    operations = ('+', '-', '*', '/')

    for digits_set in combinations(digits_set, 4):
        s = set()
        for digits in permutations(digits_set):
            for operation in product(operations, repeat=3):
                for p1 in range(2, 5):
                    if p1 == 4:
                        p2_limit = 4
                    else:
                        p2_limit = 3
                    for p2 in range(p2_limit, 5):
                        p3 = 5
                        result = list(digits)
                        result.insert(p1, operation[0])
                        result.insert(p2 + 1, operation[1])
                        result.insert(p3 + 2, operation[2])
                        result = parse_rpn(result)
                        if result > 0 and (result).is_integer():
                            s.add(int(result))

        list_to_check = sorted(s)
        if list_to_check[0] == 1:
            max_in_list = 1
            for i in range(1, len(list_to_check)):
                if list_to_check[i] - list_to_check[i - 1] == 1:
                    max_in_list = i + 1
                else:
                    break
            if max_in_list > max_chain:
                max_chain = max_in_list
                max_index = digits_set

    print(max_index)


print(timeit(solve, number = 1), 's')

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')







print('\n--------------------------SOLUTION 6, Michiel, Netherlands  --------------------------')
t1  = time.time()

# I decided to try some problems in python. Seems to be handy here with the combinations,
# permutations and products from itertools. Also the lambda's came in handy.
# I skipped this problem for quite some time because I thought I had to parse things or build trees,
# but I realised parentheses are not important at all, and as long as you add both orders
# for the non-commutative operations you can easily brute-force it.


from itertools import combinations, permutations, product

digits = range(10)

length = 0
for subset in combinations(digits, 4):
    possibilities = set()
    for perm_digit in permutations(subset):
        for perm_op in product((lambda x,y : x+y, lambda x,y : x-y,
                                lambda x,y : y-x, lambda x,y : x*y,
                                lambda x,y : x/y, lambda x,y : y/x),repeat=3):
            try:
                number = perm_op[2](perm_op[1](perm_op[0](perm_digit[0],
                                perm_digit[1]),perm_digit[2]),perm_digit[3])
            except ZeroDivisionError:
                continue
            if number < 1 or number != round(number,0):
                continue
            possibilities.add(int(number))
    while(possibilities.issuperset(range(1,length+1))):
        best_one = subset
        length += 1

print (best_one, length)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 8,  mbh038, England --------------------------')
t1  = time.time()

# 4**3=64 ways to choose 3 operators from 4
# 9C4=126 ways to choose 4 digits from 9
# 24 ways to order each set of digits
# 5 ways to parenthesise the formulae - and we need only investigate three of those
#
# So 64×126×24×3=58060864×126×24×3=580608 possibilities.
#
# Hence, a brute force approach seemed reasonable, although 9s is a bit slow! I will work on that.
# Maybe also on the fact that, according to DFHD, my code may be eval-evil :)
# The hard bit for me was working out the possible ways to parenthesise the formulae - 5.
# Then I happened upon Catalan numbers and Dyck words and so on.
# As it stands, I have to put the first 3 of those possibilities in manually
# (we do not need to consider the other two since they are the reverse of the first two),
# but I would like the code to work them out itself. More work needed!

import itertools as it
import time

def p93():
    t=time.clock()

    operations='+-*/'
    digits='123456789'

    #the five possible ways to perenthesize our formiulae: (C3=5)
    #((a ? b) ? c) ? d
    #(a ? (b ? c)) ? d
    #(a ? b) ? (c ? d)
    #a ? ((b ? c) ? d) - mirror image of #2
    #a ? (b ? (c ? d)) - mirror image of #1

    final={}
    for four in it.combinations(digits,4):
        results=set()
        for d in it.permutations(four,4):
            for op in it.product(operations,repeat=3):
                perm0=['((',d[0],op[0],'',d[1],')',op[1],'',d[2],')',op[2],d[3],'']
                perm1=['(',d[0],op[0],'(',d[1],'',op[1],'',d[2],'))',op[2],d[3],'']
                perm2=['(',d[0],op[0],'',d[1],')',op[1],'(',d[2],'',op[2],d[3],')']
                perms=[perm0,perm1,perm2]
                for i in range(len(perms)):
                    try:
                        result=eval(''.join([x for x in perms[i]]))
                        if result>0 and result==int(result):
                            results.add(int(result))
                    except ZeroDivisionError:
                        pass
        final[''.join([x for x in four])]=results


    #find digit set giving maximum run of consecutive result values, starting from 1,
    maxlen=-1
    for k,v in final.items():
        i=1
        while 1:
            if i not in v:
                break
            i+=1
        if i>maxlen:
            maxlen=i
            best=k

    print(best,maxlen-1,time.clock()-t)

p93()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 9,  IMPROVED ,mbh038, England --------------------------')
t1  = time.time()


# Here is an rpn version of the same ugly code that now at least has the merits that is slightly faster,
# at 7s, avoids the evil of eval().
# The question of what is a valid parenthesis is replaced by the question of what is a valid rpn expression.
# As jfreiberg said above, there can only be  5 classes of these: ABCDxyz, ABCxDyz, ABCxyDz,ABxCDyz and ABxCyDz,
# where ABCD are operands and xyz are operators.
# Thus we need only consider expressions within one of these classes.

import itertools as it
import time
def p93rpn():

    t=time.clock()
    operators='+-*/'
    digits='123456789'

    #there can be only 5 possible orderings of operands and operators
    #must start with two operands, finish with an operator, and must always
    #have more operands than operators to the left of any point in the expression.
    case1=[[0,1,2,3],[4,5,6]]
    case2=[[0,1,2,4],[3,5,6]]
    case3=[[0,1,2,5],[3,4,6]]
    case4=[[0,1,3,4],[2,5,6]]
    case5=[[0,1,3,5],[2,4,6]]

    cases=[case1,case2,case3,case4,case5]

    final={}
    for four in it.combinations(digits,4):
        results=[]
        for ds in it.permutations(four,4):
            for ops in it.product(operators,repeat=3):
                S=[0]*7
                for case in cases:
                    for x in range(4):
                        S[case[0][x]]=ds[x]
                    for x in range(3):
                        S[case[1][x]]=ops[x]
                    expression=' '.join([x for x in S])
                    try:
                        result=rpn(expression)
                        if result>0 and result==int(result):
                            results.append(int(result))
                    except:
                        pass

        final[''.join([x for x in four])]=results

    #find digit set giving maximum run of consecutive result values, starting from 1,
    maxlen=-1
    for k,v in final.items():
        i=1
        while 1:
            if i not in v:
                break
            i+=1
        if i>maxlen:
            maxlen=i
            best=k

    print(best,maxlen-1,time.clock()-t)

def rpn(exp):
    operators='*/+-'
    stack = [];
    for v in exp.split(' '):
        if v in operators:
            if len(stack)<2:
                return "Invalid Expression - too few values"
            b = stack.pop()
            a = stack.pop()
            if v=='-': result = a-b
            if v=='+': result = a+b
            if v=='*': result = a*b
            if v=='/': result = a/b
            stack.append(result)
        else:
            stack.append(int(v))
    if len(stack)==1:
        return stack.pop()
    return "invalid expression - too many values"

p93rpn()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


