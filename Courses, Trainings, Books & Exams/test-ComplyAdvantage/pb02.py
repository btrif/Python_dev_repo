
import string

l = '34'
print( l.isalnum() )


st = u"this2009"
print(st , st.isnumeric())

st = u"23443434"
print (st ,st.isnumeric() )

print('\n ------------------- SOLUTION ------------------')

# s = "    13 DUP 4 POP 5 DUP + DUP + -   "
# s = "5 6 + - "
# s= " 3 DUP 5 - - "
# s = '13 DUP 4 POP 5 DUP + DUP + -'
s = '12 DUP 737 POP DUP 773 583 14 POP DUP 368  991 DUP - POP  - DUP + 30 + + - DUP POP + - POP POP 354  - POP  DUP'

def solution1(S):
    L = []
    S = S.strip()
    print(S.split(' ') )
    for i in S.split(' ') :
        # print(i , type(i) )
        if i == ' ' : continue
        if i.isdigit() : L.append( int(i) )

        try :
            if i == "DUP" :     L.append(L[-1])

            if i == "POP" : L.pop(-1)

            if i == "+" :
                a, b = L[-1], L[-2]
                L = L[:-2]
                L.append(a+b)

            if i == "-" :
                a, b = L[-1], L[-2]
                L = L[:-2]
                L.append(a-b)

        except :
            IndexError
            return -1

        print('  -- L=  ', L)

    return L[-1]

print('\n' ,solution1(s) )

print('\n------------------- SECOND SOLUTION -----------------------------')
s = '12 DUP 737 POP DUP 773 583 14 POP DUP 368  991 DUP - POP  - DUP + 30 + + - DUP POP + - POP POP 354  - POP  DUP'

def solution(S):
    L = []
    S = S.strip()
    print(S.split(' ') )
    for i in S.split(' ') :
        # print(i , type(i) )
        if i == ' ' : continue
        if i.isdigit() : L.append( int(i) )

        if i == "DUP" :
            if len(L) > 0 :    L.append(L[-1])
            else : return -1

        if i == "POP" :
            if len(L) > 0 :    L.pop(-1)
            else : return -1

        if i == "+" :
            if len(L) >1 :
                a, b = L[-1], L[-2]
                L = L[:-2]
                L.append(a+b)
            else : return -1

        if i == "-" :
            if len(L) > 1 :
                a, b = L[-1], L[-2]
                L = L[:-2]
                L.append(a-b)
            else : return -1

        # print('  -- L=  ', i, L)

    if len(L) >0 : return L[-1]
    return -1


print('\n' ,solution(s) )




print('\n ------------------ AUTOMATED TESTS -----------------------')

def automated_test():
    import random

    for j in range(1,100) :
        S = 'DUP POP + -'
        s = [ i for i in S.split(' ') ]
        # print( s  )

        A = '12'
        for i in range( random.randint(5, 50) ) :
            x = x1 = x2 = random.choice(  s  )
            y = str(random.randint(1, 1000))
            z = random.choice( ( x, x1, x2 , y) )
            A+=' '+ z
        print(str(j)+'.      ', solution(A) ,'          ' ,A )

automated_test()